# Arxiv Daily Deep Report - 2026-03-25

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 7
---

## 1. Prompt Amplification and Zero-Shot Late Fusion in Audio-Language Models for Speech Emotion Recognition

**作者**: Saurabh Kataria, Xiao Hu
**链接**: [2603.23057](https://arxiv.org/abs/2603.23057)
**分类**: Speech Emotion Recognition | **关键词**: Speech Emotion Recognition, Audio-Language Models, Zero-Shot, Late Fusion, Prompt Engineering

# 论文详细总结

## 核心痛点
- Audio-Language Models (ALMs) 在语音情感识别 (SER) 任务中具有零样本预测能力，但存在情感模糊性和对提示选择敏感的问题，导致性能不稳定。
- 专门的 Foundation Models (FMs) 在封闭式 SER 任务中表现最佳，但如何结合 ALMs 与 FMs 以超越现有 SOTA 性能尚未充分探索。

## 方法创新
- 提出 ZS-Fuse 方法：一种后融合策略，通过将双编码器 ALM 的零样本情绪估计与监督微调的 FM 表示相结合。具体地，使用 LayerNorm 和 concatenation 将零样本分数与 FM 向量融合。
- 引入提示工程技术：包括简单的提示集合（每个情绪类使用三种提示形式）和新颖的提示放大技术，通过重复音频和文本查询来增强零样本能力。提示放大作为可控的放大旋钮，旨在发现更强的零样本性能。

## 实验结果
- 在三个数据集（RAVDESS, MSP-Podcast, IEMOCAP）上评估，使用四种 FMs（WavLM-Base+, WavLM-Large, HuBERT-Base, HuBERT-Large）和三种 ALMs（CLAP, ReCLAP, CLSP）。
- 结果显示，ZS-Fuse 结合 CLSP ALM 时，在多数情况下优于 SOTA 基线（如 WavLM-Large），特别是在 RAVDESS 和 IEMOCAP 数据集上观察到 UAR 改进。
- 提示放大技术能进一步提升性能，但最佳音频-文本重复组合需谨慎选择，以避免意外性能下降。

## 一句话评价
论文通过创新的零样本后融合方法，有效结合了 ALMs 的语义理解和 FMs 的专业能力，为语音情感识别任务提供了新的 SOTA 基准。

## 其他关键点
- 论文强调了双编码器 ALMs（如 CLAP）在零样本 SER 中的潜力，优于生成式 ALMs。
- 实验包括零样本评估和提示放大分析，揭示了模型对重复次数的敏感性和优化挑战。

---

## 2. Modelling Emotions is an Elusive Pursuit in Affective Computing

**作者**: Anders Rolighed Larsen, Sneha Das, Line Clemmensen
**链接**: [2603.23017](https://arxiv.org/abs/2603.23017)
**分类**: Affective Computing | **关键词**: Affective Computing, Emotion Modeling, Categorical Emotion Labels, Continuous Dimensional Models, Emotional Ambiguity

# 核心痛点
论文指出，情感计算中广泛使用的分类情感标签（如Ekman的基本情感，包括happy、sad、anger）掩盖了情感的细微差别、模糊性和主观性。这导致系统不确定性高，应用领域受限，尤其是在处理情感模糊性、混合情感、跨模态不一致和注释者分歧时。分类标签的刚性边界与情感的动态、模糊本质不匹配，挑战了基于单一分类标签的"地面真值"概念。

# 方法创新
论文主张采用连续维度模型（如效价、唤醒和优势，VAD）以更准确地捕捉情感的连续性。提出使用软标签技术、分布模型、模糊分类器和情感分析框架来处理情感模糊性，例如通过多任务学习模型学习注释者特定的标签分布。强调从分类标签转向分布表示，以保留情感的内在模糊性和多样性，从而提高系统的解释性和伦理部署。

# 实验结果
基于对IEMOCAP等数据集的批判分析，论文显示分类标签与VAD值之间存在显著偏差，注释者分歧常见（例如，多数投票掩盖了分歧）。新兴方法如分布模型能更好地处理模糊性，提高召回率和解释性。论文引用相关研究（如软标签技术和模糊分类器）支持连续和分布表示的优势，但实验细节因内容截断而不完整。

# 一句话评价
这篇论文为情感计算领域提供了深刻的批判视角，推动从刚性分类向灵活、连续的情感建模转变，有望提升系统真实性和伦理兼容性。

---

## 3. MSP-Conversation: A Corpus for Naturalistic, Time-Continuous Emotion Recognition

**作者**: Luz Martinez-Lucas, Pravin Mote, Abinay Reddy Naini, Mohammed Abdelwahab, Carlos Busso
**链接**: [2603.22536](https://arxiv.org/abs/2603.22536)
**分类**: Speech Emotion Recognition | **关键词**: Affective Computing, Speech Emotion Recognition, Time-Continuous Annotations, Naturalistic Speech, Emotional Dynamics

# 论文总结

## 核心痛点
- 早期语音情感识别（SER）系统依赖有限数据集和传统机器学习模型，难以捕捉情感表达的动态性和上下文依赖性。
- 现有情感语料库缺乏自然性、时间连续注释、多样性和大规模数据，限制了深度学习方法在动态SER中的应用。

## 方法创新
- 引入了MSP-Conversation语料库，包含超过70小时的对话音频，源自从公开播客，确保自然和自发的情感表达。
- 提供时间连续的情感注释（包括valence、arousal、dominance），使用操纵杆收集瞬时感知，优于传统的utterance-level注释。
- 语料库重叠于MSP-Podcast语料库的子集，便于直接比较in-context与out-of-context注释方法。
- 包括详细说话人日记和预定义数据分区，支持多说话人交互分析和模型训练。

## 实验结果
- 分析显示注释分布可靠，评估者间一致性高，表明标签质量良好。
- 与MSP-Podcast的比较有助于验证时间连续注释的有效性，并促进动态SER研究。
- 基线SER实验使用多种机器学习方法（具体结果未在片段中详述，但论文已概述评估框架）。

## 一句话评价
该语料库为自然环境下动态语音情感识别研究提供了宝贵资源，填补了现有数据集的空白，有望推动情感计算领域的发展。

---

## 4. The Interspeech 2026 Audio Encoder Capability Challenge for Large Audio Language Models

**作者**: Heinrich Dinkel, Jiahao Zhou, Guanbo Wang, Yadong Niu, Junbo Zhang, Yufeng Hao, Ying Liu, Ke Li, Wenwu Wang, Zhiyong Wu, Jian Luan
**链接**: [2603.22728](https://arxiv.org/abs/2603.22728)
**分类**: General Audio Processing | **关键词**: audio encoder, large language model, benchmark, LALM, XARES-LLM

### 核心痛点
大型音频语言模型（LALMs）的性能依赖于音频编码器的语义丰富性，但当前大多数先进LALMs仅使用有限选择（如Whisper）的预训练音频编码器，导致架构多样性瓶颈和集成差距，影响模型的通用理解和生成能力。

### 方法创新
论文提出Interspeech 2026 Audio Encoder Capability Challenge，通过XARES-LLM框架提供统一的生成评估。该框架使用预训练音频编码器作为前端，结合LLM解码器（如SmolLM2-135M），通过训练轻量投影层（如MLP和LoRA）进行连接，评估编码器在分类（Track A：如关键词识别、情感分析）和理解（Track B：如语音转录、音频描述）任务中的表现。挑战设计包括开发轨道（Track A、B）和隐藏轨道（Track A Hidden、B Hidden），以标准化的方式解耦编码器开发与LLM微调。

### 实验结果
在Track A（分类任务）中，THU-Voice以平均分91.2%领先，在ASV2015和VoxCeleb1-Bin等任务中表现优异，显示其强大的音频特征提取能力；THU-HSCI-2以90.8%紧随其后，在FSD50k和GTZAN Genre等任务中突出。Track B（理解任务）中，trans-encoder以平均分65.9%最高，在语音转录和音频描述任务中表现稳健。XARES-LLM框架确保了结果的稳定性和可复现性，硬件差异对排名影响小于1%。

### 一句话评价
该挑战通过创新的生成评估框架，有效推动了音频编码器技术的标准化和性能提升，为下一代多模态语言模型的发展奠定了重要基础。

---

## 5. Who Spoke What When? Evaluating Spoken Language Models for Conversational ASR with Semantic and Overlap-Aware Metrics

**作者**: Naohiro Tawara, Samuele Cornell, Alexander Polok, Marc Delcroix, Lukáš Burget, Shinji Watanabe
**链接**: [2603.22709](https://arxiv.org/abs/2603.22709)
**分类**: Conversational Speech Recognition | **关键词**: conversational speech recognition, speaker diarization, semantic evaluation, overlap-aware metrics, speech language models

# 详细总结

## 核心痛点

对话自动语音识别（CASR）在处理重叠语音、远场噪声和可变说话者数量时仍然具有挑战性。传统评估指标如词错误率（WER）及其变体（如 tcpWER）无法有效捕捉语义错误，并且对重叠区域的识别性能缺乏细粒度分析，限制了系统比较的准确性。

## 方法创新

论文引入了两个关键创新评估指标：
1. **tcpSemER**：扩展时间约束最小排列词错误率（tcpWER），使用基于嵌入的语义相似性（如 MiniLM-L12v2）替代 Levenshtein 距离，以衡量语义错误率，更关注意义改变的错误。
2. **重叠感知分解**：将 tcpWER 和 cpWER 分解为重叠（E_ov）和非重叠（E_1spk）部分，支持独立评估不同区域的识别性能，并提供标准化版本以隔离固有难度。

## 实验结果

在三个数据集（Mixer-6、NOTSOFAR-1、DiPCo）上系统比较了基于 LLM 的系统（包括任务特定 LLM 如 VibeVoice 和 Voxtral Mini Transcribe v2，以及通用多模态 LLM 如 Gemini 3.0 Flash）和模块化流水线系统（如单通道 DiCoW 和多通道 NTT CHiME-8）。主要发现：
- 基于 LLM 的系统在双说话者设置（如 Mixer-6）中表现竞争性，但随着说话者数量和重叠增加（如 DiPCo），性能显著下降。
- 模块化流水线系统在复杂场景中更稳健，特别是在多通道配置下。
- 新指标 tcpSemER 对文本规范化方案更鲁棒（相对变化 3-21% vs. tcpWER 的 17-56%），能有效区分语义和表面错误。

## 一句话评价

该论文通过提出语义和重叠感知指标，为对话 ASR 系统评估提供了更全面和鲁棒的框架，有助于揭示不同方法的优劣并推动领域进步。

---

## 6. Precision-Varying Prediction (PVP): Robustifying ASR systems against adversarial attacks

**作者**: Matías Pizarro, Raghavan Narasimhan, Asja Fischer
**链接**: [2603.22590](https://arxiv.org/abs/2603.22590)
**分类**: Speech Recognition | **关键词**: automatic speech recognition, adversarial attacks, adversarial robustness, adversarial detection

# 核心痛点
自动语音识别 (ASR) 系统在安全关键领域（如自动驾驶、医疗）部署增加，但易受对抗攻击，可能导致严重后果。现有防御方法如输入变换和对抗训练有局限性：输入变换可能被攻击者适应并引入延迟或感知伪影；对抗训练计算成本高、可扩展性差，且常降低良性输入性能。检测方法如 Noise Flooding 计算昂贵，其他方法依赖模型内部信息或对良性变化敏感。

# 方法创新
提出 Precision-Varying Prediction (PVP) 方法，通过改变 ASR 模型推理时的数值精度（如 FP32、FP16、BF16）来增强对抗鲁棒性。核心创新包括：
1. **随机精度采样**：在推理时随机切换精度，使针对特定精度优化的对抗示例失效，提高鲁棒性。
2. **精度多样性检测**：评估输入在多种精度下的转录，计算精度多样性评分（基于词错误率），使用高斯分类器区分对抗示例。方法无需重新训练、模型无关、高效，适用于 Green AI 部署。

# 实验结果
实验使用多种 ASR 模型（CTC、seq2seq、Transformer、Whisper）和攻击类型（Carlini & Wagner、Psychoacoustic），在 LibriSpeech 数据集上进行。结果：
- **鲁棒性提升**：随机精度采样显著降低攻击成功率，良性输入性能无退化。
- **检测性能**：精度多样性检测在多种模型和攻击上表现竞争，能可靠识别对抗示例。
- **自适应攻击评估**：针对多精度优化攻击，PVP 仍保持有效性。

# 一句话评价
PVP 是一种简单、训练无关的方法，有效增强 ASR 系统对抗鲁棒性和检测能力，具有实际应用潜力。

---

## 7. Velocity Potential Neural Field for Efficient Ambisonics Impulse Response Modeling

**作者**: Yoshiki Masuyama, Francois G. Germain, Gordon Wichern, Chiori Hori, Jonathan Le Roux
**链接**: [2603.22589](https://arxiv.org/abs/2603.22589)
**分类**: Spatial Audio Processing | **关键词**: Ambisonics, room impulse response interpolation, physics-informed neural network, velocity potential

# 核心痛点
当前方法如物理感知方向感知神经声场（PI-DANF）在插值一阶Ambisonics（FOA）房间脉冲响应（RIR）时，通过软惩罚项将神经网络输出正则化以遵循物理原理（如线性动量方程）。然而，PI-DANF的预测结果仍可能偏离物理方程，无法保证严格遵循，导致在测量数据有限时重建精度受限。

# 方法创新
本研究提出速度势神经场（VPNF），通过建模单通道速度势函数来重构FOA信号。VPNF使用神经网络近似速度势函数，然后通过自动微分计算其对时间和麦克风位置的偏导数，直接得到FOA的四个通道（声音压力和粒子速度）。这种方法确保重构的FOA信号在任意时间和位置自动满足线性动量方程，无需额外惩罚项。此外，VPNF可加入基于波方程的软惩罚项以进一步正则化。网络架构采用改进的多层感知机（MLP）和SIREN激活函数，优化时结合数据保真度损失和物理损失。

# 实验结果
实验在模拟的FOA RIR数据集上进行，使用HARP1工具生成10个随机房间的早期反射数据。评估设置包括从稀疏测量（如30-200个位置）重构RIR。VPNF与基准方法（如普通神经场和PI-DANF）比较，结果显示在测量数据较少时，VPNF在重构精度和物理一致性方面表现更优，确认了其有效性。实验还表明VPNF+变体（通过修改网络参数化）进一步提升了性能。

# 一句话评价
VPNF通过严格整合物理原理到神经网络设计中，显著提高了一阶Ambisonics房间脉冲响应插值的准确性和效率，尤其是在数据有限场景下。

---

