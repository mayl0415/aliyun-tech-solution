---
title: "文档智能_文档AI_智能文档处理_数据智能"
short_title: "PLCNet: Real-time Packet Loss Concealment with Semi-supervised Generative Adversarial Network"
url: https://www.aliyun.com/product/ai/docmind
category_l1: "视觉智能"
category_l2: ""
keywords: "文档智能,文档AI,智能文档处理,数据智能,IDP,文字提取, PDF转Word,文档解析,表格解析,文档结构化"
crawled_at: 2026-02-05T14:15:29.529165
---

# Abstract

## 产品简介

公测中 文档智能  播放视频 文档智能（Document Mind），基于多年技术积累打造的多模态文档识别与理解引擎，为用户提供各类文档的结构化信息抽取和智能化文档处理。支持通用场景和自定义场景下的多样化文档处理需求。产品咨询答疑，请加钉钉交流群：155680013413

## 产品图标

## 产品图片

![图片1](https://img.alicdn.com/imgextra/i1/O1CN01cOD0qc1r0CG3Nu2eV_!!6000000005568-2-tps-2700-2400.png)

![图片2](https://img.alicdn.com/imgextra/i2/O1CN01iKDT2425Yuu78KCW3_!!6000000007539-2-tps-1773-1900.png)

![图片3](https://img.alicdn.com/imgextra/i2/O1CN01Ektvua1ckiFOYq0GI_!!6000000003639-2-tps-900-800.png)

![图片4](https://img.alicdn.com/imgextra/i3/O1CN01UYmSwa23h2hPxKCgQ_!!6000000007286-2-tps-900-800.png)

![图片5](https://docmind-api-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/model/demo/image/4c878fc030374cd2968175d633cf01b0.jpeg)

![图片6](https://docmind-api-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/model/demo/image/2dc3dcd6a983cb57e1667e159f826b1f.jpeg)

![图片7](https://docmind-api-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/model/demo/image/afe202443e2d117219bc9585fa979f18.jpeg)

## 应用场景

检索增强生成RAG 大模型训练
检索增强生成RAG 依托文档智能解析服务对文档内容统一处理后，搭配RAG从大规模的文档集合中检索内容并生成更丰富、更具信息量回答，广泛用于问答系统、文档生成、信息检索系统等。
能够提供 文档智能解析 基于对文档的内容信息、版面信息和逻辑信息的分析理解，结合搜索技术和大模型能力进行后续的应用开发。 文档格式转换 把不可编辑的PDF转换为可编辑的Word格式，将文档数据处理成切片后的分段文本数据，结合大模型生成文答式服务。 推荐搭配使用
文档解析 （大模型版）

## 产品功能

文档理解 作为大模型应用场景及RAG前置处理链路，提供高质量、高精度的文档解析服务。
文档格式转换 将PDF、图片等不可编辑的文档转换为Word、Excel等可编辑的文档格式，在实现高精度内容识别的同时，最大限度地保留文档版式样式。 相关推荐：

## 产品规格

文档理解 文档格式转换
- █████ ████████████████ ██ █████ ██ █████ ██ █████ 询价中 立即购买
体验中心 文档解析（大模型版） 电子文档解析 PDF转Word 图片转Word PDF转Excel 图片转Excel PDF转图片 图片转PDF 对各类文档进行快速准确解析，适用于大模型的数据预处理、文档问答等场景
示例文档.pdf 展开
Baiyun Liu, Qi Song, Mingxue Yang, Wuwen Yuan, Tianbao Wang
Alibaba Group, China
"{baiyun.lby, qiqi.sq, yangmingxue.ymx, wuwen.yww, penger.wtb}@alibaba-inc.com"
Packet loss is one of the main reasons for speech quality degradation in voice over internet phone (VOIP) calls. However, the existing packet loss concealment (PLC) algorithms are hard to generate high-quality speech signal while maintaining low computationalcomplexity. In this paper, a causal wave-to-wave non-autoregressive lightweight PLC model(PLCNet) is proposed, which can do real-time streaming process with low latency. In addition, we introduce multiple multi-resolution discriminators and semi-supervised training strategy to improve the ability of the encoder part to extract global features while enabling the decoder part to accurately reconstruct waveforms where packets are lost. Contrary to autoregressive model, PLCNet can guarantee the smoothness and continuity of the speech phase before and after packet loss without any smoothing operations. Experimental results show that PLCNet achieves significant improvements in perceptual quality and intelligibility over three classical PLC methods and three state-of-the-art deep PLC methods. In the INTERSPEECH 2022 PLC Challenge, our approach has ranked the 3rd place on PLCMOS(3.829) and the 3rd place on the final score (0.798).
"Index Terms: packet loss concealment, generative adversarial network, semi-supervised, non-autoregressive, low complexity"
In VOIP communication, speech signal is transmitted as packets over the network through encoding and compression technology. However, due to the influence of the network environment, some audio packets cannot be transmitted to the receiver, resulting in short-term interruption of the speech signal, whichdinnturnaffectscals sPeechqualityand intelligibility during long-term calls. To solve the above problems, the PLC algorithm came into being.
"The traditional PLC solution is based on signal analysis[1-2], which can be divided into two types: based on the sender and based on the receiver. The former is to use the encoded redundant information to recover the lost speech signal. However, this method requires extra bandwidth. The latter is to reconstruct the speech signal by using the decoding parameter information before packet loss. The biggest advantage of the traditional PLC method is that the calculation is simple and can be processed online; the disadvantage is that it can only effectively combat packet loss of about 40ms and cannot deal with long-term continuous burst packet loss. Therefore, the processing capability of the traditional PLC algorithms is very limited."
In recent years, the research of deep learning in the field of PLC has shown great potential due to the powerful generative capability of deep neural network (DNNs). The
existing deep PLC methods are to reconstruct the lost speech signal at the receiver. The first is an offline non-causal processing framework [3-7]. In addition to using historical unmissed frames, it is also possible to use broader contextual information including future frames. These methods are not suitable for online applications.
The second is a causal processing framework that uses historical unmissed frames for post-processing. B.K. Lee et al.[8] are pioneers in using autoregressive model to solve the packet loss problem. Since then, deep PLC algorithms based on autoregressive models have been continuously proposed. Such as convolutional recurrent network (CRN) [9-10], long-short term memory network (LSTM)[11-12] and WaveRNN[13]. The common feature of these methods is to use the effective information of previous frames to recursively inference the current frame. However, the context leading up to the frame to be predicted can contain many reconstructed frames instead of original frames, creating a mismatch between training and inference. When long-term continuous burst packet loss occurs, the generated waveform will be greatly attenuated and the of speech quality needs to be further improved. In addition, the phase of the compensated speech signal and the real speech signal is discontinuous. A smoothing operation is required, which will damage the quality of the speech signal that is not lost.
Contrary to autoregressive model, generative adversarial network (GAN) based methods have been shown to be effective in generating high-quality audio in a parallel manner [14]. Shi et al. [15] conducted experiments in the time domain, using convolutional neural network as generator and discriminator to address packet loss and missing spectrum. Pascual et al.[16] also proposed a GAN-based adversarial encoder network. The input of the generator is the Mel spectrum and the output is the time domain waveform. In addition, Wang et al. [17] utilized U-Net and time-frequency discriminator for packet loss compensation. However, they have high computatio complexity in terms of both the number of parameters and the inference latency, making them difficult to use for real-time processing.
"To address the above issues, PLCNet is proposed. This model was used to participate in the INTERSPEECH 2022 PLC Challenge[18]. And this paper makes the following key contributions:"
· A streaming causal wave-to-wave non-autoregressive generative adversarial network is proposed, which has low latency and can maintain the continuity of the speech phase before and after packet loss.
●To achieve superior audio quality while keeping low computationallcomplexity, multiple multi-resolution discriminators are adopted.
"Figure 1: The architecture ofPLCNet."
·To improve the ability of the encoder to extract global features, a semi-supervised training strategy is introduced.
Through the objective quality index evaluation, PLCNet outperforms both traditional PLC algorithms and state-of-the-art deep PLC algorithms. In the PLC Challenge, our approach has ranked the 3rd place on the final score. The remainder of this paper is organized as follows.
Section II describes the proposed PLCNet framework in detail. Section III shows the experimental results and analysis. Then draw conclusions in Section IV.
In order to solve the problem that existing PLC methods are difficult to generate high-quality speech while maintaining low computational complexity in real-time scenarios. We proposed PLCNet, which not only lightweight but also efficient. The architecture of PLCNet is shown in Figure 1. Next, we will introduce model architecture, training inference strategy and loss function adopted in this paper in detail.
The generator of PLCNet is a symmetric encoder-decoder structure with skip connections and residual units. The encoder and decoder each have 4 sub-modules, each sub-module of the encoder consists of 3 residual units and a down-sampling module and each sub-module of the decoder consists of an up-sampling module and 3 residual units. The residual unit alternately uses 1-D dilated convolution with kernel size of 7and 1-D convolution with kernel size of 1. The dilation rate is gradually increased using (1,3, 9). The input is first transformed by 1-D convolution with kernel size of 7, then the encoder maps the 16khz waveform to the 50hz representation through down-sampling block of (2,4,5,8) in the form of a stride convolution. The decoder uses the transposed convolution method to up-sampling in reverse order, restores the features to the same dimension as the speech. The number of channels is doubled when down-sampling and halved when up-sampling. The middle bottleneck layer acts as a bridge between encoder and decoder and consists of 3 1-D convolutions with kernel size of7. A skip-connection is used between the corresponding layers of the encoder and decoder to allow information such as phase or alignment to pass through. We use the ELU activation function [19] and weight normalization in the generator to guarantee the stability of adversarial training. Finally, the output of the decoder is a mono signal, with tanh limiting the output range to [-1,1]. To be able to process real-time audio streams on low-power mobile devices, all our convolutions are causal.
To jointly optimize the waveform-domain adversarial loss, we employ multi-period discriminator (MPD)[20-21] and multi-scale discriminator (MSD)[20-21] to identify speech signal from two different perspectives. The MSD method is derived from the MelGAN vocoder. Through the average pooling operation, the length of the speech sequence is halved successively. Then the convolution operation is performed on the speech signals of different scales. Finally, it is flattened and output. The MPD method folds the single-channel audio sequence into a two-channel audio with different fixed-lengths called period, and then apply 2-D convolution on the folded data. The disadvantage of this approach is the folded data on each channel is mixed with artifacts of different frequencies. In edy order to make up for this defect, we proposed multi-length discriminator (MLD), to improve ability of discriminating synthetic or real audio as much as possible. Firstly, the single-channel audio is folded into multi-channel audio by wavelet transform[20]. Then apply 1-D dilated convolution as in [22]. In this way, each channel in the folded data contains few or no artifacts of other frequencies, ensuring the stability and accuracy of the discrimination.
The flowchart of the training stage is shown in Figure 2. In addition to audio samples of the current frame, a binary flag mask is added to the input as one of the channels to indicate whether the current silence frame is real or corresponds to lost packets. On the one hand, we use generator G and discriminator D for adversarial training. The D is trained to classify ground truth samples to 1 and the samples synthesized from G to 0. The G is trained to fake the D by updating the sample quality to be classified to a value almost equal to 1; On the other hand, we employ mean teacher[23] to perform semi-supervised training on the encoder part of G to further improve its ability to extract global features. The core idea of mean teacher is that the encoder part acts as both student and teacher. First, the teacher model is used to encode the unmasked training samples to generate the learning target of the student model. Second, the student model to encode the masked training samples and to predict the complete data representation. The weight of the teacher model
is exponential moving average (EMA) of the weight of the student model
"t at time-step t, calculated as:"
Set EMA decay a=0.99 during ramp-up phase andα=0.999 in later training. Since the student model is random at the beginning, the teacher model needs to forget the previous incorrect student weights. When good parameters have been learned, the student model improves slowly and the teacher
model has a longer memory the better. We use the Adam optimizer[24] for training with a batch size of 128 and a constant learning rate of0.0003. We trained on 8 NVIDIA Tesla V100 GPUs for 300k iterations. We use the last checkpoint of each training run to evaluate the results.
The flowchart of the inference stage is shown in Figure 2. Since the PLCNet is a causal structure and the required information for the current frame is available, it can do real-time streaming inference by preserving the past intermediate data into rolling buffer. The inference process can be summarized as follows. Firstly, it is necessary to judge whether the current frame is lost or not. If there is no lost, set the binary flag mask=0 and the model outputs as it is; If there is lost, the value of the samples is set to 0 and mask=1 to tell the model that there is signal needs to be reconstructed. The model looks at the available past information through its receptive field to reconstruct the packet loss. The prediction of all future samples is performed in parallel and any past packet loss will not be predicted for the inference of the next frame. Instead. the network has to learn to reconstruct using only the packets that have not been lost in the past, which also forces it to have a stronger ability to reconstruct against successive packet losses. Moreover, PLCNet can guarantee the smoothness and continuity of the speech phase before and after packet loss without any smoothing operations.
"For the generator G and discriminator D, the training objectives follow LSGAN [25], which replace the binary cross-entropy terms of the original GAN objectives with least squares loss functions for non-vanishing gradient flows. GAN losses for G and D are defined as:"
"L_{ad \\nu \\left( D \\right) }{=}E_{ \\left( x,s \\right) }[ \\left( { \\cal D} \\left( x \\right) {-}I \\right) ^{2}+ \\left( { \\cal D} \\left( { \\cal G} \\left( s \\right) \\right) ^{2}]"
"where x denotes the ground truth audio and s is a lossy one. In addition, we add multi-resolution STFT loss [21], which can effectively capture the time-frequency distribution of the real waveform, defined as:"
"spectral convergence and log STFT magnitudeloss, respectively. Forr differentIRspectral resolutions.P:which1areobtainedwiththesame STFT configurations as in [21]. The third is the time domain loss, which calculates the L1 distance between the real waveform and the generated waveform, defined as:"
"The fourth is the consistency loss, which calculates the L2distance between the output of the 4 encoder blocks of the teacher model and the output of the 4 encoder blocks of the student model, calculated as:"
"{ \\cal L}_{con}==E_{ \\left( x,s \\right) }[ \\left( {{{y}_{t}} \\left( x \\right) {-}f_{t} \\left( s \\right) \\right) }^{2}] (6)"
represents the teacher model prediction at time-step
"represents the student model prediction at time-step t. Our final objectives for the generator and discriminator are:"
",time=100 and 入con=1000."
"Figure 2: The flowchart of training and inference stage."
We conduct experiments on the VCTK corpus [26], which contains dozens of hours of neutral utterances from 109speakers. First, we preprocess the corpus with a voice activity detector, filter out silences longer than 100ms at the beginning and end ofthe file, and resample it to 16 kHz. Second, we divide the corpus into training, validation and test subsets of hierarchical speaker identities, so they contain 100, 4 and 5speakers, respectively. For PLC tasks, it is essential to simulate realistic scenarios of packet loss. A packet in the experiments contained a 20ms speech frame and the lost packets were simulated using opus codec demo which is available at
. The packet loss rate range of training data is set to 10%-40% and the maximum continuous packet loss length is 120ms. Each speech sequence is randomly selected. Similarly, the test subset also has 5 different packet loss rates of 10%,20%,30% and 40%.
We compare PLCNet with 3 classical PLC methods and 3 state-of-the-art deep PLC methods to illustrate the superiority. First, a zero-filled PLC method be used to establish a lower bound for the reconstruction method. Second, we use the opus's PLC[27] WebRTC's PLC[28] and evs's PLC[29]as classical PLC methods baseline. Third, we consider 3 state-of-the-art models in the deep PLC field, which are the mel-to-wave non-autoregressive adversarial auto-encoding network (PLAAE)[16],the wave-to-wave autoregressive convolutional recurrent network(CRN)[11] and wave-to-wave autoregressive time-frequency generative adversarial network (TFGAN) [17]. We performed experiments as described in the paper under the VCTK dataset, all models are causally implemented and trained for 300k steps until convergence on the validation set.
To evaluate the effect of different PLC methods, we employ 2objective measures, which are Perceptual Evaluation of Speech Quality (PESQ)[30] and Short Time Objective Intelligibility(STOI) [31]. PESQ scores range is -0.5-4.5, STOI score ranges is 0-1, with larger values indicating higher intelligibility and better quality of speech. In addition, the INTERSPEECH 2022PLC Challenge also provides PLC-MOS neural network model that estimates ofhuman ratings ofaudio files with healed packet losses [18]. The official ranking is based on the score which reflects both Crowd-Sourced Mean Opinion Score and Word Accuracy[32].
We investigate the effectiveness of the proposed discriminator and mean teacher semi-supervised schemes. The experimental results under different packet loss rates are shown in Table 1. First, only the generator G is called G in Table 1; second, the generator G and the discriminator D are called G+D in Table 1:third, the generator G and the mean teacher semi-supervised are called G+semi-supervised in Table 1. It can be clearly seen from the table that the introduction of the discriminator D increases the average of PESQ by 0.26 dB and the average of STOI by 7.59% and enables the generator to generate near-real samples. In addition, the introduction of mean teacher semi-supervised scheme improves the average of PESQ by 0.23 dB and the average of STOI by 6.33%. Since update method of EMA for the teacher model, the weights improve the output of all layers on average, not just the output of the top layer, the target model has a better intermediate representation. That is, the quality of the generated speech can be improved without increasing the generation network model.
The evaluation results of the proposed PLCNet and baseline systems are presented in figure 3, where (a) and (b) represent the average of PESQ and the average of STOI under different packet loss rates, respectively. The horizontal axis represents different algorithms, and the vertical axis represents the scores. It can be clearly seen from the figure 3 that the proposed PLCNet is optimal under these two objective evaluation indicators. Compared with the best-performing evs's PLC in classical baseline system, PLCNet has an increase of 0.34db in PESQ and 11.54% in STOI. Compared with the best-performing PLAAE in the baseline system, PLCNet improves PESQ by 0.19db and STOI by 3.57%.
Moreover, Table 2 presents the trainable parameters and the number of multiply accumulate operations (MACs) per second of all of the DNNs-based competing methods. One can see that the proposed PLCNet can maintain generate high-quality speech signal while having many fewer parameters and a lower computational complexity. Furthermore, the PLCNet takes 1.5ms to infer a frame of 20ms speech signal on an Intel Core i5 quad-core machine clocked at 2.4 GHz.
(a)PESQ (b) STOI
"Figure 3: The histogram ofPESQ and STOI for different methods."
"Table 2: The comparison in terms oftrainable parameters"
(10°) and multiply accumulate operations (10°) ofmodels.
We participated in the INTERSPEECH 2022 PLC Challenge using the PLCNet. The officially released results on the blind test set in Table 3 show that PLCNet significantly outperforms the challenge baseline with absolute 0.915 PLCMOS gain and0.073 final score gain. Our method ranked the 3rd place in PLCMOS and the 3rd place in final score.
This paper proposes a casual wav-to-wav semi-supervised lightweight generative adversarial network --PLCNet, which learns to reconstruct lost speech signals through an encoding-decoding process. Objective metrics show that PLCNet consistently outperforms other baseline models under different packet loss rates. In other words, the proposed method is not only lightweight but also efficient. In the INTERSPEECH 2022PLC Challenge, our approach has ranked the 3rd place on the final score. In future work, we will try to introduce an adaptive attention mechanism into the model to further improve the ability to resist continuous packet loss.
"Table 1: The results ofablation experiments on PESQ and STOI under different packet loss rates."
"Table 3: The results of subjective ratings in terms ofMOS and Word accuracy for the blind test set of the PLC Challenge."
"[1] S. M. Kay and S. L. Marple, \"Spectrum analysisA modern perspective,\"in Proceedings of the IEEE, vol. 69, no. 11, pp.1380-1419,Nov.1981."
"[2] C. A. Rodbro, M. N. Murthi, S. V. Andersen and S. H. Jensen,\"Hidden Markov model-based packet loss concealment for voice over IP,\"IEEE Transactions on Audio, Speech, and Language Processing, vol. 14, no. 5, pp. 1609-1623,2006."
"[3] O. Ronneberger, P. Fischer and T. Brox, \"U-Net: Convolutional Networks for Biomedical Image Segmentation,\"International Conference on Medical image computing and computer-assisted intervention. Springer, Cham, 2015: 234-241."
"[4] A. Marafioti, N. Perraudin, N. Holighaus and P. Majdak, \"A context encoder for audio inpainting,\"IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 27, no. 12,pp.2362-2372.2019."
5| Y.-L. Chang, K.-Y. Lee, P.-Y. Wu, H.-Y. Lee and W. Hsu, "Deep Long Audio Inpainting,"arXiv preprint arXiv:1911.06476,2019.
"[6] H. Zhou, Z. Liu, X. Xu, P. Luo, and X. Wang, \"Vision-Infused Deep Audio Inpainting,\" in 2019 IEEE/CVF International Conference on Computer Vision (ICCV), Seoul, Korea (South):Oct. 2019, pp. 283-292."
"[7] G. Morrone, D. Michelsanti, Z.-H. Tan and J. Jensen, \"Audio-ino\"inIC4SS p 20Visual Speech Inpainting with Deep Learning,\"in ICASSP 2021-2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Jun. 2021, pp. 6653-6657.-51"
18 B.K. Lee and J.H. Chang, "Packet Loss Concealment Based on Deep Neural Networks for Digital Speech Transmission,"IEEE/ACM Trans. Audio, Speech and Lang. Proc., vol. 24, no. 2, p.378387,2016.
"[9] J. Lin, Y. Wang, K. Kalgaonkar, G. Keren, D. Zhang and C. Fuegen, \"A Time-Domain Convolutional Recurrent Network for Packet Loss Concealment\"inICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Jun. 2021, pp. 7148-7152."
"[10]M. M. Mohamed and B. W. Schuller, \"ConcealNet: An End- to-end Neural Network for Packet Loss Concealment in Deep Speech Emotion Recognition,\"arXiv preprint arXiv:2005.07777,2020."
"[11]R. Lotfidereshgi and P. Gournay, \"Speech Prediction Using an Adaptive Recurrent Neural Network with Application to Packet Loss Concealment,\" in IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). Calgary, AB, Canada: IEEE,2018, pp. 5394-5398."
"[12]]S. Hochreiter and J. Schmidhuber, \"Long Short-term Memory,'Neural computation, vol. 9, no. 8, pp. 1735-1780,1997."
"[13]F.Stimberg, A. Narest and A. Bazzica, \"WaveNetEQ-Packet Loss Concealment with WaveRNN,\"2020 54th Asilomar Conference on Signals, Systems, and Computers, 2020,pp. 672-676."
"[14]]J. Kong,J. Kim and J. Bae, \"Hifi-gan: Generative adversarial networks for efficient and high fidelity speech synthesis,\"Advances in Neural Information Processing Systems, 2020, 33:s17022-17033."
"[15]Y. Shi, N. Zheng, Y. Kang and W. Rong, \"Speech Loss Compensation by Generative Adversarial Networks,\" in 2019Asia-Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC), Nov. 2019, pp.347-351."
"[16]|S. Pascual,J. Serra, and J. Pons, \"Adversarial Auto-Encoding for PackettLossConcealment,\"2021IEEEWorkshop on Applications of SignalProcessing to Audio and Acoustics(WASPAA).2021:71-75."
"[17]|J. Wang, Y. Guan, C. Zheng, R. Peng and X. Li, \"A temporal-spectral generative adversarial network based end-to-end packet loss concealment for wideband speech transmission,\"The Journal of the Acoustical Society of America, vol. 150, no. 4, pp. 2577-2588,Oct.2021."
"[18]L. Diener, S. Sootla, S. Branets, A. Saabas, R. Aichner and R. Cutler, \"INTERSPEECH 2022 Audio Deep Packet Loss Concealment Challenge\", in INTERSPEECH2022-23rd Annual"
Conferenceof theeInternational SpeechhCommunication Association, 2022,submitted.
「19]D.-A. Clevert, T. Unterthiner and S. Hochreiter, "Fast and Accurate Deep Network Learning by Exponential Linear Units(ELUs),"Computer Science, 2015.
"[20]J.-H. Kim, S.-H. Lee, J.-H. Lee and S.-W. Lee, \"Fre-GAN:AdversarialFrequency-consistenntAudioSynthesis'', arXiv preprint arXiv:2106.02297,2021."
"[21]G. Yang, S. Yang, K. Liu, P. Fang, W. Chen and L. Xie, \"Multi-band MelGAN: Faster waveform generation for high quality text-to-speech,\" in Proc. of IEEE Spoken Language Technology Workshop(SLT).2021, pp. 492-498."
"[22]R. Yamamoto, E. Song and J. -M. Kim, \"Parallel Wavegan: A FastWaveform GenerationnModelBased onGenerative AdversarialNetworks with Multi-Resolution"
ICASSP2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP),2020, pp.6199-6203.
"[23]A. Baevski, W.-N. Hsu, Q. Xu, A. Babu, J. Gu and M. Auli,\"data2vec: A General Framework for Self-supervised Learning in Speech, Vision and Language'\", arXiv preprint arXiv:2202.03555,2022."
"[24]D.-P. Kingma and J. Ba, \"Adam: A method for stochastic optimization,\"arXiv preprint arXiv:1412.6980,2014."
"[25]M. Xudong, L. Qing, X. Haoran, R. YK.Lau, W. Zhen and S.P. Smolley, \"Least squares generative adversarial networks'\", In Proceedings of the IEEE International Conference on Computer Vision, pages 2794-2802,2017."
"[26]C. Veaux,J. Yamagishi and K. MacDonald, \"CSTR VCTK Corpus: English multi-speaker corpus for CSTR voice cloning toolkit,\""
"[27]\"ITU-T Recommendation 722.1: low-complexity coding at 24and 32 kbit/s for hands-free operation in systems with low frame loss,\"2005."
"[28]W.W.W. Consortium, \"WebRTC 1.0: Real-Time Communi-cation Between Browsers,\""
", 2021, online; accessed 28 April 2021."
"[30]A. W. Rix, J. G. Beerends, M. P. Hollier and A. P. Hekstra,\"Perceptual evaluation of speech quality (PESQ)-a new method for speech quality assessment of telephone networks and codecs,\"2001 IEEE International Conference on Acoustics, Speech, and Signal Processing. Proceedings (Cat. No.01CH37221),2001,pp.749-752 vol.2."
"[31]C.H.Taal, R. C. Hendriks, R. Heusdens and J. Jensen, \"A short-time objective intelligibility measure for time-frequency weighted noisy speech,\"2010IEEE International Conference on Acoustics, Speech and Signal Processing,2010,pp. 4214-4217."
"[32]R. Cutler, B. Nadari, M. Loide, S. Sootla and A. Saabas, \"Crowd-sourcing approach for subjective evaluation of echo impairment,\"2020,arXiv: 2010.13063."
"{ 6 items \" Status \" : \"Success\" \" RequestId \" : \"80955FCD-9B1E-1C73-BFF3-4DC3937BF1D2\" \" CreateTime \" : \"2024-08-14 13:49:33\" \" Completed \" : true"
"\"Data\" : { 3 items \" numberOfSuccessfulParsing \" : 112 \"layouts\" : 112 items"
"[ 0 - 100 ]"
"[ 100 - 112 ] \" status \" : \"success\" } \" Id \" : \"docmind-PRE-20240814-b0b7229e5ca946018d198ac2f42f596d\" }"

## 产品优势

- 算法技术先进 依托阿里丰富的文档场景，打磨先进的多模态文档识别与理解引擎，算法效果与性能指标处于较高水平。
- 行业应用丰富 覆盖招投标、政务、金融财税等多行业多场景应用，可满足各行各业的文档处理需求。
- 部署方式灵活 支持公共云API、混合云Docker、aPaaS、SaaS等多种产品部署方式，产品接入灵活，使用门槛低。
- 服务质量可靠 提供高可用的文档处理能力，已在海量文档处理业务中反复锤炼，服务稳定性高，支持弹性扩缩容。

## 文档与工具

- 产品简介 快速了解文档智能 什么是文档智能 文档理解 文档格式转换 文档自学习
产品简介 快速了解文档智能
- 用户指南 5分钟接入文档智能 新手指引 API使用指南 控制台使用指南 小程序使用指南
用户指南 5分钟接入文档智能
- API文档 API接口使用文档 API概览 服务入口 文档智能解析 PDF转Word
API文档 API接口使用文档
- 常见问题 常见问题供查阅参考 文档智能技术的处理流程 文档智能和文字识别的区别 如何选择合适的能力 产品收费方式是什么样的
常见问题 常见问题供查阅参考

## 更多产品与服务

- 文档理解 对各类文档和表格进行结构化识别与理解，并可在此基础上完成文档抽取等多种通用场景下的文档处理任务。 查看详情

