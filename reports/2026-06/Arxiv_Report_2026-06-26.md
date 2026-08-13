# Arxiv Daily Deep Report - 2026-06-26

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 9
---

## 1. DNSMOS-C: Improving End-to-end Speech Quality Models via Contrastive Learning

**作者**: Xinyu Liang, Fredrik Cumlin, Victor Ungureanu, Chandan K.A. Reddy, Christian Schuldt, Saikat Chatterjee
**链接**: [2606.26903](https://arxiv.org/abs/2606.26903)
**分类**: Speech Quality Assessment | **关键词**: speech quality assessment, contrastive learning, deep neural network, representation learning, DNSMOS

## 核心痛点
现有的非侵入式语音质量评估（SQA）模型要么依赖大规模自监督学习（SSL）模型或多模态大语言模型，计算开销大；要么紧凑型模型（如DNSMOS Pro）泛化能力有限，对未见过的失真或录音条件适应性差。

## 方法创新
提出DNSMOS-C，在DNSMOS Pro的中间嵌入层引入基于MOS的对比学习损失（SCOREQ triplet loss），实现端到端联合优化。模型保持轻量级架构（4层卷积+全局池化+3层全连接），同时通过对比损失引导嵌入空间按感知质量排序，提升泛化性。训练损失为高斯负对数似然（GNLL）加对比损失，平衡因子λ=1。

## 实验结果
在BVCC、Tencent、NISQA等数据集上，DNSMOS-C在相关性指标（LCC、SRCC）上持续优于DNSMOS Pro，且标准差更低（训练更稳定）。在跨域测试集（NISQA TEST FOR/P501/LIVETALK）上，相关性指标多数提升。潜在空间分析（PCA、聚类）表明，对比损失使嵌入空间按MOS排序，并保留对失真/噪声类型的分辨能力。

## 一句话评价
DNSMOS-C通过轻量级对比学习损失显著提升紧凑型端到端SQA模型的泛化能力和训练稳定性，且不增加推理开销。

---

## 2. voxmap-studio: An open-source speaker diarization annotation tool with built-in cost instrumentation

**作者**: Fumiaki Yamaguchi
**链接**: [2606.26842](https://arxiv.org/abs/2606.26842)
**分类**: Speaker Diarization | **关键词**: speaker diarization, annotation, human-in-the-loop, annotation cost, open-source tool

## 核心痛点
现有说话人日志标注工具（如 gryannote）虽然关注标注成本，但并未实际度量成本。人工标注耗时且昂贵，且缺乏量化不同辅助手段效果的机制。

## 方法创新
提出 voxmap-studio，一个基于 React 的开源标注工具，集成 pyannote 生态系统。创新点包括：
- **快速初始化**：使用步幅加速的日志引擎自动生成假设，标注者只需纠正而非从头绘制。
- **内置成本度量**：记录每种编辑操作（创建、删除、分割、调整大小、重新分配）的次数和耗时，作为一等输出。
- **确认门控导出**：每个片段需人工确认（至少听一遍）才能导出，并注入“幻影”片段作为注意力检查，防止未验证输出泄漏。
- **标签辅助**：通过嵌入相似度高亮不确定片段、聚类画廊和推荐功能加速标注。

## 实验结果
在 AMI 语料库 9 个文件上进行初步研究，比较三种条件：C1（纯手动）、C2（自动初始化+不确定性高亮）、C3（额外添加画廊和推荐）。结果：
- C1 成本最高（editOps=761, DER=0.177），且以创建操作为主。
- C2 成本最低（editOps=278, DER=0.079），工作转向纠正。
- C3 反而成本上升（editOps=418），说明更多辅助未必更好。

## 一句话评价
该工具首次将标注成本作为一等输出，为量化不同辅助策略的效果提供了实证基础，但初步研究样本量小，结果需进一步验证。

---

## 3. A Large-Scale Database and Predictive Model of Listener-Rated Ease of Speech Understanding in Commercial Hearing Aids

**作者**: Andrew Sabin, Steve Taddei, Abram Bailey
**链接**: [2606.26342](https://arxiv.org/abs/2606.26342)
**分类**: Speech Understanding / Audio Quality Assessment for Hearing Aids | **关键词**: Hea¬ring aids, Ease of Speech Understanding, Perceptual dataset, Whisper, HASPIv2, MUSHRA, Subjective listening test

## 论文总结

### 核心痛点
当前助听器语音理解评估指标（如 HASPIv2）主要基于模拟失真下的客观可懂度，与真实消费者在商业助听器上的主观感知（如“理解容易度”）缺乏明确关联，难以反映实际用户体验。

### 方法创新
1. **大规模数据集**：收集了来自HearAdvisor网站的151,608个评分（筛选后104,298个），涵盖83款商业助听器产品在72个声学场景下的10,394段双耳录音。听者为自我报告听力损失者，采用MUSHRA启发的盲听测试，对助听器录音进行0-4分的“理解容易度”评分。
2. **预测模型**：使用冻结的Whisper-small编码器，对辅助音频和干净参考音频分别提取时域均值池化的768维嵌入，计算差向量后输入小型MLP（约0.89M参数）预测评分。针对不同背景噪声强度（响亮/安静）使用不同编码器层（层5/层2）和独立训练的头。
3. **训练策略**：以场景级（合并多个说话者配置）为目标，权重基于评分数量平方根，优化加权MSE。

### 实验结果
- 在未参与训练的设备上，模型场景级相关系数r=0.92（HASPIv2为0.83）；响亮场景r=0.89（HASPIv2 0.75）；安静场景r=0.79（HASPIv2 0.58）。
- 响亮场景性能达到人工评分split-half信度上限；安静场景接近该上限。
- 对增益和信噪比的控制实验验证了模型响应的合理性。

### 一句话评价
本文通过大规模真实数据和基于Whisper的差异嵌入方法，有效预测了听者对商业助听器语音理解的主观容易度，显著优于传统客观指标HASPIv2。

---

## 4. wav2tok 2.0: Scalable Audio Tokenization Maintaining Explicit Pairwise Token Alignment for Efficient Audio Retrieval

**作者**: Adhiraj Banerjee, Vipul Arora
**链接**: [2606.26824](https://arxiv.org/abs/2606.26824)
**分类**: Audio Retrieval / Spoken Term Detection | **关键词**: speech tokenization, spoken term detection, audio retrieval, bidirectional mamba, voice search, CTC alignment, DTW, contrastive learning, vector quantization

## 核心痛点
wav2tok 2.0 针对查询-示例口语词检测（QbE-STD）任务，现有方法如 wav2tok 依赖紧密耦合的聚类和对齐训练，难以扩展；BEST-STD 等虽可扩展但仅隐式处理对齐。

## 方法创新
提出两阶段训练框架：
1. **Stage I**: 基于 BEST-STD 架构，通过对比学习（SimCLR风格）和向量量化学习判别性、说话人不变的帧级表征。
2. **Stage II**: 引入显式成对令牌一致性约束：
   - **CTC对齐损失**: 最大化正样本为锚点下的去重令牌序列的CTC似然，禁止空白令牌。
   - **DTW对齐帧级令牌预测损失（新颖）**: 利用DTW对齐路径，为每个锚帧选择对齐帧中余弦相似度最大的正样本令牌作为目标，最小化负对数似然。
   - **自适应权重**: 通过对比损失与CTC损失的比值动态调整CTC权重，稳定训练。

## 实验结果
在 LibriSpeech train-clean-100 的令牌一致性评估中，wav2tok 2.0 在 unigram 和 bigram Jaccard 相似度上全面优于 HuBERT、WavLM、SpeechTokenizer、EnCodec、BEST-STD 及 wav2tok（如 256 代码本：0.83 vs. 0.80 unigram, 0.75 vs. 0.72 bigram）。在 QbE-STD 检索基准上一致超越 BEST-STD 和通用 tokenizer。

## 一句话评价
wav2tok 2.0 在保持可扩展性的同时，通过显式对齐损失显著提升了口语词检测的令牌一致性，是检索导向语音标记化的新标杆。

---

## 5. WQ-Fusion: Dynamic Gated Attention for Cross-Domain Audio Representation

**作者**: Mingda Lin, Lei Ding, Xinyue Zhou, Tiantian Xiong, Hanchen Pei, Gongping Huang, Hao Zhang, Jingdong Chen, Jacob Benesty
**链接**: [2606.26556](https://arxiv.org/abs/2606.26556)
**分类**: Audio Representation Learning | **关键词**: Cross-Domain Audio Representation, Dynamic Gated Attention, Whisper, Qwen2-Audio, Feature Fusion, Adaptive Feature Modulation

# 论文总结

## 核心痛点
- 现有音频编码器针对特定任务（语音、音乐、事件）具有归纳偏置，难以同时兼顾高保真声学细节和深层语义抽象。
- 静态融合（如简单拼接）无法根据下游任务动态调整特征权重，限制了跨域通用表示能力。

## 方法创新
- 提出WQ-Fusion双编码器框架，融合Whisper（语音表征）和Qwen（语义推理）的互补优势。
- 引入**自适应特征调制（AFM）**模块，通过预测缩放和平移参数对齐异构特征空间。
- 设计**逐元素门控注意力机制**，利用门控信号动态选择或抑制特定维度特征，实现上下文感知的路由。

## 实验结果
- 在Interspeech 2026 Audio Encoder Capability Challenge (Track A) 上，WQ-Fusion总体得分0.836，显著优于最强单编码器基线。
- 消融实验和对比验证了动态门控和AFM的有效性。

## 一句话评价
本文提出了一种动态门控融合的双编码器框架，有效解决了单编码器跨域泛化不足的问题，在通用音频表示上达到SOTA。

---

## 6. When Does Quality-Aware Multimodal Fusion Matter? A Leakage-Safe Diagnostic for Decision-Level Dependence

**作者**: Jaden Moon, Arvind Pillai, Andrew Campbell
**链接**: [2606.26473](https://arxiv.org/abs/2606.26473)
**分类**: Multimodal Fusion | **关键词**: multimodal fusion, quality-aware fusion, reliability estimation, decision-level dependence, diagnostic, stress detection, sentiment analysis

## 核心痛点
多模态系统常使用质量感知融合（quality-aware fusion）根据模态可靠性加权，但现有评估仅报告整体性能，未验证可靠性分数是否真正影响模型决策，可能仅因数据相关性或架构灵活性而提升。

## 方法创新
提出**泄漏安全的诊断方法**：固定训练后的模型和输入，在测试时打乱可靠性分数（Broken-Q）与原始对齐分数（Clean-Q）比较。若预测依赖分数，性能应下降。实验仅在全观测样本上进行，排除缺失影响。同时计算排列间隙（permutation gap）和Oracle headroom量化潜在改进空间。

## 实验结果
- **StressID**（压力识别）和**CMU-MOSEI**（情感分析）上，打乱原生质量分数后性能几乎不变（排列间隙接近零），尽管Oracle表明有提升空间。
- **正控制实验**：当质量分数与模态正确性对齐时，打乱导致显著下降，证明诊断方法能检测到真实依赖。
结论：质量感知融合仅在质量估计能准确识别当前实例的可靠模态时才改变决策。

## 一句话评价
本文提出简洁有效的诊断方法，揭示了现有质量感知融合方法在常见设置下未真正利用质量信号，为多模态鲁棒性研究提供了重要反思。

---

## 7. Sarashina2.2-TTS: Tackling Kanji Polyphony in Japanese Speech Generation via Data Scaling and Targeted Data Synthesis

**作者**: Lianbo Liu, Shiao Zhu, Kai Washizaki, Reo Yoneyama, Haesung Jeon, Mengjie Zhao, Yusuke Fujita, Hao Shi, Nao Yoshida, Yuan Gao, Roman Koshkin, Yukiya Hono, Yui Sudo
**链接**: [2606.25369](https://arxiv.org/abs/2606.25369)
**分类**: Text-to-Speech | **关键词**: Kanji Polyphony, Japanese TTS, Data Scaling, Targeted Data Synthesis, PronSteering, Joyo Kanji Yomi Benchmark, Kana-CER

## 核心痛点
日语TTS面临汉字多音字（kanji polyphony）挑战：2136个常用汉字共有4378种读音，上下文决定读音；现有系统训练数据中日语占比低，缺乏针对性数据增强；评估缺乏汉字级标注，且CER/WER受正字法变体干扰。

## 方法创新
1. **数据策略**：使用约361k小时语音数据（日语194k+英语167k），平衡双语比例；设计目标数据增强管道，覆盖所有常用汉字，集成LLM句子生成、字典韵律标注和文本端发音控制模型 PronSteering。
2. **评估方法**：构建 Joyo Kanji Yomi Benchmark（含13,095句汉字级标注）；提出 Kana-CER，在假名空间比较朗读与参考，避免正字法变体。
3. **模型架构**：基于 Sarashina2.2-0.5B-Instruct，结合 S3Tokenizer V2（ASR训练的语义tokenizer）、流匹配解码器（CosyVoice 2）和 HiFi-GAN 声码器。

## 实验结果
- 在 Joyo Kanji Yomi Benchmark 上所有CER指标优于基线；JSUT基准上发音准确率与最佳基线持平。
- 零样本日语语音合成中说话人相似度最高。
- 跨语言评估中唯一能保持稳定日语发音的系统。

## 一句话评价
通过大规模数据缩放和针对性数据合成，有效解决了日语汉字多音字问题，实现了SOTA读音准确率和跨语言鲁棒性。

---

## 8. PairAlign: A Framework for Sequence Tokenization via Self-Alignment with Applications to Audio Tokenization

**作者**: Adhiraj Banerjee, Vipul Arora
**链接**: [2605.06582](https://arxiv.org/abs/2605.06582)
**分类**: Audio Tokenization | **关键词**: self-alignment, sequence tokenization, autoregressive decoder, edit distance, compact audio tokens, cross-view consistency, geometric prior, neural codec

# PairAlign: A Framework for Sequence Tokenization via Self-Alignment

## 核心痛点
现有音频tokenizer大多基于帧级或短窗级别的量化、聚类或重建，导致序列级别的属性（跨实现一致性、长度、终止、紧凑性、编辑几何）难以直接控制。编辑距离是自然的序列度量，但不可微，难以直接优化。

## 方法创新
PairAlign提出通过序列级自对齐学习紧凑的音频token字符串。将tokenization视为条件序列生成：encoder输出连续条件，autoregressive decoder生成从BOS到EOS的符号序列，直接学习token身份、顺序、长度和终止。训练使用两个内容保持的视图，使每个视图的token字符串在另一视图表示下高似然，同时利用in-batch负样本区分。采用三阶段训练：Stage I训练VQ几何tokenizer作为基线；Stage II冻结encoder和quantizer，利用确定性VQ目标训练autoregressive decoder进行交叉配对；Stage III引入EMA teacher进行自适应序列tokenization，并包含anti-bypass正则化、长度约束等技术。

## 实验结果
在连续3秒语音上，PairAlign学习到紧凑、词汇丰富、非退化的token字符串，具有强跨视图一致性。检索时速率12.71 tokens/s，相对于VQ几何基线减少约55%的token数。在编辑距离检索中表现良好，但暴露了紧凑性-局部性权衡：在高密度几何或预训练SSL tokenizer上不一定全面占优。

## 一句话评价
PairAlign通过自对齐与自回归解码将帧级几何先验扩展为序列级紧凑音频tokenizer，实现了跨视图一致且可编辑距离搜索的符号表示。

---

## 9. CodecSep: Prompt-Driven Universal Sound Separation on Neural Audio Codec Latents

**作者**: Adhiraj Banerjee, Vipul Arora
**链接**: [2509.11717](https://arxiv.org/abs/2509.11717)
**分类**: Universal Sound Separation | **关键词**: Text-guided sound separation, Neural audio codec, Universal sound separation, FiLM conditioning, Transformer masker

# CodecSep 论文总结

## 核心痛点
- 现有文本引导声音分离系统（如AudioSep）计算量大，不适合低延迟边缘部署或基于编解码器的场景。
- 基于神经音频编解码器（NAC）的分离器（如CodecFormer、SDCodec）高效但局限于固定类别或固定音源分离，缺乏开放词汇的文本引导能力。

## 方法创新
- 提出CodecSep，首个在NAC潜在空间中直接进行文本引导通用声音分离的框架。
- 使用冻结的DAC编解码器作为骨干，结合轻量级Transformer掩码器，通过CLAP文本嵌入生成FiLM参数来调节掩码器。
- 在编解码器潜在空间中进行显式掩码，而非解码器式潜在生成，更高效且有效。

## 实验结果
- 在dnr-v2和五个开放域基准测试上，相比AudioSep，CodecSep在分离保真度（SI-SDR）上持续提升，在感知质量（ViSQOL）上保持竞争力，人类MOS-LQS也有提升。
- 细粒度语义监督比粗粒度提示更有效；显式掩码优于解码器式潜在生成。
- 在编解码器流部署中，CodecSep端到端仅需1.35 GMACs，比AudioSep少54倍计算量。

## 一句话评价
CodecSep通过直接在神经音频编解码器潜在空间中进行文本引导掩码，实现了高效、低延迟的通用声音分离，显著降低了计算成本，同时保持了分离性能。

---

