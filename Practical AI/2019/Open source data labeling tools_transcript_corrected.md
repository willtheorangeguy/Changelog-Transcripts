[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.24 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.72 → 20.34] This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 → 25.10] And we're excited to share they now offer dedicated virtual droplets.
[25.10 → 29.04] And unlike standard droplets, which use shared virtual CPU threads,
[29.04 → 32.88] their two performance plans, general purpose and CPU optimized,
[33.40 → 36.08] they have dedicated virtual CPU threads.
[36.42 → 40.86] This translates to higher performance and increased consistency during CPU intensive processes.
[41.34 → 45.20] So if you have build boxes, CCD, video encoding, machine learning, ad serving,
[45.50 → 49.98] game servers, databases, batch processing, data mining, application servers,
[50.20 → 54.92] or active front end web servers that need to be full duty CPU all day every day,
[55.14 → 57.92] then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 → 61.26] Pricing is very competitive starting at 40 bucks a month.
[61.66 → 66.38] Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 → 69.02] Again, do.co slash Changelog.
[69.02 → 86.38] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.76 → 88.56] productive, and accessible to everyone.
[88.94 → 93.42] This is where conversations around AI, machine learning, and data science happen.
[93.42 → 98.20] Join the community and snag with us around various topics of the show at changelog.com slash community.
[98.54 → 99.38] Follow us on Twitter.
[99.48 → 100.96] We're at Practical AI FM.
[101.48 → 102.28] And now onto the show.
[107.16 → 111.22] Well, welcome to another episode of Practical AI.
[111.22 → 115.62] I'm Daniel Whiten ack, a data scientist with SIL International.
[116.04 → 123.50] And as always, I'm joined by my co-host, Chris Benson, a principal AI strategist at Lockheed Martin.
[123.76 → 124.36] How are you doing, Chris?
[124.48 → 125.14] Doing great, Daniel.
[125.20 → 125.84] How's it going today?
[126.46 → 128.06] It is going good.
[128.20 → 133.82] And I think when listeners will be listening to this in the future,
[134.12 → 138.30] if we're to imagine into the future, you will be at the NVIDIA conference.
[138.30 → 138.82] Is that right?
[138.82 → 139.90] That is accurate.
[140.02 → 143.04] As listeners are downloading this, I'm probably in Washington, D.C.
[143.48 → 148.02] I'll have just finished doing some commentary for the Alpha Pilot race.
[148.22 → 152.00] And those of you who aren't familiar, we had a recent episode about Alpha Pilot,
[152.40 → 154.26] which is really cool, autonomous drone racing.
[154.60 → 157.72] And as of the point where you're downloading this on Tuesday,
[157.90 → 160.18] which may potentially be tomorrow for you,
[160.18 → 165.08] I will be conducting a sort of fireside chat slash panel
[165.08 → 173.02] about Alpha Pilot and AI at the edge at NVIDIA's GTC DC event on Tuesday evening.
[173.14 → 176.06] So I hope if you're listening to this, and you happen to be at GTC,
[176.38 → 177.54] I hope you'll come attend.
[177.76 → 179.02] And whether you do or not, find me.
[179.08 → 182.56] I'll be there all week and find me and let me know you're a Practical AI listener.
[182.74 → 183.78] And let's connect.
[183.86 → 184.94] I can't wait to meet people there.
[185.52 → 186.36] Yeah, that sounds great.
[186.36 → 187.96] I can't wait to hear about how it goes.
[188.52 → 192.76] Well, today, you know, if I think about practical AI, Chris,
[193.26 → 198.54] and I asked you, what is the most practical of practical AI things?
[198.86 → 199.46] What would you say?
[200.52 → 201.94] You already know what I'm going to say.
[202.00 → 203.02] You're setting me up for that.
[203.48 → 204.20] It's labelling.
[204.40 → 206.06] I'm teeing you up for the right answer.
[206.16 → 210.98] Oh my God, it's labelling data the bane of my existence over the last few years
[210.98 → 212.32] in terms of doing AI.
[212.32 → 215.78] If we can get the data labelled, then I'm finally at a happy place
[215.78 → 218.20] where I can start doing training and have some fun.
[219.32 → 224.74] So today is all about the data and all about labelling the data.
[225.34 → 231.14] And we're joined by Michael Malik, who is CEO and founder at Hard
[231.14 → 235.92] and one of the contributors and maintainers of Label Studio.
[236.52 → 237.06] Welcome, Michael.
[237.52 → 238.06] Hello, hello.
[238.98 → 239.80] Thanks for inviting me.
[239.80 → 243.58] And we were able to grab Michael for an interview
[243.58 → 245.76] while he is doing his world travels.
[245.96 → 247.48] He's, I think, right now in Moscow.
[247.74 → 248.04] Is that right?
[248.74 → 249.16] Awesome.
[249.44 → 249.64] Yeah.
[249.78 → 253.56] Well, thank you for joining us even in the midst of your jet lag.
[253.76 → 254.24] Oh, yeah.
[254.80 → 255.22] Yeah.
[255.34 → 259.78] So if you could just give us a little bit of an intro to yourself,
[260.14 → 263.86] your background, how you kind of got involved in AI, ML things,
[263.94 → 265.14] some of the things you've done,
[265.14 → 269.24] and how you ended up with a focus on data labelling.
[270.00 → 270.48] Sure.
[271.18 → 273.58] So I got into AI.
[273.70 → 276.98] It was quite, I think, interesting path for me
[276.98 → 282.32] because I have started with Lisp programming in Common Lisp.
[283.28 → 286.84] And that at some point, I got this book by Peter Norvig,
[287.24 → 288.34] who I think right now at Google,
[288.90 → 292.48] that is called Paradigms of Artificial Intelligence.
[293.44 → 297.22] And it was kind of a mixture between Common Lisp
[297.22 → 300.32] and using Common Lisp to program AI.
[300.94 → 303.80] It was quite an old book, even when I got it.
[304.12 → 305.16] I think it was released.
[305.30 → 305.94] Yeah, it sounds intense.
[305.94 → 310.06] It was like 91 or 93, something like that.
[310.68 → 315.14] But it got me really interested into the whole concept about AI
[315.14 → 316.82] and how to program AI systems.
[317.58 → 320.44] And so from there, I kind of started to pick up
[320.44 → 325.42] all they actually need to be building production level AI systems.
[325.42 → 328.54] And I'm here talking about more of like math background,
[328.90 → 330.22] statistics background.
[331.36 → 334.88] And yeah, so that's what got me really, really,
[334.88 → 337.82] like really interested into the whole AI concept,
[338.02 → 340.32] Common Lisp 50 years old programming language.
[340.32 → 344.34] Well, my first programming language was Fortran
[344.34 → 346.06] and used it quite a bit.
[346.32 → 348.92] So I'm glad that I left it behind.
[349.14 → 352.86] But we all have, at least some of us have those roots
[352.86 → 354.40] in older languages.
[355.16 → 357.60] Yeah, it's like if we're talking about Common Lisp,
[357.78 → 360.44] it's like I still kind of a big fan of the language.
[361.20 → 364.68] And it's a pity that it's not kind of catching up with
[364.68 → 367.32] and not becoming more mainstream these days.
[367.32 → 371.46] Is that how common is it to find people these days
[371.46 → 375.18] working in AI or machine learning and using Common Lisp?
[375.34 → 376.54] Not common at all.
[376.68 → 377.44] Not common at all.
[377.78 → 379.94] Not common at all to give a punt.
[380.18 → 380.60] Oh, yeah.
[380.80 → 382.80] The only one who I can actually remember
[382.80 → 385.94] is the person Gabor Relish,
[386.10 → 389.00] who has won a number of AI competitions.
[389.42 → 390.98] I think those were organized by Google.
[391.54 → 394.32] And he wrote all his programs in Common Lisp.
[394.32 → 397.82] And those were very interested to study
[397.82 → 400.44] and to explore how he would approach things.
[401.52 → 402.34] Yeah, that's cool.
[402.52 → 404.18] So you started out there.
[404.36 → 406.62] How did you end up coming to the point
[406.62 → 410.36] where you started thinking about founding your own thing
[410.36 → 412.60] that would impact the AI community?
[412.92 → 413.26] Yeah, sure.
[413.94 → 415.20] Yeah, so at the time,
[415.26 → 418.56] and it was something about a year ago,
[418.56 → 421.62] me and my then-to-be co-founder,
[421.88 → 423.88] we went to this hiking trip
[423.88 → 426.30] in the high-altitude mountains.
[427.04 → 428.64] And I think the lack of oxygen
[428.64 → 430.76] kind of contributed into us
[430.76 → 433.02] starting the company.
[433.48 → 434.18] Where was this?
[434.54 → 435.12] Himalayas.
[435.80 → 436.72] Oh, wow.
[437.08 → 437.34] Awesome.
[437.50 → 438.10] Yeah, yeah, yeah.
[438.10 → 440.34] What was the max elevation?
[441.00 → 444.72] So I think I was giving up at almost 6,000.
[444.72 → 447.82] Yeah, 6,000 meters.
[448.08 → 448.50] Yeah, yeah, yeah.
[449.08 → 450.88] My co-founder, he went further,
[451.34 → 452.98] but the weather was really, terrible.
[453.08 → 454.40] So he had to turn back.
[455.06 → 455.62] So, yeah.
[455.76 → 456.96] So as co-founders,
[457.04 → 458.22] you've been through a lot together.
[458.56 → 459.28] I'm so jealous.
[459.78 → 460.38] Yeah, I mean,
[460.42 → 462.54] it's probably as hard as it gets,
[462.60 → 464.12] like all those conditions, you know.
[465.26 → 465.56] Yeah.
[465.64 → 468.20] What is VC funding and fundraising round
[468.20 → 469.34] as compared to that?
[469.82 → 470.74] It's the easy trip.
[472.08 → 473.16] 2,000 meters.
[473.16 → 476.34] Yeah, nice.
[476.34 → 478.48] So the company is Hard.
[478.84 → 480.60] And so, you know,
[480.66 → 481.24] not to,
[481.42 → 482.62] I think we've already spoiled
[482.62 → 483.64] the punchline here,
[483.74 → 485.30] but it has to do with data labelling.
[485.50 → 487.36] So how did you kind of get to a place
[487.36 → 489.76] where data labelling was something
[489.76 → 491.76] that you felt like you wanted to
[491.76 → 493.12] devote a lot of effort to?
[493.32 → 494.66] So we kind of,
[494.74 → 497.08] we were working on some algorithms
[497.08 → 498.52] in our spare time,
[498.80 → 500.34] just trying things.
[500.34 → 502.56] And by the time we decided
[502.56 → 503.32] to start a company,
[503.66 → 504.86] we all realized that
[504.86 → 507.12] at our past or current companies,
[507.26 → 508.18] the biggest issue
[508.18 → 510.00] that we had to handle ourselves
[510.00 → 512.28] was the data labelling part.
[512.96 → 515.40] And we were talking to multiple
[515.40 → 516.82] data scientists,
[517.24 → 518.12] machine learning experts,
[518.12 → 518.26] experts,
[518.48 → 519.84] and they have all agreed
[519.84 → 522.04] that it's kind of unsolved problem
[522.04 → 524.34] and more or less like a holy grail.
[524.34 → 526.68] If you're able to get your labels
[526.68 → 528.12] in the right moment,
[528.36 → 529.50] in the right place,
[529.50 → 531.10] then you basically end up
[531.10 → 532.92] with high quality models.
[534.14 → 535.60] And by the time we realized
[535.60 → 536.62] that it's not only us
[536.62 → 538.22] who had these problems,
[538.50 → 540.20] but also other developers
[540.20 → 541.56] and other companies,
[541.72 → 543.28] then we decided to proceed
[543.28 → 544.34] and start the company
[544.34 → 545.64] around the data labelling.
[545.64 → 547.86] So I, for one,
[548.00 → 549.92] you heard how I reacted to that
[549.92 → 550.62] in the very beginning
[550.62 → 551.34] about labelling,
[551.56 → 552.88] that being the bane
[552.88 → 553.44] of my existence.
[553.62 → 554.34] I, for one,
[554.78 → 556.48] am I thanking you very much
[556.48 → 558.38] for attending to that issue
[558.38 → 560.12] because everybody
[560.12 → 561.42] in the data science world
[561.42 → 564.78] wants to do the sexy AI training
[564.78 → 565.92] and such as that.
[566.48 → 567.58] This is a problem
[567.58 → 568.46] that has needed
[568.46 → 569.58] serious attention
[569.58 → 570.40] for a long time.
[570.92 → 572.16] So as I ask you about it,
[572.18 → 572.80] I just wanted to start
[572.80 → 574.20] by saying thank you very much.
[574.20 → 576.36] It's a problem,
[576.44 → 576.90] I feel like,
[577.00 → 579.62] to have wider impact
[579.62 → 581.20] than, like,
[581.56 → 582.72] creating a single
[582.72 → 584.22] state-of-the-art model
[584.22 → 584.84] and publishing,
[585.02 → 586.74] like, a very hyped paper.
[586.88 → 587.22] Oh, yeah.
[587.24 → 588.42] Like, this is the sort of problem
[588.42 → 589.82] that has a much wider impact.
[590.20 → 590.60] Absolutely.
[590.94 → 592.44] So I guess I want to start off
[592.44 → 593.14] by just kind of,
[593.64 → 594.80] if you could kind of tell us
[594.80 → 595.40] a little bit about
[595.40 → 596.86] where does data labelling
[596.86 → 598.24] fit into the kind of
[598.24 → 599.14] the larger workflow
[599.14 → 601.06] that we're all engaged in
[601.06 → 602.02] in the AI world
[602.02 → 603.00] and, you know,
[603.04 → 603.92] how does it relate
[603.92 → 605.96] to the AI problems
[605.96 → 607.54] that we are all working on?
[607.70 → 608.24] And, you know,
[608.34 → 609.54] Daniel has been focusing
[609.54 → 611.14] on lots of stuff
[611.14 → 612.88] having to do with language stuff
[612.88 → 614.72] and I've worked in robotics
[614.72 → 616.20] and different types
[616.20 → 617.68] of image classification stuff.
[617.82 → 618.94] So how does labelling
[618.94 → 621.00] fit into these workflows?
[621.44 → 621.82] Yeah, sure.
[622.44 → 624.44] So I think my personal take
[624.44 → 626.44] is that data labelling
[626.44 → 627.28] and annotation
[627.28 → 629.50] is basically the core
[629.50 → 632.44] of any AI-based product.
[633.28 → 634.64] Because if you are building
[634.64 → 635.82] on the labelled data,
[635.96 → 636.26] of course,
[636.82 → 638.18] because if you are not able
[638.18 → 640.58] to go into your data sets
[640.58 → 642.60] and relabel some things
[642.60 → 643.46] that, for example,
[643.62 → 644.66] might have been labelled
[644.66 → 646.88] incorrectly or inaccurately,
[647.44 → 648.92] then you just end up
[648.92 → 649.56] with the models
[649.56 → 651.70] that are not working well.
[652.46 → 654.20] So my take is that
[654.20 → 655.66] data labelling,
[655.66 → 657.50] it's the first step
[657.50 → 658.94] that comes after
[658.94 → 660.32] collecting the data.
[661.32 → 662.44] And it's something
[662.44 → 663.44] from where everything
[663.44 → 664.40] basically begins.
[665.14 → 666.58] And I also like to think
[666.58 → 667.52] about it in a way
[667.52 → 668.32] that sometimes
[668.32 → 669.82] when you get the data set
[669.82 → 671.22] or you collect the data set,
[671.38 → 672.66] you're not sure
[672.66 → 673.60] what's inside of it.
[674.02 → 675.18] So it's not only
[675.18 → 676.52] that you need to label it,
[676.78 → 678.16] but while you're doing
[678.16 → 678.70] the labelling,
[678.84 → 679.70] you are also kind of
[679.70 → 681.02] exploring your data set,
[681.46 → 682.84] finding the edge cases
[682.84 → 684.78] or some examples
[684.78 → 685.66] that you have not
[685.66 → 686.22] thought about.
[686.74 → 687.96] So I think the data
[687.96 → 688.84] labelling is basically
[688.84 → 690.72] the core functionality
[690.72 → 693.24] or shall be a core functionality
[693.24 → 696.04] of any data science team
[696.04 → 697.56] or the team
[697.56 → 699.20] that builds AI-based products.
[699.62 → 699.76] Yeah.
[699.90 → 701.12] So in terms of
[701.12 → 703.28] like the types of data
[703.28 → 705.16] that people generally
[705.16 → 706.38] need to label
[706.38 → 707.24] or annotate,
[707.34 → 708.10] as Chris mentioned,
[708.26 → 708.78] there's, of course,
[708.82 → 710.36] a lot of different types
[710.36 → 711.04] of data
[711.04 → 712.32] that are relevant to AI.
[712.32 → 713.60] And in some cases,
[713.68 → 715.02] AI models might work
[715.02 → 716.70] on multiple types of data.
[717.16 → 719.06] But maybe you could just give
[719.06 → 721.16] some common types of data
[721.16 → 723.00] that people need to label
[723.00 → 723.82] or annotate
[723.82 → 725.80] or maybe the most common ones
[725.80 → 726.50] that you run across.
[726.94 → 728.20] So I would say
[728.20 → 729.92] that most common ones,
[730.62 → 731.68] images, of course.
[732.20 → 734.68] So when you are placing
[734.68 → 736.48] a bounding box on the image,
[736.74 → 737.56] when you're doing
[737.56 → 738.80] semantic segmentation
[738.80 → 739.46] on the image,
[739.46 → 741.50] you can also think about
[741.50 → 743.02] even classifying images
[743.02 → 745.08] as a data labelling problem.
[745.28 → 746.36] So you basically assign
[746.36 → 746.96] in a class
[746.96 → 747.90] to the entire image
[747.90 → 749.16] what you see
[749.16 → 749.98] on the image.
[750.20 → 751.06] Is it, for example,
[751.80 → 753.16] an image of a fruit
[753.16 → 755.30] or image of a person?
[756.00 → 757.06] Then text.
[757.88 → 760.00] So you can be
[760.00 → 761.22] classifying text,
[761.40 → 761.84] for example,
[761.96 → 762.56] for sentiment.
[763.28 → 764.22] You can be doing
[764.22 → 765.82] named entity recognition.
[766.44 → 766.90] Audio.
[766.90 → 769.08] Again, you can be doing
[769.08 → 770.42] speaker separation.
[771.08 → 773.38] You can be classifying audio
[773.38 → 774.92] for a number of classes
[774.92 → 775.90] or doing the
[775.90 → 777.16] multi-class classification.
[778.04 → 779.34] So those, I would say,
[779.38 → 780.46] most common ones.
[780.56 → 781.40] Then you, of course,
[781.50 → 782.50] have time series.
[783.36 → 784.60] Now you also have
[784.60 → 785.42] 3D spaces
[785.42 → 787.16] with all the leader sensors
[787.16 → 788.32] that are coming
[788.32 → 789.52] and this data is coming
[789.52 → 791.18] from autonomous vehicles
[791.18 → 792.84] and videos.
[792.84 → 794.38] So I would say
[794.38 → 797.12] these six data types
[797.12 → 798.92] are the most common ones
[798.92 → 801.02] and inside each data type
[801.02 → 801.84] you kind of have
[801.84 → 803.52] different types
[803.52 → 804.28] of labelling
[804.28 → 805.24] or annotations
[805.24 → 806.04] that you can apply
[806.04 → 807.74] to this particular data type
[807.74 → 809.38] and that usually depends
[809.38 → 810.74] on what you're looking
[810.74 → 811.96] to achieve in the end.
[812.86 → 814.18] Yeah, and as you have said,
[814.22 → 815.78] you can also mix those.
[816.66 → 818.10] Yeah, so the type
[818.10 → 819.84] of annotation
[819.84 → 821.30] that you perform
[821.30 → 822.46] is really tied
[822.46 → 823.58] to the task
[823.58 → 824.28] or the objective
[824.28 → 825.44] that you want your model
[825.44 → 825.84] to perform.
[825.84 → 826.26] Yeah, totally.
[826.48 → 826.68] Right?
[826.78 → 827.42] So it's like
[827.42 → 829.12] if you want to pick out
[829.12 → 830.30] entities in text,
[830.42 → 831.38] which is what's done
[831.38 → 832.60] in named entity recognition,
[832.80 → 833.64] like you want to determine
[833.64 → 835.44] are there any places
[835.44 → 836.28] or people
[836.28 → 837.72] that are mentioned
[837.72 → 839.00] in this text,
[839.00 → 840.84] then you need to have
[840.84 → 841.70] data
[841.70 → 843.08] that you have manually
[843.08 → 843.94] labelled
[843.94 → 844.72] in some sort of
[844.72 → 845.64] gold standard way
[845.64 → 847.08] to help the model
[847.08 → 847.80] figure out
[847.80 → 849.66] based on those examples
[849.66 → 851.18] what the relationship
[851.18 → 851.82] should be
[851.82 → 853.04] between input data
[853.04 → 854.78] and the output
[854.78 → 856.24] of those entities.
[856.44 → 857.64] So there's a bunch
[857.64 → 858.24] of, I guess,
[858.52 → 859.62] there's probably
[859.62 → 860.78] infinite different
[860.78 → 862.16] like types of annotations
[862.16 → 863.38] that you can come up with
[863.38 → 864.34] because there's,
[864.34 → 864.60] you know,
[864.66 → 865.98] infinite different tasks
[865.98 → 866.90] that you might want
[866.90 → 867.44] to perform.
[867.64 → 868.50] Is that accurate?
[868.82 → 869.32] Yep, totally.
[869.76 → 870.46] Yeah, it depends on
[870.46 → 871.06] the data set
[871.06 → 871.72] that you have
[871.72 → 872.32] at your disposal
[872.32 → 873.32] and then it depends
[873.32 → 874.22] on also what you're
[874.22 → 874.88] looking to achieve
[874.88 → 875.94] with your model.
[876.50 → 877.68] And you're absolutely right.
[877.80 → 879.42] You're labelling the data
[879.42 → 882.72] and then based on your labelling,
[882.92 → 883.68] the model kind of
[883.68 → 884.58] learns the patterns
[884.58 → 886.00] and try to identify
[886.00 → 886.84] the same patterns
[886.84 → 888.46] from the new data
[888.46 → 889.36] that comes in.
[890.08 → 891.14] And that's how you basically
[891.14 → 891.90] get a prediction
[891.90 → 892.60] from your model.
[893.60 → 895.14] So it occurs to me
[895.14 → 895.80] that we've kind of
[895.80 → 896.78] thrown some terms
[896.78 → 897.56] around a little bit
[897.56 → 898.62] and we've talked about
[898.62 → 899.68] labelling and annotation
[899.68 → 901.32] and recognizing
[901.32 → 902.38] that not everybody
[902.38 → 903.08] has had a chance
[903.08 → 903.64] to do this
[903.64 → 904.38] that might be listening.
[904.88 → 906.82] What does it actually mean
[906.82 → 908.00] to annotate that data?
[908.20 → 908.36] You know,
[908.38 → 909.54] when you're annotating
[909.54 → 910.44] or labelling data,
[910.84 → 911.44] what is it
[911.44 → 912.82] you're specifically doing?
[913.18 → 914.38] What is required
[914.38 → 915.50] to achieve that?
[915.62 → 916.88] And what is the
[916.88 → 918.18] practical benefit
[918.18 → 919.04] of going through
[919.04 → 919.76] that process?
[920.12 → 920.24] Sure.
[920.78 → 923.34] So the process itself,
[923.74 → 924.02] again,
[924.06 → 924.74] it's very dependent
[924.74 → 925.84] on the data set
[925.84 → 926.94] and what you're trying
[926.94 → 927.38] to achieve,
[927.44 → 928.02] like the problem
[928.02 → 928.64] that you're trying
[928.64 → 929.10] to solve.
[929.56 → 930.60] But in general,
[930.60 → 931.64] I would describe it
[931.64 → 932.62] as basically
[932.62 → 935.06] creating some metadata
[935.06 → 937.00] for every item
[937.00 → 937.94] in your data set.
[938.64 → 939.86] So this metadata,
[940.38 → 940.82] for example,
[940.94 → 941.72] for an image,
[942.16 → 942.62] this metadata
[942.62 → 945.18] might be a rectangle
[945.18 → 946.64] at a certain position
[946.64 → 948.90] with a certain class
[948.90 → 950.48] applied to this rectangle,
[950.80 → 951.88] which is basically called
[951.88 → 953.04] a bounding box labelling.
[954.10 → 955.54] And to do so,
[955.70 → 957.08] you need to have
[957.08 → 957.86] the tool
[957.86 → 960.12] that enables you
[960.12 → 961.44] to put this bounding box
[961.44 → 962.30] at the right position
[962.30 → 964.06] and to assign the label,
[964.36 → 965.54] the class that you want
[965.54 → 966.58] to this bounding box.
[967.54 → 969.96] And a lot actually depends
[969.96 → 970.56] on the tool,
[970.72 → 971.62] how accurately
[971.62 → 972.84] and how quickly
[972.84 → 973.90] you can do that
[973.90 → 975.58] in case your data set
[975.58 → 976.58] is huge
[976.58 → 978.34] and in case you're looking
[978.34 → 980.54] for very high quality labelling.
[981.04 → 983.04] Because in the result,
[983.32 → 985.04] the quality of your models
[985.04 → 985.80] in most cases
[985.80 → 986.88] is directly tied
[986.88 → 988.14] to how accurately
[988.14 → 989.68] your data is labelled.
[990.12 → 990.78] Gotcha.
[991.04 → 991.94] And one of the things
[991.94 → 992.62] that you mentioned,
[992.72 → 993.08] by the way,
[993.20 → 994.28] being bounding box
[994.28 → 994.94] a couple of times,
[994.98 → 995.86] just wanted to note,
[996.20 → 997.14] kind of define that
[997.14 → 997.74] for a second.
[998.06 → 998.90] A bounding box,
[998.96 → 1000.00] if you're looking
[1000.00 → 1001.22] at an image
[1001.22 → 1002.10] and you're trying
[1002.10 → 1003.80] to define
[1003.80 → 1005.06] the value
[1005.06 → 1005.78] of different parts
[1005.78 → 1006.36] of that image
[1006.36 → 1007.16] for purposes
[1007.16 → 1008.50] of training subsequently,
[1008.92 → 1010.04] then a bounding box
[1010.04 → 1011.78] is really just like it sounds.
[1011.86 → 1013.08] It's a geometric shape
[1013.08 → 1014.22] that you're assigning
[1014.22 → 1015.14] to different parts
[1015.14 → 1015.76] of the image
[1015.76 → 1016.64] to define
[1016.64 → 1017.92] the different areas
[1017.92 → 1018.38] of the image
[1018.38 → 1018.84] that you want
[1018.84 → 1019.22] the model
[1019.22 → 1020.08] to either focus on
[1020.08 → 1020.76] or not focus on.
[1020.76 → 1020.94] Yep.
[1021.00 → 1021.40] I just wanted
[1021.40 → 1021.90] to note that.
[1021.96 → 1022.06] Yep.
[1022.06 → 1034.58] What is up,
[1034.66 → 1035.44] Practically I listeners?
[1035.64 → 1036.26] We're working with
[1036.26 → 1036.84] Infinite Red
[1036.84 → 1037.42] to promote their
[1037.42 → 1038.88] free AI mini course.
[1039.10 → 1039.50] It's called
[1039.50 → 1040.64] AI Demystified.
[1040.96 → 1041.86] Learn more and enrol
[1041.86 → 1044.18] at learn ai.infinite.red.
[1044.34 → 1045.40] This free five-day
[1045.40 → 1046.02] mini course
[1046.02 → 1047.44] is a great introduction
[1047.44 → 1048.48] to the most important
[1048.48 → 1049.02] concepts,
[1049.14 → 1049.44] types,
[1049.44 → 1050.86] and business applications
[1050.86 → 1052.50] for AI and machine learning.
[1052.80 → 1053.82] Each day of the course
[1053.82 → 1055.20] includes a lesson,
[1055.48 → 1056.24] a quiz,
[1056.40 → 1057.04] and an assignment
[1057.04 → 1058.14] to submit your learning.
[1058.62 → 1059.26] And after you've
[1059.26 → 1060.08] completed the course,
[1060.22 → 1061.08] you'll also get
[1061.08 → 1062.52] a certificate of completion
[1062.52 → 1063.84] for your LinkedIn profile
[1063.84 → 1064.82] or for your portfolio.
[1065.52 → 1066.28] If you've been feeling
[1066.28 → 1067.42] lost in the world of AI
[1067.42 → 1068.78] and hearing lots of buzzwords,
[1069.06 → 1069.66] then by the end
[1069.66 → 1070.38] of this mini course,
[1070.44 → 1070.72] you'll be able
[1070.72 → 1071.92] to speak intelligently
[1071.92 → 1073.84] about AI and machine learning
[1073.84 → 1074.74] and their practical
[1074.74 → 1075.70] business applications.
[1076.26 → 1076.54] Again,
[1076.64 → 1077.16] this course
[1077.16 → 1078.28] is completely free.
[1078.28 → 1079.64] Learn more and enrol
[1079.64 → 1081.70] at learn ai.infinite.red.
[1081.90 → 1082.36] Again,
[1082.52 → 1084.28] learn ai.infinite.red.
[1096.04 → 1097.00] Okay, Michael.
[1097.18 → 1098.38] So let's say
[1098.38 → 1100.14] that I'm convinced
[1100.14 → 1101.06] that I need to do
[1101.06 → 1101.76] data labelling
[1101.76 → 1102.62] and I'm convinced
[1102.62 → 1103.76] that I should put time
[1103.76 → 1104.28] into it.
[1104.42 → 1106.32] It is an important part
[1106.32 → 1107.52] of my AI workflow
[1107.52 → 1109.20] and one of the most
[1109.20 → 1109.92] important parts
[1109.92 → 1110.52] because it has
[1110.52 → 1111.74] this direct impact
[1111.74 → 1112.68] on the quality
[1112.68 → 1114.02] of my predictions.
[1114.62 → 1115.30] And let's say
[1115.30 → 1116.52] that I have
[1116.52 → 1118.38] 100,000 samples
[1118.38 → 1119.00] or more
[1119.00 → 1120.38] to label.
[1120.64 → 1121.54] There's obvious
[1121.54 → 1122.30] challenges
[1122.30 → 1123.14] around the
[1123.14 → 1124.92] time-consuming nature
[1124.92 → 1125.76] that it would take
[1125.76 → 1126.38] to label
[1126.38 → 1127.04] each of those
[1127.04 → 1128.16] 100,000 samples.
[1128.30 → 1128.88] Are there other
[1128.88 → 1129.62] challenges
[1129.62 → 1130.86] like I'm thinking
[1130.86 → 1132.02] in terms of
[1132.02 → 1133.30] maybe bias
[1133.30 → 1134.08] or like
[1134.08 → 1135.64] crowdsourcing this
[1135.64 → 1136.00] or like
[1136.00 → 1136.52] what sorts
[1136.52 → 1137.08] of challenges
[1137.08 → 1138.00] do people face
[1138.00 → 1138.44] when they're
[1138.44 → 1139.96] labelling data
[1139.96 → 1140.82] maybe other
[1140.82 → 1141.52] than the obvious
[1141.52 → 1142.08] one like
[1142.08 → 1143.28] the time-consuming
[1143.28 → 1143.96] nature of it?
[1144.16 → 1144.86] Oh, many,
[1145.02 → 1145.44] many.
[1146.76 → 1148.02] So time,
[1148.20 → 1148.42] yeah,
[1148.56 → 1148.94] definitely.
[1149.16 → 1149.74] If you have
[1149.74 → 1150.38] big enough data
[1150.38 → 1150.80] sets,
[1150.92 → 1151.76] millions of items,
[1152.30 → 1152.80] it's going to take
[1152.80 → 1153.30] a lot of time
[1153.30 → 1154.02] to label it.
[1154.44 → 1155.58] Then quality,
[1156.18 → 1156.98] how do you verify
[1156.98 → 1158.26] that the results
[1158.26 → 1159.10] of the labelling
[1159.10 → 1159.94] and the actual
[1159.94 → 1160.96] labels are,
[1161.22 → 1161.52] for example,
[1161.58 → 1161.98] if we're talking
[1161.98 → 1162.98] about bounding boxes,
[1162.98 → 1164.22] that the bounding boxes
[1164.22 → 1165.60] are in correct positions,
[1166.04 → 1166.48] biases,
[1167.14 → 1168.86] when different people
[1168.86 → 1170.96] label the same data set,
[1171.04 → 1171.64] you may end up
[1171.64 → 1172.86] with different results,
[1173.10 → 1174.42] so personal biases.
[1175.28 → 1177.22] Then even before that,
[1177.36 → 1178.36] you actually need
[1178.36 → 1180.48] to have a tool
[1180.48 → 1181.84] to help you do that
[1181.84 → 1183.26] because data sets
[1183.26 → 1184.16] are different types
[1184.16 → 1184.84] of annotations
[1184.84 → 1185.34] and labelling
[1185.34 → 1186.10] are very different,
[1186.30 → 1187.44] so you have to
[1187.44 → 1188.24] invest time
[1188.24 → 1189.92] into either creating
[1189.92 → 1190.60] your own tool
[1190.60 → 1191.30] or using something
[1191.30 → 1192.38] from the open source
[1192.38 → 1194.92] and there are
[1194.92 → 1195.64] basically many more.
[1196.08 → 1196.76] I would say that
[1196.76 → 1197.88] two major ones
[1197.88 → 1199.28] are time
[1199.28 → 1200.14] and quality.
[1200.78 → 1200.88] Yeah.
[1201.28 → 1202.10] Yeah, so quality
[1202.10 → 1202.90] being around
[1202.90 → 1204.34] the verification
[1204.34 → 1205.52] of the data,
[1205.66 → 1206.00] right?
[1206.16 → 1206.60] So like,
[1206.92 → 1208.16] if I crowdsource,
[1208.30 → 1208.92] let's say,
[1209.50 → 1210.26] a million
[1210.26 → 1212.14] parallel translations
[1212.14 → 1213.76] between two languages,
[1214.44 → 1215.66] how do I know
[1215.66 → 1216.82] that those
[1216.82 → 1217.92] were actually
[1217.92 → 1219.48] good translations
[1219.48 → 1220.60] given that I
[1220.60 → 1221.56] don't already
[1221.56 → 1223.04] have the model?
[1223.16 → 1223.84] So it seems like
[1223.84 → 1224.56] it's a sort of
[1224.56 → 1225.34] chicken and egg
[1225.34 → 1226.36] sort of thing.
[1226.56 → 1227.22] How do you deal
[1227.22 → 1228.24] with something like that?
[1228.32 → 1229.60] Yeah, to add to that,
[1230.42 → 1231.06] that works
[1231.06 → 1232.88] if you can crowdsource,
[1233.40 → 1233.68] right?
[1233.84 → 1234.68] So for example,
[1234.68 → 1235.46] if you're dealing
[1235.46 → 1236.34] with the data
[1236.34 → 1237.16] that requires
[1237.16 → 1237.78] kind of like
[1237.78 → 1239.44] domain-specific knowledge,
[1239.94 → 1240.50] for example,
[1241.06 → 1241.94] medical images,
[1242.60 → 1242.88] right?
[1243.12 → 1244.32] You can't crowdsource
[1244.32 → 1244.70] that.
[1245.34 → 1246.64] Yeah, and it's expensive
[1246.64 → 1247.66] to hire doctors,
[1247.66 → 1248.22] I imagine.
[1248.22 → 1249.38] Yeah, and then
[1249.38 → 1250.18] another one,
[1250.36 → 1251.32] if privacy
[1251.32 → 1252.10] is an issue,
[1252.74 → 1253.70] then you also
[1253.70 → 1254.64] can't crowdsource
[1254.64 → 1254.98] that.
[1255.12 → 1255.94] You need to have
[1255.94 → 1256.98] in-house data
[1256.98 → 1257.70] labelling team.
[1258.74 → 1259.80] So for the
[1259.80 → 1260.66] quality control,
[1260.84 → 1261.36] there are
[1261.36 → 1262.50] multiple ways
[1262.50 → 1263.58] how you can
[1263.58 → 1264.98] verify the results.
[1265.64 → 1266.34] One of them
[1266.34 → 1267.10] is
[1267.10 → 1268.58] you can
[1268.58 → 1269.40] kind of
[1269.40 → 1270.82] label
[1270.82 → 1271.48] fraction
[1271.48 → 1272.00] of your data
[1272.00 → 1272.42] set,
[1273.18 → 1274.24] verify it
[1274.24 → 1275.44] multiple times
[1275.44 → 1276.54] that it was
[1276.54 → 1277.48] labelled correctly,
[1277.70 → 1278.48] then you can
[1278.48 → 1279.36] train a model
[1279.36 → 1280.44] on top of that
[1280.44 → 1281.68] and further
[1281.68 → 1282.44] use this model
[1282.44 → 1283.26] to verify
[1283.26 → 1284.14] the subsequent
[1284.14 → 1285.10] labels that
[1285.10 → 1285.44] are coming.
[1286.00 → 1286.68] Another one,
[1286.74 → 1287.56] you can distribute
[1287.56 → 1288.56] the same task
[1288.56 → 1289.50] to multiple
[1289.50 → 1290.72] annotators
[1290.72 → 1292.22] and verify
[1292.22 → 1292.98] if they're in
[1292.98 → 1293.88] consensus between
[1293.88 → 1294.68] each other or not.
[1295.28 → 1296.16] So when you're
[1296.16 → 1296.78] talking about
[1296.78 → 1297.56] sort of bringing
[1297.56 → 1298.46] the model
[1298.46 → 1299.04] into
[1299.04 → 1300.82] this process,
[1300.82 → 1301.56] is that what
[1301.56 → 1302.46] people refer to
[1302.46 → 1303.76] as model
[1303.76 → 1304.64] in-the-loop
[1304.64 → 1306.20] versus out-of-the-loop
[1306.20 → 1306.88] labelling,
[1307.24 → 1308.06] where you actually
[1308.06 → 1309.46] kind of have a
[1309.46 → 1310.44] model that's
[1310.44 → 1311.06] trained on some
[1311.06 → 1311.60] of your data
[1311.60 → 1312.26] when you're trying
[1312.26 → 1313.20] to label more
[1313.20 → 1314.26] data and
[1314.26 → 1315.06] updating that.
[1315.18 → 1315.48] Is that what
[1315.48 → 1315.82] that means?
[1316.40 → 1317.28] I call it
[1317.28 → 1317.74] more or less
[1317.74 → 1318.78] like automatic
[1318.78 → 1319.30] labelling.
[1320.04 → 1320.70] And here,
[1320.82 → 1321.52] the most important
[1321.52 → 1322.82] piece is
[1322.82 → 1323.62] how do you pick
[1323.62 → 1324.54] those items
[1324.54 → 1325.90] in the first place?
[1326.40 → 1326.78] Basically,
[1326.78 → 1327.38] if you have
[1327.38 → 1328.06] a very large
[1328.06 → 1328.76] data set,
[1328.86 → 1329.60] how do you pick
[1329.60 → 1330.42] those items
[1330.42 → 1331.10] that you want
[1331.10 → 1332.00] to label first
[1332.00 → 1333.36] and using
[1333.36 → 1333.96] those labels,
[1334.10 → 1334.48] you kind of
[1334.48 → 1334.90] can build
[1334.90 → 1335.22] the model,
[1335.32 → 1335.80] but how do
[1335.80 → 1336.02] you pick
[1336.02 → 1336.50] the items?
[1337.06 → 1337.46] And so
[1337.46 → 1338.66] this field
[1338.66 → 1340.12] is called
[1340.12 → 1340.94] active learning
[1340.94 → 1342.84] and active
[1342.84 → 1343.28] learning is
[1343.28 → 1344.14] basically a way
[1344.14 → 1344.76] to pick
[1344.76 → 1345.18] the items
[1345.18 → 1345.56] from your
[1345.56 → 1346.10] data set
[1346.10 → 1346.72] that provide
[1346.72 → 1347.70] you enough
[1347.70 → 1348.24] information
[1348.24 → 1348.80] about the
[1348.80 → 1349.22] data set
[1349.22 → 1349.76] as a whole.
[1350.18 → 1350.68] So you're
[1350.68 → 1351.32] analyzing the
[1351.32 → 1351.84] data set
[1351.84 → 1352.22] and picking
[1352.22 → 1352.98] exactly those
[1352.98 → 1353.64] items that you
[1353.64 → 1354.20] want to label
[1354.20 → 1355.34] first in order
[1355.34 → 1355.84] to be able
[1355.84 → 1357.38] to label
[1357.38 → 1357.86] the rest
[1357.86 → 1358.50] of the data
[1358.50 → 1359.16] set for you.
[1359.16 → 1361.24] So how are
[1361.24 → 1362.08] people currently
[1362.08 → 1362.90] approaching data
[1362.90 → 1363.64] labelling at this
[1363.64 → 1363.90] point?
[1364.06 → 1364.74] What are the
[1364.74 → 1365.46] range of
[1365.46 → 1366.34] techniques and
[1366.34 → 1367.00] the tooling that
[1367.00 → 1367.88] you have that
[1367.88 → 1368.52] you would use
[1368.52 → 1369.04] for that
[1369.04 → 1369.38] you might have
[1369.38 → 1369.74] seen?
[1370.34 → 1370.70] And also,
[1370.88 → 1371.08] I guess,
[1371.20 → 1372.24] what's lacking
[1372.24 → 1372.86] in that at this
[1372.86 → 1373.10] point?
[1373.64 → 1373.86] Yeah.
[1374.32 → 1375.44] So I think
[1375.44 → 1376.08] right now there
[1376.08 → 1377.12] are two ways.
[1377.28 → 1377.74] Basically,
[1378.00 → 1379.04] first one is
[1379.04 → 1379.68] using the
[1379.68 → 1380.06] services.
[1380.82 → 1382.22] So you just
[1382.22 → 1382.66] send your
[1382.66 → 1383.70] data sets to
[1383.70 → 1384.14] the service
[1384.14 → 1385.26] company and you
[1385.26 → 1386.24] get back the
[1386.24 → 1387.40] label data sets,
[1387.50 → 1388.02] the results.
[1388.02 → 1389.00] And second
[1389.00 → 1390.60] one is either
[1390.60 → 1391.20] building your
[1391.20 → 1392.74] in-house team or
[1392.74 → 1394.24] just using your
[1394.24 → 1395.30] data science team
[1395.30 → 1396.76] and using the
[1396.76 → 1397.70] tools to help
[1397.70 → 1398.36] them do that.
[1399.08 → 1400.28] So the
[1400.28 → 1401.00] problem with the
[1401.00 → 1402.00] first one with
[1402.00 → 1402.42] the service
[1402.42 → 1403.52] companies is that
[1403.52 → 1404.96] you don't have
[1404.96 → 1405.68] control over the
[1405.68 → 1406.12] process.
[1406.88 → 1407.50] So you just get
[1407.50 → 1408.28] back the results
[1408.28 → 1408.92] and then it's
[1408.92 → 1409.42] your job to
[1409.42 → 1410.28] verify if results
[1410.28 → 1410.88] are of good
[1410.88 → 1411.62] quality or not.
[1412.12 → 1412.94] In most cases,
[1413.38 → 1414.04] you don't get
[1414.04 → 1414.66] good quality
[1414.66 → 1415.08] results.
[1415.48 → 1416.54] And then again,
[1416.64 → 1417.24] if you're dealing
[1417.24 → 1418.00] with the data that
[1418.00 → 1418.72] requires domain
[1418.72 → 1419.60] specific knowledge,
[1420.06 → 1420.82] usually you can't
[1420.82 → 1421.48] outsource that
[1421.48 → 1421.88] easily.
[1422.60 → 1423.50] And privacy is
[1423.50 → 1424.14] another issue.
[1424.74 → 1425.24] With the second
[1425.24 → 1426.26] one, what we have
[1426.26 → 1427.06] found out that a
[1427.06 → 1427.68] lot of companies,
[1427.82 → 1428.50] they are starting
[1428.50 → 1429.72] with some sort of
[1429.72 → 1431.22] using some sort of
[1431.22 → 1432.30] open source solution
[1432.30 → 1434.08] just to get their
[1434.08 → 1435.74] data labelled and
[1435.74 → 1436.92] basically build the
[1436.92 → 1437.90] first version of
[1437.90 → 1438.42] their models.
[1439.10 → 1439.72] And what they
[1439.72 → 1440.82] find out is that
[1440.82 → 1442.68] they need to
[1442.68 → 1444.06] upgrade the tool
[1444.06 → 1445.02] and tweak the
[1445.02 → 1445.60] tool to their
[1445.60 → 1446.46] needs more and
[1446.46 → 1447.64] more before it
[1447.64 → 1448.44] becomes this
[1448.44 → 1449.70] mysterious tool
[1449.70 → 1450.72] that you kind
[1450.72 → 1451.36] of don't want
[1451.36 → 1451.82] and you don't
[1451.82 → 1452.64] have resources to
[1452.64 → 1453.38] support anymore.
[1453.90 → 1454.72] At this point,
[1454.82 → 1455.20] they are looking
[1455.20 → 1456.02] for something that
[1456.02 → 1457.28] is more production
[1457.28 → 1458.48] ready and is
[1458.48 → 1459.20] ready to scale.
[1459.20 → 1463.18] So in terms of
[1463.18 → 1464.96] the range of
[1464.96 → 1465.60] things, I
[1465.60 → 1466.28] imagine that
[1466.28 → 1468.38] there's a ton of
[1468.38 → 1470.42] different types of
[1470.42 → 1470.96] models and
[1470.96 → 1471.72] architectures that
[1471.72 → 1472.38] people use for
[1472.38 → 1472.88] these different
[1472.88 → 1473.28] tasks.
[1473.42 → 1473.68] Like you've
[1473.68 → 1474.30] mentioned sentiment
[1474.30 → 1475.34] analysis, image
[1475.34 → 1475.90] classification.
[1476.58 → 1477.70] I imagine that
[1477.70 → 1479.66] the burden in
[1479.66 → 1480.96] different of these
[1480.96 → 1482.30] model types is
[1482.30 → 1483.84] heavier in terms
[1483.84 → 1486.18] of data labelling.
[1486.18 → 1487.88] And maybe, Chris,
[1487.96 → 1488.58] I know you've
[1488.58 → 1489.32] worked in like
[1489.32 → 1491.68] masking images
[1491.68 → 1493.90] for robot
[1493.90 → 1494.66] perception and
[1494.66 → 1495.02] that sort of
[1495.02 → 1495.14] thing.
[1495.30 → 1495.52] Yeah, different
[1495.52 → 1496.52] types of CNNs.
[1497.16 → 1497.72] Yeah, that's
[1497.72 → 1499.40] much harder than
[1499.40 → 1500.60] let's say sentiment
[1500.60 → 1502.10] analysis in text
[1502.10 → 1502.76] where you just kind
[1502.76 → 1503.40] of say is it
[1503.40 → 1504.10] positive or
[1504.10 → 1504.74] negative.
[1505.24 → 1506.36] As a result of
[1506.36 → 1507.08] that, are there
[1507.08 → 1508.20] types of problems
[1508.20 → 1508.88] or the types of
[1508.88 → 1509.52] models that you
[1509.52 → 1509.92] might want to
[1509.92 → 1510.46] create where
[1510.46 → 1511.50] there's already a
[1511.50 → 1512.50] lot of good data
[1512.50 → 1513.24] out there that's
[1513.24 → 1514.26] publicly labelled that
[1514.26 → 1515.20] you can use like
[1515.20 → 1515.90] let's say for
[1515.90 → 1516.72] sentiment analysis
[1516.72 → 1517.64] versus other
[1517.64 → 1518.50] problems where
[1518.50 → 1519.54] just due to the
[1519.54 → 1520.38] nature of how
[1520.38 → 1521.32] difficult it is to
[1521.32 → 1521.94] label, you're kind
[1521.94 → 1522.52] of stuck with
[1522.52 → 1523.18] doing it on your
[1523.18 → 1523.38] own?
[1523.62 → 1524.60] Yeah, I think
[1524.60 → 1525.38] yeah, so for
[1525.38 → 1526.06] some problems
[1526.06 → 1527.52] definitely, and
[1527.52 → 1528.06] like for the
[1528.06 → 1529.10] easier problems,
[1529.56 → 1530.30] in most cases
[1530.30 → 1531.22] you can use
[1531.22 → 1531.96] transfer learning.
[1532.76 → 1533.72] So you basically
[1533.72 → 1534.44] start with a
[1534.44 → 1535.28] pre-trained model
[1535.28 → 1536.70] and then you
[1536.70 → 1537.64] label just a
[1537.64 → 1538.36] small fraction
[1538.36 → 1540.58] and you train
[1540.58 → 1541.64] the model, the
[1541.64 → 1542.24] transfer learning
[1542.24 → 1543.12] model with that
[1543.12 → 1543.50] data.
[1543.50 → 1545.68] data and that
[1545.68 → 1546.54] works pretty
[1546.54 → 1549.12] well, but in
[1549.12 → 1550.40] most cases you
[1550.40 → 1551.16] get the data,
[1551.32 → 1551.74] like especially
[1551.74 → 1552.18] if you're getting
[1552.18 → 1552.94] the data from the
[1552.94 → 1554.50] real world, then
[1554.50 → 1555.46] it's not that easy
[1555.46 → 1556.34] to use existing
[1556.34 → 1557.12] models for that.
[1558.18 → 1558.84] So I guess this
[1558.84 → 1559.56] might be a good
[1559.56 → 1560.66] turning point to
[1560.66 → 1561.72] kind of talk about,
[1561.84 → 1562.22] if you could tell
[1562.22 → 1562.94] us a little bit
[1562.94 → 1564.32] about your company
[1564.32 → 1565.66] and what Label
[1565.66 → 1567.30] Studio does and
[1567.30 → 1568.18] kind of how does
[1568.18 → 1568.86] the company and the
[1568.86 → 1569.56] product relate to
[1569.56 → 1570.48] each other and
[1570.48 → 1571.18] what are they?
[1571.62 → 1571.78] Sure.
[1572.38 → 1573.02] So yeah, the
[1573.02 → 1573.66] company name is
[1573.66 → 1575.08] Harder and Harder
[1575.08 → 1576.02] is a data
[1576.02 → 1576.90] labelling platform
[1576.90 → 1578.32] that makes
[1578.32 → 1579.36] entire data
[1579.36 → 1580.12] science teams
[1580.12 → 1580.86] more productive
[1580.86 → 1582.94] and helps
[1582.94 → 1584.34] build higher
[1584.34 → 1585.40] quality, safer
[1585.40 → 1586.28] and smarter
[1586.28 → 1587.04] models as a
[1587.04 → 1587.38] result.
[1588.28 → 1589.50] And we have
[1589.50 → 1590.34] open source
[1590.34 → 1591.66] product that is
[1591.66 → 1592.34] called Label
[1592.34 → 1592.64] Studio.
[1593.48 → 1594.30] So the
[1594.30 → 1595.00] difference between
[1595.00 → 1595.76] this is that
[1595.76 → 1597.10] Label Studio is
[1597.10 → 1598.00] just the front end
[1598.00 → 1598.36] part.
[1598.36 → 1600.58] So you get
[1600.58 → 1601.96] the labelling
[1601.96 → 1603.14] interface where
[1603.14 → 1604.44] you can upload
[1604.44 → 1605.86] your data and
[1605.86 → 1607.02] go item by
[1607.02 → 1607.98] item and label
[1607.98 → 1608.22] it.
[1609.20 → 1609.96] And the
[1609.96 → 1610.50] company, the
[1610.50 → 1611.22] commercial offering
[1611.22 → 1612.36] is basically where
[1612.36 → 1613.98] you can also use
[1613.98 → 1614.94] our pre-trained
[1614.94 → 1615.98] models to help
[1615.98 → 1616.54] to go through
[1616.54 → 1617.06] the data set
[1617.06 → 1617.46] faster.
[1617.78 → 1619.38] You can invite
[1619.38 → 1620.40] your whole team
[1620.40 → 1622.02] to collaborate on
[1622.02 → 1622.82] the data labelling
[1622.82 → 1624.80] and exploring your
[1624.80 → 1625.42] data sets.
[1625.42 → 1626.90] and we have
[1626.90 → 1627.82] also extensive
[1627.82 → 1628.82] process for the
[1628.82 → 1629.72] quality control
[1629.72 → 1631.02] helping you to
[1631.02 → 1632.18] verify that the
[1632.18 → 1633.04] results that you're
[1633.04 → 1634.04] getting are
[1634.04 → 1635.10] actually what you're
[1635.10 → 1635.66] looking for.
[1636.32 → 1637.28] Yeah, so this is
[1637.28 → 1638.28] like Label Studio.
[1638.28 → 1639.10] You can kind of
[1639.10 → 1639.78] think as the
[1639.78 → 1640.70] open front end
[1640.70 → 1641.72] that anyone could
[1641.72 → 1642.22] use.
[1642.40 → 1642.76] You know, you
[1642.76 → 1643.42] could just get off
[1643.42 → 1644.40] of GitHub to
[1644.40 → 1645.66] help aid you in
[1645.66 → 1646.84] your annotation if
[1646.84 → 1647.52] let's say you want
[1647.52 → 1648.08] to start from
[1648.08 → 1648.56] scratch.
[1649.10 → 1649.52] But as you
[1649.52 → 1649.94] mentioned,
[1650.46 → 1650.96] starting from
[1650.96 → 1651.76] scratch isn't
[1651.76 → 1652.68] always necessary
[1652.68 → 1653.70] and isn't
[1653.70 → 1655.00] always practical
[1655.00 → 1655.84] or efficient,
[1656.06 → 1656.28] right?
[1656.38 → 1657.42] So the things
[1657.42 → 1657.92] that you mentioned,
[1658.00 → 1658.58] I see you mentioned
[1658.58 → 1660.34] like auto relabelling
[1660.34 → 1661.90] and native active
[1661.90 → 1662.42] learning.
[1662.58 → 1663.26] You already mentioned
[1663.26 → 1664.16] those things a little
[1664.16 → 1664.84] bit, but those are
[1664.84 → 1665.66] the things that kind
[1665.66 → 1666.46] of augment the
[1666.46 → 1666.96] processes.
[1667.22 → 1667.66] Is that right?
[1668.16 → 1668.28] Yeah.
[1668.66 → 1669.92] And what I like
[1669.92 → 1670.92] about the open
[1670.92 → 1671.68] source, the Label
[1671.68 → 1672.82] Studio, it's the
[1672.82 → 1674.84] first open source
[1674.84 → 1676.18] data labelling tool
[1676.18 → 1677.78] that you can not
[1677.78 → 1679.36] only download and
[1679.36 → 1680.40] run, you can also
[1680.40 → 1681.74] embed it into your
[1681.74 → 1682.62] own pipelines.
[1683.38 → 1683.86] Ah, okay.
[1683.96 → 1684.80] So does that mean
[1684.80 → 1686.00] like you can run it
[1686.00 → 1687.08] non-interactively
[1687.08 → 1687.86] somehow or how
[1687.86 → 1688.74] would that work out
[1688.74 → 1689.54] in practice?
[1689.88 → 1690.60] So in progress,
[1690.74 → 1691.56] many different ways.
[1691.76 → 1692.70] So you can use the
[1692.70 → 1693.60] tool to create the
[1693.60 → 1694.68] labels, and you can
[1694.68 → 1695.70] also use this tool
[1695.70 → 1697.10] to look at what
[1697.10 → 1698.38] predictions of your
[1698.38 → 1698.62] model.
[1699.42 → 1700.74] So you can embed
[1700.74 → 1702.24] this tool into your
[1702.24 → 1704.52] pipeline, and you can
[1704.52 → 1705.62] verify what your
[1705.62 → 1707.04] model predictions are.
[1707.58 → 1709.02] You can ask your
[1709.02 → 1710.26] team members or for
[1710.26 → 1710.82] example, the main
[1710.82 → 1711.88] knowledge experts to
[1711.88 → 1712.66] provide the label
[1712.66 → 1714.96] for specific items
[1714.96 → 1715.92] in your data set.
[1716.10 → 1716.92] So there are
[1716.92 → 1718.38] multiple ways how
[1718.38 → 1719.78] you can embed and
[1719.78 → 1720.22] use it.
[1720.58 → 1721.20] And it's really
[1721.20 → 1722.96] flexible in the way
[1722.96 → 1724.84] how you can define
[1724.84 → 1726.02] the different types
[1726.02 → 1727.06] of tasks it can
[1727.06 → 1727.44] handle.
[1727.44 → 1729.80] could you describe some
[1729.80 → 1731.50] of those tasks as well
[1731.50 → 1732.08] just to kind of give
[1732.08 → 1733.48] us a sense of what
[1733.48 → 1734.30] all it can do and
[1734.30 → 1735.26] what's required for
[1735.26 → 1736.04] input and output on
[1736.04 → 1736.22] those?
[1736.30 → 1736.48] Sure.
[1736.84 → 1737.62] We originally started
[1737.62 → 1738.90] from the idea that
[1738.90 → 1740.74] we as founders of the
[1740.74 → 1741.82] company, of the
[1741.82 → 1742.28] company, we were
[1742.28 → 1743.54] coming from different
[1743.54 → 1744.50] machine learning
[1744.50 → 1745.02] backgrounds.
[1745.02 → 1746.46] So I was more
[1746.46 → 1748.20] concentrated on images
[1748.20 → 1750.74] and visual data and
[1750.74 → 1752.20] my co-founders, they
[1752.20 → 1754.24] were concentrating on
[1754.24 → 1755.60] audio and text.
[1756.36 → 1757.84] So we had this idea
[1757.84 → 1759.14] about building the
[1759.14 → 1760.48] data labelling tool that
[1760.48 → 1761.42] is configurable.
[1762.36 → 1763.16] And so what we have
[1763.16 → 1764.62] created is basically a
[1764.62 → 1766.44] very high level kind of
[1766.44 → 1768.30] components that you
[1768.30 → 1769.30] stick together.
[1769.70 → 1771.34] Think about it as you are
[1771.34 → 1772.30] building the web page
[1772.30 → 1773.62] using HTML in the
[1773.62 → 1774.38] same way you are
[1774.38 → 1775.34] building your data
[1775.34 → 1776.32] labelling interface.
[1776.52 → 1778.06] It usually takes from
[1778.06 → 1780.88] five to 25 lines of
[1780.88 → 1782.16] HTML like config
[1782.16 → 1782.54] language.
[1783.54 → 1784.94] And as a result, you
[1784.94 → 1786.00] can get a data
[1786.00 → 1787.62] labelling tool that you
[1787.62 → 1788.54] can use to label
[1788.54 → 1790.32] audio images and text
[1790.32 → 1790.78] right now.
[1791.18 → 1792.40] And we will be adding
[1792.40 → 1793.72] video before the end
[1793.72 → 1794.24] of the year.
[1794.96 → 1798.02] And you can do many
[1798.02 → 1798.60] different things.
[1798.90 → 1799.68] So all that we have
[1799.68 → 1800.68] discussed, like basically
[1800.68 → 1801.94] bounding boxes, name
[1801.94 → 1804.34] entity, you can do all
[1804.34 → 1805.12] of them at the same
[1805.12 → 1806.08] time if you want to.
[1807.32 → 1808.30] And it's basically
[1808.30 → 1809.96] depending on the task
[1809.96 → 1811.12] and depending on the
[1811.12 → 1812.44] data set that you have,
[1812.82 → 1814.40] you can configure it as
[1814.40 → 1816.24] a like Swiss army knife.
[1816.58 → 1818.44] You can configure it and
[1818.44 → 1819.46] tailor it for your
[1819.46 → 1820.16] particular needs.
[1820.16 → 1830.94] This episode is brought to
[1830.94 → 1831.94] you by Rubicon, Cloud
[1831.94 → 1833.02] Native Con, and you are
[1833.02 → 1834.08] invited to attend this
[1834.08 → 1835.56] flagship conference from
[1835.56 → 1836.14] the Cloud Native
[1836.14 → 1837.00] Computing Foundation.
[1837.18 → 1838.66] Rubicon, Cloud Native Con,
[1838.94 → 1839.98] North America 2019.
[1840.36 → 1841.22] It's happening November
[1841.22 → 1842.98] 18th through the 21st in
[1842.98 → 1844.08] San Diego, California.
[1844.40 → 1845.76] This conference gathers
[1845.76 → 1847.60] adopters and technologists
[1847.60 → 1848.76] from leading up a source
[1848.76 → 1850.14] in cloud native communities.
[1850.50 → 1852.06] Use the code KANA
[1852.06 → 1853.44] PracticalAI19.
[1853.64 → 1855.12] Again, KANA
[1855.12 → 1856.18] PracticalAI19
[1856.18 → 1857.38] to get 10% off
[1857.38 → 1858.62] registration or check the
[1858.62 → 1859.28] show notes for a special
[1859.28 → 1860.78] link to register and a
[1860.78 → 1861.90] link to to convince your
[1861.90 → 1862.54] boss letter.
[1862.92 → 1863.62] Again, check the show notes
[1863.62 → 1864.58] for links to learn more
[1864.58 → 1865.26] and register.
[1865.26 → 1879.26] All right.
[1879.34 → 1880.98] So every once in a while on
[1880.98 → 1882.70] this podcast, the topic
[1882.70 → 1885.38] intersects very nicely with a
[1885.38 → 1886.60] problem that I'm trying to
[1886.60 → 1887.82] solve in my own work.
[1887.90 → 1888.82] And this is one case.
[1888.82 → 1890.74] So in those cases, as Chris
[1890.74 → 1892.56] knows, I like to selfishly
[1892.56 → 1894.08] try to get the guests to help
[1894.08 → 1895.46] solve my problem on the fly.
[1896.16 → 1897.70] So one of those problems is
[1897.70 → 1900.24] I have not found a tool that
[1900.24 → 1902.62] will let me easily label
[1902.62 → 1904.46] reading comprehension data.
[1904.58 → 1905.70] So this is the case where you
[1905.70 → 1907.62] have like a question and a
[1907.62 → 1909.20] piece, a passage of text.
[1909.34 → 1910.92] And then the output that you
[1910.92 → 1913.96] want is answer that is drawn
[1913.96 → 1915.86] from that text, maybe a span
[1915.86 → 1917.78] within the article text or
[1917.78 → 1918.44] something like that.
[1918.68 → 1920.40] And there's no tool out there
[1920.40 → 1922.30] that at least that I found
[1922.30 → 1922.84] that does that.
[1922.96 → 1924.56] So with Label Studio, could
[1924.56 → 1925.92] you kind of walk me through,
[1926.58 → 1927.98] let's say I came to Label
[1927.98 → 1929.92] Studio, and what would it take
[1929.92 → 1931.54] to set up that sort of
[1931.54 → 1933.04] interface with these Label
[1933.04 → 1934.48] Studio components?
[1934.56 → 1935.26] Would that be possible?
[1935.54 → 1935.92] Possible.
[1936.12 → 1936.42] Yes.
[1936.68 → 1938.26] So I would suggest, yeah,
[1938.30 → 1939.56] basically installing it,
[1939.92 → 1941.42] then looking at the templates
[1941.42 → 1943.80] that we provide, use the
[1943.80 → 1945.74] template as a starting point,
[1946.26 → 1948.22] and then looking at the tags
[1948.22 → 1950.64] that you can use for your
[1950.64 → 1952.04] particular problem.
[1952.90 → 1954.56] So based on your description,
[1954.76 → 1955.92] I think, yeah, it's very much
[1955.92 → 1956.16] doable.
[1956.32 → 1956.42] Yep.
[1956.92 → 1957.08] Yeah.
[1957.18 → 1959.14] So because I'm a data scientist
[1959.14 → 1961.50] and slash backend person,
[1961.50 → 1963.24] and I don't know that much
[1963.24 → 1965.26] front end, but maybe I've
[1965.26 → 1967.08] hacked on HTML before.
[1967.34 → 1968.80] Would that be something I could
[1968.80 → 1969.12] tackle?
[1969.22 → 1970.10] Like how much front end
[1970.10 → 1971.06] experience do I need?
[1971.48 → 1973.10] So it depends on how much
[1973.10 → 1973.58] you want.
[1973.84 → 1975.36] I would say if there are
[1975.36 → 1976.76] components that cover your
[1976.76 → 1978.56] use case, and we right now
[1978.56 → 1980.38] have around 20 different
[1980.38 → 1982.80] components, then you don't
[1982.80 → 1985.18] need any, almost zero
[1985.18 → 1986.94] knowledge about the front
[1986.94 → 1987.96] end development.
[1988.50 → 1990.20] If you know how to stack up
[1990.20 → 1992.10] the HTML like tags, then
[1992.10 → 1992.90] you're good to go.
[1993.26 → 1995.48] But then while we were
[1995.48 → 1997.26] creating the tool, we made
[1997.26 → 1999.82] it is extensible in a way that
[1999.82 → 2001.04] you can create your own
[2001.04 → 2001.62] components.
[2002.60 → 2004.26] So for example, if we don't
[2004.26 → 2006.04] have right now support for
[2006.04 → 2008.62] the video, you can create
[2008.62 → 2010.54] your own components to
[2010.54 → 2012.74] render video and connect
[2012.74 → 2014.44] it to, for example, check
[2014.44 → 2015.76] boxes that you can use for
[2015.76 → 2016.30] classification.
[2017.08 → 2019.22] So in most cases, we try to
[2019.22 → 2021.50] cover, I would say, 80% of
[2021.50 → 2023.46] the most common cases with
[2023.46 → 2024.26] the components that we
[2024.26 → 2025.10] develop ourselves.
[2025.52 → 2026.88] But then we also give you an
[2026.88 → 2028.74] ability to extend it for your
[2028.74 → 2029.50] particular needs.
[2030.50 → 2032.28] So if you're, you know, kind
[2032.28 → 2033.26] of extending that a little
[2033.26 → 2034.54] bit, if you're a data
[2034.54 → 2035.80] scientist or an AI
[2035.80 → 2037.46] developer, and you're
[2037.46 → 2039.28] trying to integrate Label
[2039.28 → 2041.10] Studio into your own data
[2041.10 → 2043.06] pipeline and pull data out
[2043.06 → 2044.60] for experimentation, how does
[2044.60 → 2046.14] that integration go?
[2046.40 → 2047.50] You know, and maybe draw an
[2047.50 → 2048.70] example or something like,
[2048.82 → 2049.70] you know, you're using a
[2049.70 → 2051.26] notebook with TensorFlow or,
[2051.40 → 2052.36] you know, whatever, PyTorch.
[2052.80 → 2054.46] And how does that look from a
[2054.46 → 2055.94] practical standpoint if I'm
[2055.94 → 2057.00] going to sit down and use the
[2057.00 → 2057.20] tool?
[2057.42 → 2057.58] Yeah.
[2057.84 → 2059.20] So from the notebook
[2059.20 → 2061.16] example, we will be releasing
[2061.16 → 2063.72] the package specifically for the
[2063.72 → 2065.80] Python notebook that will make it
[2065.80 → 2068.26] super easy to initialize Label
[2068.26 → 2069.48] Studio inside the Python
[2069.48 → 2071.16] notebook and work with that.
[2071.36 → 2072.52] If you're looking into
[2072.52 → 2074.06] integrating it into your
[2074.06 → 2075.92] workflow, you would need to
[2075.92 → 2077.42] install the NPM package.
[2078.08 → 2078.88] You would just need to
[2078.88 → 2081.18] initialize that with the data
[2081.18 → 2082.22] from your data set.
[2083.04 → 2085.36] And then you create kind of a
[2085.36 → 2088.56] UI, how to visualize this data
[2088.56 → 2090.46] and how to label it.
[2090.46 → 2092.94] So basically, we split up the
[2092.94 → 2094.18] components that you have in
[2094.18 → 2096.28] Label Studio into two major
[2096.28 → 2096.76] ways.
[2097.12 → 2098.72] Those that are used to visualize
[2098.72 → 2100.46] the data and those that are used
[2100.46 → 2101.82] to label it.
[2102.30 → 2104.38] So you can think about it that if
[2104.38 → 2105.48] you're looking at the text
[2105.48 → 2107.30] documents, that's visualizing
[2107.30 → 2107.78] text.
[2108.36 → 2110.10] And then if you want to put the
[2110.10 → 2112.00] spans on the text doing name
[2112.00 → 2113.68] identity recognition, that's
[2113.68 → 2115.50] another tag that is doing just
[2115.50 → 2116.08] that action.
[2116.08 → 2118.76] And you're also able to create
[2118.76 → 2121.86] to load your predictions from
[2121.86 → 2123.34] your current models if you have
[2123.34 → 2123.72] those.
[2124.40 → 2126.24] And you can also complete
[2126.24 → 2128.14] labelling in different ways.
[2128.62 → 2130.14] So for example, if you want to
[2130.14 → 2131.74] have multiple people look at the
[2131.74 → 2134.46] same text and let them label it,
[2134.92 → 2136.90] you'll have two different results
[2136.90 → 2138.28] and then you can compare those
[2138.28 → 2138.72] results.
[2138.90 → 2140.82] And that kind of pushing of
[2140.82 → 2143.08] predictions into the tool or
[2143.08 → 2145.48] let's say, like for my training
[2145.48 → 2147.34] script, I want to pull the latest
[2147.34 → 2149.42] annotations out.
[2149.58 → 2150.96] I saw you mention some things
[2150.96 → 2153.32] about maybe a REST interface or
[2153.32 → 2153.96] something like that.
[2154.06 → 2155.60] Or like how does that interaction
[2155.60 → 2157.30] work and the sort of the plumbing
[2157.30 → 2158.32] between the two?
[2158.42 → 2159.88] Once you've got Label Studio up
[2159.88 → 2161.48] and running, what's the most
[2161.48 → 2163.40] useful way of plumbing between an
[2163.40 → 2165.74] annotation tool and your
[2165.74 → 2167.76] training and inference in your
[2167.76 → 2168.24] experience?
[2169.12 → 2170.14] Again, two ways.
[2170.28 → 2172.22] First one, where we provide just
[2172.22 → 2173.36] the front end part, right?
[2173.42 → 2174.72] It's basically NPM.
[2174.72 → 2176.48] It's JavaScript package.
[2177.38 → 2181.70] And you initialize the package and
[2181.70 → 2183.88] you send the data into the package.
[2184.12 → 2185.20] So there is basically, there is no
[2185.20 → 2185.94] API, nothing.
[2186.48 → 2187.72] It's as simple as that.
[2188.50 → 2191.04] And there is second part where we
[2191.04 → 2193.12] provide you with the data manager
[2193.12 → 2196.52] and we initialize the Label Studio
[2196.52 → 2197.48] front end for you.
[2197.48 → 2201.36] So in that case, you just give us,
[2201.70 → 2203.48] give Label Studio the JSON
[2203.48 → 2206.48] formatted file, and we read the data
[2206.48 → 2207.02] from there.
[2207.02 → 2207.86] Cool.
[2208.18 → 2208.44] Yeah.
[2208.86 → 2211.60] This is still reasonably new in that
[2211.60 → 2212.88] you were just in the Himalayas
[2212.88 → 2215.62] thinking about it, you know, a year
[2215.62 → 2216.00] ago.
[2216.18 → 2218.34] But actually, it seems like if I'm
[2218.34 → 2220.38] looking at the GitHub on Label Studio,
[2220.38 → 2223.08] it seems like there's been some
[2223.08 → 2225.68] activity there and there seems to be
[2225.68 → 2227.74] a bit of a community developing.
[2227.94 → 2229.00] Have you been able to get contributions
[2229.58 → 2231.94] of components and start to interact
[2231.94 → 2233.84] with the community in that context?
[2233.84 → 2234.56] Yeah.
[2235.32 → 2237.66] Community response thus far was great.
[2238.32 → 2240.32] And what people like about the Label
[2240.32 → 2243.24] Studio is that you can basically in
[2243.24 → 2245.90] 10 minutes, you can build your own
[2245.90 → 2246.88] data labelling tool.
[2247.38 → 2247.86] That's one.
[2248.34 → 2251.08] Second one is that the UI is very
[2251.08 → 2251.54] simple.
[2251.74 → 2253.26] So because you only use what you
[2253.26 → 2254.98] actually need for your particular
[2254.98 → 2257.34] data labelling needs, you only use
[2257.34 → 2260.64] those components and the UI is super
[2260.64 → 2261.08] simple.
[2261.68 → 2263.54] So there is nothing that you actually
[2263.54 → 2265.02] don't need in the UI.
[2265.72 → 2267.76] And as I have mentioned, it's the first
[2267.76 → 2269.36] data labelling tool that you can
[2269.36 → 2270.98] actually embed into your applications
[2270.98 → 2273.34] and you can easily extend.
[2274.10 → 2276.30] We are getting, right now, we are
[2276.30 → 2278.28] getting more bug reports than
[2278.28 → 2278.94] contributions.
[2279.54 → 2282.16] So contributions are always welcome.
[2282.82 → 2284.82] You know, for some reason that
[2284.82 → 2286.02] doesn't surprise me.
[2286.58 → 2287.10] Yeah.
[2287.42 → 2288.42] But it's a good thing.
[2288.68 → 2289.58] But it's a good thing.
[2289.66 → 2289.84] Yeah.
[2289.84 → 2291.84] Well, it can be a good thing.
[2293.38 → 2295.20] It's a track to make things better.
[2295.44 → 2297.00] So, you know, it sounds like a pretty
[2297.00 → 2297.58] great endeavour.
[2297.78 → 2299.74] I'm really, really looking forward to
[2299.74 → 2300.56] using it myself.
[2300.76 → 2302.20] And I'm pretty excited about it.
[2302.22 → 2303.72] So it's been a great conversation from
[2303.72 → 2304.22] my standpoint.
[2304.74 → 2307.26] I guess having brought it this far,
[2307.40 → 2309.62] all the way from the Himalayas to it is
[2309.62 → 2311.76] code that the rest of us out here can
[2311.76 → 2312.48] start utilizing.
[2313.12 → 2315.28] What do you see as some of the biggest
[2315.28 → 2318.10] open problems that are still out there
[2318.10 → 2320.24] in this data labelling space?
[2320.54 → 2322.92] And how do you see it being augmented
[2322.92 → 2325.52] in the future, either by your own team
[2325.52 → 2327.74] or by contributions from outside?
[2327.92 → 2328.98] You know, what's next?
[2329.64 → 2330.10] Sure.
[2330.32 → 2332.66] So I think there are many things
[2332.66 → 2333.58] happening right now.
[2333.80 → 2335.80] A few that I want to mention is that
[2335.80 → 2337.74] I personally think that moving forward,
[2337.94 → 2339.70] at least some part of the data labelling
[2339.70 → 2342.74] is going to be commoditized just because
[2342.74 → 2344.46] the models are getting better and better
[2344.46 → 2347.28] and you'll be able to reuse those models
[2347.28 → 2348.18] at some point.
[2348.58 → 2350.16] Maybe not right now, but soon.
[2350.58 → 2352.40] Then there is another trend with a weak
[2352.40 → 2355.70] supervision that you can also use
[2355.70 → 2357.22] to label your data set.
[2357.94 → 2360.76] And so I think what's coming next is
[2360.76 → 2363.48] we really need to start putting a lot of
[2363.48 → 2366.02] thinking into quality control.
[2366.66 → 2369.46] Because what a lot of companies that I talk to
[2369.46 → 2372.20] found out is that you outsource your data
[2372.20 → 2374.06] labelling, you get back the labels,
[2374.22 → 2375.84] they are of very low quality.
[2376.64 → 2378.68] And as a result, your models are failing
[2378.68 → 2379.48] in the real world.
[2380.04 → 2382.96] That's a very common and valid concern
[2382.96 → 2384.18] and happens actually a lot.
[2384.86 → 2387.66] So quality, how do we verify that
[2387.66 → 2389.48] the labels are of high quality?
[2389.96 → 2392.48] Another one is understanding and finding
[2392.48 → 2394.10] edge cases in your data sets
[2394.10 → 2396.54] and trying to understand how to label those.
[2397.16 → 2398.46] That's also very interesting because
[2398.46 → 2400.92] if you have real world data sets
[2400.92 → 2403.32] that consists of millions of images,
[2403.54 → 2406.32] there is no way you can look into each image
[2406.32 → 2407.38] by hand.
[2407.56 → 2409.68] You need some ways to automate that
[2409.68 → 2411.74] and pick those items for you
[2411.74 → 2414.66] that needs some attention.
[2414.66 → 2417.84] So I would say, at least from my standpoint,
[2417.98 → 2420.68] we're right now concentrating on the quality control a lot.
[2421.42 → 2422.74] Yeah, that makes a lot of sense.
[2422.84 → 2425.56] It sounds like there's no shortage of things
[2425.56 → 2427.84] to explore there and improve upon.
[2427.96 → 2429.80] But it does sound like actually
[2429.80 → 2433.96] AI augmentation of the labelling process,
[2434.40 → 2436.64] especially in terms of quality control
[2436.64 → 2438.88] and all of those things is going to be really important.
[2438.88 → 2441.06] So if people are listening
[2441.06 → 2443.40] and they want to try out Label Studio,
[2443.84 → 2446.82] they want to kind of follow you on this journey
[2446.82 → 2448.46] and as things come out,
[2448.74 → 2451.00] where can they find out more about Label Studio
[2451.00 → 2454.94] and maybe get started and try out a few things?
[2455.16 → 2456.08] And also maybe,
[2456.50 → 2457.80] what are some of the great ways
[2457.80 → 2460.40] that maybe people could contribute to Label Studio
[2460.40 → 2462.92] because you are getting those bug reports
[2462.92 → 2464.38] and other things?
[2464.38 → 2465.94] What are some of the ways
[2465.94 → 2468.24] that the community can give back as well?
[2468.38 → 2468.58] Sure.
[2468.76 → 2471.18] So I would say the easiest way
[2471.18 → 2474.34] that you can try out Label Studio right now
[2474.34 → 2477.98] is NPM install label slash studio.
[2478.72 → 2482.80] But then labelstud.io is our website
[2482.80 → 2484.22] and GitHub.
[2484.58 → 2487.74] Yeah, it's GitHub.com slash hardback slash label studio.
[2488.28 → 2490.64] We have documentation there
[2490.64 → 2492.30] and some quick guides
[2492.30 → 2494.24] how you can start very quickly
[2494.24 → 2497.28] it's basically a couple lines of common line
[2497.28 → 2499.06] and you're up and running.
[2499.42 → 2500.36] With the contributions,
[2500.78 → 2505.36] yeah, you can open up the list of issues on GitHub
[2505.36 → 2508.40] with whatever you want to help us.
[2509.02 → 2510.38] We ideally are looking at
[2510.38 → 2513.46] if people are doing some sort of labelling themselves
[2513.46 → 2516.22] and we have not covered that cases yet,
[2516.58 → 2519.20] instead of building their own data labelling tool,
[2519.72 → 2522.90] they can contribute a component to Label Studio.
[2522.90 → 2526.74] So those contributions are very welcome,
[2527.44 → 2529.92] particularly in the 3D spaces,
[2530.14 → 2530.78] in videos.
[2531.24 → 2534.72] We have some work done on time series,
[2535.08 → 2537.18] but there is always more to be done.
[2537.78 → 2539.48] So yeah, that would be perfect ways.
[2539.48 → 2540.60] Awesome.
[2540.60 → 2540.74] Awesome.
[2541.12 → 2544.10] Well, thank you for taking some time
[2544.10 → 2545.04] during your travels
[2545.04 → 2548.14] to deep dive with us on data labelling
[2548.14 → 2550.34] and talk about a lot of these challenges
[2550.34 → 2552.20] and a lot of the great things you're doing
[2552.20 → 2554.16] at Hard and Label Studio.
[2554.54 → 2557.60] We'll definitely put those links in our show notes
[2557.60 → 2559.12] so people can find them.
[2559.12 → 2561.98] And I know I'll be coming back to my team
[2561.98 → 2564.18] to think about how we can get up
[2564.18 → 2567.44] a reading comprehension data labelling tool.
[2567.78 → 2567.80] Yeah.
[2568.44 → 2569.40] I was just going to say,
[2569.44 → 2571.02] he's given me hope for the future here.
[2573.10 → 2575.52] There is hope in the midst of data labelling.
[2576.26 → 2577.36] A long way to go.
[2577.46 → 2578.18] A long way to go.
[2578.66 → 2579.02] Yeah.
[2579.14 → 2579.32] Yeah.
[2579.32 → 2580.52] Still a long ways to go,
[2580.68 → 2582.36] but it's encouraging to know
[2582.36 → 2584.38] that people are working in this space
[2584.38 → 2587.22] and also that there's kind of a modular approach
[2587.22 → 2588.78] where we can build up components.
[2589.06 → 2590.12] That's really exciting.
[2590.68 → 2592.52] So thank you so much for joining us.
[2592.74 → 2594.30] It was really, really great to talk to you
[2594.30 → 2595.96] and hope to run into you sometime
[2595.96 → 2597.32] at a conference or somewhere.
[2597.46 → 2598.10] Thanks very much, Ami.
[2598.56 → 2599.32] Thanks a lot.
[2601.68 → 2602.22] All right.
[2602.28 → 2604.88] Thank you for tuning into this episode of Practical AI.
[2605.12 → 2605.92] If you enjoyed the show,
[2605.98 → 2606.60] do us a favour,
[2606.72 → 2607.26] go on iTunes,
[2607.44 → 2608.10] give us a rating,
[2608.38 → 2610.24] go in your podcast app and favourite it.
[2610.24 → 2612.06] If you are on Twitter or a social network,
[2612.16 → 2613.06] share a link with a friend,
[2613.14 → 2613.82] whatever you got to do,
[2613.96 → 2615.50] share the show with a friend if you enjoyed it.
[2615.80 → 2618.46] And bandwidth for Changelog is provided by Vastly.
[2618.58 → 2620.02] Learn more at Fastly.com.
[2620.20 → 2621.14] And we catch our errors
[2621.14 → 2622.58] before our users do here at Changelog
[2622.58 → 2623.42] because of Rollbar.
[2623.64 → 2626.02] Check them out at rollbar.com slash Changelog.
[2626.34 → 2628.84] And we're hosted on Linde Cloud servers.
[2628.84 → 2630.80] Head to linode.com slash Changelog.
[2630.90 → 2631.36] Check them out.
[2631.42 → 2632.26] Support this show.
[2632.66 → 2635.12] This episode is hosted by Daniel Whiten ack
[2635.12 → 2635.84] and Chris Benson.
[2636.30 → 2638.36] The music is by Break master Cylinder.
[2638.36 → 2640.66] And you can find more shows just like this
[2640.66 → 2642.18] at ChangeLog.com.
[2642.26 → 2643.04] When you go there,
[2643.12 → 2644.32] pop in your email address,
[2644.58 → 2645.54] get our weekly email,
[2645.66 → 2647.14] keeping you up to date with the news
[2647.14 → 2648.46] and podcasts for developers
[2648.46 → 2650.64] in your inbox every single week.
[2651.00 → 2651.82] Thanks for tuning in.
[2651.94 → 2652.68] We'll see you next week.
[2652.68 → 2653.90] Bye-bye.
[2653.90 → 2654.30] Bye-bye.
[2654.48 → 2654.68] Bye-bye.
[2654.90 → 2656.10] Bye-bye.
[2656.58 → 2657.36] Bye-bye.
[2663.50 → 2664.16] Bye-bye.
[2665.14 → 2665.20] Bye-bye.
[2665.22 → 2665.28] Bye-bye.
[2665.30 → 2665.66] Bye-bye.
[2665.88 → 2666.32] Bye-bye.
[2666.40 → 2667.48] Bye-bye.
[2667.48 → 2669.34] Bye-bye.
[2669.68 → 2669.98] Bye-bye.
[2669.98 → 2670.52] Bye-bye.
[2670.52 → 2671.04] Bye-bye.
[2671.04 → 2671.48] Bye-bye.
[2671.48 → 2671.60] Bye-bye.
[2671.70 → 2672.00] Bye-bye.
[2672.26 → 2672.62] Bye-bye.
[2674.76 → 2675.12] Bye-bye.
[2675.12 → 2675.56] Bye-bye.
[2675.56 → 2676.58] Bye-bye.
[2676.58 → 2677.02] Bye-bye.
[2677.08 → 2677.84] Bye-bye.
[2677.84 → 2678.18] Bye-bye.
[2678.18 → 2678.62] Bye-bye.
[2678.62 → 2681.08] Bye-bye.
[2681.08 → 2682.08] Bye-bye.
[2682.08 → 2682.48] Bye-bye.
