---
title: "Molecular Biology as Digital Code: Genome to Gene Editing"
subtitle: How cells store data in four letters, copy it, compile it into proteins, and edit it
byline: Science explainer
orientation: portrait
columns: 2
paper: a1
width: 1200
document_number: PO-034
colours:
  accent: "#059669"
  secondary: "#047857"
footer:
  left: DNA as Digital Code
  centre: Science Reference
  qr: https://en.wikipedia.org/wiki/Central_dogma_of_molecular_biology
  qr-label: The central dogma
---

## Key figures {.stats style=tiles}

| Value | Label |
|---|---|
| 2 bits | Per base pair: A, C, G or T |
| About 750 MB | In one copy of the human genome, 3.1 billion base pairs |
| 64 codons | Three-letter words, for 20 amino acids and stop |
| 1 in 10⁹ | Errors per base copied, after proofreading and repair |

## Introduction {.abstract}

Four billion years before silicon, cells evolved dense digital storage and a way to execute it. **DNA** is the protected master copy in the nucleus. To build a protein, the cell copies a gene into short-lived **messenger RNA** and cuts out the parts that do not code. It then feeds it through a **ribosome**, which translates three letters at a time into the chain that folds into a protein.

## 1. The central dogma {.wide}

```flow
[DNA in the nucleus: the master copy|navy] -transcription, RNA polymerase-> [Pre-mRNA: exons and introns|blue] -splicing-> [Mature mRNA, to the cytoplasm|teal] -translation, ribosome-> [Protein|green]
Like source code kept safe on disk while temporary builds run in memory: the DNA stays in the nucleus, and working copies do the work.
```

## 2. Four letters, mirrored

DNA uses four bases, **A**, **C**, **G** and **T**: two bits each. The double helix is a mirror with built-in parity.

```cards cols=1 style=top
Base pairing | A pairs only with T (two hydrogen bonds), and G only with C (three). When a base is damaged, repair enzymes read its partner on the other strand and put it back | green
Exons and introns | Only about 1.5 % of human DNA codes for protein. Genes come in pieces, exons, separated by introns; joining exons in different ways lets about 20,000 genes make many more proteins | teal
```

## 3. A gene, framed like a packet

```segments
title: A gene and its mature mRNA (not to scale)
1 | Promoter | Where copying starts | navy
2 | 5′ UTR and the start codon, AUG | Header | blue
3 | Exon 1 | Code | green
1 | Intron | Cut out | amber
3 | Exon 2, stop codon, poly-A tail | Code and trailer | teal
```

## 4. Why three letters a word

There are 20 amino acids. One base gives 4 words and two give 16, too few; three give **4³ = 64**. In RNA, uracil (U) takes the place of thymine:

```tape
cells: A U G G C U G G C U A A
1-3 | Met: start | green
4-6 | Ala | blue
7-9 | Gly | navy
10-12 | Stop | red
```

```cards cols=1 style=label
Redundancy | GCU, GCC, GCA and GCG all mean alanine: a change in the third letter is often silent
Reading frame | The ribosome reads in threes from AUG; one extra or missing letter shifts every word after it
```

## 5. DNA and silicon {.wide}

```compare
| DNA | Silicon (SSD, DRAM)
Density | **About 215 petabytes per gram** | A few terabytes per SSD chip
Lifetime | **Hundreds of thousands of years** cold and dry; mammoth DNA over a million years old has been read | 5 to 10 years unpowered: flash leaks charge
Speed | 50 to 1,000 bases a second per enzyme | **Gigabytes a second**
Parallelism | **Trillions of enzymes at once** | Up to thousands of cores
Energy | Powered by ATP, at a tiny fraction of silicon's energy per operation | Watts to megawatts
```

## 6. CRISPR-Cas9: search and replace

Bacteria evolved **CRISPR** as a record of past viruses. Jennifer Doudna and Emmanuelle Charpentier turned **Cas9** into a programmable editor for any genome.

```steps
Program the guide | A 20-letter guide RNA matching the target is loaded into Cas9
Scan for the PAM | Cas9 checks the genome only next to a three-letter mark, NGG | blue
Match and cut | If the 20 letters match, Cas9 cuts both strands | amber
Repair | The cell either joins the ends, which usually disables the gene, or copies in a template you supply | green
```

## 7. Epigenetics: settings, not code {style=card colour=green}

A neuron and a liver cell carry the same DNA. Marks on and around it decide which genes run:

```cards cols=1 style=label
Methylation | Methyl groups on cytosines switch genes off without changing a letter
Histone packing | DNA wound tightly round histones is hidden; unwound, it can be read
Transcription factors | Proteins that bind promoters and switch genes on in response to hormones, light or stress
Base editing | Newer Cas9 variants change one letter, such as C to T, without cutting both strands
```

## 8. Glossary

```glossary cols=1
Cas9 | The CRISPR enzyme that cuts DNA where its guide matches
Codon | Three bases that name one amino acid, or stop
gRNA | Guide RNA: the 20-letter search string
mRNA, tRNA | Messenger RNA; transfer RNA, which brings each amino acid
PAM | Protospacer adjacent motif: NGG, next to the target
UTR | Untranslated region at either end of an mRNA
```

## In short {.summary}

Life runs on a four-letter digital code. DNA keeps the master copy with built-in parity, mRNA carries working copies, ribosomes translate them with a 64-word table, and CRISPR edits the source in place.

### Mirrored and checked

Base pairing and repair copy billions of letters with about one error in a billion.

### Same code, different settings

Epigenetic marks switch different genes on in different cells.

### CRISPR is search and replace

Change the 20-letter guide, and the same enzyme edits a different gene.
