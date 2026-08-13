# Arxiv Daily Deep Report - 2026-05-01

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 5
---

## 1. LRS-VoxMM: A benchmark for in-the-wild audio-visual speech recognition

**作者**: Doyeop Kwak, Jeongsoo Choi, Suyeon Lee, Joon Son Chung
**链接**: [2604.27866](https://arxiv.org/abs/2604.27866)
**分类**: Audio-Visual Speech Recognition | **关键词**: audio-visual speech recognition, benchmark, in-the-wild, LRS-VoxMM, VoxMM, lip reading, visual speech recognition

## 论文总结

### 核心痛点
- 现有AVSR基准（如LRS3）多为受限场景（新闻、Ted演讲），语音清晰，性能饱和，视觉信息贡献不显著。
- 野外数据集（如VoxMM）未标准化为通用基准，预处理繁琐，难以直接使用。

### 方法创新
- **LRS-VoxMM**：从VoxMM中筛选适合AVSR的样本，按LRS风格预处理（音频16kHz，视频25fps 224×224，人脸跟踪对齐），统一目录结构和标签格式。
- **样本筛选**：排除重叠语音、唱歌、部分可见人脸、场景变化等，人工检查确保质量。
- **转录归一化**：数字转口语形式，保留LRS2/3中的填充词，提供SyncNet置信度和强制对齐词级时间戳。
- **合成失真集**：发布4个失真版本（噪声easy/hard、3种失真联合easy/hard），用于评估极端声学退化下的AVSR表现。

### 实验结果
- 所有基线在LRS-VoxMM上的WER显著高于LRS3，证明难度更大。
- 随失真加剧，AVSR优于音频ASR，视觉信息贡献更明显。
- 视觉-only模型表现极差，基准对视觉和声学均具挑战性。
- 复现的Auto-AVSR*（无LRS3训练）在最严重失真下反而更鲁棒。

### 一句话评价
LRS-VoxMM是一个更具挑战性、覆盖多样场景和退化条件的野外AVSR基准，能更好评估视觉信息的实际价值。

---

## 2. BUT System Description for CHiME-9 MCoRec Challenge

**作者**: Dominik Klement, Alexander Polok, Nguyen Hai Phong, Prachi Singh, Lukáš Burget
**链接**: [2604.27436](https://arxiv.org/abs/2604.27436)
**分类**: Speech Recognition | **关键词**: Audio-Visual Speech Recognition, Target-Speaker ASR, LLM-driven Clustering, CHiME Challenge, Multi-talker Overlapping Speech

# 论文总结

## 核心痛点
- 多说话人自动语音识别在重叠语音场景下难以识别目标说话人，尤其缺乏视觉线索的整合。
- 现有音视频ASR系统在真实未受控场景中表现不佳。
- 官方基线聚类仅依赖语音重叠时长，忽略语义上下文，导致非重叠同组说话人被误分类。

## 方法创新
1. **长文本目标说话人音视频ASR系统**：
   - 使用预训练的NVIDIA Parakeet-v2 ASR模型作为声学编码器，AV-HuBERT作为视觉编码器。
   - 通过可学习权重聚合AV-HuBERT各层特征，经1D卷积和FFN对齐后，采用乘法门控融合机制动态控制视觉与声学信息的比例。
   - 支持单次解码处理长录音（通过填充缺失帧并拼接）。
2. **基于LLM的对话聚类方法**：
   - 使用Qwen3.5大语言模型判断说话人是否活跃（是否有主题），并估计活跃说话人间的话题相似度。
   - 对活跃说话人进行层次凝聚聚类（阈值0.7），对被动说话人则利用语音重叠时长作为距离度量分配到现有簇。

## 实验结果
- 在CHiME-9 MCoRec开发集上：WER 33.7%，聚类F1 0.97，比官方基线分别改进16.2% WER和0.15 F1。
- 在测试集上排名第二，与最佳系统差距极小（WER差0.16%，F1差0.5%）。

## 一句话评价
该工作通过融合预训练音视频模型和LLM驱动聚类，显著提升了多说话人重叠语音场景下的转录和分组性能。

---

## 3. A Knowledge-Driven Approach to Target Speech Extraction in the Presence of Background Sound Effects for Cinematic Audio Source Separation (CASS)

**作者**: Chun-wei Ho, Sabato Marco Siniscalchi, Kai Li, Chin-Hui Lee
**链接**: [2604.27403](https://arxiv.org/abs/2604.27403)
**分类**: Audio Source Separation | **关键词**: Speech separation, target speech extraction, cinematic audio source separation, background sound effects, speech attributes, knowledge-driven, manner-of-articulation

## 核心痛点
传统数据驱动的语音分离方法（如MRX、Demucs等）在电影音频源分离（CASS）中面临挑战：电影音频背景音效复杂多变，且难以获取大量特定条件的训练数据；同时，现有方法忽视了电影脚本这一可用知识源。

## 方法创新
提出一种知识驱动的目标语音提取方法，利用发音方式（manner of articulation）作为辅助知识。框架包括：
1. 将电影音频与脚本进行强制对齐，获取帧级发音方式标注（鼻音、近音、闪音、塞音、擦音、塞擦音、元音共7类）。
2. 构建发音感知分离器：将帧级发音向量（m=7）通过线性投影层与音频特征（d=1025）相加，作为语音提取器的输入。
3. 语音提取器可采用任何目标音频提取架构，输出分离的语音。

## 实验结果
在Sound Demixing Challenge的DNR-nonverbal数据集（训练1000、验证50、测试100段1分钟混合音频）上进行实验。结果表明：使用发音感知嵌入的方法相比不使用任何知识源的方法，在包含背景音效的语音片段上取得更好的分离效果。

## 一句话评价
通过引入发音方式这一语言学知识，有效提升了复杂电影音频中目标语音的提取性能，为知识驱动与数据驱动结合提供了新思路。

---

## 4. Beyond the Baseband: Adaptive Multi-Band Encoding for Full-Spectrum Bioacoustics Classification

**作者**: Eklavya Sarkar, Marius Miron, David Robinson, Gagan Narula, Milad Alizadeh, Ellen Gilsenan-McMahon, Emmanuel Chemla, Olivier Pietquin, Matthieu Geist
**链接**: [2604.27936](https://arxiv.org/abs/2604.27936)
**分类**: Bioacoustics Classification | **关键词**: 多频带编码, 自适应融合, 生物声学, 全频谱, 外差法, 基带, 时间扩展, 预训练模型

## 核心痛点
现有生物声学分类模型大多基于16 kHz采样率预训练，仅能处理0-8 kHz基带，丢失大量动物高频叫声信息（如蝙蝠可达200 kHz）。时间扩展方法虽能压缩高频至基带，但会降低频谱分辨率并增加计算开销。

## 方法创新
提出**自适应多频带编码框架**：将原始音频全频谱分解为多个非重叠频带，通过**外差法**将各频带下变频至基带，分别输入预训练编码器提取特征，再通过五种融合策略（均值池化、门控池化、混合专家、混合门控、自注意力）得到统一表示。该方法兼容任何现有音频模型，无需重新训练。

## 实验结果
在三个数据集（Dogs、CBI、Bats）上使用八种预训练模型和五种融合策略进行实验。表示分析和分类实验表明：融合表示在两个数据集上显著优于基带和时间扩展基线；对于高采样率模型（如48 kHz BirdNET），多频带方法仍能带来额外增益。

## 一句话评价
一种轻量级、即插即用的多频带融合框架，有效利用超声频段信息，显著提升跨物种生物声学分类性能。

---

## 5. Predicting Upcoming Stuttering Events from Three-Second Audio: Stratified Evaluation Reveals Severity-Selective Precursors, and the Model Deploys Fully On-Device

**作者**: Nazar Kozak
**链接**: [2604.27279](https://arxiv.org/abs/2604.27279)
**分类**: Stuttering Prediction / On-device Speech Processing | **关键词**: Stuttering prediction, pre-onset prediction, on-device, severity-selective, stratified evaluation, cross-population transfer, calibration, Apple Neural Engine

### 核心痛点
现有的口吃检测系统只能在事件发生时识别（检测），无法提前预测，导致治疗干预（如合声提示）滞后。音频预测对于闭环干预至关重要，但此前缺乏可部署规模的系统。

### 方法创新
1. **任务定义**：给定一个3秒音频片段，预测下一个连续3秒片段是否包含口吃事件（Block、SoundRep、Prolongation），排除填充词。
2. **模型**：616K参数的4块CNN，包含共享的128维嵌入和两个二分类头（事件检测和预阻塞预测）。联合训练，预阻塞头损失权重为事件头的2倍。
3. **分层评估**：按下一片段实际事件类型分层，发现模型对严重事件（Block AUC 0.601, SoundRep AUC 0.617）有预测能力，对填充词（AUC 0.45）和单词重复（AUC 0.49）无效。
4. **跨群体迁移**：直接应用于儿科口吃儿童语音（FluencyBank Teaching），检测AUC 0.674，预测AUC 0.655，无需微调。
5. **设备端部署**：导出CoreML/ONNX/TFLite，Apple Neural Engine延迟0.25-0.55ms，流式模拟仅用4Hz实时预算的0.54%。Platt校准后ECE从0.177降至0.010。
6. **负消融实验**：记录五种未提升性能的方法（Future-Guided Learning, GRU融合, 时间轴连接, 非对称focal loss, 直接阻塞目标训练）。

### 实验结果
- 测试集预阻塞AUC 0.581 [0.542, 0.619]（95%置信区间排除随机）。
- 分类型：Block 0.601, SoundRep 0.617（置信区间排除随机）；Prolongation 0.520（部分随机）；WordRep 0.480, Interjection 0.429（低于随机）。
- 跨语料库：DisfluencySpeech AUC 0.58-0.60，LibriStutter类似。
- 多种子稳定性：三种种子测试AUC 0.540-0.604。

### 一句话评价
该论文首次实现音频口吃预测并完全在设备端运行，通过分层评估揭示了严重事件的预兆信号，且模型可零样本迁移至儿科临床语音，但整体预测性能仍有提升空间。

---

