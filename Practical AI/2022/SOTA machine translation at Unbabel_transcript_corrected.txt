[0.00 → 2.52] We have started a project on this.
[2.66 → 4.34] It's to combine these systems,
[4.48 → 5.94] these quality estimation systems,
[6.12 → 7.60] with the machine translation itself.
[7.90 → 10.62] So that is something that we started working on this,
[10.70 → 12.66] but I believe that you can work on this
[12.66 → 14.26] for the next few years,
[14.26 → 16.34] and there are a lot of things that we can improve there.
[16.94 → 18.74] Yeah, that gets me really excited.
[19.06 → 22.60] I think it's a direction that it's going to be really nice.
[22.92 → 25.10] This is the Quality Aware decoding project
[25.10 → 27.34] that is basically what I just mentioned [27.34 → 29.10] what we have been talking about
[29.10 → 30.88] of having these quality predictions
[30.88 → 33.14] about the hypothesis translations.
[33.78 → 36.76] The idea behind this project that Ricardo is talking about
[36.76 → 39.44] is what if we bring the quality estimation or comment
[39.44 → 42.48] already to inside the ME process,
[42.66 → 47.22] and then we can make the machine translation aware
[47.22 → 49.42] or more aware about its quality,
[49.54 → 51.12] having a signal from a different model.
[51.30 → 53.22] So this is what this project is about.
[59.10 → 66.04] Welcome to Practical AI,
[66.46 → 69.02] a weekly podcast making artificial intelligence
[69.02 → 71.72] practical, productive, and accessible to everyone.
[72.10 → 72.88] Subscribe now.
[73.02 → 73.76] If you haven't already,
[73.96 → 76.86] head to practicalai.fm for all the ways.
[77.24 → 79.56] Special thanks to our partners at Vastly
[79.56 → 81.70] for delivering our shows superfast
[81.70 → 82.86] to wherever you listen.
[83.18 → 85.04] Check them out at fastly.com.
[85.04 → 87.42] And to our friends at fly.io.
[87.82 → 90.32] We deploy our app servers close to our users,
[90.56 → 91.38] and you can too.
[91.70 → 93.60] Learn more at fly.io.
[93.60 → 102.34] Welcome to another episode of Practical AI.
[102.64 → 103.98] This is Daniel Whiten ack.
[104.08 → 106.78] I'm a data scientist with SIL International,
[107.12 → 109.68] and I'm joined this week by Ricardo Ray
[109.68 → 112.78] and Jose Souza from Unable
[112.78 → 116.48] here at EM NLP 2022 in Abu Dhabi.
[116.60 → 117.18] How are you doing, guys?
[117.38 → 118.26] Hi, we are fine.
[118.38 → 119.30] Hi, good.
[119.64 → 121.28] How is EM NLP for you?
[121.28 → 125.90] So far, we have been mostly attending WMT workshop.
[126.04 → 127.46] Yeah, and what's WMT?
[127.64 → 128.34] What does that stand for?
[128.80 → 129.02] Right.
[129.18 → 133.22] WMT stands for Workshop on Statistical Translation.
[133.50 → 134.42] Workshop on Machine Translation.
[134.46 → 135.22] On Machine Translation.
[135.34 → 138.04] But this is an historical acronym
[138.04 → 140.96] because it's actually now a conference.
[141.24 → 143.18] I would say that it's the main conference
[143.18 → 144.12] of machine translation,
[144.44 → 147.06] and it has been happening for several years.
[147.74 → 150.28] And it's always collocated with EM NLP,
[150.28 → 154.10] so it's nice because it's one of the biggest NLP conferences
[154.10 → 156.88] together with the biggest MT conference.
[157.30 → 160.58] It's mostly attended by researchers,
[161.26 → 165.14] so not so much by people in localization industry,
[165.56 → 168.22] but it's interesting to know what's happening
[168.22 → 169.42] in terms of research,
[169.62 → 170.90] the latest approaches,
[171.22 → 173.48] and methodologies for evaluation as well.
[173.80 → 176.52] Yeah, and is that the industry that Unable is in?
[176.52 → 178.90] Could you just give people a little bit of an understanding
[178.90 → 180.30] of what Unable is?
[180.62 → 180.78] Sure.
[180.98 → 183.32] So Unable is a translation company.
[183.78 → 185.88] We provide translations,
[186.24 → 188.88] trying to unite the best of both worlds,
[189.32 → 191.12] which is using machine translation
[191.12 → 193.10] and professional translators
[193.10 → 194.54] to provide these translations,
[194.76 → 196.10] and the best of both worlds,
[196.10 → 200.46] because if you only rely on translators themselves,
[200.70 → 203.30] it's very difficult to scale this process of translation
[203.30 → 205.86] to different volumes of content.
[206.58 → 208.22] And that's why you use machine translation
[208.22 → 210.16] to speed up this process,
[210.28 → 211.76] and then you use the translators
[211.76 → 213.52] to correct if necessary.
[214.36 → 215.50] And that's, I think,
[215.58 → 218.46] the biggest difference of Unable
[218.46 → 219.56] to other companies,
[219.74 → 222.04] which is we are the pioneers
[222.04 → 224.10] to use something called quality estimation
[224.10 → 225.76] to actually decide whether
[225.76 → 227.84] if we should post-edit or not,
[228.28 → 228.84] the translations.
[229.62 → 232.18] And I guess we are big on also
[232.18 → 234.24] evaluation technology, evaluation,
[234.98 → 237.58] and I think Ricardo can talk about Comet.
[238.08 → 240.78] Yeah, like what José just explained
[240.78 → 244.14] about the difference between combining humans and MT.
[244.64 → 246.18] So if you have a mechanism
[246.18 → 249.04] that tells you that your machine translation output is perfect,
[249.80 → 251.22] then you don't need a human.
[251.22 → 252.98] But for you to do this,
[253.14 → 257.72] you clearly need a very reliable quality estimation system,
[257.84 → 259.46] a system that receives that translation
[259.46 → 262.50] and is able to give you an accurate score
[262.50 → 263.88] for that translation.
[264.36 → 267.12] And that's why Unable has been focusing
[267.12 → 268.64] for so many years
[268.64 → 270.88] on specifically quality estimation
[270.88 → 272.00] and also evaluation.
[272.56 → 275.62] Evaluation, it's a little bit more general.
[275.96 → 278.66] It can also include things like metrics,
[278.66 → 280.58] where you compare the translation output
[280.58 → 282.38] with a reference translation
[282.38 → 283.80] that you believe to be perfect.
[284.12 → 286.08] And it's what people typically use
[286.08 → 287.78] when training models and stuff like that.
[288.18 → 289.46] For the past few years,
[289.50 → 290.88] we have been developing a metric
[290.88 → 293.24] that is being widely adopted
[293.24 → 294.68] by the research community
[294.68 → 296.34] and also the industry,
[296.54 → 297.46] which is called Comet.
[298.24 → 300.36] Comet has been very successful
[300.36 → 301.76] in the last two years.
[302.36 → 304.14] And yeah, it was developed by us.
[304.14 → 308.60] We also developed a quality estimation framework
[308.60 → 311.58] that was also gained a lot of traction
[311.58 → 313.32] three years ago, I think.
[313.56 → 314.84] Yeah, 2019 it was.
[314.98 → 316.52] Yeah, called Open,
[317.00 → 319.16] which is basically similar
[319.16 → 322.42] in terms of the model approach and everything,
[322.56 → 324.48] but it does not rely on a reference.
[324.90 → 326.84] So it's what we use internally
[326.84 → 328.68] for performing quality estimation.
[329.52 → 331.42] Yeah, I think this sums up a little bit.
[331.42 → 333.90] That said, just one thing is that
[333.90 → 335.14] all of this is only possible
[335.14 → 336.58] because over the years,
[336.68 → 339.34] Mabel established some quality controls
[339.34 → 340.30] for the translations.
[341.14 → 344.34] And this started by using something,
[344.66 → 346.42] a framework called MQM,
[347.24 → 348.06] which stands for
[348.06 → 350.54] Multidimensional Quality Metric,
[351.02 → 352.72] which is basically a typology
[352.72 → 354.34] and then guidelines
[354.34 → 355.86] on how to use this typology
[355.86 → 357.10] with different phenomena
[357.10 → 360.84] that happens when translation is made
[360.84 → 363.04] that goes from accuracy,
[363.52 → 366.16] you know whether the translations are adequate,
[366.82 → 367.50] if they're fluent,
[367.82 → 370.08] and then there's a whole taxonomy about that.
[370.68 → 372.64] So this kind of evaluation
[372.64 → 374.90] enabled us to accumulate data
[374.90 → 378.16] about the quality of translations over time
[378.16 → 379.26] that we can then use
[379.26 → 381.06] to train quality estimation
[381.06 → 384.34] or metric evaluation models.
[384.84 → 386.14] Yeah, so this seems different.
[386.26 → 387.90] I think some listeners probably
[387.90 → 389.18] in their experience
[389.18 → 389.98] with like modelling
[389.98 → 391.32] and other domains
[391.32 → 392.22] or with other data
[392.22 → 393.08] are probably familiar
[393.08 → 394.88] with like a confidence score
[394.88 → 395.62] or a probability.
[395.88 → 397.74] So this goes like way beyond that, right?
[397.82 → 398.96] So just to clarify,
[399.26 → 400.20] this is not like
[400.20 → 401.88] just a confidence score
[401.88 → 402.92] coming out of your model
[402.92 → 404.76] like that of translation,
[404.76 → 406.78] but this is actually a metric
[406.78 → 407.46] that you're running
[407.46 → 409.08] on the output of your model.
[409.16 → 409.56] Is that right?
[409.90 → 410.22] Exactly.
[410.48 → 411.02] Yeah, exactly.
[411.02 → 415.08] Yeah, and so explain maybe Comet a little bit
[415.08 → 417.62] because that has like gained so much traction.
[417.94 → 420.20] What is maybe different about Comet?
[420.44 → 421.42] Another, you know,
[421.50 → 422.28] popular one I know
[422.28 → 424.14] for machine translation is called Blue.
[424.58 → 426.62] So what distinguishes Comet
[426.62 → 428.70] as different from maybe that
[428.70 → 430.54] or like other metrics that are out there?
[430.74 → 432.06] So like you were saying,
[432.28 → 434.72] Blur is a very well-known metric,
[434.88 → 437.02] but Blur is a lexical metric.
[437.02 → 440.68] And this means that Blur will take the empty output
[440.68 → 443.58] and it will compare with a reference
[443.58 → 445.46] that was created from a human.
[446.08 → 448.88] And usually the typical setup
[448.88 → 451.04] is that we only compare that empty output
[451.04 → 452.32] with a single reference.
[452.92 → 454.42] And as we might know,
[454.82 → 456.10] there are multiple ways
[456.10 → 458.54] to translate a specific sentence.
[459.06 → 462.60] So a lot of times Blur will give a very low score
[462.60 → 466.00] for a very good translation because of that.
[466.00 → 468.68] Sometimes it also gives you a very high score
[468.68 → 470.78] for a very bad translation
[470.78 → 473.42] because of another aspect of Blur
[473.42 → 475.68] it's that it's going to give the same weight
[475.68 → 477.00] to all words.
[477.16 → 479.08] So if you have a named entity
[479.08 → 480.74] that is not correctly translated,
[481.36 → 483.72] it's going to be like one word
[483.72 → 486.16] that is missing from being perfect.
[486.72 → 488.26] And Blur will give a very high score.
[488.50 → 490.38] If you miss like a punctuation,
[491.08 → 493.28] the score penalty will be exactly the same.
[493.40 → 495.26] Although the errors are completely different
[495.26 → 496.26] in terms of severity.
[496.26 → 499.14] Just one thing to differentiate between,
[499.54 → 501.50] just to explain a little bit more Blur
[501.50 → 503.10] is that the way that it looks
[503.10 → 505.14] at both the translation hypothesis
[505.14 → 506.06] and the references,
[506.82 → 508.70] looking at each word
[508.70 → 510.36] and trying to understand
[510.36 → 512.28] if there is an overlap of each word
[512.28 → 513.72] with the reference.
[514.06 → 516.46] And it does that for combinations of,
[516.74 → 518.88] for one word or for combinations of two,
[519.08 → 520.44] three and four words usually,
[520.74 → 522.46] which we call engrams.
[522.46 → 525.18] So, and then it has a brevity penalty
[525.18 → 527.24] that is basically to penalize
[527.24 → 528.70] if the translation is too small,
[528.84 → 529.66] too short.
[529.98 → 531.76] So that's basically the rationale.
[532.08 → 533.94] And there is a class of metrics
[533.94 → 535.24] called like that.
[535.30 → 536.94] I think we are calling lexical metrics.
[537.20 → 537.88] Yeah, lexical metrics.
[537.88 → 538.12] Yeah.
[538.32 → 540.70] So TER, which is translation error rate,
[541.18 → 542.12] it's similar to that.
[542.48 → 543.94] CHRF, it's similar to that,
[544.04 → 546.00] but CHRF goes at the character level.
[546.70 → 547.90] So this is a class of things
[547.90 → 550.74] that is very different from Comet,
[550.96 → 551.28] I think.
[551.66 → 551.86] Yeah.
[552.04 → 553.08] Comet takes advantage
[553.08 → 555.42] of the representations coming
[555.42 → 556.74] for large language models
[556.74 → 558.52] like XML-Ruberta.
[558.66 → 560.30] We have been using XML-Ruberta.
[560.30 → 562.80] And basically those representations
[562.80 → 564.34] allow you to compare words
[564.34 → 565.30] in an embedding space.
[565.64 → 567.24] So two words that might not be
[567.24 → 567.96] exactly the same,
[568.02 → 569.40] but have the exact same meaning,
[570.02 → 573.32] the Comet will use those representations
[573.32 → 575.08] to output a score.
[575.72 → 578.32] Now, the other thing that we add on top
[578.32 → 580.66] is that we train those representations
[580.66 → 582.74] to be more suitable
[582.74 → 584.36] for the specific task
[584.36 → 586.32] of machine translation evaluation.
[586.32 → 587.88] And I'm saying this
[587.88 → 590.08] because this is a very important difference
[590.08 → 591.70] from other metrics
[591.70 → 593.18] that have also been proposed
[593.18 → 594.04] like BERT score,
[594.54 → 595.86] where because of the fact
[595.86 → 596.76] that you don't have
[596.76 → 599.32] any fine-tuning on top,
[599.46 → 600.68] if you use BERT score
[600.68 → 601.88] and you say,
[602.16 → 603.84] I love you, or I hate you,
[604.22 → 605.76] because love and hate
[605.76 → 607.74] will have similar embeddings,
[608.46 → 609.92] the score will be very high
[609.92 → 611.14] when in fact
[611.14 → 612.54] they are the complete opposites.
[613.02 → 615.46] So we start from a pre-training model,
[615.46 → 618.26] but then by training the model
[618.26 → 619.38] with some supervision
[619.38 → 622.40] from human labels on errors,
[622.98 → 624.12] the model learns that
[624.12 → 625.94] I love you, or I hate you
[625.94 → 628.10] for this specific task,
[628.46 → 629.74] they are complete opposites.
[630.40 → 632.92] And I think that kind of splits apart,
[633.38 → 635.02] Comet from all the metrics
[635.02 → 636.72] that were being proposed before
[636.72 → 639.14] that either fall into the lexical category
[639.14 → 641.00] or into the embedding category.
[641.76 → 642.38] Yeah, that's great.
[642.50 → 643.54] And you also mentioned
[643.54 → 644.80] just in passing,
[644.80 → 646.70] like there was another kind of category
[646.70 → 648.10] of quality estimation
[648.10 → 649.96] that didn't require a reference.
[650.12 → 651.32] Could you talk about that a little bit?
[651.66 → 653.40] Yeah, so the idea is very similar
[653.40 → 654.66] to the idea of Comet.
[654.86 → 656.20] So the difference is that
[656.20 → 658.00] when you have access to a reference,
[658.24 → 659.32] which is the case of Comet,
[659.86 → 661.78] when you create the embeddings
[661.78 → 663.70] for the empty outputs,
[664.22 → 666.00] they will be perfectly aligned
[666.00 → 666.78] with the embeddings
[666.78 → 667.54] from the reference
[667.54 → 668.26] because they are
[668.26 → 669.88] on the exact same language.
[670.46 → 671.50] On quality estimation,
[671.50 → 673.38] you are comparing it
[673.38 → 674.46] directly to the source.
[674.80 → 675.86] So the embeddings
[675.86 → 677.72] will not align perfectly.
[678.08 → 679.26] And still,
[679.44 → 680.38] what happens is that
[680.38 → 681.16] during training,
[681.84 → 683.08] using human supervision,
[683.36 → 684.40] the model learns to
[684.40 → 686.00] what is correct
[686.00 → 686.80] and what is incorrect,
[686.80 → 688.04] only comparing
[688.04 → 689.30] the empty output
[689.30 → 691.96] directly with the source.
[691.96 → 693.36] So quality estimation
[693.36 → 694.64] serves a different kind
[694.64 → 695.28] of application
[695.28 → 696.38] than the metrics
[696.38 → 697.70] like BLUE,
[697.86 → 698.42] CHEF,
[698.56 → 698.96] and Comet,
[699.60 → 700.94] which is usually
[700.94 → 701.80] I want to know
[701.80 → 702.64] what is the quality
[702.64 → 703.98] of specific sentences
[703.98 → 704.88] or translations
[704.88 → 706.70] given their source sentences.
[707.20 → 707.64] For Comet,
[708.04 → 708.76] usually what you're
[708.76 → 709.30] more interested,
[709.54 → 711.68] Comet or the other metrics,
[712.10 → 712.80] you're more interested
[712.80 → 713.66] in understanding
[713.66 → 714.86] the difference between models
[714.86 → 716.14] or empty systems.
[716.14 → 717.32] So you're evaluating
[717.32 → 718.44] at some sort of,
[719.18 → 719.90] trying to understand
[719.90 → 720.80] at some sort of
[720.80 → 722.24] test set level
[722.24 → 723.46] or evaluation set level
[723.46 → 724.90] so that you can decide
[724.90 → 726.00] whether I go with model,
[726.60 → 727.64] empty model A,
[727.76 → 728.32] B, or C.
[728.86 → 729.80] And then in quality estimation
[729.80 → 730.36] is basically
[730.36 → 731.38] to take decisions
[731.38 → 732.46] on the fly
[732.46 → 733.26] at real time
[733.26 → 734.68] in which I cannot wait
[734.68 → 735.46] for someone
[735.46 → 736.44] to make a reference
[736.44 → 737.42] or a post-edition
[737.42 → 738.50] and decide,
[738.64 → 738.80] okay,
[739.12 → 740.78] can I trust this translation?
[741.28 → 742.00] If I don't,
[742.36 → 743.30] should I throw it out?
[743.36 → 743.80] Is that bad
[743.80 → 744.60] that I should do it
[744.60 → 745.12] from scratch?
[745.12 → 746.68] Or I can still give it
[746.68 → 747.26] to someone
[747.26 → 748.74] that can repurpose this
[748.74 → 749.80] and rephrase it,
[749.84 → 750.06] you know?
[750.58 → 751.76] So they're slightly
[751.76 → 752.76] different in the applications,
[753.54 → 753.98] but this is something
[753.98 → 754.82] that you can talk about
[754.82 → 755.90] about the trends.
[756.46 → 757.28] They start to,
[757.56 → 758.20] like I think
[758.20 → 759.30] Ricardo was teasing,
[760.06 → 762.24] to intersect themselves
[762.24 → 762.90] a bit.
[763.14 → 763.84] I would say that
[763.84 → 765.44] the metrics field,
[765.70 → 766.76] so the evaluation
[766.76 → 768.04] on the metrics side,
[768.56 → 771.28] was stuck with B for a long time.
[771.82 → 772.50] Quality estimation,
[772.72 → 773.64] on the other hand,
[773.90 → 774.22] was,
[774.22 → 775.34] I feel that
[775.34 → 776.44] there were more
[776.44 → 777.74] research
[777.74 → 779.18] and more innovation
[779.18 → 779.94] on that field.
[780.48 → 780.82] Actually,
[780.88 → 781.80] that was our motivation
[781.80 → 783.36] when we built Comet.
[783.58 → 784.66] We tried to replicate
[784.66 → 785.78] what was being done,
[785.98 → 786.86] the state of the art
[786.86 → 787.98] of what was being done
[787.98 → 789.32] on quality estimation.
[789.56 → 790.54] We tried to bring it
[790.54 → 792.14] to the metrics field,
[792.26 → 793.28] and now
[793.28 → 795.22] the modelling approaches
[795.22 → 796.36] are very similar,
[796.48 → 797.64] but it was viewed
[797.64 → 798.66] as two completely
[798.66 → 799.80] different tasks
[799.80 → 800.56] for years.
[800.56 → 801.28] So,
[801.72 → 802.88] just to give insight
[802.88 → 803.46] on what,
[804.08 → 805.14] a bit of context
[805.14 → 806.48] on what Ricardo said
[806.48 → 807.50] about the progress
[807.50 → 808.60] in quality estimation.
[809.08 → 809.26] So,
[809.34 → 810.14] I did my PhD
[810.14 → 811.66] on working on this
[811.66 → 812.66] kind of problem,
[813.12 → 814.34] and I finished
[814.34 → 815.72] like in 2015.
[816.36 → 816.54] So,
[816.62 → 817.22] I was working
[817.22 → 818.00] from 2012
[818.00 → 819.04] until 2015
[819.04 → 820.08] on problems
[820.08 → 820.66] around this,
[820.66 → 822.66] and the approaches
[822.66 → 823.08] back then,
[823.14 → 823.74] they were basically
[823.74 → 824.82] using feature-based
[824.82 → 825.20] approaches
[825.20 → 825.98] like classical
[825.98 → 827.08] machine learning,
[827.64 → 829.64] and with deep learning
[829.64 → 830.64] and access
[830.64 → 832.44] to embeddings
[832.44 → 833.22] and now
[833.22 → 834.34] large protein models,
[834.80 → 835.44] this very,
[835.70 → 836.90] very fast
[836.90 → 837.60] shifted
[837.60 → 838.68] to this kind
[838.68 → 839.24] of approaches,
[839.82 → 840.92] and the performance
[840.92 → 841.82] of these models,
[842.08 → 842.88] of these approaches
[842.88 → 844.64] also are much better
[844.64 → 845.60] than when I used
[845.60 → 847.00] to first work
[847.00 → 847.32] on this.
[847.54 → 847.56] So,
[847.84 → 848.86] the quality of these
[848.86 → 849.96] quality estimation models
[849.96 → 850.40] nowadays,
[850.40 → 851.10] that they are
[851.10 → 851.76] very useful.
[851.90 → 852.42] You can actually
[852.42 → 853.24] do a lot of things
[853.24 → 853.54] with them,
[853.60 → 854.12] like I was saying,
[854.50 → 854.96] and yeah,
[855.00 → 855.40] I just wanted
[855.40 → 856.48] to compliment that
[856.48 → 857.08] because for me,
[857.20 → 857.48] it was,
[857.72 → 858.54] I was not working
[858.54 → 859.02] on the field
[859.02 → 860.66] specifically this problem
[860.66 → 861.64] for, I don't know,
[861.68 → 862.18] three years,
[862.24 → 862.58] I guess.
[862.82 → 863.68] When I came back
[863.68 → 863.96] to it,
[864.02 → 864.22] it was,
[864.38 → 864.56] whoa,
[865.20 → 866.42] now it's really
[866.42 → 867.68] up to everything,
[867.82 → 868.06] you know.
[876.56 → 877.38] Could you explain
[877.38 → 877.66] a little bit,
[877.70 → 878.12] so you mentioned
[878.12 → 879.66] how like in Comet
[879.66 → 880.40] or in these other
[880.40 → 880.74] models,
[880.86 → 881.92] you might be comparing
[881.92 → 883.38] like the embeddings
[883.38 → 884.58] of words,
[885.02 → 886.34] but words don't always
[886.34 → 887.68] map like one-to-one
[887.68 → 888.66] between languages,
[889.00 → 890.16] and sometimes I don't
[890.16 → 890.72] know if you're looking
[890.72 → 891.34] at sentences
[891.34 → 892.20] or other things,
[892.30 → 893.06], but could you describe
[893.06 → 893.98] like some of the
[894.30 → 894.98] I guess what are the
[894.98 → 895.78] main challenges
[895.78 → 896.82] looking forward
[896.82 → 897.68] that like aren't
[897.68 → 899.02] solved yet in terms
[899.02 → 900.06] of like next steps
[900.06 → 901.08] with quality estimation
[901.08 → 902.20] and things that you're
[902.20 → 902.84] looking at now
[902.84 → 903.42] that you see
[903.42 → 904.58] as open problems?
[904.58 → 905.26] Yeah,
[905.40 → 906.28] you actually touched
[906.28 → 907.26] a very nice,
[907.52 → 908.64] very nice point.
[908.84 → 909.10] It's,
[909.46 → 910.48] I wouldn't say
[910.48 → 911.26] that it's not
[911.26 → 911.86] that the words
[911.86 → 913.20] don't align very well,
[913.26 → 914.04] but sometimes
[914.04 → 914.82] what we see
[914.82 → 916.20] is that the embeddings
[916.20 → 916.72] themselves
[916.72 → 917.54] for certain
[917.54 → 919.78] specific words
[919.78 → 920.74] are not
[920.74 → 922.30] discriminative
[922.30 → 922.82] enough,
[922.82 → 924.16] and we have seen
[924.16 → 924.50] some,
[924.90 → 925.20] for instance,
[925.20 → 925.94] if you translate
[925.94 → 926.58] the sentence,
[926.94 → 927.52] this apple
[927.52 → 928.86] costs 50 cents,
[928.86 → 929.62] you translate it
[929.62 → 930.12] to Portuguese,
[930.12 → 931.58] and the translation
[931.58 → 931.90] needs,
[932.08 → 932.64] I'm not going to
[932.64 → 933.30] say it in Portuguese,
[933.42 → 934.04] but pretend that
[934.04 → 934.68] I'm speaking Portuguese,
[934.96 → 935.80] the perfect translation
[935.80 → 936.94] would also be 50 cents,
[937.04 → 937.90] but for some reason
[937.90 → 938.56] the empty might
[938.56 → 939.78] have hallucinated
[939.78 → 940.46] and say that
[940.46 → 942.06] it's 500 cents.
[942.62 → 943.78] So it's basically
[943.78 → 945.16] changing the price
[945.16 → 945.86] of an apple
[945.86 → 946.70] and this is
[946.70 → 948.06] a critical error
[948.06 → 949.06] in many scenarios,
[949.60 → 950.26] but if you look
[950.26 → 950.92] at the embedding
[950.92 → 952.10] space of the
[952.10 → 953.70] 500 or the
[953.70 → 954.40] embedding of
[954.40 → 955.48] 50,
[956.12 → 957.02] it's going to be
[957.02 → 957.94] very similar
[957.94 → 959.08] and it's going to
[959.08 → 959.70] be very
[959.70 → 961.40] hard for the
[961.40 → 962.12] neural network
[962.12 → 962.82] that is trying
[962.82 → 963.64] to differentiate
[963.64 → 965.16] these two things,
[965.52 → 966.34] it's going to be
[966.34 → 967.68] a very hard task
[967.68 → 968.26] because there is
[968.26 → 969.40] not enough signal.
[969.88 → 970.46] You also see
[970.46 → 971.04] the same thing
[971.04 → 971.62] with some
[971.62 → 972.68] named entities
[972.68 → 973.92] and currently
[973.92 → 975.34] there has been
[975.34 → 976.54] some work,
[976.62 → 977.10] some progress
[977.10 → 977.96] in trying to
[977.96 → 979.10] look at the
[979.10 → 979.80] quality estimation
[979.80 → 980.38] and metrics
[980.38 → 981.42] and try to figure out
[981.42 → 982.40] why they are not
[982.40 → 983.20] working for
[983.20 → 984.18] this kind of
[984.18 → 985.04] very specific
[985.04 → 985.52] phenomena.
[986.06 → 986.38] Actually,
[986.70 → 987.68] yesterday we had
[987.68 → 988.88] a lot of
[988.88 → 989.82] presentations
[989.82 → 991.18] about challenge
[991.18 → 991.84] sets that
[991.84 → 992.58] try to test
[992.58 → 993.32] metrics for
[993.32 → 994.04] these specific
[994.04 → 994.52] phenomena.
[995.26 → 996.56] So in WMT
[996.56 → 997.12] we have
[997.12 → 998.68] several competitions,
[999.06 → 999.94] several what we
[999.94 → 1000.72] call share tasks
[1000.72 → 1002.64] and inside the
[1002.64 → 1003.48] metrics share task
[1003.48 → 1004.16] where people are
[1004.16 → 1004.90] trying to compete
[1004.90 → 1006.30] to create
[1006.30 → 1007.12] better metrics,
[1007.52 → 1008.26] there was also
[1008.26 → 1009.56] a share task
[1009.56 → 1011.10] that we call
[1011.10 → 1011.92] the challenge
[1011.92 → 1012.80] set subtask
[1012.80 → 1014.26] where people
[1014.26 → 1015.78] submit examples
[1015.78 → 1016.60] that are challenging
[1016.60 → 1017.24] for metrics.
[1017.80 → 1018.58] And then the
[1018.58 → 1019.34] participants from
[1019.34 → 1020.10] the metrics task
[1020.10 → 1020.78] have to score
[1020.78 → 1021.44] those examples
[1021.44 → 1022.68] and then we get
[1022.68 → 1024.00] the scores back
[1024.00 → 1024.98] to the developers
[1024.98 → 1025.82] of the challenges
[1025.82 → 1026.50] for them to
[1026.50 → 1027.16] analyze.
[1027.90 → 1028.68] And a lot of
[1028.68 → 1029.68] people looked
[1029.68 → 1030.26] into this
[1030.26 → 1031.70] and tried to
[1031.70 → 1032.12] make some
[1032.12 → 1032.98] suggestions for
[1032.98 → 1033.66] future work
[1033.66 → 1034.74] in how to
[1034.74 → 1035.42] improve metrics
[1035.42 → 1035.86] for this.
[1035.98 → 1037.04] So if you guys
[1037.04 → 1037.92] are interested in
[1037.92 → 1038.12] this,
[1038.22 → 1039.44] take a look at
[1039.44 → 1040.22] the findings from
[1040.22 → 1040.94] the metrics task
[1040.94 → 1041.94] because they are
[1041.94 → 1042.78] interesting findings
[1042.78 → 1044.80] and pointers for
[1044.80 → 1045.58] future work in
[1045.58 → 1046.50] this area.
[1047.06 → 1047.46] One of the
[1047.46 → 1048.08] problems of
[1048.08 → 1049.52] this model-based
[1049.52 → 1050.66] MT evaluation
[1050.66 → 1052.06] approaches is that
[1052.06 → 1053.56] first they are
[1053.56 → 1054.76] based on the
[1054.76 → 1055.70] data that the
[1055.70 → 1056.56] pre-trained models
[1056.56 → 1057.42] were trained on.
[1058.14 → 1059.28] So there's
[1059.28 → 1059.94] everything there.
[1060.02 → 1060.66] There's bias
[1060.66 → 1062.12] and there's a
[1062.12 → 1063.22] limited amount
[1063.22 → 1064.52] or it can be a
[1064.52 → 1065.20] lot of data as
[1065.20 → 1066.14] well, but all
[1066.14 → 1067.16] the idiosyncrasies
[1067.16 → 1068.36] of that data are
[1068.36 → 1069.20] encoded in the
[1069.20 → 1069.80] pre-trained models.
[1070.10 → 1071.42] Then when you
[1071.42 → 1072.34] fine-tune this
[1072.34 → 1073.24] for the specific
[1073.24 → 1074.04] tasks that they
[1074.04 → 1075.40] need to work on,
[1075.58 → 1076.30] namely quality
[1076.30 → 1076.96] estimation and
[1076.96 → 1077.78] MT evaluation,
[1078.44 → 1079.50] they also are
[1079.50 → 1080.64] limited in data
[1080.64 → 1081.46] in the sense that
[1081.46 → 1082.84] we have orders of
[1082.84 → 1083.80] magnitude less
[1083.80 → 1085.34] label data for
[1085.34 → 1085.80] this fine-tuning
[1085.80 → 1086.20] process.
[1086.46 → 1087.58] So this can have
[1087.58 → 1088.56] its biases and
[1088.56 → 1089.54] it can have also
[1089.54 → 1091.42] like taking the
[1091.42 → 1092.26] example of Apple,
[1092.50 → 1093.02] for some reason
[1093.02 → 1094.16] you've never seen
[1094.16 → 1095.04] Apple the company,
[1095.32 → 1095.98] but you saw only
[1095.98 → 1096.94] for the fruit.
[1097.48 → 1098.86] So every time you
[1098.86 → 1099.34] see Apple, you
[1099.34 → 1100.10] translate that to
[1100.10 → 1100.44] the fruit.
[1101.06 → 1102.20] You actually say
[1102.20 → 1103.38] that if the model
[1103.38 → 1104.20] translates that to
[1104.20 → 1105.58] the fruit, the
[1105.58 → 1106.62] evaluation thing is
[1106.62 → 1106.90] going to say,
[1106.96 → 1107.54] ah, it's fine.
[1107.92 → 1108.80] Because in the
[1108.80 → 1110.12] evaluation data that
[1110.12 → 1110.68] you used to train
[1110.68 → 1111.86] the model, you
[1111.86 → 1112.72] never saw, for
[1112.72 → 1113.62] some reason, the
[1113.62 → 1113.88] brand.
[1114.54 → 1115.62] So, and this is
[1115.62 → 1116.32] related to the
[1116.32 → 1117.50] name-density problem
[1117.50 → 1118.50] that Richard was
[1118.50 → 1118.72] saying.
[1118.72 → 1121.72] So, I think one
[1121.72 → 1122.84] step, we are giving
[1122.84 → 1123.68] the first step as a
[1123.68 → 1124.10] community to
[1124.10 → 1124.96] understand that now
[1124.96 → 1125.90] and, you know,
[1125.92 → 1127.26] really poke it and
[1127.26 → 1128.60] see, okay, there's a
[1128.60 → 1130.34] hole here and now
[1130.34 → 1131.54] the next step is how
[1131.54 → 1133.10] to, you know,
[1133.22 → 1133.82] alleviate that
[1133.82 → 1134.18] problem.
[1134.86 → 1135.80] I don't think it's
[1135.80 → 1136.64] possible to alleviate
[1136.64 → 1137.90] completely solve, but
[1137.90 → 1139.08] we are for sure
[1139.08 → 1140.18] will try to alleviate
[1140.18 → 1141.18] this for these models
[1141.18 → 1141.44] now.
[1141.86 → 1143.44] There is a and
[1143.44 → 1144.00] there are a lot of
[1144.00 → 1144.84] complaints out of
[1144.84 → 1146.04] people, not
[1146.04 → 1146.92] complaints, but, you
[1146.92 → 1147.70] know, even us when
[1147.70 → 1148.78] we are using different
[1148.78 → 1149.44] models, not only
[1149.44 → 1150.74] ours, we see that
[1150.74 → 1151.66] these models fall
[1151.66 → 1152.48] short sometimes.
[1153.10 → 1154.24] And this can be very
[1154.24 → 1155.30] bad in a commercial
[1155.30 → 1157.08] setting or even in
[1157.08 → 1158.38] sensitive scenarios in
[1158.38 → 1160.08] which if you get
[1160.08 → 1161.68] two cents and the
[1161.68 → 1162.84] translate, the model
[1162.84 → 1164.14] that translated this
[1164.14 → 1164.90] to, I don't know,
[1165.36 → 1166.44] two million, that's
[1166.44 → 1167.50] not very nice, right?
[1167.56 → 1168.64] You might have some
[1168.64 → 1169.94] legal implications with
[1169.94 → 1170.24] that.
[1170.84 → 1171.56] So, yeah.
[1172.18 → 1172.72] I don't know, are
[1172.72 → 1173.54] there other open
[1173.54 → 1174.68] problems, I think.
[1174.90 → 1175.98] For me, one big
[1175.98 → 1177.68] problem is that
[1177.68 → 1178.94] and this is also
[1178.94 → 1179.48] a trend that we
[1179.48 → 1180.48] see in the metrics
[1180.48 → 1181.20] and in the quality
[1181.20 → 1182.60] estimation task, is
[1182.60 → 1183.50] that bigger models
[1183.50 → 1184.80] have better predictive
[1184.80 → 1185.20] power.
[1185.48 → 1187.32] So, people, usually
[1187.32 → 1188.04] what they are doing
[1188.04 → 1190.28] is just thrown more
[1190.28 → 1192.08] GPUs at it and just
[1192.08 → 1192.94] train a bigger model
[1192.94 → 1194.24] and this seems to be
[1194.24 → 1195.52] giving improvements
[1195.52 → 1195.92] as well.
[1196.02 → 1197.34] But the problem is
[1197.34 → 1198.38] that not every
[1198.38 → 1199.40] practitioner can
[1199.40 → 1200.44] actually use these
[1200.44 → 1201.60] models once they are
[1201.60 → 1202.88] trained because they
[1202.88 → 1204.02] take, they need
[1204.02 → 1205.06] bigger and bigger
[1205.06 → 1207.00] GPUs which are
[1207.00 → 1208.30] costlier even at
[1208.30 → 1209.00] inference time.
[1209.58 → 1210.78] So, we actually had
[1210.78 → 1212.38] a paper in EMT, the
[1212.38 → 1213.74] European Association
[1213.74 → 1214.72] for Machine Translation
[1214.72 → 1216.12] Conference, that was
[1216.12 → 1217.00] actually making
[1217.00 → 1218.98] comets smaller and
[1218.98 → 1220.12] it's like a diminutive
[1220.12 → 1221.08] in the name of the
[1221.08 → 1221.86] paper, the name of
[1221.86 → 1222.40] the model is
[1222.40 → 1223.90] competing, which is a
[1223.90 → 1225.04] diminutive of comet,
[1225.60 → 1227.48] like Portuguese, very
[1227.48 → 1228.52] Portuguese way to say
[1228.52 → 1228.72] it.
[1229.10 → 1230.30] And it was also a first
[1230.30 → 1231.10] step towards that.
[1231.10 → 1232.26] But I think there is a
[1232.26 → 1233.34] lot to be done for all
[1233.34 → 1234.22] the other models and
[1234.22 → 1234.88] also for comet.
[1235.48 → 1236.14] Yeah, definitely.
[1236.40 → 1238.24] I think competing was
[1238.24 → 1239.38] just the first step
[1239.38 → 1240.20] into that direction.
[1241.04 → 1241.98] There is a lot of
[1241.98 → 1242.88] things that can be
[1242.88 → 1243.58] improved in
[1243.58 → 1245.00] distillation of these
[1245.00 → 1245.80] models, even the
[1245.80 → 1246.72] evaluation models like
[1246.72 → 1247.70] we did for competing.
[1248.24 → 1249.52] And not just for
[1249.52 → 1250.36] evaluation, we have
[1250.36 → 1251.76] been focusing this
[1251.76 → 1253.18] podcast a little bit
[1253.18 → 1254.16] on evaluation.
[1254.86 → 1256.46] But on machine
[1256.46 → 1257.54] translation, you have
[1257.54 → 1258.26] the same problem.
[1258.48 → 1258.84] On machine
[1258.84 → 1260.06] translation, bigger
[1260.06 → 1260.50] models,
[1260.50 → 1261.72] have been
[1261.72 → 1263.88] achieving impressive
[1263.88 → 1264.96] machine translation
[1264.96 → 1265.48] quality.
[1265.88 → 1267.00] But it's very hard
[1267.00 → 1268.70] for everyone to
[1268.70 → 1269.68] develop those models
[1269.68 → 1270.72] and it's even
[1270.72 → 1272.36] harder for people to
[1272.36 → 1273.40] deploy those models.
[1274.12 → 1275.34] We face this at
[1275.34 → 1275.62] In babel.
[1275.76 → 1277.46] We develop our own
[1277.46 → 1278.32] machine translation
[1278.32 → 1279.82] systems, and we have
[1279.82 → 1280.50] seen this trend.
[1280.62 → 1281.52] We get improvements
[1281.52 → 1282.76] if we keep scaling
[1282.76 → 1284.28] our empties.
[1284.68 → 1285.76] But then we have
[1285.76 → 1287.62] difficulties serving
[1287.62 → 1288.34] those empties.
[1288.34 → 1291.92] We know that not
[1291.92 → 1293.04] every company has
[1293.04 → 1294.08] the capacity to
[1294.08 → 1295.42] build such big
[1295.42 → 1296.74] models like big
[1296.74 → 1297.42] tech companies
[1297.42 → 1298.16] develop.
[1298.94 → 1300.26] So yeah, it's not
[1300.26 → 1300.82] just in the
[1300.82 → 1301.66] evaluation side, but
[1301.66 → 1302.18] also in the
[1302.18 → 1302.68] machine translation
[1302.68 → 1303.12] side.
[1303.60 → 1304.90] It is something that
[1304.90 → 1305.76] people should look
[1305.76 → 1306.34] forward to.
[1306.56 → 1307.46] It's without losing
[1307.46 → 1308.42] performance, how to
[1308.42 → 1309.38] make these things
[1309.38 → 1311.04] smaller and easier
[1311.04 → 1311.60] to deploy.
[1311.60 → 1312.62] Yeah, and would
[1312.62 → 1313.58] you say on the
[1313.58 → 1315.08] model side
[1315.08 → 1316.32] specifically, like
[1316.32 → 1317.32] Jose, you mentioned
[1317.32 → 1318.96] sort of models
[1318.96 → 1319.68] getting bigger and
[1319.68 → 1319.98] bigger.
[1320.72 → 1321.76] Some people might
[1321.76 → 1322.70] have seen like
[1322.70 → 1324.66] nice Giphy's about
[1324.66 → 1325.46] like an encoder
[1325.46 → 1326.44] decoder and one
[1326.44 → 1327.24] language coming in
[1327.24 → 1327.74] and one language
[1327.74 → 1328.42] coming out and
[1328.42 → 1329.52] transformer models.
[1329.78 → 1331.26] But what are some
[1331.26 → 1332.12] things others are
[1332.12 → 1332.74] exploring maybe
[1332.74 → 1333.62] yourselves that
[1333.62 → 1334.76] like are either
[1334.76 → 1336.00] different approaches
[1336.00 → 1336.84] or you mentioned
[1336.84 → 1337.78] distillation and all
[1337.78 → 1338.52] these other things to
[1338.52 → 1339.46] make models smaller.
[1339.46 → 1340.62] But are there
[1340.62 → 1342.26] different architectures
[1342.26 → 1343.36] or techniques being
[1343.36 → 1343.84] explored?
[1343.98 → 1344.92] I think I saw one
[1344.92 → 1345.40] of your papers
[1345.40 → 1346.34] something about like
[1346.34 → 1348.10] CNN MT or
[1348.10 → 1348.46] something.
[1348.68 → 1349.24] I don't know if you
[1349.24 → 1349.84] can speak to that,
[1349.92 → 1350.06] but.
[1350.58 → 1351.60] Yeah, we just at
[1351.60 → 1352.56] this moment there is
[1352.56 → 1353.52] a poster on the
[1353.52 → 1355.00] usage of KNN MT
[1355.00 → 1356.36] for the chat
[1356.36 → 1357.00] share task.
[1357.52 → 1357.96] So this is
[1357.96 → 1359.32] something called I
[1359.32 → 1359.84] think this is
[1359.84 → 1360.56] broadly called
[1360.56 → 1361.56] dynamic adaptation
[1361.56 → 1362.92] and one approach
[1362.92 → 1364.04] to that is doing
[1364.04 → 1365.18] CNN MT that
[1365.18 → 1367.14] rather than actually
[1367.14 → 1368.24] fully fine-tuning
[1368.24 → 1369.44] one base model
[1369.44 → 1370.38] like one of these
[1370.38 → 1371.04] large pre-trained
[1371.04 → 1371.36] models.
[1371.86 → 1372.96] You actually just
[1372.96 → 1373.94] do some data
[1373.94 → 1374.84] retrieval approach
[1374.84 → 1375.92] in which you
[1375.92 → 1377.26] combine the
[1377.26 → 1378.32] contents of a
[1378.32 → 1379.18] data store that
[1379.18 → 1380.46] has relevant data
[1380.46 → 1381.36] for the use case
[1381.36 → 1381.90] that you're trying
[1381.90 → 1382.46] to serve with
[1382.46 → 1383.10] machine translation
[1383.10 → 1384.78] and then at
[1384.78 → 1386.00] decoding time when
[1386.00 → 1386.56] you are assembling
[1386.56 → 1387.16] the translation
[1387.16 → 1388.78] using the
[1388.78 → 1389.94] translation probabilities
[1389.94 → 1390.60] of the model
[1390.60 → 1391.64] you interpolate
[1391.64 → 1392.66] these probabilities
[1392.66 → 1393.26] with the
[1393.26 → 1394.56] probabilities of
[1394.56 → 1395.64] words or
[1395.64 → 1397.02] expressions contained
[1397.02 → 1398.10] in the data
[1398.10 → 1398.46] store.
[1398.46 → 1399.70] So this way
[1399.70 → 1400.52] you avoid
[1400.52 → 1401.28] having to
[1401.28 → 1402.26] fully fine tune
[1402.26 → 1402.90] a model for
[1402.90 → 1403.54] each use case
[1403.54 → 1404.14] that you have
[1404.14 → 1405.04] and this is
[1405.04 → 1405.64] something that we
[1405.64 → 1406.16] started to
[1406.16 → 1407.00] research and
[1407.00 → 1407.66] approach at
[1407.66 → 1407.98] Unable.
[1408.44 → 1409.10] But I just
[1409.10 → 1409.90] must say that
[1409.90 → 1410.70] this doesn't
[1410.70 → 1411.10] solve the
[1411.10 → 1411.78] problem of
[1411.78 → 1412.26] the base
[1412.26 → 1412.78] model being
[1412.78 → 1413.14] big.
[1413.48 → 1413.90] You just
[1413.90 → 1414.54] avoid fine
[1414.54 → 1415.06] tuning it
[1415.06 → 1415.52] completely.
[1416.20 → 1417.24] So there's
[1417.24 → 1417.54] still the
[1417.54 → 1418.26] problem of
[1418.26 → 1419.40] okay how do
[1419.40 → 1420.82] I shrink or
[1420.82 → 1421.86] compress this
[1421.86 → 1423.32] model so that
[1423.32 → 1425.10] I can reliably
[1425.10 → 1427.14] and cheaply
[1427.14 → 1428.38] explore it for
[1428.38 → 1429.38] translation and
[1429.38 → 1430.36] this is like
[1430.36 → 1430.78] you said
[1430.78 → 1432.34] distillation
[1432.34 → 1433.44] quantization and
[1433.44 → 1434.44] other compressing
[1434.44 → 1434.90] techniques.
[1435.22 → 1436.00] Just to
[1436.00 → 1436.70] complement what
[1436.70 → 1438.34] José was saying
[1438.34 → 1439.64] about the
[1439.64 → 1440.56] key and nearest
[1440.56 → 1441.24] neighbour approach
[1441.24 → 1443.14] another very big
[1443.14 → 1443.92] advantage of this
[1443.92 → 1444.68] is that it's very
[1444.68 → 1445.96] easy to combine
[1445.96 → 1446.76] with translation
[1446.76 → 1447.94] memories which we
[1447.94 → 1448.50] know that they
[1448.50 → 1449.56] are widely used
[1449.56 → 1450.72] in a translation
[1450.72 → 1452.44] industry and this
[1452.44 → 1453.42] is a seamless way
[1453.42 → 1454.52] to basically take
[1454.52 → 1455.18] the MT and
[1455.18 → 1456.12] make the MT work
[1456.12 → 1456.50] with those
[1456.50 → 1457.34] translation memories
[1457.34 → 1458.82] because you can
[1458.82 → 1459.64] build this data
[1459.64 → 1460.28] store that will
[1460.28 → 1461.62] help the model to
[1461.62 → 1462.58] translate the
[1462.58 → 1463.78] content accordingly.
[1464.38 → 1465.52] So just to add
[1465.52 → 1466.86] that also which I
[1466.86 → 1467.80] believe that it's
[1467.80 → 1468.72] very important for
[1468.72 → 1469.80] the localization
[1469.80 → 1471.54] industry in general.
[1472.26 → 1473.26] Great yeah well
[1473.26 → 1474.10] we've talked a lot
[1474.10 → 1475.80] about challenges I
[1475.80 → 1476.76] guess which is fun
[1476.76 → 1477.98] to talk about at a
[1477.98 → 1478.78] research conference
[1478.78 → 1479.34] for sure.
[1479.68 → 1480.36] What are some
[1480.36 → 1481.36] things just like
[1481.36 → 1482.48] generally about
[1482.48 → 1483.20] like the machine
[1483.20 → 1484.22] translation industry
[1484.22 → 1485.72] or Unable or
[1485.72 → 1486.62] other things that
[1486.62 → 1488.04] you make both of
[1488.04 → 1489.06] you sort of excited
[1489.06 → 1489.98] and you know
[1489.98 → 1490.88] optimistic about
[1490.88 → 1491.36] the future.
[1491.78 → 1492.22] What are some of
[1492.22 → 1493.00] those things that
[1493.00 → 1493.78] excite you?
[1494.04 → 1494.74] It doesn't have to
[1494.74 → 1495.70] be an MT or
[1495.70 → 1496.56] you know things
[1496.56 → 1497.00] you've seen at
[1497.00 → 1497.82] this conference or
[1497.82 → 1498.38] things that you're
[1498.38 → 1499.26] following that give
[1499.26 → 1501.00] you some encouragement
[1501.00 → 1501.94] and excitement about
[1501.94 → 1502.80] the future of the
[1502.80 → 1503.30] space where we're
[1503.30 → 1503.58] working.
[1504.20 → 1504.96] Actually I'm very
[1504.96 → 1506.00] passionate about
[1506.00 → 1507.72] evaluation in general.
[1508.26 → 1509.32] I think that shows
[1509.32 → 1510.06] up in my work
[1510.06 → 1511.16] because I mostly
[1511.16 → 1511.96] work on evaluation.
[1511.96 → 1513.20] I've been getting
[1513.20 → 1514.44] very excited with
[1514.44 → 1515.12] the progress that
[1515.12 → 1515.94] we have been doing
[1515.94 → 1516.94] in evaluation.
[1517.54 → 1519.70] I think like we
[1519.70 → 1520.78] have started a
[1520.78 → 1521.60] project on this
[1521.60 → 1523.20] that we's to
[1523.20 → 1523.98] combine these
[1523.98 → 1525.04] systems this quality
[1525.04 → 1526.08] estimation systems
[1526.08 → 1527.60] with the machine
[1527.60 → 1528.52] translation itself.
[1529.24 → 1530.04] So that is
[1530.04 → 1530.98] something that we
[1530.98 → 1532.30] we started working
[1532.30 → 1533.34] on this but I
[1533.34 → 1534.34] believe that you
[1534.34 → 1535.10] can work on this
[1535.10 → 1536.40] for the next few
[1536.40 → 1537.16] years and there is
[1537.16 → 1537.90] a lot of things that
[1537.90 → 1538.56] we can improve
[1538.56 → 1538.78] there.
[1539.42 → 1540.40] Yeah that gets me
[1540.40 → 1541.18] really excited.
[1541.52 → 1542.50] I think it's a
[1542.50 → 1543.46] direction that it's
[1543.46 → 1544.14] going to be really
[1544.14 → 1545.06] nice.
[1545.66 → 1546.84] Yeah this is the
[1546.84 → 1548.54] quality aware decoding
[1548.54 → 1549.42] project that is
[1549.42 → 1550.72] basically what I just
[1550.72 → 1551.94] mentioned what
[1551.94 → 1552.86] we have been talking
[1552.86 → 1554.32] about of having this
[1554.32 → 1555.08] quality predictions
[1555.08 → 1556.76] about the hypothesis
[1556.76 → 1557.32] translations.
[1557.68 → 1558.94] The idea behind this
[1558.94 → 1560.50] project that Riccardo is
[1560.50 → 1561.28] talking about is what
[1561.28 → 1562.08] if we bring the
[1562.08 → 1563.24] quality estimation or
[1563.24 → 1565.08] comment already to
[1565.08 → 1566.80] inside the MT process
[1566.80 → 1569.32] and then we can make
[1569.32 → 1570.74] the machine translation
[1570.74 → 1572.98] aware or more aware
[1572.98 → 1573.84] about its quality
[1573.84 → 1574.92] having a signal from
[1574.92 → 1575.54] a different model.
[1576.14 → 1577.28] So this is what this
[1577.28 → 1578.02] project is about.
[1578.62 → 1580.24] So we have a paper at
[1580.24 → 1581.32] NATO this year
[1581.32 → 1582.42] describing that.
[1582.90 → 1583.74] So yeah this is pretty
[1583.74 → 1585.30] exciting and I think
[1585.30 → 1587.30] in terms of more
[1587.30 → 1588.58] broad challenges what
[1588.58 → 1589.80] I find interesting is
[1589.80 → 1591.36] that I don't believe
[1591.36 → 1592.74] that translation is
[1592.74 → 1593.14] solved.
[1593.46 → 1594.82] I think a few years
[1594.82 → 1596.22] ago some people
[1596.22 → 1596.94] claimed that there
[1596.94 → 1597.86] was human parity
[1597.86 → 1600.02] between MT systems
[1600.02 → 1601.62] or some MT models
[1601.62 → 1603.22] and humans and
[1603.22 → 1604.78] translators but then
[1604.78 → 1606.28] what it turned out
[1606.28 → 1608.06] that the actual
[1608.06 → 1609.12] translators that were
[1609.12 → 1611.02] used were not really
[1611.02 → 1612.24] professional translators
[1612.24 → 1613.78] like I know English
[1613.78 → 1614.80] right, but I'm not a
[1614.80 → 1616.08] native speaker and I
[1616.08 → 1616.64] cannot translate
[1616.64 → 1618.02] everything, so I'm not
[1618.02 → 1619.18] a subject-matter expert
[1619.18 → 1620.72] on different topics
[1620.72 → 1621.62] so I cannot actually
[1621.62 → 1622.64] if you give me some
[1622.64 → 1624.00] chemistry content to
[1624.00 → 1625.02] translate into English
[1625.02 → 1626.62] from Portuguese I
[1626.62 → 1627.90] cannot do it right.
[1628.02 → 1629.38] So I think what's
[1629.38 → 1630.38] exciting is to see that
[1630.38 → 1631.40] the technology is
[1631.40 → 1632.14] allowing us to
[1632.14 → 1632.90] translate better and
[1632.90 → 1634.22] better maybe compared
[1634.22 → 1635.42] to me as a non-native
[1635.42 → 1636.28] speaker when I'm
[1636.28 → 1637.42] translating some
[1637.42 → 1639.24] content but still
[1639.24 → 1639.90] there's a lot of
[1639.90 → 1640.58] there are a lot of
[1640.58 → 1642.12] challenges to actually
[1642.12 → 1644.06] translate very well
[1644.06 → 1645.58] very specific content
[1645.58 → 1647.48] that is you know
[1647.48 → 1649.38] requires very specific
[1649.38 → 1651.38] terminology and very
[1651.38 → 1652.80] specific way of
[1652.80 → 1654.12] actually building the
[1654.12 → 1656.44] sentences and what is
[1656.44 → 1657.60] much better is actually
[1657.60 → 1659.26] the fluency that this
[1659.26 → 1660.16] machine translation
[1660.16 → 1660.94] models are giving
[1660.94 → 1662.40] nowadays but what
[1662.40 → 1663.86] remains is still a
[1663.86 → 1664.60] challenge is that
[1664.60 → 1665.66] sometimes the
[1665.66 → 1666.78] translations they look
[1666.78 → 1668.12] very good, but they are
[1668.12 → 1669.16] not on point so they
[1669.16 → 1670.20] are not adequate they
[1670.20 → 1670.84] are talking about
[1670.84 → 1671.50] something slightly
[1671.50 → 1672.96] different or completely
[1672.96 → 1674.88] different, so I think
[1674.88 → 1676.16] this is exciting I mean
[1676.16 → 1677.44] nothing not everything
[1677.44 → 1678.58] is solved but at the
[1678.58 → 1679.46] same time is encouraging
[1679.46 → 1680.70] right is encouraging in
[1680.70 → 1682.06] this sense so yeah
[1682.06 → 1683.56] great well as we close
[1683.56 → 1684.84] out here where can
[1684.84 → 1686.22] people find out more
[1686.22 → 1687.06] about Unable and
[1687.06 → 1688.24] specifically maybe some
[1688.24 → 1689.98] of this research that
[1689.98 → 1691.02] that's going on and
[1691.02 → 1693.16] and also you mentioned
[1693.16 → 1694.56] beforehand that Unable
[1694.56 → 1696.02] was possibly hiring as
[1696.02 → 1696.72] well where can people
[1696.72 → 1697.60] find out about that
[1697.60 → 1699.12] right so we have our
[1699.12 → 1700.54] website like Unbabel.com
[1700.54 → 1701.36] and we have our
[1701.36 → 1703.04] Twitter handle like at
[1703.04 → 1704.60] Unable you can follow
[1704.60 → 1706.66] our news from there we
[1706.66 → 1708.54] are just put up a
[1708.54 → 1709.92] research blog in which
[1709.92 → 1711.08] we are going to be
[1711.08 → 1712.34] writing about our
[1712.34 → 1714.12] research this is going
[1714.12 → 1715.82] to be possibly in the
[1715.82 → 1717.08] links in your info
[1717.08 → 1717.92] box I don't know yeah
[1717.92 → 1718.60] we'll put it in the
[1718.60 → 1719.78] show notes for sure and
[1719.78 → 1721.38] yeah we are also
[1721.38 → 1722.94] hiring soon like we
[1722.94 → 1724.54] are starting to accept
[1724.54 → 1725.60] applications for the
[1725.60 → 1727.40] next year for research
[1727.40 → 1729.14] scientists in different
[1729.14 → 1730.22] levels and different
[1730.22 → 1731.88] geographies so Unable
[1731.88 → 1733.26] we didn't talk about it
[1733.26 → 1734.74] but it was born in
[1734.74 → 1736.82] Portugal in Lisbon but
[1736.82 → 1738.54] now we have offices all
[1738.54 → 1739.54] around the world we
[1739.54 → 1740.42] have offices in the
[1740.42 → 1741.42] west coast in the US
[1741.42 → 1743.36] in the east coast London
[1743.36 → 1744.64] you know and some other
[1744.64 → 1746.70] places in Europe and we
[1746.70 → 1747.82] are going to post this
[1747.82 → 1749.36] also to give an email for
[1749.36 → 1750.22] contact for people who
[1750.22 → 1751.42] are interested in all the
[1751.42 → 1752.28] research that we're doing
[1752.28 → 1753.84] and other works we
[1753.84 → 1754.86] don't we have open
[1754.86 → 1755.96] positions not only for
[1755.96 → 1757.52] research scientists but
[1757.52 → 1758.58] also for the engineers
[1758.58 → 1760.66] and other positions that
[1760.66 → 1761.64] are not technical so
[1761.64 → 1763.34] well uh yeah, thank you
[1763.34 → 1764.44] Jose thank you, Ricardo
[1764.44 → 1765.68] really appreciate you
[1765.68 → 1766.76] taking time I know
[1766.76 → 1767.40] there's a lot of good
[1767.40 → 1768.50] posters around to see
[1768.50 → 1769.38] and all that so
[1769.38 → 1770.24] thanks for taking time
[1770.24 → 1772.04] thanks Daniel thank you
[1772.04 → 1782.34] all right that is our
[1782.34 → 1783.74] show for this week if you
[1783.74 → 1785.12] dig it don't forget to
[1785.12 → 1786.70] subscribe head to
[1786.70 → 1788.44] practicalai.fm for all
[1788.44 → 1789.66] the ways and if
[1789.66 → 1791.00] practical AI has benefited
[1791.00 → 1792.58] your life pay it forward
[1792.58 → 1793.80] by sharing the show with a
[1793.80 → 1794.82] friend or a colleague
[1794.82 → 1796.06] word of mouth is the
[1796.06 → 1797.06] number one way people
[1797.06 → 1798.16] find shows like ours
[1798.16 → 1799.72] thanks again to Vastly
[1799.72 → 1800.88] for fronting our static
[1800.88 → 1802.86] assets to fly.io for
[1802.86 → 1803.68] backing our dynamic
[1803.68 → 1805.32] requests to Break master
[1805.32 → 1806.24] Cylinder for the beats
[1806.24 → 1807.40] and to you for listening
[1807.40 → 1809.02] we appreciate you that's
[1809.02 → 1810.20] all for now we'll talk to
[1810.20 → 1811.04] you again on the next
[1811.04 → 1811.26] one
[1811.26 → 1812.26] you
[1812.26 → 1814.26] you
[1814.26 → 1816.26] you
[1816.26 → 1818.26] you
[1818.26 → 1820.26] you
[1820.26 → 1821.26] you
[1821.26 → 1822.26] you
[1822.26 → 1823.26] you
[1823.26 → 1823.76] you
[1823.76 → 1827.22] you
[1827.22 → 1831.20] you
[1831.20 → 1834.30] you
[1834.30 → 1836.34] you
[1836.34 → 1837.02] you
[1837.02 → 1837.20] you
[1837.20 → 1841.80] you
[1841.80 → 1843.88] you
[1843.88 → 1845.30] you
[1845.30 → 1846.74] you
[1846.74 → 1847.42] you
[1847.42 → 1848.28] you
[1848.28 → 1848.90] you
[1848.90 → 1849.46] you
[1849.46 → 1849.50] you
[1849.50 → 1849.56] you
[1849.56 → 1849.82] you
[1849.82 → 1853.44] you
