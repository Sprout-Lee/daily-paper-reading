# Arxiv Daily Deep Report - 2026-06-04

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 14
---

## 1. Differentiable Articulatory Copy-Synthesis of Biphonic Singing

**作者**: Mateo Cámara, María Pilar Daza-Llin, Fernando Marcos-Macías, José Luis Blanco
**链接**: [2606.04943](https://arxiv.org/abs/2606.04943)
**分类**: Audio Synthesis / Articulatory Synthesis | **关键词**: Biphonic singing, Sygyt, differentiable waveguide, articulatory copy-synthesis, Kelly-Lochbaum model, formant focusing

## 核心痛点
传统发音模型难以复制双声唱歌（如Sygyt）中窄带共振峰聚焦效应，标准低维声道参数化无法精确控制高频泛音区域。

## 方法创新
提出可微分Kelly-Lochbaum波导扩展模型，包含：（1）舌下辅助声源；（2）三次B样条声道参数化；（3）空间可学习阻尼；（4）泛音显著性损失函数。通过梯度下降端到端优化。

## 实验结果
在20个独立Sygyt片段（5位歌手、10个音高）上，相比发音基线降低30-38%对数谱距离，在泛音区域提升最显著；倒谱包络分析显示能准确恢复合并共振峰结构；表现优于DDSP谐波+噪声基线。

## 一句话评价
提出首个基于可微分发音模型的双声唱歌复制合成方法，物理参数可解释且性能优异。

---

## 2. UAT: Unified Audio-Text Diffusion for Audio Generation, Editing, and Captioning

**作者**: Hui Wang, Yifan Yang, Zeyue Tian, Yuhang Jia, Jinghua Zhao, Long Zhou, Bing Han, Cheng Liu, Jiaming Zhou, Geng Tu, Yong Qin
**链接**: [2606.04939](https://arxiv.org/abs/2606.04939)
**分类**: Audio Generation and Understanding | **关键词**: audio generation, audio editing, audio captioning, diffusion model, unified audio-text modeling, continuous latent diffusion, masked discrete diffusion, dual-stream architecture, Diffusion Transformer

### 核心痛点
- 音频生成（如文本到音频）和音频理解（如音频字幕）通常采用不同模型：生成依赖连续潜空间扩散模型，理解依赖自回归语言模型，导致任务隔离、优化分离，难以实现跨任务知识迁移和统一建模。
- 现有统一方法存在局限：混合架构（Hybrid）中生成与理解组件在独立潜空间优化，缺乏联合建模；AR-centric方法受离散音频令牌信息瓶颈和从左到右解码限制，生成质量与全局连贯性不足。
- 直接改造现有TTA扩散模型用于统一框架面临架构不对称（文本仅作为静态条件）和模态差异（连续音频 vs 离散文本）两大挑战。

### 方法创新
- **UAT**：首个扩散为中心的统一音频-文本框架，支持音频生成、编辑和字幕。核心为**耦合双流DiT架构**：在预训练TTA扩散骨干上添加轻量文本流，使音频流和文本流逐层相互调节（音频流以当前文本状态为条件，文本流以更新后的音频状态为条件）。
- **双模态扩散**：音频采用连续潜扩散（velocity prediction），文本采用掩码离散扩散（masked discrete diffusion），在共享骨干中联合优化，实现双向音频-文本建模。
- **多任务推理**：通过改变观察条件和受损模态，同一模型支持三种任务：文本到音频生成、文本引导音频编辑、音频字幕。

### 实验结果（摘要提及）
- UAT在音频生成和编辑任务上保持强劲性能，同时字幕性能达到竞争性水平，证明扩散中心统一模型在声学合成与语义预测间取得良好平衡。
- 详细实验（原文未完全展示）包括客观指标（如FAD、CLAP score）和主观评测。

### 一句话评价
UAT通过耦合连续音频扩散与离散文本扩散的双流DiT架构，首次实现扩散中心框架下的统一音频生成、编辑与字幕，有效桥接声学合成与语义理解。

---

## 3. Read What You Hear: Reference-Free Hypotheses Evaluation with Acoustic Discrepancy

**作者**: Zhihan Li, Hankun Wang, Yiwei Guo, Bohan Li, Xie Chen, Kai Yu
**链接**: [2606.04680](https://arxiv.org/abs/2606.04680)
**分类**: Speech Recognition | **关键词**: speech recognition, hypothesis evaluation, hypothesis refinement, acoustic discrepancy, TTS, unsupervised, error localization

## 核心痛点
传统的自动语音识别（ASR）评估依赖参考文本（如WER），但实际场景中参考文本往往不可得。现有无参考方法如内部置信度或语言模型评分，要么校准差、过自信，要么忽略语音信号本身。缺乏既能局部定位错误又无需额外训练的指标。

## 方法创新
提出READ（Reference-free Hypothesis Evaluation with Acoustic Discrepancy），利用预训练的离散自回归TTS模型（如CosyVoice2），在教师强制模式下计算给定文本假设下语音令牌的条件负对数似然，作为声学差异度量。通过TTS注意力图提取单调对齐，将帧级差异映射回文本段，实现细粒度错误定位。无需额外训练，可直接用于假设优化（句子级重打分、段级组合、与ROVER集成）。

## 实验结果
- READ与WER强相关（相关系数0.72-0.85），噪声下相关性更高。
- 用于假设优化：句子重打分和段级组合实现高达20%相对错误率降低，尤其在噪声条件下（SNR=0dB时提升显著）。
- 段级组合中98%的合并输出在每个段内同时降低READ。

## 一句话评价
首个利用TTS生成模型的声学差异实现无参考、细粒度、鲁棒的ASR假设评估与优化方法。

---

## 4. Masked Wavelet Scattering Transform Neural Field for Sound Field Reconstruction

**作者**: Xinmeng Luan, Samuel A. Verburg, Efren Fernandez-Grande, Gary Scavone
**链接**: [2606.04370](https://arxiv.org/abs/2606.04370)
**分类**: Sound Field Reconstruction / HRTF Upsampling | **关键词**: Wavelet Scattering Transform, Neural Field, Sound Field Reconstruction, HRTF, Masking, Multi-scale features, Statistical prior

## 核心痛点
声场重建（尤其是HRTF上采样）面临数据稀疏、个性化差异大、传统深度学习方法易过拟合的问题。小样本条件下，难以捕捉多尺度统计结构。

## 方法创新
提出**Masked Wavelet Scattering Transform Neural Field (MSNF)**，两阶段框架：
1. **Phase 1：Mask Identification**——从少量多受试者数据中学习二进制掩码，筛选出跨个体一致性的WST系数。
2. **Phase 2：Neural Field Reconstruction**——利用MLP神经场连续建模声场，损失函数结合观测MSE和掩码后的WST系数MSE，施加统计先验正则化。
关键技术：WST作为可解释、固定滤波器组的特征提取器，避免学习型CNN过拟合；掩码机制保留共享结构，滤除噪声。

## 实验结果（摘要未完整提供，但文中提及）
通过HRTF上采样任务验证，与基线方法（消融研究）比较，证明MSNF有效提升稀疏观测下的重建精度。

## 一句话评价
首次将WST作为先验用于声场重建，提出掩码神经场框架，兼具可解释性与小样本泛化能力。

---

## 5. Representation Matters in Randomized Smoothing for Audio Classification

**作者**: Jong-Ik Park, Shreyas Chaudhari, José M. F. Moura, Carlee Joe-Wong
**链接**: [2606.04210](https://arxiv.org/abs/2606.04210)
**分类**: Audio Robustness | **关键词**: 随机平滑, 音频分类, 鲁棒性认证, 表示感知, 预处理, 认证半径, 特征空间

## 核心痛点
直接随机平滑（RS）在音频分类中是不明确的，因为音频预处理（归一化、特征提取、后处理）改变了被认证的空间，导致相同的半径可能对应不同的认证对象。

## 方法创新
提出表示感知的报告框架，要求明确指定：认证对象（波形、特征空间、后处理）、扰动位置、增益策略、原始半径、信号相对尺度（SNR等效）、后噪声变换。定义了三种合同：固定增益波形平滑、特征空间平滑、后处理波形平滑。

## 实验结果
在关键词检测（Speech Commands）和环境声音分类（ESC-50）上诊断：
- 相同原始半径（0.007996）下，不同波形能量导致不同SNR（83.98 vs 90.97 dB）；
- 特征空间平滑在ESC-50上获得更高认证准确率（68.42% vs 65.53%），但认证的是特征而非波形；
- 裁剪或峰值归一化改变有效扰动几何（D_geom差异达230-351×）。

## 一句话评价
本文揭示了音频随机平滑中表示选择的关键影响，为鲁棒性报告的标准化提供了重要指导。


---

## 6. Audio Interaction Model

**作者**: Zhifei Xie, Zihang Liu, Ze An, Xiaobin Hu, Yue Liao, Ziyang Ma, Dongchao Yang, Mingbao Lin, Deheng Ye, Shuicheng Yan, Chunyan Miao
**链接**: [2606.05121](https://arxiv.org/abs/2606.05121)
**分类**: Audio Interaction / Streaming Audio Language Model | **关键词**: AUDIO-INTERACTION, SOUNDFLOW, StreamAudio-2M, Proactive-Sound-Bench, streaming audio, real-time interaction, audio language model

### 核心痛点
当前的大型音频语言模型（LALMs）均为离线模式，需要完整音频片段才能响应，且流式音频模型各自仅处理单一任务（如流式ASR或语音对话），缺乏统一的在线交互能力。

### 方法创新
本文提出**AUDIO-INTERACTION**，一个统一的流式在线交互模型，通过“感知-决策-响应”循环实时处理音频流，自主决定何时响应或保持沉默。其训练框架**SOUNDFLOW**包含三部分：
1. **交互数据合成**：通过分层事件策展流水线（含TFJP模块）将短片段合成为连贯的长交互序列。
2. **交互感知训练**：将音频建模为块级序列决策，引入历史回顾和理解感知沉默机制。
3. **异步交互推理**：采用先进先出方案解耦编码与解码，降低首帧延迟4.5倍。
此外，构建了**STREAMAUDIO-2M**数据集（302k小时，2.6M样本，覆盖7大能力28子任务）和**PROACTIVE-SOUND-BENCH**评测集。

### 实验结果
在8个基准上，AUDIO-INTERACTION在主流任务上保持竞争力（MMAU 58.15 vs 57.81），并在全语音和多轮设置中超越现有模型。同时解锁了实时ASR、流式音频指令跟随和主动帮助等离线模型无法实现的能力。

### 一句话评价
AUDIO-INTERACTION通过统一流式架构实现了在线音频交互的范式转变，兼顾性能与实时性。

---

## 7. SURF: Separation via Unsupervised Remixing Flow

**作者**: Henry Li, Robin Scheibler, Efthymios Tzinis, Matt Shannon, Arnaud Doucet, John R. Hershey
**链接**: [2606.04921](https://arxiv.org/abs/2606.04921)
**分类**: 单通道源分离 | **关键词**: 无监督源分离, 流匹配, 重混, 自监督学习, 生成模型

## 论文总结

### 核心痛点
现有监督源分离依赖大量干净源数据，且易受域偏移影响。无监督方法多采用回归或预训练生成先验，但回归会产生伪影，而预训练先验仍需干净数据。

### 方法创新
提出**SURF**（Separation via Unsupervised Remixing Flow），一种无监督流匹配框架，直接从观测混合中学习源分离。核心步骤：
1. 教师模型（初始为MixIT）估计源；
2. 对估计源进行重混（remixing）生成新混合及伪目标；
3. 学生流匹配模型（基于FLOSS）学习预测重混源或原始混合；
4. 学生模型通过指数移动平均更新教师模型，迭代提升。

方法本质上连接了流匹配的速度场与回归目标，并揭示了与Wake-Sleep算法的联系。

### 实验结果
在图像和音频分离基准上，SURF显著优于现有无监督方法，达到新SOTA。

### 一句话评价
SURF首次将流匹配成功应用于无监督源分离，无需干净源数据，性能领先。

---

## 8. Multilingual Long-Form Speech Instruction Following: KIT's Submission to IWSLT 2026

**作者**: Enes Yavuz Ugan, Maike Züfle, Yuka Ko, Supriti Sinhamahapatra, Fabian Retkowski, Seymanur Akti, Jan Niehues, Alexander Waibel
**链接**: [2606.04730](https://arxiv.org/abs/2606.04730)
**分类**: Speech Language Models / Multilingual Instruction Following | **关键词**: multilingual, long-form speech, instruction following, data augmentation, re-ranking, minimum Bayes risk, end-to-end, cascaded, Qwen2.5-Omni, IWSLT 2026, segment concatenation, temperature scaling, Chain-of-Thought

# 论文总结

## 核心痛点
当前语音大语言模型（Speech LLMs）在处理长语音（>30秒）时存在显著性能下降，主要因为：1）大多数模型基于Whisper编码器，只支持30秒音频；2）即使较新模型（如Phi-4、Qwen2.5-Omni）移除架构限制，但缺乏长语音训练数据，导致泛化不足。IWSLT 2026指令跟随赛道的新任务（包括惊喜任务）对模型避免过拟合提出了挑战。

## 方法创新
1. **数据增强框架**：通过段拼接（speaker-aware grouping）、LLM标签生成（使用Gemma-3-12B-it、Qwen3.5-27B等）和跨语言翻译（TranslateGemma-12b-it），将短语音语料转换为超过100万条长语音训练实例（6任务×4语言）。
2. **温度缩放数据交织**：采用温度T=2的采样策略平衡不同任务表示（ASR、ST、SQA、SSUM、ACHAP等），优于固定概率策略。
3. **重排序策略改进**：系统比较6种重排序方法，发现基于似然的重排序（likelihood-based）会错误选择由分段音频处理产生的候选，损害语义任务（如QA、摘要）；提出**似然+最小贝叶斯风险解码（MBR）** 组合策略，在提升ASR的同时限制对语义任务的负面影响。
4. **提交两个系统**：端到端模型（Qwen2.5-Omni）和级联模型（Parakeet ASR + Qwen2.5-7B-Instruct），用于对比分析。

## 实验结果（部分）
- 温度T=2的采样策略在大多数任务上表现最佳。
- 基于前缀的任务路由（Chain-of-Thought task-token conditioning）在任务不平衡和任务相似度高时导致任务区分崩溃（负结果）。
- 似然+MBR重排序有效解决了ASR与语义任务之间的权衡。
- 端到端模型在多语言长语音指令跟随上优于级联模型（具体数值因内容截断未详细给出）。

## 一句话评价
本文通过大规模数据增强和创新的重排序策略，有效提升了多语言长语音指令跟随性能，揭示了似然重排序在语义任务上的失败模式，为解决长语音多任务学习提供了实用方案。

---

## 9. Entity Binding Failures in Speech LLM Reasoning: Diagnosis and Chain-of-Thought Intervention

**作者**: Ming-Hao Hsu, Xiaohai Tian, Jun Zhang, Zhizheng Wu
**链接**: [2606.04474](https://arxiv.org/abs/2606.04474)
**分类**: Speech Language Models | **关键词**: entity binding, chain-of-thought, modality gap, speech LLM reasoning, logical reasoning

## 核心痛点
语音大模型（SLLM）在复杂推理任务中显著落后于文本模型，但该差距并非均匀分布：空间、句法、事实类任务上语音性能与文本相当，而在需要实体跟踪的逻辑推理任务（如web of lies）上，语音准确率跌至随机水平。作者诊断其根本原因在于语音编码中的时间池化与降采样操作模糊了离散的实体边界，导致隐式推理中实体-属性绑定失败（entity binding failure）。

## 方法创新
提出实体感知思维链（Entity-Aware Chain-of-Thought, EA-CoT），在推理前强制模型显式列举实体、记录属性声明，将隐式绑定转换为文本空间中的显式锚定。针对web of lies任务设计四步提示：（1）列举所有人名；（2）记录每个声明；（3）逐步推理；（4）提取答案。通过对比控制实验（其他任务使用结构化CoT但无实体跟踪）和Token预算分解，确认语音增益完全来自显式语义绑定指令，而非生成长度增加。

## 实验结果
在Qwen2.5-Omni和Phi-4-Multimodal上评估VoiceBench BBH的四个子集（共1000条）。web of lies上S2T准确率从随机水平提升至接近文本水平：Qwen提升16.8个百分点（从约50%到66.8%），Phi-4提升24.4个百分点（从约50%到74.4%），模态差距大幅缩小。其他任务中语音性能本就接近文本，EA-CoT带来的增益较小。Token预算分解表明，仅增加生成长度（256→1024）无改善，增益全部来自指令本身。

## 一句话评价
该工作精准定位了语音推理落后的核心瓶颈，并通过简洁有效的推理时干预几乎消除了模态差距，为语音大模型的推理能力提升提供了全新视角。

---

## 10. CleanCodec: Efficient and Robust Speech Tokenization via Perceptually Guided Encoding

**作者**: Eugene Kwek, Feng Liu, Rui Zhang, Wenpeng Yin
**链接**: [2606.04418](https://arxiv.org/abs/2606.04418)
**分类**: Speech Tokenization / Neural Audio Codec | **关键词**: neural audio codec, speech tokenization, perceptually guided encoding, denoising, speech enhancement, vector quantization, token efficiency

# 论文总结

## 核心痛点
现有神经音频编解码器在重构质量与token效率之间难以平衡，往往编码背景噪声、录音伪影等感知无关信息，导致语义和声学信息丢失，token率过高（数百t/s），阻碍LLM-based音频生成。

## 方法创新
1. **重构为选择性信息瓶颈问题**：仅编码感知重要特征，丢弃无关信息。
2. **CleanCodec架构**：基于VQ-VAE的自编码器，使用log-mel谱图输入（避免SSL特征局限），局部编码器用ConvNeXt下采样至12.5 t/s，全局编码器提取256维说话人嵌入，双解码器（声学+语义）分别重构mel谱图和WavLM特征，Vocos声码器回波。
3. **联合训练目标**：标准音频重构损失 + 语音增强损失（退化管道：混响、噪声、滤波、重采样、MP3压缩） + 全局条件化（预训练说话人验证模型监督全局编码器，保留音色）+ 语义条件化（余弦损失匹配WavLM特征）。

## 实验结果
- 在12.5 t/s下，说话人相似度（SIM）和词错误率（WER）均优于现有编解码器（如Mimi、BiCodec、XCodec2、WavTokenizer等）。
- 下游TTS和语音转换任务中，推理速度提升最高17倍，性能提升。
- 鲁棒性：在噪声环境中重构质量更好。

## 一句话评价
CleanCodec通过感知引导的编码策略，首次在极低token率（12.5 t/s）下实现SOTA重构质量和下游任务性能，兼顾效率与鲁棒性。

---

## 11. Gauss Circle Lattices with Geometric Convolutions for Synthesizing High Dimensional Image-Source Room Impulse Responses

**作者**: Yuancheng Luo
**链接**: [2606.04358](https://arxiv.org/abs/2606.04358)
**分类**: Audio Processing, Digital Audio Effects, Room Impulse Response Synthesis | **关键词**: Image-Source Model, Gauss Circle Problem, Room Impulse Response, High-Dimensional Acoustics, Geometric Convolutions

## 核心痛点
传统图像源模型（ISM）在计算矩形房间的高阶反射时，复杂度为 O(k^N)（k为半径，N为维度），导致N≥3时计算代价高昂，难以生成高维房间脉冲响应（RIR）的混响尾部。此外，传统ISM的反射数量呈多项式增长，与真实声场的指数增长不符，导致混响时间偏差。

## 方法创新
本文提出基于高斯圆问题（GCP）的计算方法，将ISM中的晶格点计数问题转化为GCP，并利用几何卷积（FFT）降低复杂度。具体地：
- 通过递归关系（式5）和面积函数（式6），将N维晶格点计数简化为低维子问题。
- 进一步利用卷积核（式7）和FFT（式8），将复杂度降至 O(N k^2 log k)，内存需求 O(N k^2)。
- 扩展至非原点源-接收器情况（式10-11），支持坐标平移、缩放和加权（如壁面反射系数）。
- 提出两种RIR重构方法：通过体积函数的有限差分近似（2.2节），以及复数反射系数的组合（2.3节）。

## 实验结果
- 运行时分析（图3）显示：对于N≤12，卷积方法在1秒内完成，而传统方法（式4-5）在N≥3时已不可行。
- 统计特性分析（第3节）包括回声密度、能量衰减曲线（EDC）、P50能量百分位和RT60估计（R²系数），验证了生成RIR的物理合理性。
- 误差分析表明，离散化误差随k增大而减小，且可通过插值补偿。

## 一句话评价
本文通过数学降维与信号处理技巧，显著加速了高维ISM计算，为生成高密度、低着色的混响尾部提供了可行方案，但牺牲了角度依赖和连续性（仅整数坐标）。

---

## 12. Feasibility of Time-Domain DNN-Based Speech Enhancement on Embedded FPGA for Hearing Aid

**作者**: Feyisayo Olalere, Umut Altin, Kiki van der Heijden, Marcel van Gerven
**链接**: [2606.04221](https://arxiv.org/abs/2606.04221)
**分类**: Audio Enhancement | **关键词**: Embedded FPGA, Speech Enhancement, Time-Domain DNN, SuDoRM-RF++, Low Latency, Hearing Aid

## 核心痛点
助听器要求极低的延迟（<10 ms）和功耗（1-3 mW），而当前的DNN语音增强系统在嵌入式硬件上难以同时满足这些约束。传统方法如波束形成、谱减法在非平稳噪声环境下性能下降，DNN方法虽效果好但计算量大，无法直接部署。

## 方法创新
1. 首次在嵌入式FPGA（AMD-Xilinx Kria KV260）上系统部署时域语音增强模型（SuDoRM-RF++ 0.25x），覆盖语音分离和降噪两个任务。
2. 评估FP32和16位定点（F16）两种精度，分析精度降低对延迟、内存和语音质量的影响。
3. 识别数据移动（片上参数缓存）为主要瓶颈，而非算术吞吐量。
4. 使用HLS工具将C++推理流水线编译为硬件逻辑，加速开发。

## 实验结果
- 定点降噪加速器首次采样延迟为9.7 ms，满足10 ms临床阈值；语音分离延迟为16.0 ms。
- 精度减半（F16）将模型内存占用降低一半，且不影响客观语音质量。
- FPGA延迟优于CPU基线，但功耗仍高于助听器目标（需1-3 mW）。

## 一句话评价
该工作通过系统测量明确了嵌入式FPGA部署时域DNN语音增强的资源需求，并量化了与助听器部署之间的差距，为未来低功耗硬件优化提供了方向。

---

## 13. The Differentiable Auditory Loop (DAL): An ML Framework for Hyper-Personalized Hearing Aids

**作者**: Alejandro Ballesta Rosen, Jason Mikiel-Hunter, Julian Maclaren, Jack Collins, Richard F. Lyon, Simon Carlile
**链接**: [2606.04103](https://arxiv.org/abs/2606.04103)
**分类**: Audio Enhancement | **关键词**: Differentiable Auditory Loop, CARFAC, SEANet, hearing aids, neural activity pattern, personalized fitting

## 核心痛点
传统助听器依赖固定的频率增益和压缩，无法在复杂声学环境（如鸡尾酒会问题）中提供足够支持，且未解决内耳编码功能障碍（如毛细胞损伤、突触病变）。

## 方法创新
提出**可微分听觉环路（DAL）**框架，整合生物启发的CARFAC耳蜗模型（已移植至JAX）和轻量级CNN网络SEANet。通过比较正常听力与模拟听力损伤的神经活动模式（NAP）和稳定听觉图像（SAI），利用梯度下降优化SEANet，使其同时实现降噪和听力补偿。

## 实验结果
在神经表征和信号保真度指标上，DAL优化的SEANet优于传统Master Hearing Aid (MHA)基线。

## 一句话评价
首个基于可微分生物模型实现超个性化助听器信号处理的ML框架，有望硬件部署用于临床。

---

## 14. Channel-Oriented Design for EEG-to-Music Reconstruction

**作者**: Jiaxin Qing, Junwei Lu, Lexin Li
**链接**: [2606.04040](https://arxiv.org/abs/2606.04040)
**分类**: EEG-to-Music Reconstruction | **关键词**: EEG-to-music reconstruction, channel-oriented design, self-distillation, channel dropout, contrastive learning, CLAP, AudioLDM, brain-computer interface

## 论文总结

### 核心痛点
- 脑电图到音乐重建（EEG-to-music reconstruction）中，EEG信号微弱、分布广泛、易受噪声和通道变异影响。
- 现有方法早期混合通道（如卷积、池化、块级分词）会破坏微弱但具有区分性的EEG信号，阻碍下游对齐和生成。

### 方法创新
- **通道导向设计**：提出三种互补组件，保留通道级结构，延迟通道整合到后续阶段。
  - **通道级分词**：每个电极作为显式token，保留空间定位的神经证据。
  - **通道级多视角自蒸馏**：强制时间裁剪和随机通道子集间的一致性，学习鲁棒分布式表示。
  - **通道级数据增强**：结构化通道丢弃，提高对噪声、伪迹和缺失电极的鲁棒性。
- 集成到编码-对齐-解码流水线：使用预训练CLAP音乐编码器、CLIP风格对比学习和预训练扩散模型（AudioLDM）。

### 实验结果
- 在语义和嵌入级指标上优于现有最先进基线（如EEG2Mel、LaBraM、EEG DINO等）。
- CLAP分数0.683，50-way识别准确率0.487，成绩显著提升。
- 消融实验验证每个组件的贡献。
- 可解释性：通过注意力权重可视化通道贡献，揭示与听觉处理一致的解剖结构。

### 一句话评价
本文通过通道导向设计解决EEG信号早期混合导致的信息损失，显著提升从EEG到音乐的重建质量，并提供了理论分析和强经验验证。

---

