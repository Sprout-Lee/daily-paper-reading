# Arxiv Daily Deep Report - 2026-02-10

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 8
---

## 1. Input-Adaptive Spectral Feature Compression by Sequence Modeling for Source Separation

**作者**: Kohei Saijo, Yoshiaki Bando
**链接**: [2602.08671](https://arxiv.org/abs/2602.08671)
**分类**: Audio Source Separation | **关键词**: Audio Source Separation, Spectral Feature Compression, Sequence Modeling

# 详细总结

## 核心痛点
- 现有TF-domain dual-path模型广泛使用的band-split (BS)模块存在两个主要限制：1) **非输入自适应**：编码和解码过程不依赖输入，无法利用输入相关的频率模式；2) **参数数量大**：每个子带需要专用编码器和解码器模块，导致模型参数量增加，计算效率低。

## 方法创新
- 提出了**Spectral Feature Compression (SFC)**，一种输入自适应的频率特征压缩方法。SFC使用单一序列建模模块（基于cross-attention或Mamba变体）压缩输入，通过K个查询将频率信息压缩为子带特征。引入了从BS模块启发的**归纳偏置**（如设计位置偏置或查询插入策略），以有效捕捉频率模式，同时保持参数高效和输入自适应。

## 实验结果
- 在音乐源分离（MSS）和电影音频源分离（CASS）任务上进行了实验评估。SFC模块在不同分离器大小和压缩比下 consistently 优于BS模块，性能提升显著。分析显示SFC能自适应地捕获输入中的频率模式，并通过注意力可视化验证了其输入适应性。

## 一句话评价
- SFC通过结合序列建模和归纳偏置，在减少参数的同时提高了音频源分离性能，为高频音频处理任务提供了一种高效且有效的解决方案。

---

## 2. Physics-Guided Variational Model for Unsupervised Sound Source Tracking

**作者**: Luan Vinícius Fiorio, Ivana Nikoloska, Bruno Defraene, Alex Young, Johan David, Ronald M. Aarts
**链接**: [2602.08484](https://arxiv.org/abs/2602.08484)
**分类**: Sound Source Tracking | **关键词**: Variational encoder, Unsupervised learning, Sound source tracking, Physics-guided

### Core Pain Points
Existing methods for sound source tracking face significant challenges: classical array-processing algorithms (e.g., MUSIC, ESPRIT, SRP) require grid searches, precise calibration, and are sensitive to initialization. Supervised learning approaches (e.g., Cross3D, Neural-SRP) rely on costly ground truth position labels, which are difficult to obtain and hinder on-device training. Prior unsupervised methods are either not fully unsupervised, rely on multi-modal data, or suffer from high computational complexity and parameter counts, making them impractical for audio devices.

### Method Innovation
The paper proposes a physics-guided variational model for unsupervised sound source tracking. It utilizes a variational autoencoder structure with a physics-based decoder. Key innovations include:
- A variational encoder processes GCC-PHAT features and microphone array geometry to output parameters of a von Mises-Fisher distribution in latent space.
- A physics-based decoder injects spatial information via backpropagation, enabling unsupervised estimation of source directions without labeled data.
- The model is designed for single-source tracking but includes a theoretical extension to multi-source scenarios.

### Experimental Results
Experiments on real-world data demonstrate that the proposed method:
- Achieves performance comparable to state-of-the-art supervised models (e.g., Cross3D, Neural-SRP).
- Offers computational complexity similar to supervised approaches, making it feasible for practical applications.
- Exhibits robustness to altered microphone array geometries and corrupted microphone position metadata during testing.
- Generalizes well across different experimental setups, with results discussed in three main experiments.

### One-Sentence Evaluation
This paper introduces an efficient and robust unsupervised method for sound source tracking that bridges the gap between classical and supervised approaches, offering practical potential for real-world audio systems.

---

## 3. Cross-Modal Bottleneck Fusion For Noise Robust Audio-Visual Speech Recognition

**作者**: Seaone Ok, Min Jun Choi, Eungbeom Kim, Seungu Han, Kyogu Lee
**链接**: [2602.08293](https://arxiv.org/abs/2602.08293)
**分类**: Speech Recognition | **关键词**: Audio-Visual Speech Recognition, Bottleneck Fusion, Noise Robustness

# 核心痛点

传统自动语音识别（ASR）在噪声环境下性能严重下降，音频-视觉语音识别（AVSR）通过融合音频和视觉模态来提高鲁棒性，但现有融合机制往往次优、计算成本高，且跨模态交互不充分。

# 方法创新

提出 CoBRA（Cross-modal Bottleneck for Robust AVSR），一种基于瓶颈的融合框架。在 Conformer 编码器上引入一组可学习的瓶颈令牌，通过调节信息流实现跨模态交换，避免直接注意力计算以减少开销。探索了 sequential 和 mean fusion 策略，并强调融合深度是关键因素，以 mid-level 融合效果最佳。

# 实验结果

在 LRS2 和 LRS3 数据集上评估，CoBRA 在干净条件下达到词错误率（WER）1.6%（LRS3）和 2.8%（LRS2）。在噪声条件下，相比基线 CM-seq2seq，最大改进达 7.42% WER，在低信噪比（-7.5 dB）下对 babble 噪声相对改进 40.0%。模型使用仅 664 小时训练数据，表现竞争性，优于可比基线，展示了数据效率和噪声鲁棒性。

# 一句话评价

CoBRA 是一种高效、噪声鲁棒的 AVSR 方法，通过瓶颈融合平衡了计算成本和性能，为噪声环境下的语音识别提供了创新解决方案。

---

## 4. Detect, Attend and Extract: Keyword Guided Target Speaker Extraction

**作者**: Haoyu Li, Yu Xi, Yidi Jiang, Shuai Wang, Kate Knill, Mark Gales, Haizhou Li, Kai Yu
**链接**: [2602.07977](https://arxiv.org/abs/2602.07977)
**分类**: Audio Enhancement | **关键词**: Target Speaker Extraction, Keyword-guided, DAE-TSE, Speech Separation, Cocktail Party Problem

# 详细总结

## 核心痛点
传统目标说话人提取系统主要依赖预注册的干净语音作为线索来识别目标说话人，但在许多现实场景（如临时会议或语音助手交互）中，这种线索不可用，限制了现有方法的适用性。

## 方法创新
提出DAE-TSE框架，首次使用关键词（部分转录）作为线索来指定目标说话人。它采用Detect-Attend-Extract范式：通过关键词引导的线索编码器（KCE）检测关键词存在并生成说话人嵌入，KCE结合自动语音识别和说话人验证的联合训练；然后使用Band-Split RNN作为语音提取骨干，从混合语音中提取目标语音。

## 实验结果
实验表明，DAE-TSE在仅使用28.4%完整转录的情况下，优于依赖干净注册语音的标准TSE系统，并提供约100毫秒的关键词定位误差。

## 一句话评价
该工作创新性地利用部分转录作为TSE的线索，为现实场景提供了灵活实用的解决方案。

---

## 5. SoulX-Singer: Towards High-Quality Zero-Shot Singing Voice Synthesis

**作者**: Jiale Qian, Hao Meng, Tian Zheng, Pengcheng Zhu, Haopeng Lin, Yuhang Dai, Hanke Xie, Wenxiao Cao, Ruixuan Shang, Jun Wu, Hongmei Liu, Hanlin Wen, Jian Zhao, Zhonglin Jiang, Yong Chen, Shunshun Yin, Ming Tao, Jianguo Wei, Lei Xie, Xinsheng Wang
**链接**: [2602.07803](https://arxiv.org/abs/2602.07803)
**分类**: Singing Voice Synthesis | **关键词**: zero-shot synthesis, flow matching, large-scale dataset

# Summary of SoulX-Singer Paper

## Core Pain Points
- Existing open-source singing voice synthesis (SVS) systems struggle with robustness and zero-shot generalization to unseen singers.
- Early systems like DiffSinger lacked generalization due to small-scale datasets, while recent methods (e.g., StyleSinger, TCSinger) had limited data (few hundred hours), hindering practical deployment.
- Recent advances (e.g., Vevo2, YingMusic-Singer) rely on melody extraction and lack note-level duration control, causing temporal misalignment and limiting use in music production workflows.

## Method Innovations
- Introduces SoulX-Singer, a high-quality zero-shot SVS model supporting both score-based (MIDI) and melody-based inputs within a unified framework.
- Constructs a large-scale multilingual singing dataset of over 42,000 hours (Mandarin Chinese, English, Cantonese), significantly enhancing generalization.
- Uses a non-autoregressive flow matching model based on Diffusion Transformer (DiT) for efficient synthesis, with a Singing Content Encoder for multimodal feature integration.
- Develops a data processing pipeline for vocal extraction, lyric transcription, and note transcription, and introduces SoulX-Singer-Eval benchmark for standardized zero-shot evaluation.

## Experimental Results
- SoulX-Singer achieves state-of-the-art synthesis quality across multiple languages under diverse musical conditions, as shown in comparative figures against methods like Score-controlled SVS, StyleSinger, TCSinger, and Melody-controlled SVS, YingMusic-Singer, Vevosing.
- The model supports high-fidelity timbre cloning, style transfer, and flexible editing, validated on the dedicated benchmark with 50 unseen singers.

## One-Sentence Evaluation
SoulX-Singer is a groundbreaking zero-shot singing voice synthesis system that combines large-scale data, dual-input control, and advanced modeling to deliver high-quality, flexible, and practical synthesis for real-world applications.

---

## 6. Rho-Perfect: Correlation Ceiling For Subjective Evaluation Datasets

**作者**: Fredrik Cumlin
**链接**: [2602.08552](https://arxiv.org/abs/2602.08552)
**分类**: Subjective Assessment and Reliability in Machine Learning | **关键词**: subjective evaluation, correlation ceiling, reliability measure

# 论文总结

## 核心痛点
主观评分含有固有噪声，限制了模型与人类相关性，但现有可靠性度量如Pearson's correlation ratio、ICC（Intraclass Correlation）、Cronbach's alpha在异方差噪声场景下存在局限性（如假设同方差噪声或难以解释模型性能），导致模型性能评估可能误导，无法区分模型限制与数据质量问题。

## 方法创新
提出ρ-Perfect，一个实用估计方法，用于量化主观评价数据集最高可达相关性上限。它基于完美预测器（定义为条件期望E[Y|X]）与平均评分的Pearson相关系数，通过方差分解在异方差噪声下计算，仅需单个评估的评分分布（无需重复评估）。ρ-Perfect平方近似于两个独立主观评估间的测试-重测相关性，提供了理论验证和实证支持。

## 实验结果
在多个数据集（BVCC、MovieLens、SOMOS、MERP）上验证，使用分裂评分方法（Split-Raters和Split-Ratings）模拟重复评估。结果显示ρ-Perfect平方与实测相关性匹配（如BVCC中ρ-Perfect²≈0.800 vs. Corr≈0.801），有效估计了可靠性上限。比较现有度量时，ρ-Perfect更适应不平衡数据集（如MovieLens），而ICC(2, k)可能高估可靠性。实验证实ρ-Perfect能区分模型性能限制与数据质量不佳情况。

## 一句话评价
ρ-Perfect为AI模型在主观评估数据集上的性能提供了可靠的量化上界，通过量化评分噪声，有助于更准确地评估模型并区分其局限性与数据固有噪声。

---

## 7. SNC: A Stem-Native Codec for Efficient Lossless Audio Storage with Adaptive Playback Capabilities

**作者**: Shaad Sufi
**链接**: [2602.08148](https://arxiv.org/abs/2602.08148)
**分类**: Audio Compression and Storage | **关键词**: audio compression, stem separation, adaptive playback

### Core Pain Points
Current audio formats face fundamental trade-offs: lossless formats like FLAC preserve quality but lack adaptability for different playback environments, lossy formats reduce file size at the cost of fidelity and do not support stem-level access, and spatial audio formats like Dolby Atmos increase file size and licensing barriers. These limitations stem from storing audio as a fixed mix rather than composable elements.

### Method Innovation
The paper introduces the Stem-Native Codec (SNC), a novel audio container format that stores music as independently encoded stems (e.g., vocals, drums, bass) plus a low-energy mastering residual. Key innovations include: exploiting lower information entropy in separated stems for efficient compression, using Opus VBR encoding within a Matroska container, and incorporating metadata for spatial positioning and adaptive playback rules. This architecture enables bit-accurate reconstruction while reducing file size and supporting adaptive features like context-aware playback and user-controlled remixing.

### Experimental Results
SNC was validated on a 2:18 test track, achieving a 38.2% reduction in file size compared to FLAC (7.76 MB vs. 12.55 MB) while maintaining perceptual transparency (STOI = 0.996). The mastering residual had an RMS level of -29.97 dB, capturing only 6.4% of the original energy, and objective metrics like Spectral Convergence (0.0402) and SNR (24.86 dB) confirmed high fidelity. The stems-plus-residual approach successfully decouples compression efficiency from feature richness.

### One-Sentence Evaluation
SNC offers a stem-native audio codec that effectively addresses the trade-off between file size and functionality, enabling efficient lossless storage and adaptive playback capabilities for next-generation audio systems.

---

## 8. MENASpeechBank: A Reference Voice Bank with Persona-Conditioned Multi-Turn Conversations for AudioLLMs

**作者**: Zien Sheikh Ali, Hunzalah Hassan Bhatti, Rabindra Nath Nandi, Shammur Absar Chowdhury, Firoj Alam
**链接**: [2602.07036](https://arxiv.org/abs/2602.07036)
**分类**: Audio Large Language Models | **关键词**: MENASpeechBank, AudioLLMs, persona-conditioned conversations, synthetic speech data, dialect diversity

## 核心痛点
Audio大型语言模型（AudioLLMs）的发展受限于缺乏多样化、对话式和指令对齐的语音-文本数据，特别是在中东和北非（MENA）地区，方言多样性高，真实多说话者录音收集成本高且缓慢，这限制了模型在人物基础和方言覆盖方面的进步。

## 方法创新
引入MENASpeechBank，一个参考语音库，包含约18K高质量语音从124个说话者，覆盖英语、现代标准阿拉伯语和地区阿拉伯语变体。开发了一个可控合成数据管道，包括：构建基于世界价值观调查的人物档案、定义约5K对话场景分类、通过语义相似度匹配人物和场景、使用LLM生成约417K角色扮演对话（用户作为人物，助手作为帮助代理），并合成用户回合以通过参考语音保留说话者身份和多样性。

## 实验结果
论文提到评估了合成和人类录制的对话，并提供分析，但具体实验结果未在截取片段中详细展示。摘要中指出实验旨在评估合成数据对AudioLLM性能的影响，包括对话场景和口语问答任务。

## 一句话评价
这是一项数据为中心的研究，为AudioLLMs提供了关键的语音资源和端到端合成数据管道，有望推动模型在多样化和个性化语音交互中的应用。

---

