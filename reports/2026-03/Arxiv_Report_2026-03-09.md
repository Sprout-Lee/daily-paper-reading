# Arxiv Daily Deep Report - 2026-03-09

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 11
---

## 1. Doctor or Patient? Synergizing Diarization and ASR for Code-Switched Hinglish Medical Conditions Extraction

**作者**: Séverin Baroudi, Yanis Labrak, Shashi Kumar, Joonas Kalda, Sergio Burdisso, Pawel Cyrta, Juan Ignacio Alvarez-Trejos, Petr Motlicek, Hervé Bredin, Ricard Marxer
**链接**: [2603.06373](https://arxiv.org/abs/2603.06373)
**分类**: Speech Recognition | **关键词**: speaker diarization, speaker-attributed automatic speech recognition, medical condition extraction, code-switching, Hinglish

## 核心痛点
提取患者医疗条件从代码切换的Hinglish（印地语-英语混合）临床对话中面临重大挑战，包括快速说话人交替、高度重叠语音、多语言代码切换、嘈杂远场录音和自发语音，这些因素复杂化了标准提取流程。

## 方法创新
提出一个级联系统：1）使用端到端神经说话人日记化与向量聚类（EEND-VC）处理密集和重叠语音，优化用于医生-患者对话；2）通过领域特定微调、Devanagari脚本规范化和对话级LLM错误纠正，适应Qwen3 ASR模型进行转录；3）评估文本级级联系统与多模态端到端音频框架，利用开源和专有LLM进行医疗条件提取。

## 实验结果
在DISPLACE-M数据集（真实世界Hinglish医疗对话）上评估，系统达到18.59%的tcpWER（转录错误率），在DISPLACE-M挑战中获得第一名（25名参与者）。实验还对比了不同LLM性能，专有端到端模型设定了性能上限，而开源级联架构具有高度竞争力。

## 一句话评价
该系统通过协同说话人日记化和ASR，在代码切换医疗对话提取中实现了优异性能，为低资源语言和现实环境提供了有效、可复现的解决方案。

---

## 2. Cross-linguistic Prosodic Analysis of Autistic and Non-autistic Child Speech in Finnish, French and Slovak

**作者**: Ida-Lotta Myllylä, Sofoklis Kakouros
**链接**: [2603.06332](https://arxiv.org/abs/2603.06332)
**分类**: Speech Analysis | **关键词**: prosody, child speech, autism, Finnish, French, Slovak, acoustic features, cross-linguistic

**核心痛点**: 自闭症韵律差异的跨语言研究证据有限，现有研究多集中于基频（f0）分析，而对声音质量和强度动态的实证数据不足，导致对语言独立标志的识别不全面。

**方法创新**: 本研究采用多语言语料库（芬兰语、法语、斯洛伐克语），从超过5,000个停顿间单元提取88个声学特征，使用主成分分析（PCA）进行降维，并应用线性混合效应模型（LMMs）进行统计分析，以控制语言和说话者间的变异，从而孤立可能区分诊断组的韵律特征。

**实验结果**: 跨语言分析显示，自闭症说话者表现出更高的总体强度变异性、更清晰的声音质量（更高的谐波噪声比和alpha比），但减少了时间强度动态和较低的中央f0。单语分析揭示了语言特定细微差别：斯洛伐克语在基频模式上与跨语言结果一致，但在声音质量上有所不同；芬兰语结果与跨语言声音质量发现相似；法语数据因样本量有限未显示显著差异，但贡献于跨语言模型。

**一句话评价**: 该研究挑战了基于缺陷的模型，通过跨语言声学分析提出了自闭症的复杂韵律特征，强调声音质量和强度动态在语言独立标志中的重要性。

---

## 3. Classification of Autistic and Non-Autistic Children's Speech: A Cross-Linguistic Study in Finnish, French, and Slovak

**作者**: Sofoklis Kakouros, Ida-Lotta Myllylä
**链接**: [2603.06327](https://arxiv.org/abs/2603.06327)
**分类**: Speech Classification | **关键词**: autism, speech classification, cross-linguistic, prosody, child speech

**核心痛点**  
自闭症儿童的语音韵律特征在不同语言中可能存在差异，现有研究缺乏跨语言的系统性比较，难以识别哪些声学线索是语言特定的、哪些是语言通用的，这限制了鲁棒分类器的开发。

**方法创新**  
本研究采用跨语言方法，结合监督分类（XGBoost和Random Forest模型）与声学-韵律特征（通过openSMILE工具提取eGeMAPS特征），进行语内和跨语料库转移实验。研究重点不在于追求最优性能，而是作为分析工具，探索语言依赖和共享的线索，并通过特征重要性分析（如TreeSHAP和排列重要性）来识别关键声学标记。

**实验结果**  
- 语内模型：芬兰语性能最佳（准确率0.84，F1 0.88），斯洛伐克语次之（准确率0.63，F1 0.68），法语最差（准确率0.68，F1 0.56）。
- 跨语言转移：所有语料池化模型总体准确率0.61，F1 0.68。留一语料库实验显示，对斯洛伐克语（F1 0.70）和芬兰语（F1 0.78）转移成功，但对法语（F1 0.42）转移较差。
- 特征重要性分析表明，自闭症相关的声学标记部分跨语言共享，但非完全语言不变，提示需要语言感知建模。

**一句话评价**  
这项研究通过跨语言实验揭示了自闭症语音线索的部分共享性，为未来开发语言感知的鲁棒分类器提供了重要基础。

---

## 4. Continual Adaptation for Pacific Indigenous Speech Recognition

**作者**: Yang Xiao, Aso Mahmudi, Nick Thieberger, Eliathamby Ambikairajah, Eun-Jung Holden, Ting Dang
**链接**: [2603.06310](https://arxiv.org/abs/2603.06310)
**分类**: Speech Recognition | **关键词**: Continual Adaptation, Pacific Indigenous Languages, Speech Recognition, Low-Rank Adaptation, Catastrophic Forgetting, Representational Drift

## 核心痛点
语音基础模型在处理低资源太平洋土著语言时面临严重的数据稀缺和分布距离问题，这些语言缺乏大规模标注语料库，且与预训练数据中的高资源语言分布差异大。这导致模型在适应时容易发生灾难性遗忘，并引发可塑性-稳定性的严峻困境。

## 方法创新
本研究提出一个实证框架，使用Whisper-Small作为基础模型，评估了两种适应策略：全参数微调（Full Fine-Tuning）和低秩适应（LoRA）。方法包括交叉语言转移分析、表示漂移量化（通过余弦距离测量内部激活变化）和持续学习分析（序列学习多个语言），以探究适应过程中的内部动力学。

## 实验结果
实验显示，随着训练数据量增加，字符错误率（CER）和词错误率（WER）普遍改善，但LoRA在序列学习中遭受严重灾难性遗忘，而全参数微调导致更大内部表示漂移。表示漂移分析证实适应引发模型内部重组，突出了当前方法在稳定性上的不足。

## 一句话评价
本研究强调了为低资源、代表性不足语言开发数据高效且结构鲁棒的适应策略的紧迫性，以应对语音识别中的公平性和可扩展性挑战。

---

## 5. StreamVoiceAnon+: Emotion-Preserving Streaming Speaker Anonymization via Frame-Level Acoustic Distillation

**作者**: Nikita Kuzmin, Kong Aik Lee, Eng Siong Chng
**链接**: [2603.06079](https://arxiv.org/abs/2603.06079)
**分类**: Speaker Anonymization | **关键词**: Speaker Anonymization, Emotion Preservation, Streaming Speech Processing, Knowledge Distillation

## 核心痛点
流式说话者匿名化（SA）在保留情感内容方面面临挑战，主要问题包括：1. 基于神经音频编解码器语言模型的音频延续训练范式倾向于退化源情感，模型默认到主导声学模式而非保留副语言属性；2. VQ瓶颈丢弃了携带情感信息的细粒度声学细节，导致情感退化。

## 方法创新
提出StreamVoiceAnon+方法，通过以下创新点解决情感保留问题：1. 监督微调（SFT），使用相同说话者的中性-情感话语对进行训练，强制模型从源内容生成情感输出而非复制提示模式；2. 帧级情感蒸馏，在声学令牌隐藏状态上应用蒸馏损失，隔离情感学习与内容监督，避免梯度竞争。所有修改仅限于微调阶段，无推理延迟增加，流式延迟保持180ms。

## 实验结果
在VoicePrivacy 2024协议上评估：1. 情感保留（UAR）达49.2%，相对于基线（39.7%）提升24%；2. 可理解性（WER）为5.77%；3. 隐私（EER）为49.0%，保持较强隐私。与先前沿流式方法相比，实现了最高的情感保留和零推理开销。

## 一句话评价
StreamVoiceAnon+通过改进训练范式和引入帧级蒸馏，有效提升流式说话者匿名化中的情感保留，同时维持隐私和可理解性，适用于实时隐私保护应用。

---

## 6. Activation Steering for Accent-Neutralized Zero-Shot Text-To-Speech

**作者**: Mu Yang, John H. L. Hansen
**链接**: [2603.05977](https://arxiv.org/abs/2603.05977)
**分类**: Text-to-Speech | **关键词**: Text-To-Speech, activation steering, accent neutralization, accent conversion, zero-shot TTS

## 核心痛点
零-shot Text-to-Speech (TTS) 模型在生成语音时，难以解耦口音和音色等语音特征，导致输出常同时继承参考语音的口音和音色，限制了其在口音自由语音克隆等应用中的实用性。

## 方法创新
提出一种新颖的、后处理的、无需训练的方法，称为激活引导（activation steering）。首先离线提取层特定的引导向量（steering vectors），这些向量基于TTS模型内部激活在带口音和中性语音之间的差异。在推理时，应用这些引导向量来引导模型生成口音中和、音色保留的语音，方法基于Qwen3-TTS模型实现，采用单层引导策略。

## 实验结果
实验使用ARCTIC和L2-ARCTIC数据集提取引导向量，并在L2-ARCTIC和speechocean762数据集上进行评估。结果显示，引导向量能有效减少输出口音（如降低口音匹配率AMR-CN，提高中性口音匹配率AMR-US），同时对未见说话者表现出强泛化能力。音色相似度得到较好保持，方法高效且适用于实时应用。

## 一句话评价
该方法为口音中和零-shot TTS提供了一种高效、实用的解决方案，无需额外训练，具有广泛的应用前景，如语音克隆和语言学习辅助。

---

## 7. Reconstruct! Don't Encode: Self-Supervised Representation Reconstruction Loss for High-Intelligibility and Low-Latency Streaming Neural Audio Codec

**作者**: Junhyeok Lee, Xiluo He, Jihwan Lee, Helin Wang, Shrikanth Narayanan, Thomas Thebaud, Laureano Moro-Velazquez, Jesús Villalba, Najim Dehak
**链接**: [2603.05887](https://arxiv.org/abs/2603.05887)
**分类**: Neural Audio Codec | **关键词**: neural audio codec, streaming model, self-supervised representation

# 核心痛点
现有神经音频编解码器主要优化为梅尔频谱重建，导致音频可理解性差；语义编码器蒸馏（SED）方法仅关注编码器，不保证解码器输出的可理解性，且可能引入声学质量下降问题。

# 方法创新
提出了自监督表示重建（SSRR）损失，将自监督表示（如 W2V-BERT 2.0）作为重建目标，直接优化编解码器输出以重建这些表示，从而提高可理解性并加速训练。该方法整合到 JHCodec 中，这是一个零预视、流式 Transformer 架构的编解码器，支持低延迟应用。

# 实验结果
SSRR 损失显著加速训练收敛，使用单 GPU 即可达到竞争性能；提高音频可理解性指标（如词错误率 WER）；实现高可理解性且无需额外预视机制，降低延迟。JHCodec 在实验中表现出最先进的性能，同时保持低训练成本。

# 一句话评价
JHCodec 结合 SSRR 损失，有效解决了神经音频编解码器在可理解性与低延迟之间的权衡，是一个实用的流式音频压缩方案。

---

## 8. ImKWS: Test-Time Adaptation for Keyword Spotting with Class Imbalance

**作者**: Hanyu Ding, Yang Xiao, Jiaheng Dong, Ting Dang
**链接**: [2603.05821](https://arxiv.org/abs/2603.05821)
**分类**: Speech Recognition | **关键词**: Keyword Spotting, Test-Time Adaptation, Class Imbalance

### 核心痛点
关键词识别（KWS）在环境噪声中准确性下降，现有测试时适应（TTA）方法（如 AdaKWS）在处理严重类别不平衡（稀有关键词 vs 频繁背景声音）时失败，导致标准熵最小化（EM）使模型对频繁类别过于自信，忽略稀有关键词检测。

### 方法创新
论文提出 ImKWS 方法，包含两个创新点：1) 解耦熵最小化（DEM），将标准熵分解为奖励分支和惩罚分支，通过可调参数独立控制更新强度，缓解类别不平衡导致的偏置；2) 多视图一致性损失，通过音频变换增强预测一致性，确保梯度稳定并抑制噪声样本影响。方法结合两阶段样本选择策略优化适应过程。

### 实验结果
在 Google Speech Commands 数据集上模拟严重不平衡（关键词:非关键词 = 1:8）和不同信噪比（SNR）噪声环境，ImKWS 在宏 F1 分数上显著优于基线方法（如 TBN、Tent、SAR、ETA、AdaKWS）。例如，在 ESC-50 噪声下，ImKWS 在 SNR = -10 dB 时宏 F1 比 AdaKWS 提高 1.23%，显示其在低 SNR 和不平衡场景下的鲁棒性。

### 一句话评价
该论文首次针对现实不平衡场景的 KWS TTA 提出有效解决方案，通过解耦熵和一致性正则化显著提升了适应性能，为轻量级语音模型的动态部署提供了新思路。

---

## 9. Activation Steering for Accent Adaptation in Speech Foundation Models

**作者**: Jinuo Sun, Yang Xiao, Sung Kyun Chung, Qiuchi Hu, Gongping Huang, Eun-Jung Holden, Ting Dang
**链接**: [2603.05813](https://arxiv.org/abs/2603.05813)
**分类**: Speech Recognition | **关键词**: accent adaptation, activation steering, speech foundation models

# 详细总结

## 核心痛点
口音变异性是自动语音识别（ASR）系统的主要错误来源，导致用户群体间性能差异，影响公平性和可访问性。现有方法如参数微调或参数高效微调（PEFT）成本高、缺乏控制，且未理解口音信息在模型中的编码位置。

## 方法创新
论文提出将口音变化视为隐藏表示中的可解释子空间，通过在激活空间中进行层间分析和控制。方法包括：提取编码器层激活，估计口音诱导的平均偏移方向；使用 Accent Alignment Score（AAS）和特异性分数量化层对口音的敏感性，发现口音信息集中在中间编码器层；引入无参数激活转向，在推理时通过注入转向向量修改表示，而无需更新模型权重。

## 实验结果
在 VCTK 和 L2-ARCTIC 数据集上，针对八个口音（如苏格兰、南美、西班牙等）进行实验。结果显示，中间层对口音最敏感，激活转向能显著降低词错误率（WER），提高 ASR 性能。

## 一句话评价
该方法为语音基础模型的口音适应提供了可解释、高效且可扩展的解决方案，增强了 ASR 的鲁棒性和公平性。

---

## 10. Whisper-CD: Accurate Long-Form Speech Recognition using Multi-Negative Contrastive Decoding

**作者**: Hoseong Ahn, Jeongyun Chae, Yoonji Park, Kyuhong Shim
**链接**: [2603.06193](https://arxiv.org/abs/2603.06193)
**分类**: Speech Recognition | **关键词**: speech recognition, contrastive decoding, long-form asr, inference-time, hallucination mitigation

### 核心痛点

长语音识别中，大型编码器-解码器模型如 Whisper 常出现幻觉（如虚构词、重复循环、内容省略），错误在分段处理时积累和放大，尤其在利用前段转录作为解码上下文时加剧。

### 方法创新

提出 Whisper-CD，一个训练免费的对比解码框架，基于多负信号对比：使用三种音频扰动（高斯噪声注入、静音信号、音频时间偏移）生成负 logits，通过 log-sum-exp 聚合形成统一目标，在推断时逐令牌解码以抑制幻觉。

### 实验结果

在五个英语长语音基准测试（如 CORAAL、Earnings22）中，Whisper-CD 显著减少词错误率（WER），最高降低 24.3 百分点，生成吞吐量比波束搜索快 48%，且兼容现有 Whisper 系统无需重训练。

### 一句话评价

Whisper-CD 是一种高效、无需训练的解码时方法，能有效解决长语音识别中的多样错误模式，提升准确性和实用性。

---

## 11. Omni-C: Compressing Heterogeneous Modalities into a Single Dense Encoder

**作者**: Kin Wai Lau, Yasar Abbas Ur Rehman, Lai-Man Po, Pedro Porto Buarque de Gusmão
**链接**: [2603.05528](https://arxiv.org/abs/2603.05528)
**分类**: Multimodal Learning | **关键词**: Multimodal learning, Contrastive learning, Unified encoder

# 核心痛点
现有多模态系统通常依赖单独的专业模态编码器（如图像、音频、文本编码器），导致系统复杂性和计算开销随模态数量线性增加。统一模型如Mixture-of-Experts (MoE) 虽然尝试解决，但引入参数膨胀、路由开销和更高训练复杂度，仍需多编码器并行加载。

# 方法创新
本文提出Omni-C（Omni-Compress），一个基于Transformer的单一密集编码器，通过无模态对比自监督学习在大型未对齐数据上预训练，学习跨异构模态（图像、音频、文本）的共享表示。关键创新包括：最大化参数共享的主干网络、轻量级模态特定投影头缓解模态间冲突，无需MoE、配对监督或路由机制。设计支持顺序模态处理和低内存推理，适合内存受限系统部署。

# 实验结果
实验显示Omni-C在单模态任务（如图像分类）和跨模态任务（如检索和零射推断）中达到与专业模型相当的性能。零射性能在音频和文本上略有下降，但通过轻量级线性探测或参数高效微调（如SBoRA）可大幅恢复。与多编码器基线相比，推理内存使用显著减少，提高效率。t-SNE可视化表明模态在嵌入空间中形成清晰分离的簇，同时保持了模态内判别力。

# 一句话评价
Omni-C通过简化架构和自监督学习，实现高效统一的多模态表示学习，为降低系统复杂性和内存开销提供了创新解决方案。

---

