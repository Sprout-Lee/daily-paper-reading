# Arxiv Daily Deep Report - 2026-04-28

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 8
---

## 1. Explainable AI in Speaker Recognition -- Making Latent Representations Understandable

**作者**: Yanze Xu, Wenwu Wang, Mark D. Plumbley
**链接**: [2604.23354](https://arxiv.org/abs/2604.23354)
**分类**: Speaker Recognition | **关键词**: Explainable AI, Speaker Recognition, Hierarchical Clustering, Cluster-Class Matching, Liebig Score

## 核心痛点
现有可解释AI（XAI）研究在说话人识别任务中仅关注网络表示的扁平聚类（如K-means），忽略了表示之间可能存在的层次关系。

## 方法创新
1. 首次将层次聚类算法（SLINK和HDBSCAN）用于分析说话人识别网络的表示空间，发现表示存在层次聚类现象（inner hierarchical clustering）。
2. 提出层级聚类-类别匹配（HCCM）算法，自动将层次聚类簇与预定义的语义类别（如性别、国籍）进行一对一匹配，识别出单个或合取语义类别。
3. 设计Liebig分数（L-score），基于木桶原理，诊断匹配性能中限制最大的因素（如召回率或精确率），优于传统F-score。

## 实验结果
论文未在片段中提供详细数值结果，但通过算法评估（Rosenberg方法）验证了层次聚类质量，并使用HCCM成功将部分簇匹配到个体语义类（如“male”、“UK”）及合取类（如“male and UK”）。

## 一句话评价
该工作为理解神经网络的内部表示组织提供了新视角，通过层次聚类分析揭示了说话人识别网络中超越独立簇的复杂结构，并提出可解释的匹配与诊断工具。

---

## 2. Predictive Directional Selective Fixed-Filter Active Noise Control for Moving Sources via a Convolutional Recurrent Neural Network

**作者**: Boxiang Wang, Zhengding Luo, Dongyuan Shi, Junwei Ji, Xiruo Su, Woon-Seng Gan
**链接**: [2604.23144](https://arxiv.org/abs/2604.23144)
**分类**: 主动噪声控制 | **关键词**: Active Noise Control, Selective Fixed-Filter ANC, Sound Source Localization, Moving Source Tracking, Convolutional Recurrent Neural Network

## 核心痛点
传统方向性选择性固定滤波器主动噪声控制（D-SFANC）在应对移动噪声源时存在响应滞后问题，由于依赖当前帧的到达方向（DoA）选择控制滤波器，无法提前适应声源位置变化，导致噪声抑制性能下降。

## 方法创新
提出预测性方向性SFANC（PD-SFANC），利用卷积循环神经网络（CRNN）从多帧参考信号中提取时空特征，预测下一帧的DoA，从而预先选择最合适的预训练控制滤波器。系统采用双模块架构：协处理器（如手机）以帧率运行CRNN进行滤波器预选，实时控制器以采样率执行噪声消除，实现无延迟的主动控制。CRNN通过交叉熵损失训练，所有参数自动学习，无需人工调参。

## 实验结果
数值模拟在多种移动场景下（静态、匀速、变速）对比了多个基线方法（FxLMS、SFANC、D-SFANC、DFG-SFANC），PD-SFANC在噪声追踪能力和动态降噪性能上均表现出优越性。CRNN的DoA预测分类准确率在测试环境下达到86.8%-91.7%（不同信噪比和混响条件）。

## 一句话评价
本文通过CRNN预测移动声源轨迹，实现了对方向性固定滤波器ANC系统的前瞻性控制，显著提升了动态噪声抑制效果，并降低了系统复杂度。

---

## 3. In-Sync: Adaptation of Speech Aware Large Language Models for ASR with Word Level Timestamp Predictions

**作者**: Xulin Fan, Vishal Sunder, Samuel Thomas, Mark Hasegawa-Johnson, Brian Kingsbury, George Saon
**链接**: [2604.22817](https://arxiv.org/abs/2604.22817)
**分类**: Speech Recognition | **关键词**: Word-level Timestamp Prediction, Speech-aware Large Language Model, Granite-speech, Timestamp Embedding Regularization, Data Augmentation

# 论文总结

## 核心痛点
传统的词级时间戳预测通常依赖外部强制对齐工具（如HMM、CTC），需要额外的对齐步骤和词典，且端到端模型可能存在识别准确率与时间戳预测之间的权衡。

## 方法创新
本文在Granite-speech模型基础上提出In-Sync框架，实现联合转录与词级时间戳预测。主要创新包括：
1. **语音长度增强**：拼接连续话语，平衡长尾时间戳分布，提升大时间戳的覆盖。
2. **时间戳嵌入正则化**：引入辅助损失，通过高斯核目标矩阵强制时间戳嵌入的相似度结构，体现单调时序。
3. **减少教师强制**：在自回归生成中随机扰动时间戳输入，增强模型鲁棒性。

## 实验结果
在多个数据集上，In-Sync变体在保持或提升ASR词错误率（WER）的同时，显著降低了时间戳平均偏移（AAS）和畸形样本比例（MAL）。完整策略（长度增强+正则化+减少教师强制）在平均指标上优于混合训练基线。

## 一句话评价
In-Sync通过轻量级训练策略高效地将时间戳预测融入语音大语言模型，无需外部对齐工具，同时提升ASR性能。

---

## 4. All That Glitters Is Not Audio: Rethinking Text Priors and Audio Reliance in Audio-Language Evaluation

**作者**: Leonardo Haw-Yang Foo, Chih-Kai Yang, Chen-An Li, Ke-Han Lu, Hung-yi Lee
**链接**: [2604.24401](https://arxiv.org/abs/2604.24401)
**分类**: Audio-Language Evaluation | **关键词**: large audio-language models, benchmark evaluation, audio understanding, text prior, audio reliance, evaluation methodology

# 总结

## 核心痛点
现有音频语言基准测试未能反映真实的听觉理解能力，模型无需音频输入即可通过文本先验（text prior）获得60-72%的准确率；音频依赖项中仅3.0-4.2%需要完整音频，大部分可通过局部片段解决。

## 方法创新
提出了两个诊断轴：
- **文本先验（Text Prior）**：量化无音频输入时模型的表现，通过Text Backbone、None（无音频）和Full（完整音频）三个设置对比。
- **音频依赖（Audio Reliance）**：通过将音频分割为等长片段，计算保留率（retention rate）和片段充分性，区分片段足够与跨片段依赖。

联合分析将项目分为五类：文本可解（TS）、音频需要（AN）、片段充分（FS）、跨片段（XS）、音频有害（AH）、不可解（UN）。

## 实验结果
- 在MMAU、MMAR、MMAU-Pro三个基准上评估8种LALM。
- 无音频输入时，模型保留60-72%的完整音频准确率。
- 音频依赖项中仅3.0-4.2%需要完整音频，其余可由局部片段解决。
- 文本先验率（R_TP）表明基准测试分数主要反映文本推理而非听觉理解。

## 一句话评价
该论文系统地揭示了音频语言基准测试中的文本先验和局部音频依赖问题，为更可靠的评估设计提供了实用指导。

---

## 5. An event-based sequence modeling approach to recognizing non-triad chords with oversegmentation minimization

**作者**: Leekyung Kim, Jonghun Park
**链接**: [2604.24386](https://arxiv.org/abs/2604.24386)
**分类**: Automatic Chord Recognition | **关键词**: Automatic Chord Recognition, Sequence-to-Sequence, Oversegmentation, Non-triad chords, Token representation, Encoder pre-training, Music Information Retrieval

## 核心痛点
- 自动和弦识别（ACR）面临三大挑战：**过分割**（帧级分类导致的边界不稳定）、**数据稀缺**（标注困难、版权限制）、**数据不平衡**（复杂非三和弦样本少）。
- 现有方法对非三和弦（如七和弦、减七和弦）识别效果差。

## 方法创新
1. **段级序列到序列（Seq2Seq）框架**：将ACR重构为自回归的段级预测任务，仅在边界处检测和弦变化，避免逐帧分类导致的过分割。
2. **两种令牌表示**：
   - **MERGE**：时间令牌 + 和弦令牌（完整和弦标签）。
   - **SPLIT**：时间令牌 + 根音令牌 + 质量令牌（和弦性质），通过分解增加稀有质量的训练数据。
3. **编码器预训练**：基于和弦相似性（WCSR指标的mi-rex criterion）计算嵌入相似度的MSE损失，提升编码器对相似音频的表示能力。

## 实验结果
- 在471首流行歌曲数据集上5折交叉验证，衡量指标：WCSR（7种严格度）和分割质量（SQ，含过/欠分割）。
- 最终模型pTE-DS（预训练+SPLIT令牌+编码器-解码器）在所有指标上超越基线BTC，尤其在严格标准（tetrads）下提升显著（从65.5%到73.2%）。
- SQ方面，pTE-DS（88.6）高于BTC（84.6），主要归功于过分割减少。

## 一句话评价
本文首次将ACR建模为段级Seq2Seq任务，通过创新的令牌分解和预训练策略有效缓解过分割与数据不平衡问题，在复杂和弦识别上取得SOTA。


---

## 6. Speech Enhancement Based on Drifting Models

**作者**: Liang Xu, Diego Caviedes-Nozal, Bastiaan Kleijn, Longfei Felix Yan, Rasmus Kongsgaard Olsson
**链接**: [2604.24199](https://arxiv.org/abs/2604.24199)
**分类**: Audio Enhancement | **关键词**: Speech enhancement, drifting models, diffusion models, consistency models, single-step inference, generative models, latent space, self-supervised learning

### 核心痛点
- 传统扩散模型依赖迭代采样（10-100步），推理延迟高，难以满足实时语音增强需求。
- 判别模型（如RNN、LSTM）易产生频谱过平滑和人工伪影。
- GAN训练不稳定，易模式崩塌。

### 方法创新
- **DriftSE**：基于Drifting Models的生成式框架，将去噪重定义为分布均衡问题，原生实现单步推理（1 NFE）。
- 提出两种范式：**直接映射**（从含噪观测直接映射）和**条件生成**（从高斯先验条件生成）。
- 引入**语义潜在空间**：使用预训练SSL编码器（HuBERT/WavLM）提取帧级特征，在该空间计算漂移场（Drifting Field），通过吸引力（靠近干净分布）和排斥力（远离当前生成分布）驱动映射函数达到均衡。
- 训练无需配对数据，仅通过分布匹配即可优化。

### 实验结果
- 在**VoiceBank-DEMAND**测试集上：
  - 直接映射：PESQ 3.15，SI-SDR 16.1 dB。
  - 条件生成：SCOREQ 4.33。
- 在**DNS Challenge 2020**盲测集上展现最优泛化性能。
- 单步推理，性能超越多步扩散基线（如Consistency Models）。

### 一句话评价
DriftSE以单步生成范式实现了高保真语音增强，兼顾质量与效率，为实时应用提供了新方向。

---

## 7. Talker-T2AV: Joint Talking Audio-Video Generation with Autoregressive Diffusion Modeling

**作者**: Zhen Ye, Xu Tan, Aoxiong Yin, Hongzhan Lin, Guangyan Zhang, Peiwen Sun, Yiming Li, Chi-Min Chan, Wei Ye, Shikun Zhang, Wei Xue
**链接**: [2604.23586](https://arxiv.org/abs/2604.23586)
**分类**: Joint Audio-Video Generation / Talking Head Synthesis | **关键词**: autoregressive diffusion, joint audio-video generation, talking head synthesis, cross-modal modeling, variable-length generation

## 核心痛点
现有联合音频视频生成模型（如双分支扩散Transformer）存在两个缺陷：1) 在去噪全过程中通过交叉注意力机制将高低层次信息完全耦合，而音频和视频的低级实现在本质上是不同的渲染过程，这种均匀耦合导致不必要的纠缠和建模效率降低；2) 非自回归、固定输出长度，无法适应输入文本长度和自然变化的语速。

## 方法创新
提出**Talker-T2AV**自回归扩散框架，将生成分解为两个阶段：
- **高层次跨模态建模**：共享自回归语言模型作为高层时序规划器，将音频和视频编码为时间对齐的潜序列，通过元素级求和融合，以文本为前缀自回归预测下一个联合补丁。
- **低层次模态专有渲染**：两个轻量级扩散Transformer头独立解码隐状态为帧级音频和视频潜变量，分别处理各自信号特性。
该设计天然支持变长输出，且单一模型无需架构修改即可执行联合音频视频生成、音频驱动说话头、视频配音等任务。

## 实验结果
在说话头基准上，Talker-T2AV在唇同步精度、视频质量、音频质量上均优于双分支扩散Transformer基线，同时比级联管线获得更强跨模态一致性，并在音频驱动合成和视频配音上匹配或超越专用系统。

## 一句话评价
一个通过将高低层次解耦、自回归扩散实现灵活变长、强跨模态联合的说话头音频视频生成框架。

---

## 8. Audio2Tool: Bridging Spoken Language Understanding and Function Calling

**作者**: Ramit Pahwa, Apoorva Beedu, Parivesh Priye, Rutu Gandhi, Saloni Takawale, Aruna Baijal, Zengli Yang
**链接**: [2604.22821](https://arxiv.org/abs/2604.22821)
**分类**: Speech Tool Calling Benchmark | **关键词**: Audio2Tool, SpeechLM, Tool Calling, Benchmark, Acoustic Robustness, Multi-tier Reasoning

## 核心痛点
现有语音助手基准测试缺乏领域广度、声学多样性和组合推理复杂性，无法有效评估工具调用能力。级联管道（ASR-LLM）受限于ASR错误传播和副语言特征丢失。

## 方法创新
提出Audio2Tool数据集，包含30,000个查询，覆盖智能汽车、智能家居和可穿戴三个领域。设计八级复杂度层次（直接指令、参数化、多意图、隐式推理、大海捞针、纠正、对话、意图混合），并采用零样本语音克隆TTS和多样噪声模拟真实环境。

## 实验结果
评估多种最新SpeechLM和ASR-LLM管道，在简单命令上性能良好，但在组合性和声学挑战下显著下降。

## 一句话评价
首个针对真实工具调用和声学条件的大规模语音基准，系统性地测试了语音到工具管线的鲁棒性。

---

