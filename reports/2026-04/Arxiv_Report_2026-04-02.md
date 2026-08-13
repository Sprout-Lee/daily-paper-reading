# Arxiv Daily Deep Report - 2026-04-02

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 5
---

## 1. Diff-VS: Efficient Audio-Aware Diffusion U-Net for Vocals Separation

**作者**: Yun-Ning (Amy)Hung, Richard Vogl, Filip Korzeniowski, Igor Pereira
**链接**: [2604.01120](https://arxiv.org/abs/2604.01120)
**分类**: Music Source Separation | **关键词**: Diffusion Model, Music Source Separation, Vocal Separation, U-Net, EDM

# 核心痛点
- 生成性方法在音乐源分离任务中，尤其在客观指标如信号失真比（SDR）上，表现通常不如判别性方法。
- 现有生成性模型（如MSDM、Diff-DMX-musdb）需要大量参数（如400M）和多步采样（如150步），导致推理效率低下和泛化能力有限。
- 训练数据多为合成音乐，对真实世界音乐的适应性和主观感知质量评估不足。

# 方法创新
- 首次将Elucidated Diffusion Model（EDM）框架应用于人声分离任务，使用复杂短时傅里叶变换（STFT）频谱图作为音频表示，减少了采样步骤到少于10步。
- 基于音乐感知设计改进DDPM++模型：引入频带分割（band-splitting）和双路径RoFormer块（dual-path RoFormer blocks），以分别处理频谱图的时间和频率轴，提升模型对音频特性的适应性。
- 输入处理包括峰值归一化、幅度变换（amplitude transformation）和频带分割，以优化频谱图的能量分布和训练稳定性。

# 实验结果
- 模型参数为57M，相对紧凑，在单GPU上训练约一周。
- 在MUSDB18-HQ数据集上，无额外数据时cSDR达到10.12 dB，有额外数据（235小时）时达到10.88 dB，与判别性基线（如SCNet-L、BS-RoFormer）竞争。
- 在代理主观评价指标（MERT-L12嵌入MSE）上表现良好，显示感知质量与SOTA系统相当。
- 消融研究表明归一化和架构改进分别提升cSDR约0.17 dB和0.91 dB，验证了方法有效性。

# 一句话评价
Diff-VS通过高效应用EDM框架和音乐感知的U-Net改进，首次在声源分离中实现了生成性方法与判别性方法在客观和主观指标上的竞争力，推动了生成性模型在该领域的实用化探索。

---

## 2. VisG AV-HuBERT: Viseme-Guided AV-HuBERT

**作者**: Aristeidis Papadopoulos, Rishabh Jain, Naomi Harte
**链接**: [2604.00982](https://arxiv.org/abs/2604.00982)
**分类**: Audio-Visual Speech Recognition | **关键词**: Audio-Visual Speech Recognition, Multi-task Training, Visemes

## 核心痛点
当前音频-视觉语音识别（AVSR）系统虽然集成了大型语言模型解码器，但改进是来自于语言建模还是音频-视觉编码不明确；此外，音素或视素信息的整合在AVSR中较少被探索，限制了模型在噪声条件下的鲁棒性。

## 方法创新
提出了Viseme-Guided AV-HuBERT (VisG AV-HuBERT)，一个多任务微调框架，通过辅助视素分类来增强模型对视觉发音特征的依赖。该方法扩展了AV-HuBERT，添加了一个轻量级的视素预测子网络，使用混合CTC/CE损失函数进行联合优化。

## 实验结果
在LRS3数据集上评估，VisG AV-HuBERT在基线AV-HuBERT上实现了可比或改进的性能，特别是在重噪声条件下。例如，在-10 dB SNR（语音噪声）下，词错误率从13.59%降至6.60%（相对改进51.4%）。错误分析显示替换错误显著减少，表明语音单元区分能力提升。在LRS2数据集上的评估确认了泛化能力。

## 一句话评价
该工作证明了显式视素建模能有效增强编码器表示，为通过编码器级改进开发噪声鲁棒的AVSR系统提供了新方向。

---

## 3. Description and Discussion on DCASE 2026 Challenge Task 4: Spatial Semantic Segmentation of Sound Scenes

**作者**: Masahiro Yasuda, Binh Thien Nguyen, Noboru Harada, Romain Serizel, Mayank Mishra, Marc Delcroix, Carlos Hernandez-Olivan, Shoko Araki, Daiki Takeuchi, Tomohiro Nakatani, Nobutaka Ono
**链接**: [2604.00776](https://arxiv.org/abs/2604.00776)
**分类**: Sound Event Detection and Separation | **关键词**: Spatial Semantic Segmentation, Sound Event Detection, Source Separation, DCASE Challenge, First-order Ambisonics

# Summary

## Core Pain Points
- Real-world sound scenes often contain multiple sources from the same class (e.g., multiple people talking simultaneously), which introduces ambiguity in detection and separation.
- Mixtures may have zero target sound events, requiring systems to accurately identify silence amidst background noise and interference, posing challenges for continuous operation.

## Methodological Innovations
- Introduction of the CAPI-SDRi (Class-Aware Permutation-Invariant SDRi) metric to handle duplicated labels using permutation-invariant objectives, replacing the previous CA-SDRi.
- Development of the SpAudSyn tool for flexible and reproducible mixture synthesis, providing dry reference signals and JSON parameterization for exact reconstruction.
- Task setting updates for DCASE 2026: allowing repeated labels and zero-target mixtures to better simulate real-world acoustic conditions.

## Experimental Results
- In DCASE 2025 Challenge Task 4, eight teams submitted 24 systems, with most surpassing the baseline and demonstrating notable improvements in sound event detection and separation. Some approaches included iterative schemes for refinement.
- For DCASE 2026, the task is enhanced with new settings, but specific experimental results from submissions are not detailed in this excerpt (as it focuses on task description and dataset).

## One-Sentence Evaluation
This challenge task significantly advances spatial audio processing by incorporating realistic complexities and robust evaluation, driving progress in immersive communication and smart environment applications.

---

## 4. OmniVoice: Towards Omnilingual Zero-Shot Text-to-Speech with Diffusion Language Models

**作者**: Han Zhu, Lingxuan Ye, Wei Kang, Zengwei Yao, Liyong Guo, Fangjun Kuang, Zhifeng Han, Weiji Zhuang, Long Lin, Daniel Povey
**链接**: [2604.00688](https://arxiv.org/abs/2604.00688)
**分类**: Text-to-Speech | **关键词**: Zero-Shot Text-to-Speech, Multilingual, Diffusion Language Models

### 核心痛点
现有零-shot文本到语音（TTS）模型通常仅支持有限语言（如几十种），忽略数百种低资源语言，限制了全球语音技术覆盖。传统的离散非自回归（NAR）模型依赖复杂的两阶段管道（文本到语义，再到声学），导致错误传播和信息瓶颈，影响音频质量和训练效率。

### 方法创新
OmniVoice提出单阶段离散NAR架构，基于扩散语言模型风格，直接映射文本到多码书声学令牌，简化流程并避免两阶段问题。关键创新包括：
- **全码书随机掩码**：随机掩码所有码书令牌（平均50%掩码率），替代传统"逐层"掩码，提升训练收敛速度和生成质量。
- **LLM初始化**：从预训练自回归大语言模型（LLM）初始化Transformer主干，继承语言知识，首次在NAR TTS中应用，显著提高语音可理解性。
- **大规模多语言数据**：构建581k小时开放源数据集，覆盖600+语言，采用语言级重采样策略（β=0.8）平衡高低资源语言，支持广泛覆盖。

### 实验结果
在581k小时多语言数据集上训练，覆盖超过600种语言。在中文、英文和102种语言的多语言基准测试中，实现了最先进（SOTA）性能，在可理解性、说话者相似性和自然度方面优于现有方法。模型还支持多维度控制（如提示去噪、语音属性设计），增强实用性。

### 一句话评价
OmniVoice是首个大规模多语言零-shot TTS模型，通过简化架构和创新训练策略，实现了前所未有的语言覆盖和高质量语音生成，为全球低资源语言提供了可行解决方案。

---

## 5. An Empirical Recipe for Universal Phone Recognition

**作者**: Shikhar Bharadwaj, Chin-Jou Li, Kwanghee Choi, Eunjung Yeo, William Chen, Shinji Watanabe, David R. Mortensen
**链接**: [2603.29042](https://arxiv.org/abs/2603.29042)
**分类**: Speech Recognition | **关键词**: phone recognition, multilingual speech, self-supervised learning, CTC loss, accented English

# 核心痛点
- 现有电话识别模型在多语言和低资源设置中泛化能力不足：英语模型难以适应其他语言，而多语言模型未能充分利用预训练自监督学习表示。
- 缺乏对训练方法（如数据规模、架构、损失目标）影响的系统量化研究，导致性能潜力未完全发挥。

# 方法创新
- 提出PhoneticXEUS模型：基于大规模多语言预训练自监督学习模型XEUS，使用Self-Conditioned CTC损失函数进行微调，结合多语言数据集IPAPack++（约17k小时语音）。
- 设计控制消融实验：评估不同CTC变体（如InterCTC、Hierarchical CTC）、SSL表示（如MMS、XEUS）和数据规模对性能的影响，以建立优化训练配方。

# 实验结果
- 在PRiSM基准测试中，PhoneticXEUS达到最先进性能：多语言数据集平均PFER为17.7%，带口音英语数据集平均PFER为10.6%。
- 消融研究关键发现：
  - SelfCTC损失在跨语言泛化中表现最佳，优于其他CTC变体。
  - SSL表示（如XEUS）显著提升性能，优于从头训练的模型。
  - 增加多语言数据规模改善多语言性能，同时对英语性能无负面影响。
- 分析显示模型在跨语言迁移、口音变异和发音特征识别方面具有鲁棒性。

# 一句话评价
该研究提供了一个实证驱动的训练配方，通过结合大规模多语言数据和自监督学习表示，显著提升了电话识别的多语言泛化能力，推动了语音处理领域的发展。

---

