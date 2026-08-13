# Arxiv Daily Deep Report - 2026-06-25

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 12
---

## 1. SE-AGCNet: An End-to-End Framework for Joint Speech Enhancement and Loudness Control in Meeting Scenarios

**作者**: Jinming Zhang, Wei Rao, Xionghu Zhong, Eng Siong Chng
**链接**: [2606.25959](https://arxiv.org/abs/2606.25959)
**分类**: Audio Enhancement | **关键词**: Speech Enhancement, Automatic Gain Control, Joint Training, Meeting Room Acoustics, Loudness Control

## 核心痛点
传统音频流水线将语音增强（SE）和自动增益控制（AGC）作为独立模块级联，导致两种局限：AGC先于SE会无差别放大噪声和语音，降低信噪比；SE先于AGC则易过度抑制低音量语音，且残留噪声被AGC放大。

## 方法创新
1. **端到端联合框架 SE-AGCNet**：在时频域联合优化SE和AGC，采用MP-SENet作为SE骨干，并引入非对称重加权策略（对过度抑制施加10倍惩罚），促使SE保留低音量语音；AGC模块通过RMS归一化、频率卷积、BiLSTM和频谱重建实现音量平衡，训练中采用条件加权损失抑制静音区噪声放大。
2. **数据模拟管道 SE-AGC-DataGen**：针对AGC任务缺乏公开数据集，基于LibriTTS构建LibriAGC数据集，模拟多说话人、音量变化（突发尖峰、渐变等）及真实噪声（风扇、键盘等），并生成SE目标（干净但音量不平衡）和AGC目标（干净且音量平衡）。
3. **标准化响度评估指标**：引入ITU-R BS.1770和EBU R128标准的集成响度（LUFS）、短期响度（St LUFS）和响度范围（LRA），更客观地评估AGC效果。

## 实验结果
- 在LibriAGC、MMCSG和AliMeeting-far数据集上，SE-AGCNet在语音质量（SIGMOS、DNSMOS、PESQ）和ASR（WER/CER）指标上优于传统级联基线。
- 响度指标达到目标-23 LUFS，且LRA较小，证明音量平衡效果好。
- 真实场景评估进一步验证了数据模拟管道的有效性。

## 一句话评价
SE-AGCNet通过端到端联合训练有效解决了SE与AGC的协同难题，在会议场景下显著提升语音质量和ASR性能，并提供了可复现的数据管道与标准化评测方法。

---

## 2. Joint Residual Reweighting for Classifier Free Guidance in Flow-Matching Zero-Shot TTS

**作者**: Runwu Shi, Yujin Wang, Hongjin Song, Chunxiang Jin
**链接**: [2606.25672](https://arxiv.org/abs/2606.25672)
**分类**: Text-to-Speech | **关键词**: Zero-shot TTS, Flow Matching, Classifier-Free Guidance, Joint Residual Reweighting, Speaker Similarity

## 核心痛点
标准CFG在零样本TTS中同时增强文本和说话人条件，导致两者权衡；分支选择性方法虽可分别增强但存在权衡。

## 方法创新
提出四分支残差分解（full, text-only, speaker-only, null），将全条件方向分解为文本残差、说话人残差和联合残差。基于此设计联合残差重加权，在标准CFG基础上独立控制说话人残差和联合残差，提供更细粒度的控制。

## 实验结果
在F5-TTS和CosyVoice2上，该方法在保持文本正确性的同时提升了说话人相似度（CosyVoice2在多个数据集上提升ASR错误率指标；F5-TTS在英语集上提升说话人相似度）。

## 一句话评价
提出联合残差重加权方法，通过四分支分解和独立加权联合残差，有效平衡了零样本TTS中的说话人相似度和文本准确度。

---

## 3. Fully Differentiable Neural Forced Alignment via Soft Dynamic Programming

**作者**: Rotem Rousso, Eyal Cohen, Joseph Keshet
**链接**: [2606.25460](https://arxiv.org/abs/2606.25460)
**分类**: Forced Alignment / Phoneme Alignment | **关键词**: Forced Alignment, Phoneme Alignment, Differentiable Dynamic Programming, Contrastive Learning, Soft-DP, End-to-End, Speech Segmentation, Neural Acoustic Modeling

## 核心痛点
传统的强制对齐（Forced Alignment）方法主要依赖 HMM-GMM 框架，虽然精度高但依赖发音词典和 G2P 转换，无法适应自发语音中的实际发音变化。现代端到端 ASR 模型（如 wav2vec2.0、HuBERT、Whisper）虽在识别上表现优异，但未针对时间边界定位优化，导致对齐精度不足。

## 方法创新
提出一种全可微分的神经强制对齐架构，包括：
1. **双分支编码器**：表示编码器（用于音素身份验证和边界检测，通过对比损失 MNCE 区分稳态帧和过渡帧）和上下文编码器（生成帧级音素概率）。
2. **可微软动态规划解码器**：基于 Soft-DP 的端到端可训练模块，保持梯度流动。
3. **对比损失（MNCE）**：增强稳态音素区域与过渡边界区域的声学区分。
4. **端到端联合优化**：结合 MNCE、交叉熵和 Soft-DP 损失。

## 实验结果
在手工标注的英语基准上超越 HMM-GMM 和现有神经对齐方法，并泛化到词级对齐和未见语言。

## 一句话评价
首个结合对比表示学习与可微动态规划的端到端音素对齐系统，显著提升边界精度。

---

## 4. Does Translation-Enhanced Speech Encoder Pre-training Affect Speech LLMs?

**作者**: Tomoya Mizumoto, Yusuke Fujita
**链接**: [2606.25444](https://arxiv.org/abs/2606.25444)
**分类**: Speech LLM, Speech Encoder Pre-training, Cross-lingual Translation | **关键词**: Speech LLM, speech encoder, translation-enhanced pre-training, cross-modal alignment, bidirectional translation

## 核心痛点
传统将预训练语音编码器（如基于ASR或SSL的模型）接入大语言模型（LLM）构建Speech LLM时，存在表征空间不对齐问题：ASR编码器产生语言特定的连续特征，而LLM工作于语言无关的语义空间，轻量适配器难以弥合这一鸿沟。

## 方法创新
提出在语音编码器预训练中引入**双向翻译任务**（X↔en），迫使编码器学习语言无关的抽象语义表示。具体设计：1）采用Whisper-style Seq2Seq架构，预训练后仅保留编码器；2）定义三种预训练配置：**ASR-Only**（仅多语言转录）、**ASR & ST (X→en)**（非英语→英语翻译，模拟Whisper）、**ASR & ST (X↔en)**（双向翻译，包含英语→其他语言）；3）改进prompt格式支持双向翻译（OWSM风格）。

## 实验结果
基于Llama-3.2-1B/3B-Instruct frozen LLM，在ASR、ST（X→en和en→X）任务上评估。**双向翻译预训练（X↔en）始终最优**：
- 在1B LLM上，ASR WER从16.6降至14.6（en），ST X→en BLEU提升（如ja: 7.1→11.8）；
- 在3B LLM上，en→X翻译（seen语言）提升显著（如zh: 28.3→30.8），unseen语言（fa, id, sv, tr）同样受益；
- 相比仅X→en翻译，双向翻译带来更一致且更大幅度的改善，证明**对称翻译目标对语义对齐的关键作用**。

## 一句话评价
该工作通过系统性对比实验，首次验证了**双向翻译预训练**能有效解决语音编码器与LLM的模态鸿沟，为构建高性能Speech LLM提供了新的预训练范式。

---

## 5. Evaluating Japanese Dialect Robustness Across Speech and Text-based Large Language Models

**作者**: Tomoya Mizumoto, Yusuke Fujita, Hao Shi, Lianbo Liu, Atsushi Kojima, Yui Sudo
**链接**: [2606.25436](https://arxiv.org/abs/2606.25436)
**分类**: Speech Language Model | **关键词**: Japanese dialect, robustness, large language model, speech language model, speech translation

## 核心痛点
方言变体对大型语言模型（LLM）和语音语言模型（SLM）构成显著挑战，尤其是日语方言的鲁棒性尚未被系统研究。

## 方法创新
- 定义**方言鲁棒性**为模型在方言输入与标准输入上的性能比值，实现公平跨模型比较。
- 采用**翻译任务**（日语方言→英语）作为评估任务，兼顾文本和语音模态。
- 构建文本LLM（LoRA微调）和SLM（语音编码器+适配器+LLM）两种架构，对比分析。
- 从三个维度探究：基础LLM方言能力是否迁移至SLM（RQ1）、方言训练数据的影响（RQ2）、语音编码器微调的作用（RQ3）。

## 实验结果
- 在CPJD方言集上，SLM的鲁棒性与对应文本LLM显著正相关（如Llama在CPJD1上文本鲁棒性0.839 vs 音频0.698）。
- 使用方言数据训练和微调语音编码器均有效提升鲁棒性。
- 不同LLM基座（Llama、LLMJP、Sarashina、Swallow）在方言鲁棒性上存在差异，但趋势一致。

## 一句话评价
本文首次系统评估日语方言在文本和语音LLM中的鲁棒性，揭示了模态间方言能力迁移规律，并指出方言数据和编码器微调是关键改进手段。

---

## 6. Adaptive Oscillatory Inductive Bias for Modeling Sharp Prosodic Dynamics in Diffusion-Based TTS

**作者**: Sandipan Dhar, Nirmesh J. Shah, Ashishkumar P. Gudmalwar, Pankaj Wasnik
**链接**: [2606.25424](https://arxiv.org/abs/2606.25424)
**分类**: Text-to-Speech | **关键词**: Text-to-Speech, Diffusion Model, Oscilla Activation Function, Prosodic Dynamics, Expressive Speech Synthesis

## 核心痛点
现有扩散式文本到语音（TTS）模型在处理表达性语音中的尖锐韵律转换（如快速音高变化、清浊音边界）时效果不佳，固定的周期激活函数（如Snake）适应性有限。

## 方法创新
本文提出自适应振荡激活函数Oscilla，定义为 `x + tanh(α sin²(x))`。该函数结合了周期性的正弦分量和可学习参数α，通过tanh饱和机制实现门控，自适应调节振荡响应，同时线性旁路保持信号稳定。将其集成至StyleTTS2的解码器中，形成OscillaTTS系统。

## 实验结果
在LJSpeech（单说话人）和ESD（多情绪）数据集上，OscillaTTS在主观（MUSHRA评分86.67±1.49）和客观指标（MCD 6.59±0.01，F0-RMSE 0.35±0.003）上均优于StyleTTS2、GlowTTS、GRADTTS、FastSpeech2等基线，尤其在韵律建模上表现更佳。

## 一句话评价
OscillaTTS通过引入可自适应调制的振荡偏置，有效提升了扩散TTS对表达性语音中尖锐动态的建模能力。

---

## 7. CrossAccent-TTS: Cross-Lingual Accent-Intensity Controllable Text-to-Speech via Disentangled Speaker and Accent Representations

**作者**: Ram Annamdevula, Ankit Tatawat, Ashishkumar P. Gudmalwar, Nirmesh J. Shah, Pankaj Wasnik
**链接**: [2606.25403](https://arxiv.org/abs/2606.25403)
**分类**: Text-to-Speech | **关键词**: Accent Conversion, Controllable Speech Synthesis, Text-to-Speech, LLM based TTS, Accent Intensity Control, Indic Languages, L2 Accent

## 核心痛点
跨语言文本到语音（TTS）中，口音转换和强度控制仍是基本挑战，尤其是对于低资源和语音多样的印度语言。现有基于大语言模型（LLM）的TTS系统虽有强跨语言泛化能力，但对口音特征和强度的显式控制有限。
## 方法创新
提出CrossAccent-TTS框架，包含口音强度控制器（Accent Intensity Controller, AIC），通过加权语言嵌入注入口音子空间，实现口音间平滑插值和推理时口音强度细粒度调制。另设口音抑制模块（Accent Suppression Module），利用对抗性学习将口音与说话人/风格表征解耦，保留说话人相似性。模型基于Qwen 2.5（0.5B）和Neucodec语音编解码器，自回归生成声学令牌。
## 实验结果
在Indic Multilingual数据集（986小时）和L2-ARCTIC数据集（27小时）上评估，CrossAccent-TTS实现了精确的口音强度控制，在口音相似性和可控性上优于IndicF5、XTTS-v2、CV AE、GST-based等基线，同时保持说话人相似性和自然度。
## 一句话评价
首次实现跨语言口音强度连续可控的TTS，在低资源印度语言和L2英语口音上均有效。

---

## 8. Phoneme-Level Mispronunciation Screening in Polish-Speaking Children with an Explainable Assistant

**作者**: Milosz Dudek, Daria Hemmerling, Kamil Kwarciak, Maciej Stroinski, Maria Pensko, Mateusz Kowalewski, Leonid Pavlovskyi, Sebastian Jurczak, Anna-Mariia Vitkovska, Zuzanna Miodonska, Natalia Mocko, Michal Krecichwost
**链接**: [2606.25181](https://arxiv.org/abs/2606.25181)
**分类**: Speech Recognition | **关键词**: child speech, mispronunciation detection, speech sound disorders, Polish, phoneme recognition, wav2vec2, explainable feedback

## 核心痛点
波兰语儿童发音错误筛查依赖专家，资源有限；波兰语辅音密集，咝音系列复杂，自动筛查难度大。

## 方法创新
- 基于wav2vec2的CTC token识别器，附加6层Transformer后编码器以稳定CTC输出。
- 扩展token集，引入括号化IPA音标（如[s], [ù]）标记常见替换，保留专家判断的替换证据。
- 对齐后根据最小编辑距离定位错误，输出可解释的诊断向量（目标、实际、类型、置信度）。
- 模板驱动的护理人员辅助工具，保守处理不确定情况（低置信度时要求重录或转专家）。
- 使用LoRA进行参数高效微调（33.3%可训练参数）。

## 实验结果
- 在10名未见儿童（559个话语）测试集上，精确序列匹配88.7%。
- 作为保守筛查代理（检测目标咝音替换），精确率72.9%，召回率61.4%，F1=0.67，误报率2.7%。
- 移除后编码器会导致精确序列匹配下降4.2个百分点。

## 一句话评价
本文提出了一种针对波兰语儿童咝音替换的可解释筛查流水线，在有限数据上取得了合理的识别和筛查性能，并设计了安全的护理人员辅助框架。

---

## 9. BCoughBench: Benchmarking Respiratory Acoustic Foundation Models Under Body-Coupled Wearable Sensor Conditions

**作者**: Mayur Sanap, Prasanna Desikan, Edgar Lobaton
**链接**: [2606.25116](https://arxiv.org/abs/2606.25116)
**分类**: Audio Health Monitoring / Foundation Model Benchmarking | **关键词**: respiratory acoustic foundation models, body-coupled sensing, wearable health monitoring, benchmark, clinical sensitivity, domain shift, cough detection

## 核心痛点
当前呼吸声学基础模型（FMs）仅在智能手机录音上评测，而临床部署日益转向体耦合（BC）可穿戴设备，其传感器通过组织和骨骼衰减高频内容，导致FM可靠性未知。

## 方法创新
- 提出BCoughBench基准，评估5个FM（OPERA-CT/CE/GT, HeAR, M2D+Resp）在5个EBEN模拟的BC传感器条件下的9个分类任务和3个年龄回归任务。
- 使用预训练EBEN反向模型将智能手机咳嗽音频转换为5种传感器等效音频（前额加速度计、软入耳式、硬入耳式、太阳穴振动拾音器、喉部麦克风），模拟BC退化。
- 多指标评估：AUROC、临床敏感性（Se@Sp95）、期望校准误差（ECE）用于分类；MAE对比均值预测基线用于回归。

## 实验结果
- 平均AUROC从0.785（智能手机）降至0.689–0.723，太阳穴振动拾音器下降最大（Δ=−0.096），软入耳式下降最小（Δ=−0.062）。
- 在大多数疾病任务下，任何BC传感器上无FM达到临床敏感性阈值（Se@Sp95≥0.20）。
- CIDRZ数据集上的性别分类崩溃（AUROC从0.954降至0.596–0.628，Δ=−0.341），而COVID检测几乎不受影响（Δ=−0.004）。
- 年龄回归稳健，在CoughVID上前额加速度计下MAE从9.61改善至8.97年。
- HeAR在回归和人口统计任务上领先，M2D+Resp在疾病和特征任务上领先。

## 一句话评价
首个系统评估呼吸声学基础模型在体耦合可穿戴传感器条件下性能的基准，揭示了显著的传感器依赖性和任务特异性退化。

---

## 10. End-to-End Voice Intent Recognition for Spontaneous Human-Drone Interaction with Naive Users

**作者**: Allan Henry (GIPSA-COPERNIC, GETALP, LPNC), Solange Rossato (GETALP), Christian Graff (LPNC), Sylvain Huet (GIPSA-COPERNIC), Jose-Ernesto Gomez-Balderas (GIPSA-COPERNIC)
**链接**: [2606.24910](https://arxiv.org/abs/2606.24910)
**分类**: Spoken Language Understanding / Voice Intent Recognition | **关键词**: End-to-End SLU, Spontaneous Speech, Human-Drone Interaction, Self-Supervised Learning, Knowledge Distillation, VoiceStick Corpus

## 核心痛点
传统无人机语音控制依赖严格预定义命令列表，无法处理非专业用户的自然口语（含犹豫、重复、修正等不流畅现象）。级联方案（ASR+语义分析）延迟高且错误传播，而端到端方法因缺乏大规模配对音频-意图数据而难以实现。

## 方法创新
提出端到端口语理解架构，冻结自监督学习（SSL）声学编码器（基于Wav2Vec），后接轻量级LSTM+注意力池化分类头。创新引入跨模态知识蒸馏：训练时利用冻结的文本教师（如CamemBERT）编码ASR转录，通过余弦损失对齐声学表示与语义嵌入，推理时无需转录。在法语自发语音语料库VoiceStick（29对非专业用户真实遥操作场景）上评估。

## 实验结果
- 简单命令：93%准确率，7ms推理延迟，远超级联基线（79%，202ms），速度提升29倍。
- 全自发语音测试集：82%准确率，跨模态蒸馏在所有配置中一致提升鲁棒性。

## 一句话评价
端到端架构结合冻结SSL编码器与知识蒸馏，在实时无人机语音控制中实现低延迟、高鲁棒性，比级联方案更优。

---

## 11. Real-Time Voice AI Hears but Does Not Listen

**作者**: Martijn Bartelds, Federico Bianchi, James Zou
**链接**: [2606.26083](https://arxiv.org/abs/2606.26083)
**分类**: Voice AI | **关键词**: real-time voice AI, emotional intelligence gap, non-lexical cues, prosody, voice-word conflict, deployment safety

## 核心痛点
当前实时语音AI系统（如GPT Realtime-2、Gemini 3.1 Flash Live、Qwen3.5 Omni系列）在决策时严重依赖词汇内容，忽视语音中的情感、语调、口音等非词汇线索，导致在紧急呼叫、欺诈检测等场景中做出错误行为（如挂断哭泣者电话、批准恐惧中的转账、注册讽刺意愿者）。

## 方法创新
- **多轮场景测试**：设计三个真实对话场景（福利回访、电汇欺诈、志愿者招募），其中词汇和语音传递相反信息，衡量系统最终行为。
- **单轮诊断**：分离感知与行动，直接询问系统是否感知到语音中的情绪，发现多数系统能识别但无视。
- **口音/年龄诊断**：测试系统对说话人属性的判断，显示其受词汇内容而非声学特征主导。

## 实验结果
- 所有四个系统在三个场景中均基于词汇做出错误决策，忽略语音线索。
- 三个系统（除Qwen3.5 Omni Flash外）能正确识别语音中的情绪，但决策时不利用。
- 提示系统注意语音仅部分改善表现，不一致。
- 系统估计口音和年龄时偏向词汇暗示的答案。

## 一句话评价
本文揭示了实时语音AI的“情感智能鸿沟”——听得见但不倾听，警示在依赖语气和情感信息的场景中需谨慎部署。

---

## 12. Velocity Prediction in Automatic Guitar Transcription

**作者**: Jackson Loth, Xavier Riley, Simon Dixon, Emmanouil Benetos
**链接**: [2606.24912](https://arxiv.org/abs/2606.24912)
**分类**: Automatic Music Transcription | **关键词**: velocity prediction, automatic guitar transcription, synthetic data, transfer learning, deep learning, CRNN, MIDI

## 核心痛点
自动吉他转录（AGT）领域缺乏带速度标签的公开数据集，且速度在吉他上的定义模糊，导致多数模型忽略速度预测。

## 方法创新
1. 使用虚拟乐器合成带速度标签的训练数据（约20小时），通过François Leduc数据集中的MIDI注释估算速度，并用五种音色渲染。
2. 两阶段训练：第一阶段在合成数据上训练完整CRNN模型（基于Kong et al.的High-Resolution Piano Transcription模型），学习速度映射；第二阶段冻结速度子模块，在真实音频数据集（GAPS、GOAT）上训练其他子模块（onset、offset、frame），使用修改后的损失函数（去除速度项）。
3. 数据增强：随机峰值滤波、混响、脉冲响应。

## 实验结果
- 在合成数据上，速度预测平均绝对误差（MAE）从基线32.39降至7.04（song split），从33.59降至11.53（timbre split）。
- 考虑速度的F1值（F50(vel)）从35.6提升至69.22（song split），从34.7提升至51.99（timbre split）。
- 音符转录F1值略有提升（91.19→91.22），但不显著。

## 一句话评价
首次提出吉他转录中的速度预测方法，通过合成数据预训练结合真实数据微调，实现了有效的速度预测，但音符转录性能提升有限。

---

