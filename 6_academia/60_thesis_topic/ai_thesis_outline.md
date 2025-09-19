# working thesis outline  
**title (working):** *hierarchical predictive processing models for eeg: a neuromorphic approach to mental imagery & aphantasia*

---

## 0. meta-notes

- **modularity:** each major section can be swapped / iterated independently (e.g., dataset choice, model variant).  
- **dataset-agnostic design:** placeholders where a public dataset name will drop in once finalized (YOTO, OpenMIIR, BCI IV, etc.).  
- **throughline:** show how *hierarchical, multi-timescale computation* improves eeg decoding **and** maps onto theoretical brain architecture.

---

## I. introduction & motivation

1. **problem statement**  
   - mental imagery is notoriously subjective; aphantasia exemplifies this difficulty.  
   - non-invasive eeg offers millisecond-level temporal insight but is noisy + low spatial resolution.  

2. **hypothesis**  
   - a model that explicitly separates *fast* (γ) and *slow* (α/β) dynamics—and exchanges *predictions/errors* across levels—will:  
     1. outperform conventional flat networks on imagery classification,  
     2. degrade in biologically plausible ways when frequency bands are “lesioned,” mimicking imagery deficits.

3. **contributions**  
   - introduce a **hierarchical predictive coding** architecture tailored to eeg.  
   - embed a lightweight **neuromorphic (reservoir / spiking)** module for richer temporal embeddings.  
   - provide an open, reproducible pipeline and lesioning framework for aphantasia-style investigations.

---

## II. background & related work

1. **predictive processing & hierarchical bayesian brain**  
   - summarize Rao & Ballard (1999), Friston, Clark; emphasize fast-error / slow-context loop.  

2. **eeg signal properties**  
   - channel layout, frequency bands, event-related potentials; relevance of γ vs α/β in top-down vs bottom-up processing.  

3. **scientific machine learning for eeg**  
   - prior CNN/RNN/Transformer approaches; limitations of treating all timescales uniformly.  

4. **neuromorphic / reservoir computing**  
   - LIF spiking neurons, echo-state networks, liquid state machines; why they suit continuous temporal data.  

5. **imagery & aphantasia literature**  
   - behavioral + neuroimaging findings; gaps a computational model can fill.

---

## III. methods

### A. dataset & preprocessing  *(flexible slot)*

- **dataset choice (TBD):**  
  - criteria: (a) contains mental imagery blocks, (b) decent #subjects, (c) open b-ids format.  
  - fallback: motor imagery sets if visual imagery set unavailable.  
- **pipeline:**  
  1. load with `mne`, metadata alignment.  
  2. notch (50/60 Hz), band-pass (1–45 Hz).  
  3. epoch around task events (-0.2 s → +1.0 s).  
  4. duplicate stream → apply **band-specific filters**: fast γ (30–45 Hz) vs slow α/β (8–30 Hz).  
  5. z-score per channel.

### B. model architecture

1. **baseline** – single-stream CNN/GRU classifier (establish performance floor).  
2. **hierarchical dual-stream**  
   - **fast branch:** temporal conv & depthwise separable convs.  
   - **slow branch:** GRU or downsampled Transformer capturing broader context.  
   - **fusion gate/attention:** cross-modal attention combines branches.  

3. **predictive coding extension**  
   - top layer predicts fast branch embedding → compute prediction error → iterate K steps (unrolled).  

4. **neuromorphic enhancement options** *(plug-and-play)*  
   - **reservoir module** between branches: fixed sparse recurrent matrix, trainable read-out.  
   - **surrogate-gradient spiking layer** replacing first conv (optional).  

### C. training procedure

- loss = classification cross-entropy + (optional) prediction-error regularizer.  
- optimizer: Adam; learning rate schedule.  
- subject-wise cross-validation; optionally LOSO (leave-one-subject-out).

### D. experimental manipulations

1. **frequency-band lesioning**  
   - zero / gaussian-noise α or γ band at inference.  
2. **hierarchical ablation**  
   - drop predictive loop; drop slow context branch.  
3. **reservoir vs learned mid-layer swap**.  

### E. evaluation metrics

- **performance:** accuracy, macro-F1, ROC-AUC.  
- **robustness:** % drop under lesioning.  
- **representation similarity:** RSA / centered-kernel alignment between model layers & electrode clusters.  
- **biological plausibility (optional):** sparsity of spiking layer, energy usage estimate.

---

## IV. results  *(to be filled post-experiments)*

- tabulate model comparisons.  
- lesioning effect plots.  
- latent t-SNE or attention heatmaps.  

---

## V. discussion

- interpret where hierarchical modeling helps (e.g., error-driven correction improves noisy trials).  
- connect lesion patterns to imagery deficits / aphantasia hypotheses.  
- limitations: eeg spatial blur, small sample size, neuromorphic scalability.  
- future work: multimodal (EEG + fMRI), online BCI adaptation, richer reservoirs (liquid silicon).  

---

## VI. conclusion

- recap findings: hierarchical predictive coding + neuromorphic tweaks = better, more brain-like EEG decoding.  
- relevance for cognitive neuroscience: computational probe of mental imagery quality.  

---

## VII. reproducibility plan

- code + data notebooks on GitHub (MIT license).  
- docker container, or colab notebook for quick run.  
- hyperparameter yaml + results csv.  
- lesioning script published for community benchmarking.

---

*living doc—sections can be expanded or rearranged as project evolves.*
