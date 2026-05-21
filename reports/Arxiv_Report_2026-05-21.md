# Arxiv Daily Deep Report - 2026-05-21

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 9
---

## 1. Speech Quality Embeddings for Improved Detection and Classification of Degradations in Speech Signals

**作者**: Michael Kuhlmann, Tobias Cord-Landwehr, Reinhold Haeb-Umbach
**链接**: [2605.21332](https://arxiv.org/abs/2605.21332)
**分类**: Speech Quality Assessment | **关键词**: speech quality, quality embeddings, degradation detection, contrastive learning, partial mix-up

## 核心痛点
传统的自动主观语音质量评估（SSQA）通常仅提供整体（ utterance-level）评分，无法捕捉局部退化，例如短暂失真。现代语音系统产生的高质量语音中退化可能仅局部出现，因此需要更精细的评估。

## 方法创新
1. **局部语音质量评估（LSSQA）**：在帧级进行质量评分。利用已有的 utterance-level MOS 标签，通过部分混合增强（partial mix-up）策略生成带帧级伪标签的训练数据。具体地，从平行语料库（清洁和退化语音）中采样，随机混合生成带有局部退化的信号，并使用预训练 LSSQA 模型的帧级输出作为伪目标。
2. **对比学习质量嵌入**：为了区分退化类型，添加第二个解码器用于提取帧级瓶颈嵌入，并引入监督对比损失（ supervised contrastive loss）。对于混合数据中的每一帧，根据其退化类型（或清洁）赋予类别标签，对比损失拉近同类嵌入、推开异类嵌入。同时考虑了相邻帧的自对比问题（排除窗口内的帧）。
3. **退化检测方式**：除了基于帧级 MOS 值的阈值检测，还提出了基于嵌入的检测方法：利用清洁参考嵌入作为注册，计算余弦相似度，与阈值比较判断是否退化。

## 实验结果
- 在域内和域外数据上，所提方法均提升了退化检测性能。嵌入基检测优于 MOS 基检测。
- 通过分析嵌入空间，发现不同退化类型形成明显聚类，但在多重退化或域外退化时聚类纯度下降。

## 一句话评价
该工作通过部分混合增强和监督对比学习，首次实现了局部退化的同时检测与分类，为语音质量评估提供了更细粒度的解释性。

---

## 2. Linearly Constrained Deep Beamformer for Multi-Speaker Scenarios

**作者**: Ilai Zaidel, Ori Engel, Bar Engel, Sharon Gannot
**链接**: [2605.21141](https://arxiv.org/abs/2605.21141)
**分类**: Audio Enhancement | **关键词**: 线性约束波束成形, 多说话人, 深度学习, LCMV, RTF估计, U-Net, 注意力机制, 零陷控制

## 核心痛点
传统线性约束波束成形（如LCMV）依赖于精确的空间签名估计，实际场景中难以保证性能；现有深度波束成形方法虽能学习空间和频谱表示，但缺乏显式空间约束，无法可靠实现干扰零陷。

## 方法创新
提出一种基于DNN的波束成形框架，通过自适应多损失函数（受增广拉格朗日启发）同时优化信号重建和线性空间约束。损失函数包含三项：
1. SI-SDR损失（目标重建）
2. 无失真响应惩罚（|w^H a_target - 1|^2）
3. 对数域零陷惩罚（10log10(||w^H A_interf||^2)）

模型采用U-Net架构，融合注意力机制，输入多通道混合信号及估计的目标RTF和干扰子空间。训练时惩罚权重逐步增加，使网络学习满足约束的波束权重。

## 实验结果
在模拟多说话人场景下，所提模型（带估计RTF）相比经典LCMV和未使用RTF引导的模型，在SI-SDR、PESQ等指标上取得更优性能，且旁瓣控制和背景噪声衰减更好。

## 一句话评价
首次将线性约束显式嵌入DNN波束成形损失函数，实现可解释的多说话人增强和可靠零陷控制。

---

## 3. A Survey of Audio Reasoning in Multimodal Foundation Models

**作者**: Zhihan Guo, Wenqian Cui, Guan-Ting Lin, Daxin Tan, Jingyao Li, Qiyong Zheng, Dingdong Wang, Jing Xiong, Han Shi, Jiaya Jia, Irwin King
**链接**: [2605.21008](https://arxiv.org/abs/2605.21008)
**分类**: Multimodal Foundation Models | **关键词**: Audio Reasoning, Multimodal Foundation Models, Chain-of-Thought Reasoning, Audio-to-Text, Audio-to-Speech, Audio-Visual Reasoning, Agentic Audio Reasoning

## 核心痛点
音频推理面临三大障碍：1）缺乏真正基于音频的推理数据；2）捷径学习和模态幻觉；3）推理深度与实时延迟之间的权衡。

## 方法创新
本文首次系统性地定义了音频推理的统一框架，将相关研究归纳为四种范式：
- **Audio-to-Text推理**：从声学信号推断文本答案，强调声学基础。
- **Audio-to-Speech推理**：在口语交互中嵌入推理，平衡推理深度与对话延迟。
- **Audio-Visual推理**：整合同步的听觉和视觉证据，需要跨模态对齐和消歧。
- **智能体音频推理**：将复杂音频任务分解为感知、规划、工具使用等模块。

此外，论文详细综述了推理范式（CoT提示、监督微调、强化学习、延迟感知交互）以及模型基础（编码器、投影器、LLM骨干、语音分词等）。

## 实验结果
作为综述论文，未提供新实验结果，但总结并对比了现有模型（如Audio-CoT、Audio-Reasoner、Mini-Omni等）在各类基准上的表现。

## 一句话评价
第一篇全面聚焦音频推理的综述，清晰梳理了问题定义、模型基础、范式分类和未来挑战。

---

## 4. From Numbers to Perception, Energy Decay Curves Prediction

**作者**: Imran Muhammad, Gerald Schuller
**链接**: [2605.20968](https://arxiv.org/abs/2605.20968)
**分类**: Room Acoustics Prediction | **关键词**: Energy Decay Curve, Room Impulse Response, 1D-CNN, Physically-informed Loss, Multi-band Prediction, Real-time Auralization

## 核心痛点
传统房间声学模拟（如射线追踪、镜像源法）计算量大，难以用于实时交互式虚拟环境。直接预测房间脉冲响应（RIR）存在高维度和相位不一致问题。

## 方法创新
提出基于1D-CNN的框架，直接从房间几何和材料属性预测多频带（24个三分之一倍频程）能量衰减曲线（EDC）。
- 采用复合损失函数：对数域MSE + 斜率惩罚（步长50的差分），确保单调衰减、抑制“阶梯”伪影。
- 模型参数从900万降至90万（90%减少），推理速度提升5倍。
- 使用线性插值上采样+随机符号粘性（RSS）方法重建完整RIR。

## 实验结果
- T30误差在5% JND（刚好可察觉差异）内，EDT均方根误差0.10s，C50均方根误差0.47dB。
- R²值：T30=0.90，EDT=0.79，C50=0.67。
- 消除了LSTM模型中的阶梯伪影，实现物理一致的单调衰减。

## 一句话评价
一种高效且物理约束的深度学习框架，通过1D-CNN和定制损失函数实现多频带EDC的精确预测，适用于实时声学渲染。

---

## 5. Raon-OpenTTS: Open Models and Data for Robust Text-to-Speech

**作者**: Semin Kim, Seungjun Chung, Taehong Moon, Sangheon Lee, Minyoung Ahn, Keon Lee, Nam Soo Kim, Jaewoong Cho, Ludwig Schmidt, Kangwook Lee, Dongmin Park
**链接**: [2605.20830](https://arxiv.org/abs/2605.20830)
**分类**: Text-to-Speech | **关键词**: Text-to-Speech, Open Dataset, Diffusion Transformer, Zero-shot TTS, Robust Evaluation, Data Curation

## 核心痛点
当前最先进的TTS模型依赖大规模私有数据集，训练数据不可公开，限制了可复现性和系统性研究。开放数据集规模不足，导致开放模型与私有模型性能差距显著。

## 方法创新
1. **Raon-OpenTTS-Pool**：构建了615K小时的公开英语语音-文本数据集，整合10个公开语料库和网络录音，是已知最大的多源开放TTS数据集。
2. **Raon-OpenTTS-Core**：通过基于模型的过滤管道（DNSMOS、WER、语音活动比）从池中筛选出510K小时194M片段的子集，提升数据质量。
3. **Raon-OpenTTS模型**：基于扩散变换器（DiT）架构，训练0.3B和1B参数模型，在多项基准上达到与私有数据训练模型可比的性能。
4. **Raon-OpenTTS-Eval**：引入鲁棒性评估基准，包含Clean、Noisy、Wild、Expressive四种声学条件，共6K提示-文本对，全面评估零样本TTS。

## 实验结果
- 在Seed-TTS-Eval上，Raon-OpenTTS-1B取得WER 1.78%、SIM 0.749，在开放权重模型中WER第二、SIM第一。
- 在CV3-Hard-EN上，WER 6.15%、SIM 0.775，两项均排名第一。
- 在Raon-OpenTTS-Eval上，平均WER和SIM最佳，CMOS偏好第二。
- 相比仅用100K小时数据训练的F5-TTS和MaskGCT，性能显著提升，接近或超越Qwen3-TTS、CosyVoice 3等私有模型。

## 一句话评价
该工作通过构建最大的开放TTS数据集和高效的过滤管道，训练出与私有数据模型性能匹敌的DiT-TTS模型，并引入多条件鲁棒性评估基准，极大推动了TTS研究的可复现性。

---

## 6. DuplexSLA: A Full-Duplex Spoken Language Model with Synchronized Speech, Language, and Action

**作者**: Haoyang Zhang, Jun Chen, Donghang Wu, Yuxin Li, Yuxin Zhang, Xiangyu Tony Zhang, Che Liu, Qingjian Lin, Yizhou Peng, Hexin Liu, Eng Siong Chng, Chao Yan, Boyong Wu, Yechang Huang, Xuerui Yang, Fei Tian
**链接**: [2605.20755](https://arxiv.org/abs/2605.20755)
**分类**: Spoken Dialogue Systems / Full-Duplex Speech Models | **关键词**: Full-Duplex, Spoken Language Model, Tool Calling, Turn-Taking, Speech-Action

## 核心痛点
- 现有全双工语音模型（turn-based pipeline）依赖外部 VAD 进行轮次控制，无法区分停顿、打断、反馈等语义，且缺乏原生的计划与工具调用通道，导致工具调用需在轮次边界进行或通过外部级联，增加延迟。

## 方法创新
- **DuplexSLA**：原生全双工语音-语言-动作基础模型，采用**双流三通道**架构：
  - 用户音频通道（80ms 因果特征）
  - 助手音频通道（TA4布局：1个文本锚点+4个离散音频token，40ms粒度）
  - 动作通道（最多10个文本token/160ms块，可包含规划文本、控制标签、JSON工具调用）
- 所有通道在160ms共享时钟上由同一个骨干网络联合自回归解码，实现听、说、计划、工具调用的同步。
- 支持语义驱动的原生打断、暂停、反馈，无需外部 VAD。
- 动作通道添加结构化标记（`<|toolcall_begin|>`等），允许助手说话时发出工具调用。
- 为满足实时推理，限制每块动作token不超过10个，超出的稀疏化到后续块。

## 实验结果
- 构建 **DuplexSLA-Bench**（2100个案例），覆盖暂停、打断、反馈轮次控制及三类工具调用场景。
- 达到亚秒级延迟，工具调用准确率与现有方法竞争。

## 一句话评价
首个原生支持语音-语言-动作同步的全双工模型，通过三通道结构实现了语义驱动的轮次控制和实时工具调用。

---

## 7. PlanRAG-Audio: Planning and Retrieval Augmented Generation for Long-form Audio Understanding

**作者**: Masao, Someki, Chien-yu, Huang, Siddhant, Arora, Samuele, Cornell, Markus, Müller, Nathan, Susanj, Rupak V, Swaminathan, Grant P, Strimel, Jing, Liu, Shinji, Watanabe
**链接**: [2605.20414](https://arxiv.org/abs/2605.20414)
**分类**: Audio Understanding / Multimodal Retrieval Augmented Generation | **关键词**: PlanRAG-Audio, Long-form Audio Understanding, Retrieval Augmented Generation, Planning, Multimodal Reasoning

## 核心痛点
长音频理解中，音频序列极长（如1小时音频对应12k文本token但100k+语音token），且需跨时间分布的多模态声学线索（语音内容、说话人身份、情感、声音事件）进行组合推理。现有LALM直接处理长音频存在计算瓶颈，而基于ASR或音频字幕的方法忽略非语言信息。

## 方法创新
提出PlanRAG-Audio，一种基于规划的检索增强生成框架：
1. **音频与语音处理**：将原始音频转换为多模态表示（转录、说话人、声音事件等），存入结构化数据库。
2. **检索计划**：LLM分析查询生成结构化计划Θ(q)，指定所需模态、过滤器、融合方式、输出字段及答案格式。
3. **结构化检索**：规则型SQL生成器将计划编译为SQL查询，执行后仅返回相关片段。
4. **答案生成**：基于检索结果生成最终答案。
该框架将推理成本与原始音频长度解耦，支持零样本处理多种长音频任务。

## 实验结果（根据摘要）
在广泛的语音/音频检索任务上，PlanRAG-Audio提高了推理准确性，并随音频持续时间增加保持性能稳定（通过将推理成本与原始音频长度解耦）。

## 一句话评价
一种通过显式规划检索来高效处理长音频多模态推理的创新框架。

---

## 8. Causal Spatio-Temporal Sound Field Reconstruction

**作者**: David Sundström, Filip Tronarp, Johan Lindström, Andreas Jakobsson
**链接**: [2605.20403](https://arxiv.org/abs/2605.20403)
**分类**: Sound Field Reconstruction | **关键词**: Causal sound field reconstruction, Spatio-temporal LMMSE, Stochastic wave equation, Diffuse field coherence, Sensor selection

## 核心痛点
实时声场控制应用中，使用因果有限窗口测量数据重建声场时，传统频域方法假设频带间独立，忽略了窗口引起的频带相关性，导致重建次优。

## 方法创新
1. 将声场建模为随机波动方程的解，利用平稳随机源分布推导出时空协方差函数，该函数在远场极限下退化为经典扩散场相干模型，同时保留了有限窗口的时域相关性。
2. 提出因果有限窗口时空线性最小均方误差（LMMSE）估计器，融合多传感器时空观测。
3. 针对计算复杂度问题，设计预算约束的时空样本选择策略，最小化目标区域的后验重建方差。

## 实验结果
在模拟和实测声场上验证，相比频域有限窗口基线方法，提出的因果时空估计器在短窗重建中性能更优，且样本选择有效降低计算成本。

## 一句话评价
本文通过随机波动方程协方差和因果时空LMMSE估计器，并结合预算约束样本选择，显著提升了因果短窗下的声场重建精度。

---

## 9. SEABAD: A Tropical Bird Activity Detection Dataset for Passive Acoustic Monitoring

**作者**: Muhammad Mun'im Ahmad Zabidi, Mohd Yamani Idna Idris, Norisma Idris
**链接**: [2605.20853](https://arxiv.org/abs/2605.20853)
**分类**: Bioacoustics / Bird Activity Detection | **关键词**: passive acoustic monitoring, bird activity detection, edge AI, tropical soundscapes, bioacoustics, dataset curation, biodiversity informatics

## 核心痛点
被动声学监测（PAM）在热带生态系统中面临挑战：持续录音产生大量无用音频（鸟鸣占比<10%），现有鸟声数据集多来自温带，模型泛化到热带效果差（声景密集、物种丰富、非鸟类生物声多）。缺乏专为边缘设备设计的短时长、二分类（存在/不存在）数据集。

## 方法创新
- **SEABAD数据集**：50,000个3秒片段（16 kHz单声道），含25,000正样本（鸟声）和25,000负样本，涵盖1,677种东南亚鸟类。
- **双分支管道**：正样本来自Xeno-Canto（六阶段流程：元数据采集→下载→去重→片段提取→物种平衡→质量保证）；负样本来自BirdVox、Freefield1010、Warblr、FSC-22、ESC-50、DataSEC六个数据集。
- **多样性感知平衡**：通过Gini系数降低长尾物种不均衡13.7%（从0.601降至0.519），同时保留种内声学变异。
- **质量审计**：1,000正样本人工验证准确率达97.8%±0.9%。

## 实验结果
基线模型MobileNetV3-Small在三随机种子上达到99.57%±0.25%准确率和0.9985±0.0002 AUC，表明标签质量高、任务可分离性强。

## 一句话评价
首个面向热带边缘部署的大规模鸟类活动检测数据集，具备高质量标签和可复现管道。

---

