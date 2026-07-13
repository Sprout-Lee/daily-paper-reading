# Arxiv Daily Deep Report - 2026-07-13

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 4
---

## 1. Technical Report for MERL's Real-TSE Challenge Submission

**作者**: Dominik Klement, Yoshiki Masuyama, Christoph Boeddeker, Kohei Saijo, Julius Richter, Gordon Wichern, Jonathan Le Roux
**链接**: [2607.09043](https://arxiv.org/abs/2607.09043)
**分类**: Target Speaker Extraction | **关键词**: 目标语音提取, 数据清洗, 多阶段训练, 真实远场, 课程学习, BSRNN, DNSMOS, 说话人相似度

### 核心痛点
现有TSE模型在合成数据上表现优异，但难以泛化到真实远场嘈杂环境，主要原因在于模拟数据与真实数据之间的领域差距。

### 方法创新
- **模型改进**：基于基线BSRNN，将EcapaTDNN-512替换为EcapaTDNN-1024，并将BSRNN深度从6增至10块。
- **数据预处理**：采用ClearerVoice增强、MFA对齐、WER过滤等清洗多源数据；使用真实远场-近讲麦克风对，通过Wiener滤波投影近讲信号到远场并增强。
- **四阶段训练课程**：
  1. 全重叠合成数据预训练（200k步）。
  2. 带噪与混响的模拟对话训练。
  3. 远场单说话人片段训练（含噪声增强）。
  4. 真实远场混合数据训练（含20%合成数据与30%阶段三数据混合）。
- **损失函数**：结合时间域L1损失、多尺度STFT幅度损失、DNSMOS损失和说话人余弦相似度损失。

### 实验结果
- 在挑战赛道2中取得第一名。
- 各阶段逐步提升TER、F1、DNSMOS等指标，第四阶段TER降至0.37，F1达0.88。
- 发现DNSMOS和说话人相似度易被过度优化，通过对抗攻击可将其推至极值而不影响TER或VAD F1。

### 一句话评价
通过高质量数据清洗与多阶段课程训练，简单的TSE模型能在真实远场场景中取得领先性能，凸显数据准备的重要性。

---

## 2. Phone Segmentation and Recognition through Phonological Activation Mapping

**作者**: Shikhar Bharadwaj, Kwanghee Choi, Stephen McIntosh, Chin-Jou Li, Eunjung Yeo, Daisuke Saito, Nobuaki Minematsu, Shinji Watanabe, Jian Zhu, David Harwath, David R. Mortensen
**链接**: [2607.09020](https://arxiv.org/abs/2607.09020)
**分类**: Speech Recognition: Phone Segmentation and Recognition | **关键词**: phone segmentation, phone recognition, self-supervised learning, phonological features, SPAM

## 核心痛点
音素分割与识别是语音处理的基础任务，但传统方法将两者分开建模，且依赖大量人工标注。专家标注一小时语音需40-100小时，成本高且主观性强。

## 方法创新
提出了SPAM（Self-supervised Phonological Activation Mapping）方法，利用自监督语音模型（S3M）的表示空间，通过音系特征向量（如清浊、鼻音等）线性分解，构建每个时间帧的激活映射。在此基础上，设计了两个无需梯度下降的轻量级预测头：
- **分割头**：基于相邻帧SPAM的余弦距离和峰值检测，定位音素边界。
- **识别头**：将每帧的SPAM与PanPhon词典中规范音系向量进行相似度匹配，实现零样本识别。
该方法仅需不到1分钟的标注数据，且能识别训练中未出现的音素。

## 实验结果
在多种语言和数据集（包括低资源语言和非典型语音）上达到强分割和识别性能，具有样本高效性和泛化能力。

## 一句话评价
巧妙利用自监督模型中的音系结构，以极简方式统一了音素分割与识别，兼具解释性和实用性。

---

## 3. ReGen: Hierarchical Multi-Prompt Representation Generation for Efficient Waveform Diffusion Models

**作者**: Sang-Hoon Lee, Ha-Yeong Choi
**链接**: [2607.09134](https://arxiv.org/abs/2607.09134)
**分类**: Text-to-Speech | **关键词**: Representation Generation, Flow Matching, Diffusion Transformer, Neural Audio Codec, Text-to-Speech, Hierarchical Multi-Prompt

# 论文总结

## 核心痛点
- 在低比特率波形生成中，表示对齐（REPA）方法导致隐表示纠缠，限制生成容量，尤其是高频细节丢失。
- 传统CFM模型在低比特率下难以保持语义和声学一致性。

## 方法创新
- **ReGen框架**：在单个DiT中联合估计表示和数据的多个向量场，通过分层结构从语义到波形逐步生成。
- **分层多提示机制**：使用掩码填充策略，同时利用语义（SSL）、声学（Mel）和波形提示进行条件生成。
- **广义流匹配（GFM）**：在向量场空间中引入排斥项，缓解零坍缩问题，提高波形级流匹配的鲁棒性。

## 实验结果
- 在12.5 Hz/400 bps低比特率下，ReGen显著提升波形重建质量。
- **ReGenVoice**（基于LDM的TTS）：在6.25 Hz潜空间运行，仅需4 GPU训练1天，RTF=0.08，达到高语音可懂度（WER）和说话人相似度（SIM）。
- 优于REPA和REPA-H基线。

## 一句话评价
ReGen通过分层表示生成替代表示对齐，在超低比特率下实现了高效、高质量的波形和语音生成。

---

## 4. Optimal Transport-based Semantic Alignment for LLM-based Audio-Visual Speech Recognition

**作者**: Xugang Lu, Peng Shen, Yu Tsao, Hisashi Kawai
**链接**: [2607.09001](https://arxiv.org/abs/2607.09001)
**分类**: Speech Recognition | **关键词**: Audio-visual speech recognition, optimal transport, feature fusion, large language model, semantic alignment, contrastive learning

### 核心痛点
现有基于大语言模型（LLM）的音频-视觉语音识别（LLM-AVSR）方法通常独立预训练音频和视觉编码器，输出经投影后融合作为软提示输入LLM进行识别。但大多数方法未显式处理音频、视觉和文本模态之间的表征差异，导致跨模态集成效果受限。此外，时间同步并不保证语义同步，直接组合时间对齐特征难以有效减少歧义。

### 方法创新
本文提出基于最优传输（OT）的语义对齐框架，在融合前显式弥合模态差距。具体来说：
1. 将音频特征、视觉特征和LLM的语言嵌入建模为共享隐空间中的经验概率分布，使用熵正则化的OT计算模态特征与语言嵌入之间的概率耦合矩阵。
2. OT耦合作为软伪标签监督对比学习，鼓励提取语义一致、跨模态一致的音频-视觉表征。
3. 对齐模块插入编码器和投影层之间，无需修改预训练编码器和LLM架构。

### 实验结果
在LRS3-TED基准上，所提方法在干净和多种SNR的噪声条件下均持续超越强基线，达到当前最佳性能（state-of-the-art）。

### 一句话评价
通过OT将多模态特征显式对齐到LLM的语言空间，显著提升了LLM-AVSR的鲁棒性和准确性。

---

