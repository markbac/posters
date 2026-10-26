---
title: "How Large Language Models and Transformers Work"
subtitle: Tokens, embeddings, self-attention and decoding one token at a time
byline: Artificial intelligence and deep learning explainer
orientation: landscape
columns: 3
paper: a1
width: 1750
document_number: PO-037
colours:
  accent: "#4f46e5"
  secondary: "#3730a3"
footer:
  left: Large Language Models
  centre: AI Reference
  qr: https://arxiv.org/abs/1706.03762
  qr-label: Attention Is All You Need
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 0.75 words | Of English text in one token, on average |
| 140 GB | Of memory for 70 billion weights at 16 bits |
| O(N²) | Cost of full attention over a context of N tokens |
| 1 token | Made by each pass through the network |

## Introduction {.abstract}

However much it seems to reason, a decoder-only **Large Language Model (LLM)** does one thing at each step. Given the tokens so far, it computes a probability for every token in its vocabulary, 100,000 to 256,000 of them, being the next. The runtime picks one, appends it, and runs the network again: **autoregressive decoding**.

## 1. One step: from prompt to next token {.wide}

```flow
[Text|navy] -tokenise-> [Token IDs|blue] -embed-> [Vectors, 8,192 numbers each|blue] -80 layers-> [Final vector|purple] -project, softmax-> [128k probabilities|amber] -sample-> [" mat"|green]
The model never sees letters or words. It sees integer IDs, turned into vectors and refined layer by layer. The new token is appended, and the whole step runs again.
```

## 2. Tokens: text as integers

A Byte-Pair Encoding (BPE) tokeniser splits text into common sub-words, each with an ID. A space usually belongs to the word after it.

```tape
cells: The ␣cat ␣sat ␣on ␣the
1-1 | 464 | navy
2-2 | 3797 | blue
3-3 | 3332 | green
4-4 | 319 | amber
5-5 | 262 | purple
```

Rare words split into several tokens: "tokenisation" may be "token", "isation".

## 3. Attention: how a word finds its context

How does "bank" know whether it means a river edge or a lender? Each token's vector makes a **query** (what am I looking for?), a **key** (what do I contain?) and a **value** (what do I pass on?). Each token takes a mix of the values of earlier tokens, weighted by how well its query matches their keys.

```equation
title: Scaled dot-product attention
\mathrm{Attention}(Q, K, V) = \mathrm{softmax}\left( \frac{Q K^{\top}}{\sqrt{d_k}} + M \right) V
Q, K, V | Queries, keys and values: the tokens' vectors times learned matrices |
d_k | Size of one key, so the scores do not grow with it |
M | The causal mask: no token sees a later one |
```

Each layer adds attention and then a **feed-forward network (FFN)** to a running "residual stream". Attention moves information between tokens. The FFN works on each token alone, and holds much of the learned knowledge.

## 4. Where the 70 billion weights are

```segments
title: Llama 2 70B, by share of its weights
82 | Feed-forward networks | 82 % | purple
17 | Attention | 17.5 % | blue
1 | Embeddings | 0.8 % | amber
```

Grouped-query attention shares one key and value among eight queries, so attention is the smaller part.

## 5. Choosing the next token

```chart type=bar title="Next token after 'The cat sat on the'" unit=" %" max=70
" mat" | 64
" floor" | 12
" sofa" | 8
" bed" | 5
Everything else | 11
```

```cards cols=1 style=top
Temperature | Dividing the scores by T before the softmax sharpens (T below 1) or flattens (T above 1) the choice. T = 0 always takes the top token | blue
Top-p | Sample only from the smallest set of tokens whose probabilities add up to p, such as 0.9 | navy
```

## 6. Two phases of serving: prefill and decode

```compare
| Prefill | Decode
What happens | All the prompt's tokens go through the network at once, filling the **KV cache** | One new token per pass. Each pass reads the whole cache and **all 140 GB of weights**
Limited by | **Compute**: matrix multiplications | **Memory bandwidth**: bytes per second from GPU memory
Measured as | **Time to first token** (TTFT) | **Inter-token latency** (ITL), or tokens a second
```

```chart type=bar title="Memory for 70 billion weights" unit=" GB" max=160
16-bit (FP16) | 140
8-bit (INT8) | 70
4-bit (INT4) | 35
```

Quantising to 4 bits cuts memory four-fold, and speeds up decode by the same factor of bytes read.

## 7. Practical rules {style=card colour=blue}

```checklist
[x] **Cache keys and values**: the KV cache saves recomputing the whole prompt for every token
[x] **Quantise for local use**: 4-bit weights fit a 70B model on one large GPU
[x] **Ground answers with retrieval (RAG)**: put trusted passages in the prompt to cut made-up facts
[x] **Mind the context window**: attention cost grows with the square of its length
```

## 8. Training in three stages {.wide}

```cards cols=3 style=top
1. Pre-training | Months on thousands of accelerators, predicting the next token over 10 to 15 trillion tokens of web, code and books. The result is a base model: it completes documents, but does not follow instructions | blue
2. Supervised fine-tuning (SFT) | Training on 100,000 to a million written conversations, each a prompt and an ideal reply, teaches turn-taking, format and following instructions | green
3. Preference tuning (RLHF, DPO) | People or models score pairs of answers, and training moves probability towards the better ones. Reasoning models also learn from maths and code with answers that can be checked | purple
```

## 9. Glossary {.wide}

```glossary cols=4
BPE | Byte-Pair Encoding, the usual tokeniser
DPO | Direct Preference Optimisation
FFN | Feed-forward network, two or three matrix multiplications
GQA | Grouped-query attention
KV cache | The stored keys and values of earlier tokens
LLM | Large Language Model
RAG | Retrieval-Augmented Generation
RLHF | Reinforcement Learning from Human Feedback
RoPE | Rotary position embedding: position as an angle
SFT | Supervised fine-tuning
TTFT, ITL | Time to first token, inter-token latency
VRAM | The GPU's own high-bandwidth memory
```

## In short {.summary}

A Transformer turns tokens into vectors, lets attention move context between them, and predicts one token at a time.

### Meaning is geometry

Words used alike have vectors that point alike, thousands of numbers long.

### Attention is a lookup by content

Every token queries every earlier token at once, which resolves pronouns and ambiguity.

### Decoding is a memory race

Each token reads every weight once, so its speed is set by memory bandwidth, not compute.
