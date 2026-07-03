# Arxiv Daily Deep Report - 2026-07-03

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 14
---

## 1. Spatial Speech Perception Systems: A Survey of Sound Source Localization, Directional Enhancement, and Speech Recognition

**作者**: Pengyuan Shao, Dimitrios Kanoulas
**链接**: [2607.02296](https://arxiv.org/abs/2607.02296)
**分类**: Unknown | **关键词**: 

无法获取全文内容，跳过总结。

---

## 2. Cross Domain Few-Shot Class-Incremental Audio Classification Via Adversarial Contrastive Learning

**作者**: Yongjie Si, Yanxiong Li, Sen Huang, Beibei Liu
**链接**: [2607.02254](https://arxiv.org/abs/2607.02254)
**分类**: Audio Classification | **关键词**: Few-shot class-incremental learning, audio classification, cross domain, adversarial contrastive learning

### 核心痛点
现有小样本增量音频分类（FCAC）方法假设基类与增量类样本同分布，但实际应用中存在域偏移。本文首次提出跨域小样本增量音频分类（CD-FCAC）问题，同时面临类增量导致的灾难性遗忘和域偏移两大挑战。

### 方法创新
提出对抗对比学习策略（Adversarial Contrastive Learning），融合对抗训练与对比学习：
- **对抗训练**：通过频谱扰动生成对抗样本模拟目标域，训练编码器提取域不变嵌入。
- **对比学习**：基训练阶段使用监督对比损失增强类内紧凑性和类间可分性。
- **增量训练**：冻结编码器，仅更新分类器，并保存旧类嵌入均值以缓解遗忘。

### 实验结果
在LS-100、NSynth-100、FSC-89三个公共数据集构成的六组跨域对上进行实验，平均准确率超过现有方法。

### 一句话评价
首次系统性地解决跨域小样本增量音频分类问题，提出的对抗对比学习策略有效提升模型在域偏移和类增量场景下的泛化能力。

---

## 3. An Efficient vLLM-Based Inference Pipeline for Unified Audio Understanding and Generation

**作者**: Haoran Wang, Jinchuan Tian, Siddhant Arora, Shinji Watanabe
**链接**: [2607.02119](https://arxiv.org/abs/2607.02119)
**分类**: Unknown | **关键词**: 

无法获取全文内容，跳过总结。

---

## 4. LMPAN: A Lightweight Multi-Path Alignment Network for Joint Full-Duplex Acoustic Echo Cancellation and Noise Suppression

**作者**: Chengwei Liu, Shaofei Xue, Haoyin Yan, Xiaotao Liang, Zheng Xue
**链接**: [2607.02062](https://arxiv.org/abs/2607.02062)
**分类**: Unknown | **关键词**: 

无法获取全文内容，跳过总结。

---

## 5. Neural Audio Codec with Adjustable Token Temporal Resolution Using Sampling-Frequency-Independent Convolutional Layers

**作者**: Tomohiko Nakamura, Wataru Nakata, Kanami Imamura, Yuki Saito
**链接**: [2607.01865](https://arxiv.org/abs/2607.01865)
**分类**: Unknown | **关键词**: 

无法获取全文内容，跳过总结。

---

## 6. Self-Supervised Test-Time Tuning for Packet Loss Concealment

**作者**: Yehoshua Dissen, Joseph Keshet
**链接**: [2607.01823](https://arxiv.org/abs/2607.01823)
**分类**: Unknown | **关键词**: 

无法获取全文内容，跳过总结。

---

## 7. Enhancing Acoustic-to-Articulatory Inversion with Multi-Target Pretraining for Low-Resource Settings

**作者**: Jesuraj Bandekar, Prasanta Kumar Ghosh
**链接**: [2607.01594](https://arxiv.org/abs/2607.01594)
**分类**: Acoustic-to-Articulatory Inversion | **关键词**: Acoustic-to-Articulatory Inversion, Multi-Target Pretraining, Low-Resource, Self-Supervised Learning, Speech Processing

## 总结

### 核心痛点
- Acoustic-to-Articulatory Inversion (AAI) 在低资源场景下性能受限，因为高质量声学-发音数据稀缺。
- 现有的 Self-Supervised Learning (SSL) 特征提取器虽能提升性能，但引入了推理延迟和计算开销，不适合实时应用。

### 方法创新
- 提出一种多目标预训练方法，在预训练阶段使用三种目标表示：
  1. **Phoneme Labels**：帧级音素标签，使用交叉熵损失。
  2. **Articulatory Feature Labels**：发音特征（place, manner, height, backness），使用四个线性层和交叉熵损失。
  3. **Critical-articulator Labels**：12维二元向量，标识关键发音器官，使用二元交叉熵损失，并对非关键音素掩码损失。
- 预训练后，替换输出层为12维线性层以预测EMA轨迹，进行微调。
- 使用非自回归Transformer架构，无需额外SSL模型，降低推理成本。

### 实验结果
- 在SpireEMA数据集上，使用不同比例训练数据（6.25%至100%）评估。
- 使用MFCC和TERA特征作为输入。
- 对比基线（无预训练）和SSL-based模型。
- 在seen speakers和unseen speakers测试集上，所提方法（如ACP-T、AC-T等）在低资源（6.25%数据）下显著提升CC（相关系数）和降低RMSE（均方根误差），且推理时间更短。
- 例如，6.25%数据时，ACP-T的CC从0.7348提升至0.7811（seen speakers），RMSE从1.4394降至1.3535。

### 一句话评价
该论文提出了一种高效的多目标预训练方法，在不增加推理开销的前提下，显著提升了低资源AAI性能，尤其适用于实时或资源受限场景。

---

## 8. Beyond Words: Towards Effective Modeling of Non-Verbal Vocalizations in ASR

**作者**: Gene Yang, Haibin Wu, Peng Su, Ruizhe Huang, Suwon Shon, Bach Do, Minxue Niu, Zhaoheng Ni, Shang-Wen Li, Florian Metze, Yossi Adi, Ming Sun, Yuzong Liu
**链接**: [2607.01563](https://arxiv.org/abs/2607.01563)
**分类**: Unknown | **关键词**: 

无法获取全文内容，跳过总结。

---

## 9. Few-Shot Open-Set Audio Classification Using Attention Information-Fused Prototypes

**作者**: Yanxiong Li, Jiaxin Tan, Qianqian Li, Guoqing Chen, Sen Huang, Tuomas Virtanen
**链接**: [2607.01297](https://arxiv.org/abs/2607.01297)
**分类**: Unknown | **关键词**: 

无法获取全文内容，跳过总结。

---

## 10. CNN Models for Microphone Array Covariance Matrix Upsampling and Acoustic Imaging

**作者**: Marianthi Adamopoulou, Parthasaarathy Sudarsanam, David Diaz-Guerra, Meng Jiang, Archontis Politis, Seyed Jalaleddin Mousavirad, Tuomas Virtanen, Jan Lundgren
**链接**: [2607.01295](https://arxiv.org/abs/2607.01295)
**分类**: Unknown | **关键词**: 

无法获取全文内容，跳过总结。

---

## 11. Audio-Based Understanding of Audiobook Narration Appeal

**作者**: Shahar Elisha, Mariano Beguerisse-Díaz, Emmanouil Benetos
**链接**: [2607.02473](https://arxiv.org/abs/2607.02473)
**分类**: Speech Paralinguistics / Audiobook Analysis | **关键词**: audiobooks, narration style, speech paralinguistics, audio processing, appeal prediction, view-rate, genre-specific modelling

## 论文总结

**核心痛点**：有声书叙述风格对听众吸引力的影响缺乏大规模数据驱动研究，现有工作局限于小样本或定性分析，无法为推荐系统和角色分配提供量化依据。

**方法创新**：
- 使用LibriVox公开数据集（8,854本有声书，1,206位叙述者，65种体裁），提取129维声学与韵律特征（通过eGeMAPSv02、YAMNet、whisper-tiny）。
- 建立全局Generalized Linear Model (GLM)、按体裁GLM和按书名（同一文本不同录音）的Linear Mixed-Effects (LME)模型，分离内容与叙述风格的影响。
- 将观看率按四分位数分类，训练逻辑回归等分类器与排序模型。

**实验结果**：
- 声学特征与观看率存在显著统计关联，且该关联在控制书名效应后仍然稳健。
- 不同体裁中声学特征的影响模式不同。
- 分类和排序任务中，声学特征具有预测能力，验证了叙述风格对吸引力的独立贡献。
- 使用Spotify内部细粒度指标复现了类似结论。

**一句话评价**：首次系统性、大规模地将有声书叙述声学特征与真实消费数据（观看率）关联起来，为个性化推荐和叙述者选择提供了数据驱动方法。

---

## 12. Unlocking Speech-Text Compositional Powers: Instruction-Following Speech Language Models without Instruction Tuning

**作者**: Congrui Du, Yang Zhang, Kaizhi Qian, Shiyu Chang
**链接**: [2607.02214](https://arxiv.org/abs/2607.02214)
**分类**: Speech Language Models | **关键词**: instruction-following, speech language model, model merging, catastrophic forgetting, pre-training

## 核心痛点
现有语音语言模型（SLM）训练遵循文本大语言模型范式，依赖大规模语音指令调优数据，面临两大瓶颈：
1. **数据膨胀**：语音序列长度是文本的20倍以上，导致有效数据规模严重不足。
2. **灾难性遗忘**：在大量语音token上继续训练会使模型遗忘原始文本LLM的知识和能力。

## 方法创新
提出**SPEECHCOMBINE**，一种无需指令调优的语音语言模型训练框架：
- 从文本LLM基座模型出发，仅进行**一次语音连续预训练**（30k小时数据），得到语音适配模型。
- 利用**模型合并**（model merging）技术，将文本指令调优模型的权重差异（Δθ_inst）直接移植到语音适配模型上，实现指令跟随能力向语音域的迁移。
- 关键设计：语音预训练必须从基座模型开始，而非指令调优模型，以保证知识结构的可组合性。

## 实验结果
- SPEECHCOMBINE能够同时遵循**文本导向指令**、**语音理解指令**（如情感、重音查询）和**语音生成指令**（如带情感约束的语音输出），而两个组合方向（Δθ_speech和Δθ_inst）均未接触过语音相关指令训练。
- 模型保留了文本LLM的**长思考能力**等高级特性。
- 验证了模型合并策略的有效性：仅需一次轻量预训练即可获得强指令跟随能力，摆脱对海量语音数据的依赖。

## 一句话评价
SPEECHCOMBINE通过创新的模型合并策略，在无需指令调优的情况下实现了跨模态指令跟随能力，为SLM训练开辟了新方向。

---

## 13. Rethinking Speech-LLM Integration for ASR: Effective Joint Speech-Text Training by Interleaving

**作者**: Ruchao Fan, Yiming Wang, Rui Zhao, Liliang Ren, Keqi Deng, Xiaoyang Chen, Ali Zare, Bo Ren, Yuxuan Hu, Junkun Chen, Yan Huang, Yelong Shen, Jinyu Li
**链接**: [2607.01733](https://arxiv.org/abs/2607.01733)
**分类**: Unknown | **关键词**: 

无法获取全文内容，跳过总结。

---

## 14. SPARCLE: SPeaker-aware Aligned Representations via Contrastive Language Embeddings

**作者**: Priyam Mazumdar, Yurii Halychanskyi, Steven Guo, Mark Hasegawa-Johnson, Volodymyr Kindratenko
**链接**: [2607.01238](https://arxiv.org/abs/2607.01238)
**分类**: Text-to-Speech | **关键词**: text-to-speech synthesis, grapheme-to-phoneme conversion, acoustic alignment, contrastive learning, speaker-aware

## 核心痛点
- 传统基于音素的TTS需要G2P转换，依赖昂贵的音素标签或手工规则，且无法捕捉说话人特定的声学变体。
- 基于字符的模型虽可扩展，但在低资源场景下性能不如音素模型，且存在发音歧义。

## 方法创新
- 提出SPARCLE模型：通过对比学习将字符嵌入与Wav2Vec2声学表示对齐，同时使用FaCodec音色嵌入作为说话人条件。
- 字符对齐：利用强制对齐获得字符与声学帧的映射，通过注意力池化处理一对多映射。
- 架构：字符Transformer（12层，12头，768维），结合1D卷积捕获局部上下文，说话人嵌入预置。
- 预训练：在LibriSpeech-960h上训练200K步，损失为对比损失（温度0.1）。

## 实验结果
- 在VCTK数据集上，SPARCLE作为TTS后端（ParrotTTS和VITS）的嵌入替代，显著降低WER和EER。
- 极端低资源（10分钟训练数据）下，WER从85.7%降至42.2%（+T）- 相比字符基线提高50%。
- 在更多数据（1小时）下，ParrotTTS WER从24.8%降至9.2%，VITS WER从121.7%降至117.3%。
- 跨域泛化：在LibriSpeech（美式英语）预训练，在VCTK（英式英语）微调仍有效。

## 一句话评价
SPARCLE通过对比学习融合声学与发音人信息，显著提升低资源TTS的发音准确性，是对G2P系统的有效替代。

---

