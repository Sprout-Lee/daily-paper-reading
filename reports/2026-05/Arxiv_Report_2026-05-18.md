# Arxiv Daily Deep Report - 2026-05-18

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 3
---

## 1. Real-time Speech Restoration using Data Prediction Mean Flows

**作者**: Sebastian Braun
**链接**: [2605.16251](https://arxiv.org/abs/2605.16251)
**分类**: Audio Enhancement | **关键词**: flow matching, mean flows, speech restoration, real-time, low latency, data prediction

## 核心痛点
- 现有语音恢复生成模型（如扩散、流匹配）多为离线大型模型，延迟高、计算量大，无法满足实时应用（如通信、助听器、AR设备）的低延迟（<30ms）和低计算量要求。
- 传统NCSN++架构因时间下采样引入>600ms算法延迟；DiffusionBuffer延迟仍达180-320ms。因果化改进会增加数倍复杂度。
- 流匹配模型的推理步骤数（NFE）与计算量正相关，需要减少步骤以降低复杂度。

## 方法创新
1. **数据预测均值流（Data Prediction Mean Flows）**：首次将改进均值流（IMF）训练与数据预测损失结合，替代瞬时速度损失，提升生成质量并减少推理步骤。
2. **低延迟网络架构**：提出新型骨干网络，在保持流匹配能力的同时，计算量降低120倍，并实现零算法延迟（仅含STFT固有延迟）。
3. **训练调度优化**：精心设计流时间分布、IMF调度（sigmoid-based r=t比率调度和cosine跨度分布调度）以及先验分布（从带噪均值开始，使用频谱相似噪声），提升性能。
4. **操作域**：在复压缩STFT域（幅度压缩c=0.3）进行流匹配，避免额外编码器/解码器引入的延迟和误差。

## 实验结果
- 在大规模训练数据上验证泛化能力，并使用真实录音进行主观和客观评估。
- 与NCSN++非因果基线相比，计算量减少120倍（MACs/s），同时实现相似音频质量，且无算法延迟（仅STFT窗口延迟）。
- 单步推理即可达到满意效果（NFE=1），显著优于需要多步的传统流匹配模型。

## 一句话评价
本文通过数据预测均值流和轻量级低延迟架构，首次实现了实时语音恢复的流匹配模型，计算量降低两个数量级，是实时音频生成领域的突破性工作。

---

## 2. Improving Automatic Speech Recognition for Speakers Treated for Oral Cancer using Data Augmentation and LLM Error Correction

**作者**: Hidde Folkertsma, Thomas Tienkamp, Sebastiaan de Visscher, Max Witjes, Rob van Son, Jiapan Guo, Bence Mark Halpern
**链接**: [2605.15854](https://arxiv.org/abs/2605.15854)
**分类**: Speech Recognition | **关键词**: automatic speech recognition, oral cancer speech, data augmentation, LLM error correction, Whisper, MMS, text-to-speech, voice conversion

## 核心痛点
传统的ASR系统在口腔癌（OC）术后患者语音识别上表现不佳，主要由于OC语音数据稀缺且变异大，导致模型泛化能力差。

## 方法创新
1. **数据增强**：对比多种增强技术，包括传统信号处理方法（时间拉伸、速度扰动、声道长度扰动）、语音转换（kNN-VC）和文本转语音（XTTSv2），生成合成数据以扩充训练集。
2. **LLM纠错**：利用大语言模型（LLM）作为后处理步骤，纠正ASR模型的输出错误，进一步提升识别性能。
3. **模型微调**：基于Whisper和MMS模型进行微调，包括全参数微调和参数高效微调（LoRA），并对比是否使用语言模型。

## 实验结果
- 在NKI-RUG-UMCG数据集上，采用留一说话者（LOSO）评估。
- TTS增强平均降低词错误率（WER）8%（相对值）。
- LLM纠错进一步使微调模型WER降低21.4-26.2%，非微调模型降低10.0%。
- 整体上，Whisper WER降低40%，MMS降低50%。

## 一句话评价
本文验证了结合数据增强和LLM纠错是提升口腔癌术后语音识别性能的有效策略。

---

## 3. Mind the Gap: Impact of Synthetic Conversational Data on Multi-Talker ASR and Speaker Diarization

**作者**: Alexander Polok, Ivan Medennikov, Jan Černocký, Shinji Watanabe, Lukáš Burget, Samuele Cornell
**链接**: [2605.15442](https://arxiv.org/abs/2605.15442)
**分类**: Multi-talker Speech Processing / 多说话人语音处理 | **关键词**: multi-talker ASR, speaker diarization, synthetic data, conversation simulation, FastMSS, DiCoW, Sortformer

## 核心痛点
真实多说话人对话数据匮乏，人工标注成本高昂且隐私受限，严重制约了多说话人ASR和说话人分离模型的发展。现有合成数据策略碎片化，缺乏对任务差异性和模拟参数影响的系统理解。

## 方法创新
- 提出**FastMSS**：高效开源多说话人对话模拟器，支持灵活的 turn-taking 建模（包括 turn hold, turn switch, interruption, backchannel），可自动从语料库学习转换参数或手动设置，支持可扩展生成和Lhotse集成，显著优于MMS-MSG和NeMo模拟器。
- 系统对比了不同模拟变量（turn-taking动态、源域、声学增强、数据混合）对**DiCoW（MT-ASR）**和**Sortformer（说话人分离）**的影响。

## 实验结果
1. **Turn-taking动态**：使用语料库拟合的统计量优于均匀先验；增大交叠率提升ASR但损害说话人分离。
2. **源域多样性**：混合多种域数据（如LibriSpeech+VoxPopuli+AMI等）优于单一域匹配，即使域完全匹配也如此。
3. **声学增强**：对说话人分离至关重要，对ASR影响较小。
4. **合成数据 vs 真实数据**：合成数据训练可接近真实数据基线；合成+真实联合训练优于仅真实训练。

## 一句话评价
该工作通过系统实验揭示了合成数据生成策略中任务相关的关键权衡，并提供了高效开源工具，对多说话人语音处理领域具有重要指导意义。

---

