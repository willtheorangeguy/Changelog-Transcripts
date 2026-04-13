[0.00 → 2.52] This is about the community and the capacity, right?
[2.70 → 5.98] And we are acting as what we call a collaborative agency,
[6.34 → 9.44] providing those resources and supporting the community
[9.44 → 11.64] to be helpful to their end users.
[11.64 → 15.70] For us, the success of us is basically the success of those end users
[15.70 → 17.02] who are building those applications.
[17.18 → 20.68] So if they're more efficient, more productive in deploying solutions
[20.68 → 23.08] into their community, we are successful
[23.08 → 24.92] because we have been able to empower them.
[25.00 → 26.82] That's really how we look at this ecosystem.
[30.00 → 32.84] Big thanks to our partners, Linde, Vastly, and Launch Darkly.
[33.04 → 35.26] We love Linde. They keep it fast and simple.
[35.40 → 37.76] Check them out at linode.com slash changelog.
[37.98 → 40.06] Our bandwidth is provided by Vastly.
[40.06 → 43.96] Learn more at Fastly.com and get your feature flags powered by Launch Darkly.
[44.12 → 45.94] Get a demo at LaunchDarkly.com.
[48.70 → 52.20] This episode is brought to you by me, myself, and AI.
[52.52 → 55.42] It's a podcast on artificial intelligence and business
[55.42 → 58.36] and it's produced by our friends at MIT Sloan Management Review
[58.36 → 59.86] and Boston Consulting Group.
[60.00 → 63.02] The question is, why do only 10% of companies succeed
[63.02 → 64.32] with artificial intelligence?
[64.84 → 66.78] That's the question they aim to answer with this podcast.
[67.38 → 70.92] Here's Google Cloud's Will Grannies on an unusual AI challenge.
[71.26 → 73.28] When I think about what AI is,
[73.52 → 75.38] I find the algorithms mathematically fascinating,
[75.60 → 78.62] but I find the use of the algorithms far more fascinating
[78.62 → 80.54] because from a technical perspective,
[81.14 → 85.78] we're finding correlations in extremely high dimensional nonlinear spaces.
[86.10 → 88.32] It's statistics at scale in some sense, right?
[88.32 → 90.80] We're finding these correlations between A and B.
[90.94 → 92.62] And those algorithms are fascinating
[92.62 → 94.34] and I'm still teaching those now, and they're fun.
[94.82 → 97.16] But what's more interesting to me is
[97.16 → 99.00] what do those correlations mean for the people?
[99.52 → 99.82] All right.
[99.90 → 101.60] Me, myself, and AI is a collaboration between
[101.60 → 104.50] MIT Sloan Management Review and Boston Consulting Group.
[104.84 → 106.24] It's available wherever you get your podcasts.
[106.38 → 108.70] Just search me, myself, and AI.
[108.70 → 128.84] Welcome to Practical AI,
[129.20 → 132.26] a weekly podcast that makes artificial intelligence practical,
[132.58 → 134.36] productive, and accessible to everyone.
[134.68 → 137.58] This is where conversations around AI, machine learning,
[137.58 → 138.76] and data science happen.
[139.00 → 142.28] Join the community and Slack with us around various topics of the show
[142.28 → 145.12] at changelog.com slash community and follow us on Twitter.
[145.26 → 146.56] We're at Practical AI.
[152.98 → 156.32] Well, welcome to another episode of Practical AI.
[156.68 → 158.48] This is Daniel Whiten ack.
[158.60 → 161.98] I'm a data scientist with SIL International,
[161.98 → 165.16] and I'm joined as always by my co-host, Chris Benson,
[165.40 → 168.20] who is a tech strategist at Lockheed Martin.
[168.74 → 169.46] How are you doing, Chris?
[169.58 → 170.24] Very well, Daniel.
[170.30 → 170.84] How are you today?
[170.96 → 173.04] I am doing wonderful.
[173.24 → 177.32] I'm blessed and pretty excited because if you remember, Chris,
[177.40 → 181.22] we had a wonderful conversation not too long ago
[181.22 → 184.50] in a new podcast series that we were launching.
[184.88 → 187.72] This podcast series is sort of a collaboration
[187.72 → 190.76] with the Open for Good Alliance,
[190.96 → 193.66] which is a sort of multi-stakeholder group
[193.66 → 198.46] that is working to create localized training data,
[198.88 → 200.26] which is one of the major obstacles
[200.26 → 203.68] for local AI innovation in Africa and Asia.
[204.14 → 206.48] And we're kind of having this podcast series
[206.48 → 209.00] with that Open for Good Alliance
[209.00 → 212.10] to spotlight some of the things that are going on
[212.10 → 213.92] with AI in Africa.
[213.92 → 219.92] Last time we talked with Joyce Named from the Carrera Lab,
[220.52 → 222.20] and Joyce is back with us today.
[222.32 → 222.88] Welcome, Joyce.
[222.96 → 223.62] Thank you, Daniel.
[223.86 → 224.88] Nice to be here.
[225.06 → 227.26] I am very excited about another podcast
[227.26 → 229.60] talking about AI in Africa
[229.60 → 232.10] and featuring another organization
[232.10 → 234.34] that's doing a lot of work in making sure
[234.34 → 237.26] that we have AI data available
[237.26 → 239.06] for male communities in Africa.
[239.74 → 241.90] I'm so excited that you've joined us again.
[242.06 → 243.78] It was a wonderful conversation before,
[243.92 → 245.26] and now we get to welcome you back
[245.26 → 248.70] as sort of co-host with us in this podcast,
[248.92 → 250.00] which is wonderful.
[250.56 → 254.94] So yeah, if you could maybe introduce our guests
[254.94 → 256.60] and the topic for the episode,
[256.60 → 258.86] and then we'll jump into some of the great things
[258.86 → 259.38] that they're doing.
[259.50 → 260.40] Yeah, thank you, Daniel.
[260.56 → 263.76] So today we are very excited to host two people
[263.76 → 266.22] from the Radiant Earth Foundation.
[266.88 → 269.98] We have Ahmed, Mohammed, and Abba Bade,
[269.98 → 271.96] who are going to talk to us
[271.96 → 273.84] about the work that they're doing
[273.84 → 276.32] around AI data collection challenges,
[276.74 → 279.10] especially looking at machine learning
[279.10 → 280.38] for Earth observation.
[280.64 → 282.30] And they're going to give us the perspective
[282.30 → 284.02] that they have, what they do,
[284.42 → 285.86] how they work with the community,
[285.86 → 290.16] and especially around the capacity building initiatives
[290.16 → 291.24] that they're involved in.
[291.48 → 293.60] And just to say that I have worked with Ahmed before
[293.60 → 294.26] in the past.
[294.38 → 296.10] So this is, you know, very refreshing
[296.10 → 298.42] to have another conversation with him today
[298.42 → 299.74] on this podcast.
[300.08 → 302.16] So Ahmed and Abba, you're very welcome.
[302.74 → 304.94] And we are very excited to listen from you
[304.94 → 307.08] and to learn about the work that Radiant Earth
[307.08 → 309.42] is doing in the AI space
[309.42 → 311.16] around the Open for Good initiative.
[311.60 → 312.90] Ahmed, you're very welcome.
[313.32 → 313.90] Hello, everyone.
[314.14 → 315.56] I'm excited to be here.
[315.88 → 318.08] Thank you, Joyce and Daniel and Chris
[318.08 → 319.22] for having us in this episode.
[319.60 → 321.28] Yeah, we're excited to hear more
[321.28 → 322.10] about what you're doing.
[322.10 → 324.32] Could you give us maybe a little bit
[324.32 → 327.64] of the sort of wider context of, you know,
[327.76 → 329.22] why Earth observation,
[329.60 → 332.28] why machine learning as related
[332.28 → 335.22] to the sustainable development goals?
[335.48 → 336.90] Yeah, so let me start with
[336.90 → 338.54] sustainable development goals,
[338.66 → 341.00] or as we always abbreviated, SDGs.
[341.30 → 343.40] These are a set of goals that were set
[343.40 → 345.66] by United Nations back in 2015
[345.66 → 348.04] with a set of targets for 2030.
[348.48 → 350.98] These goals talk about hunger, poverty,
[350.98 → 353.10] access to clean water and sanitation,
[353.54 → 356.32] climate action, life on land, sustainable cities.
[356.46 → 358.44] And basically there are 17 of them
[358.44 → 359.64] that tackle different aspects
[359.64 → 360.94] of a sustainable society.
[361.48 → 363.12] And each country is basically
[363.12 → 364.66] progressing toward those goals
[364.66 → 366.10] depending on where they start with.
[366.42 → 367.70] And they have to regularly monitor
[367.70 → 369.32] and basically report
[369.32 → 370.88] where they are with that target.
[371.24 → 373.16] Where Earth observation comes in is
[373.16 → 375.96] we have this massive number of satellites
[375.96 → 377.32] orbiting the Earth
[377.32 → 379.76] and capturing measurements on a regular basis.
[379.76 → 381.94] These data can be translated
[381.94 → 383.78] into those targets and variables
[383.78 → 385.24] that the countries need to report
[385.24 → 387.00] and also helping those countries
[387.00 → 388.66] to better monitor their progress
[388.66 → 390.58] and see where they put their efforts.
[391.02 → 392.72] Naturally, because you have a lot of data,
[392.82 → 394.78] that's where the AI and ML aspect comes in
[394.78 → 396.46] because you're dealing with
[396.46 → 398.48] basically flow of data,
[398.64 → 399.78] a continuous flow of data
[399.78 → 400.60] from these satellites.
[400.94 → 402.80] It is real big data problem.
[402.96 → 404.70] It is not just a toy big data problem
[404.70 → 406.16] because we are dealing with petabytes
[406.16 → 407.62] of data on a daily scale
[407.62 → 409.34] when you think about global scale.
[409.78 → 411.56] And that's where AI can help you
[411.56 → 412.58] derive insights,
[412.88 → 414.62] get those target numbers out,
[414.94 → 417.18] and provide support for decision makers
[417.18 → 418.58] to be more effective
[418.58 → 420.98] and affect the society down the road.
[421.42 → 423.28] So maybe Chris knows this
[423.28 → 425.90] because of his work in aerospace
[425.90 → 427.02] and other fields.
[427.42 → 428.74] But if I'm thinking of,
[428.96 → 431.18] okay, I understand the concept
[431.18 → 432.82] that there are many satellites
[432.82 → 434.78] taking pictures of the Earth.
[434.78 → 436.56] Like if I was a data scientist,
[437.18 → 439.32] like I'm not running the satellites.
[439.56 → 440.46] I don't really know,
[440.52 → 442.58] like I know how to access Google Maps
[442.58 → 444.78] or Google Earth or something like that.
[445.02 → 447.86] But like, could you explain a little bit of
[447.86 → 450.28] like who runs these satellites?
[450.66 → 451.66] Where are the images?
[452.06 → 454.72] How are they aggregated and accessed
[454.72 → 455.90] and that sort of thing?
[456.02 → 456.64] Good question.
[456.86 → 458.44] So there are two big players
[458.44 → 460.12] in this operation side.
[460.52 → 461.18] There are governments
[461.18 → 463.62] that operate many, many large satellites.
[463.62 → 465.00] The US side, we have NASA.
[465.14 → 465.90] And the European side,
[465.98 → 467.40] we have the European Space Agency.
[467.88 → 470.10] We have Japanese Space Agency, JAVA.
[470.22 → 471.62] We have Indian Aerospace Agency.
[471.76 → 472.82] Many of national countries
[472.82 → 474.08] have their own space agency
[474.08 → 475.66] that they operate satellites.
[476.58 → 478.28] Historically, the US and Europe
[478.28 → 479.78] have been the kind of bigger ones
[479.78 → 481.18] in terms of the government sector.
[481.68 → 484.00] Then there is a growing commercial sector
[484.00 → 486.50] that is operating their own fleet of satellites.
[486.94 → 488.54] And they have been kind of booming
[488.54 → 489.46] the last, I would say,
[489.52 → 491.00] 10 to 15 years particularly.
[491.00 → 493.52] And they provide a different suite of satellites
[493.52 → 494.70] and their data sets.
[495.10 → 496.96] Almost everybody is moving to the cloud.
[497.08 → 497.82] Let's put it that way,
[497.88 → 498.98] where the data sits now.
[499.24 → 500.82] Commercials are providing the data
[500.82 → 501.52] through the cloud.
[501.92 → 504.68] Governments have their own kind of data stores
[504.68 → 506.66] and kind of portals
[506.66 → 508.08] that you can access the data from.
[508.18 → 509.34] But they are also now working
[509.34 → 511.08] very closely with cloud providers,
[511.20 → 512.20] all the major ones.
[512.62 → 513.96] And you as a data user
[513.96 → 516.26] can go to those basically cloud buckets,
[516.74 → 517.84] start exploring the data.
[517.84 → 520.12] There are APIs that you can start query
[520.12 → 521.18] and search for imagery.
[521.66 → 523.92] The government data is usually open
[523.92 → 525.42] in the sense that you don't pay
[525.42 → 527.06] for the imagery to access it.
[527.34 → 527.82] But at the end,
[527.84 → 530.08] you should have your own capacity
[530.08 → 531.74] and resources and machine
[531.74 → 532.76] to receive the data.
[533.32 → 534.94] Commercials have paid data
[534.94 → 536.64] on the kind of regular basis,
[536.76 → 537.62] but they also have,
[537.98 → 538.62] at least I would say,
[538.68 → 540.44] major commercials have that.
[540.64 → 541.34] They have a disaster
[541.34 → 542.68] kind of open data program.
[542.78 → 543.74] When there is a problem,
[544.02 → 545.36] a kind of immediate situation,
[545.36 → 546.42] they release open data
[546.42 → 547.88] for disaster response.
[547.96 → 549.28] They also have research programs
[549.28 → 550.58] that academics and researchers
[550.58 → 552.40] can get kind of a quota
[552.40 → 554.12] to access some level of free imagery.
[554.64 → 556.24] So yeah, data is now moving to the cloud.
[556.38 → 557.92] That's really the paradigm shift.
[558.14 → 558.62] Given that you have
[558.62 → 559.76] all these different providers
[559.76 → 560.64] with, you know,
[560.68 → 562.26] and that when they put the satellite up,
[562.28 → 563.36] obviously they are,
[563.64 → 565.18] they have their own objectives
[565.18 → 566.56] on what they care about,
[566.66 → 567.02] what, you know,
[567.04 → 568.60] what the satellite is designed to collect,
[569.04 → 571.00] and that it's not necessarily standardized
[571.00 → 573.16] across all of those different programs.
[573.16 → 575.14] How do you go about thinking
[575.14 → 577.50] about getting a usable data set
[577.50 → 578.32] from your standpoint,
[578.32 → 580.34] from all those different sources
[580.34 → 581.72] and knowing where to go
[581.72 → 584.12] and how to put data sets together?
[584.32 → 585.24] It seems like it would be
[585.24 → 586.44] a bit of a logistics challenge.
[586.64 → 587.62] It is a logistic challenge.
[587.70 → 588.02] And actually,
[588.42 → 589.36] this is one of the things
[589.36 → 591.74] that Radiant started to kind of act
[591.74 → 592.36] in that sector
[592.36 → 594.12] and provide support to the community.
[594.32 → 596.28] So think about you as a user
[596.28 → 597.38] are looking for
[597.38 → 598.76] what we call optical imagery.
[598.90 → 600.50] Optical imagery is like an image
[600.50 → 601.86] that you get with your cell phone,
[601.86 → 602.48] but in this case,
[602.54 → 603.84] it's captured by a satellite
[603.84 → 606.02] from like a couple of hundred kilometres
[606.02 → 607.40] into the Earth orbit, right?
[607.64 → 608.86] This is typically what you see
[608.86 → 610.06] in a Google-based map,
[610.14 → 610.80] Apple-based map,
[610.80 → 612.74] or any other kind of mapping ecosystem
[612.74 → 613.54] that you work with.
[613.78 → 615.32] If you're looking for a specific image
[615.32 → 615.88] over an area,
[615.98 → 616.96] you will go to an API
[616.96 → 618.42] and query for that image, right?
[618.50 → 620.26] The problem a couple of years ago
[620.26 → 621.70] was that each provider
[621.70 → 623.32] had their own API definition
[623.32 → 625.08] and how they would record
[625.08 → 627.10] what we call metadata of that image.
[627.18 → 628.46] What is the cloud cover in there?
[628.52 → 629.60] What is the spatial bound?
[629.70 → 630.80] What is the time tag?
[630.80 → 632.88] We, as a neutral agency
[632.88 → 633.88] in the community said,
[633.98 → 634.94] hey, this is a problem.
[635.08 → 635.76] Let's get together
[635.76 → 637.48] and come up with a standard way
[637.48 → 638.72] of cataloguing our data.
[639.26 → 640.60] And this is what we have now
[640.60 → 642.72] as spatial temporal asset catalogue
[642.72 → 643.42] or stack,
[643.78 → 645.64] which is a standard specification,
[646.08 → 646.80] open source
[646.80 → 648.08] and fully community driven
[648.08 → 650.00] that defines how you're going
[650.00 → 651.16] to build your data catalogue
[651.16 → 652.62] and expose it to the end user.
[653.18 → 654.14] So now everybody
[654.14 → 655.24] who contributed to that,
[655.30 → 656.76] which is around 25 organizations
[656.76 → 658.00] are adopting that standard
[658.00 → 659.68] because they tested out,
[659.74 → 660.58] they provided feedback,
[660.58 → 661.68] and it's now becoming
[661.68 → 662.62] the universal way
[662.62 → 664.40] of searching geospatial data sets.
[664.62 → 665.86] All the major data providers
[665.86 → 666.86] are now adopting that
[666.86 → 668.04] and we at Radiant
[668.04 → 669.44] use it for our own data store.
[669.74 → 670.10] Yeah, Ahmed,
[670.24 → 671.14] just a quick question.
[671.32 → 672.22] So for example,
[672.22 → 673.42] if I wanted to have access
[673.42 → 674.08] to the data
[674.08 → 674.58] and you're saying
[674.58 → 675.86] you came in as a middle player
[675.86 → 676.78] to try and, you know,
[676.82 → 677.98] provide the standardization
[677.98 → 679.28] for access of this data.
[679.72 → 681.48] So where is this data stored?
[681.58 → 683.08] How can someone have access to it?
[683.12 → 684.10] Is it that easy
[684.10 → 685.66] that now we don't have to contact
[685.66 → 687.50] all the different asset-like providers,
[687.50 → 689.02] but go through Radiant Earth
[689.02 → 689.62] to have access
[689.62 → 690.74] to that kind of data?
[691.32 → 691.48] Yeah.
[691.64 → 692.86] So on our end,
[692.98 → 693.72] what we provide
[693.72 → 695.52] is specifically AI
[695.52 → 696.56] and ML ready data,
[696.68 → 697.36] not necessarily
[697.36 → 698.62] any satellite imagery.
[699.18 → 700.76] So Radiant basically
[700.76 → 702.04] is working in this sector,
[702.32 → 703.96] but providing those
[703.96 → 704.78] kind of benchmark
[704.78 → 706.04] training data sets
[706.04 → 707.24] that the user needs
[707.24 → 708.46] to build a machine learning model.
[708.46 → 709.36] So we don't necessarily
[709.36 → 710.78] provide the raw satellite imagery
[710.78 → 712.04] for anywhere on the Earth,
[712.38 → 713.86] but we have a data repository
[713.86 → 715.08] with a stack API
[715.08 → 715.94] and a catalogue
[715.94 → 717.56] that anybody can access.
[717.68 → 718.50] So it's open access
[718.50 → 719.26] for everyone
[719.26 → 720.42] that you can come
[720.42 → 721.18] and search for.
[721.32 → 721.92] Oh, I'm looking
[721.92 → 723.78] for a labelled data set
[723.78 → 724.62] of, for example,
[725.06 → 726.92] land cover classes in Kenya.
[727.16 → 728.56] And you can query our database
[728.56 → 731.02] and find the corresponding labels
[731.02 → 732.06] and the source imagery,
[732.24 → 732.84] which is usually
[732.84 → 733.62] from a satellite.
[734.10 → 735.30] Sometimes we also have drone,
[735.72 → 736.62] but the majority of them
[736.62 → 737.24] are satellites.
[737.24 → 739.10] Then you can use that data set
[739.10 → 740.34] to fit it into a
[740.34 → 741.92] machine learning training pipeline
[741.92 → 743.02] and build a model for,
[743.08 → 743.48] for example,
[743.58 → 744.56] land cover classification.
[744.90 → 745.12] But yeah,
[745.16 → 746.82] we have those type of data sets.
[747.24 → 748.28] Our repository is called
[748.28 → 749.36] Radiant ML Hub.
[749.60 → 750.52] And as that name says,
[750.64 → 751.78] it's a hub basically
[751.78 → 753.30] for this kind of resources.
[753.84 → 754.12] So far,
[754.16 → 755.84] we have been pretty much focused
[755.84 → 757.36] on training data sets,
[757.46 → 758.60] but we have recently launched
[758.60 → 760.18] our model repository as well,
[760.46 → 761.78] which I can talk later about it.
[762.00 → 764.00] So I'm curious as a practitioner,
[764.28 → 765.72] maybe you can go to Abba.
[765.72 → 767.84] Going from this sort of stack
[767.84 → 769.12] that's very specific
[769.12 → 769.90] and specialized
[769.90 → 770.80] to the sort of
[770.80 → 771.70] Earth observation,
[772.10 → 773.98] satellite imagery world,
[774.20 → 775.62] and kind of taking that
[775.62 → 776.68] and then mapping it
[776.68 → 778.74] into the formats
[778.74 → 779.76] that, you know,
[779.84 → 781.94] AI and ML people like.
[782.26 → 783.60] What are some of the challenges
[783.60 → 784.24] with that
[784.24 → 785.68] and going from just sort of
[785.68 → 787.80] that raw satellite imagery
[787.80 → 791.62] down into actual training data sets
[791.62 → 793.26] that can be used with models?
[793.26 → 793.82] Okay.
[794.12 → 795.84] So some of the challenges
[795.84 → 798.40] which I faced while doing that is,
[798.86 → 801.90] so you have a vast amount of data, right?
[802.00 → 803.98] And making it ML ready
[803.98 → 805.44] might be a bit tricky
[805.44 → 806.30] because you need to work
[806.30 → 807.54] with data loaders
[807.54 → 809.26] and you need to find a way
[809.26 → 810.64] which you might have
[810.64 → 812.00] time series data now,
[812.22 → 814.48] time series Earth observations, right?
[814.56 → 816.56] And it gets a little bit tricky
[816.56 → 817.88] working with those as well.
[817.88 → 819.60] So on ML Hub,
[819.70 → 821.04] we actually have tutorials
[821.04 → 822.34] as to how you could use
[822.34 → 824.18] these ML ready data
[824.18 → 826.32] and you just pass them
[826.32 → 828.58] on to your model side of things
[828.58 → 830.06] that you train from there.
[830.06 → 846.58] Earlier in the show,
[846.64 → 847.16] you heard a teaser
[847.16 → 847.86] from our friends
[847.86 → 848.72] behind the podcast,
[848.88 → 850.52] me, myself, and AI.
[850.94 → 852.14] MIT Sloan Management Review
[852.14 → 853.42] and Boston Consulting Group
[853.42 → 853.90] came together
[853.90 → 855.22] to produce this awesome podcast
[855.22 → 856.82] and every episode,
[857.10 → 858.22] hosts Sam and Sherwin
[858.22 → 858.98] talk to the leaders
[858.98 → 860.42] that are engaged in the theory
[860.42 → 862.20] and the practice of AI.
[862.66 → 864.34] I remember one project we had,
[864.72 → 866.56] we were training a chatbot
[866.56 → 869.18] and it turned out we used raw,
[869.40 → 870.02] you know, logs,
[870.22 → 871.58] all privacy assured and everything,
[871.70 → 873.18] but we used these logs
[873.18 → 874.36] that a customer had provided
[874.36 → 875.66] because they wanted to see
[875.66 → 876.96] if we could build a better model.
[877.38 → 878.30] And it turns out
[878.30 → 879.26] that the chat agent
[879.26 → 881.18] wasn't exactly speaking
[881.18 → 882.02] the way we'd want
[882.02 → 882.76] another human being
[882.76 → 883.50] to speak to us.
[883.76 → 884.54] And why?
[884.82 → 886.42] Because people get pretty upset
[886.42 → 888.24] when they're talking
[888.24 → 889.64] to customer support
[889.64 → 891.28] and the language
[891.28 → 891.90] that they use
[891.90 → 893.04] isn't necessarily language
[893.04 → 893.88] I think we would use
[893.88 → 894.52] with each other,
[894.56 → 895.70] you know,
[895.70 → 896.50] on this podcast.
[897.06 → 897.28] All right.
[897.34 → 898.12] Me, myself, and AI
[898.12 → 898.70] is a collaboration
[898.70 → 900.38] between MIT Sloan Management Review
[900.38 → 901.98] and Boston Consulting Group.
[902.10 → 902.70] It's available
[902.70 → 903.72] wherever you get your podcasts.
[903.84 → 904.58] Just search me,
[904.82 → 905.36] myself,
[905.58 → 906.16] and AI.
[906.16 → 925.86] So I'm curious
[925.86 → 927.16] after thinking about
[927.16 → 928.48] this sort of data,
[928.72 → 929.50] what it can mean
[929.50 → 930.64] for training models.
[930.78 → 931.34] I was wondering
[931.34 → 932.74] maybe Joyce
[932.74 → 934.00] and the others,
[934.10 → 934.72] could you help us
[934.72 → 935.94] connect this specifically
[935.94 → 937.36] to problems
[937.36 → 938.38] that are being solved
[938.38 → 939.12] in Africa
[939.12 → 940.88] and the sort of
[940.88 → 942.60] the types of data sets
[942.60 → 943.54] with this imagery
[943.54 → 944.42] that are relevant
[944.42 → 945.52] to some of those things?
[945.98 → 946.32] Yeah, Daniel,
[946.42 → 947.42] I think that's a very
[947.42 → 948.64] important question
[948.64 → 949.94] because if I just look
[949.94 → 950.98] at one typical example,
[951.08 → 951.40] for example,
[951.40 → 952.24] I want to understand
[952.24 → 952.90] a major problem
[952.90 → 953.54] that we have
[953.54 → 954.38] around Africa,
[954.38 → 955.12] which is the problem
[955.12 → 956.40] of deforestation, right?
[956.48 → 957.08] So you know that
[957.08 → 958.54] forest cover is a very
[958.54 → 959.54] difficult thing.
[959.58 → 960.10] And if you're looking
[960.10 → 961.34] at maybe the authorities
[961.34 → 962.72] in the different countries,
[962.72 → 963.54] they want to understand
[963.54 → 964.52] what are the major drivers
[964.52 → 965.44] of deforestation,
[965.44 → 966.90] how is deforestation
[966.90 → 967.76] occurring in the
[967.76 → 968.56] different countries?
[969.08 → 970.46] I think one of the things
[970.46 → 971.26] that I would refer to
[971.26 → 972.38] is trying to look at this,
[972.62 → 973.18] for example,
[973.26 → 974.36] the earth observation data,
[974.46 → 975.46] looking at forest cover.
[975.84 → 976.30] Maybe Ahmed,
[976.40 → 977.92] is that a specific use case
[977.92 → 978.90] that you can talk about
[978.90 → 979.84] and how radiant earth
[979.84 → 980.84] can be able to provide us
[980.84 → 982.04] with the kind of data set
[982.04 → 982.96] that governments
[982.96 → 983.94] can be able to use
[983.94 → 984.76] to understand
[984.76 → 985.62] what's going on
[985.62 → 986.22] with the forests
[986.22 → 987.12] in the different countries
[987.12 → 987.70] in Africa?
[988.18 → 988.84] Yeah, that's a very
[988.84 → 989.96] good example, actually, Joyce.
[989.96 → 990.56] So, I mean,
[990.86 → 991.80] we know in the
[991.80 → 992.90] climate change world
[992.90 → 994.32] when we talk about
[994.32 → 995.86] mitigation strategies.
[995.86 → 996.62] One of them is
[996.62 → 997.86] being able to reduce
[997.86 → 999.62] the concentration of CO2
[999.62 → 1000.30] that we have emitted
[1000.30 → 1000.98] to the atmosphere.
[1001.10 → 1001.60] And that's what
[1001.60 → 1002.66] forests are about, right?
[1002.70 → 1003.40] So, forests are
[1003.40 → 1004.30] kind of absorbing
[1004.30 → 1005.06] many of those
[1005.06 → 1005.90] and sequestering
[1005.90 → 1006.74] all the carbon
[1006.74 → 1007.72] that we have emitted
[1007.72 → 1008.36] to the atmosphere.
[1008.36 → 1009.80] So, it's essential
[1009.80 → 1010.88] for all the governments
[1010.88 → 1011.80] at the national level
[1011.80 → 1012.80] and international level
[1012.80 → 1013.38] to make sure
[1013.38 → 1014.18] we can monitor
[1014.18 → 1015.36] forested areas
[1015.36 → 1016.52] and stop any
[1016.52 → 1017.82] illegal deforestation.
[1018.38 → 1019.24] So, satellite imagery
[1019.24 → 1020.44] is providing
[1020.44 → 1021.60] that regular observation
[1021.60 → 1022.32] over a region
[1022.32 → 1023.18] that is forested
[1023.18 → 1024.14] and how AI
[1024.14 → 1025.36] can help with that
[1025.36 → 1026.16] and how the things
[1026.16 → 1027.28] that we do can help is,
[1027.68 → 1028.22] oh, a government
[1028.22 → 1029.02] wants to build
[1029.02 → 1030.08] a monitoring system
[1030.08 → 1031.26] that would basically
[1031.26 → 1032.36] run an algorithm
[1032.36 → 1033.34] every time there's
[1033.34 → 1034.18] a new observation
[1034.18 → 1035.44] available from the satellite
[1035.44 → 1037.80] and detect the boundary,
[1038.06 → 1039.30] the kind of spatial boundary
[1039.30 → 1040.00] of where are
[1040.00 → 1040.98] the forested areas
[1040.98 → 1042.80] and provide an alert
[1042.80 → 1044.24] or a kind of anomaly detection
[1044.24 → 1045.02] in the ML world
[1045.02 → 1045.88] when you think about it
[1045.88 → 1046.16] that, hey,
[1046.20 → 1047.10] there was a change here
[1047.10 → 1047.84] with respect to
[1047.84 → 1048.26] the kind of
[1048.26 → 1049.18] previous observation.
[1049.56 → 1050.50] This can be at
[1050.50 → 1051.78] any kind of
[1051.78 → 1052.94] spatiotemporal scale
[1052.94 → 1053.72] that you think about
[1053.72 → 1054.34] because we have
[1054.34 → 1055.34] observations regularly
[1055.34 → 1055.82] available
[1055.82 → 1057.16] and they are available globally.
[1057.28 → 1058.02] That's the nice thing
[1058.02 → 1059.48] with the satellite imagery
[1059.48 → 1060.14] when you have
[1060.14 → 1061.06] a satellite orbiting,
[1061.22 → 1061.86] particularly those
[1061.86 → 1062.36] that we call
[1062.36 → 1064.06] in sun-synchronous orbit
[1064.06 → 1064.96] which are synced
[1064.96 → 1066.56] with the orbit of the sun.
[1066.84 → 1068.26] You get regular measurements
[1068.26 → 1068.92] over a region
[1068.92 → 1069.98] like every five days,
[1070.34 → 1071.34] 10 a.m.
[1071.34 → 1072.56] you get a regular observation
[1072.56 → 1073.74] and you get the same thing
[1073.74 → 1075.22] anywhere on the Earth.
[1075.62 → 1076.62] So, building those models
[1076.62 → 1077.32] is easier
[1077.32 → 1078.32] with that kind of
[1078.32 → 1079.96] constant type of observation.
[1080.48 → 1080.84] But at the end,
[1080.88 → 1081.96] the governments can use that
[1081.96 → 1084.04] and have a kind of strategy
[1084.04 → 1085.36] for how they want to
[1085.36 → 1086.58] basically stop that illegal
[1086.58 → 1087.70] kind of deforestation
[1087.70 → 1089.60] or have a monitoring system
[1089.60 → 1090.64] for protected areas,
[1090.74 → 1091.54] areas that have
[1091.54 → 1092.42] a specific boundary,
[1092.86 → 1093.94] nothing should happen there,
[1094.08 → 1095.70] no kind of construction,
[1096.26 → 1096.86] no built-up
[1096.86 → 1098.00] kind of things happening.
[1098.34 → 1099.78] They can have a monitoring system
[1099.78 → 1100.34] to do that.
[1100.66 → 1101.78] This is a very kind of
[1101.78 → 1102.76] impactful and I think
[1102.76 → 1103.76] tangible use case
[1103.76 → 1104.42] for many people
[1104.42 → 1105.18] who think about
[1105.18 → 1106.24] climate change
[1106.24 → 1107.22] and climate impacts.
[1107.46 → 1108.22] Yeah, so I guess
[1108.22 → 1109.36] then we can segue into
[1109.36 → 1110.30] the work that you do
[1110.30 → 1110.94] with the communities.
[1110.94 → 1111.86] I think that's a very
[1111.86 → 1113.32] important community problem,
[1113.40 → 1114.10] right, that you want
[1114.10 → 1114.64] to understand
[1114.64 → 1115.80] what's going on ground
[1115.80 → 1116.96] but you can also use
[1116.96 → 1118.16] the Earth observation data
[1118.16 → 1119.16] to be able to understand,
[1119.32 → 1119.70] for example,
[1119.82 → 1120.98] forest cover change
[1120.98 → 1121.80] or even just trying
[1121.80 → 1123.38] to understand the yield.
[1123.62 → 1124.12] If you're looking at,
[1124.22 → 1124.52] for example,
[1124.66 → 1125.56] farmlands in Uganda
[1125.56 → 1126.68] or farmlands in Kenya,
[1126.94 → 1127.86] how does Radiant Earth
[1127.86 → 1128.82] work with the community
[1128.82 → 1129.74] to be able to solve,
[1129.94 → 1130.94] especially the SDGs
[1130.94 → 1131.50] that you listed
[1131.50 → 1132.16] at the beginning?
[1132.28 → 1132.90] So how are these
[1132.90 → 1134.02] all connected around
[1134.02 → 1135.08] now working
[1135.08 → 1136.00] with the communities?
[1136.60 → 1138.14] Particularly on the community side,
[1138.24 → 1138.84] I think the role
[1138.84 → 1139.82] that Radiant plays
[1139.82 → 1141.24] is we don't want
[1141.24 → 1142.44] to be the problem solver
[1142.44 → 1143.40] because we are just
[1143.40 → 1144.20] one organization
[1144.20 → 1145.84] and problems are so diverse
[1145.84 → 1146.36] on the ground
[1146.36 → 1147.44] but we want to be,
[1147.56 → 1149.18] as we say in our mission statement,
[1149.32 → 1150.12] we want to empower
[1150.12 → 1151.06] those organizations
[1151.06 → 1151.72] and individuals
[1151.72 → 1153.16] in their local communities
[1153.16 → 1154.66] to be able to use
[1154.66 → 1155.34] these resources,
[1155.84 → 1157.32] particularly the benchmark
[1157.32 → 1157.98] data sets
[1157.98 → 1158.72] and guidelines
[1158.72 → 1159.34] and tutorials
[1159.34 → 1160.20] that we put out
[1160.20 → 1161.32] to solve those problems.
[1161.42 → 1162.56] So we work on use cases,
[1162.68 → 1163.58] we work hand in hand
[1163.58 → 1164.48] with some stakeholders
[1164.48 → 1165.24] and governments
[1165.24 → 1165.82] on the ground
[1165.82 → 1167.00] but at the end of the day,
[1167.06 → 1167.82] the goal is really
[1167.82 → 1168.56] empowering them
[1168.56 → 1169.94] to be able to do that themselves.
[1170.38 → 1171.36] That's how we kind of
[1171.36 → 1172.60] model our partnership
[1172.60 → 1173.48] and our collaboration
[1173.48 → 1174.62] with the local agencies
[1174.62 → 1176.06] but the crop example
[1176.06 → 1176.62] that you mentioned
[1176.62 → 1178.14] is another impactful one.
[1178.34 → 1179.24] About two years ago
[1179.24 → 1181.08] when we had the locust swarm
[1181.08 → 1182.62] hitting the East Africa region
[1182.62 → 1184.96] after all the kind of cyclones
[1184.96 → 1185.94] and the wet season
[1185.94 → 1186.74] that there was there,
[1187.08 → 1188.04] there were a couple of governments
[1188.04 → 1189.14] in the East Africa region
[1189.14 → 1189.88] that were looking,
[1189.88 → 1191.64] okay, what are we growing
[1191.64 → 1192.88] in terms of crops
[1192.88 → 1193.90] this season
[1193.90 → 1194.82] and where are they?
[1194.94 → 1195.88] Because they need to have
[1195.88 → 1197.46] an immediate response
[1197.46 → 1198.12] in terms of
[1198.12 → 1199.04] what will be the impact
[1199.04 → 1199.80] of those swarms
[1199.80 → 1200.88] and the food security,
[1201.34 → 1202.56] how much they need to import,
[1202.66 → 1203.28] what is the impact
[1203.28 → 1203.86] on farmers,
[1203.94 → 1204.56] should they provide
[1204.56 → 1205.38] any subsidy there?
[1205.70 → 1206.22] And governments,
[1206.36 → 1206.72] some of them,
[1206.78 → 1207.68] didn't have any
[1207.68 → 1209.28] basically updated map
[1209.28 → 1210.30] of cropland areas
[1210.30 → 1210.98] in their region
[1210.98 → 1212.30] because that is
[1212.30 → 1213.34] a very intensive process
[1213.34 → 1213.94] if you want to go
[1213.94 → 1214.34] on the ground
[1214.34 → 1215.70] and do census every year
[1215.70 → 1217.40] and provide basically
[1217.40 → 1218.82] a baseline map of that.
[1218.82 → 1219.58] But satellite imagery
[1219.58 → 1220.92] can do that for you.
[1221.22 → 1222.52] If you have good reference
[1222.52 → 1223.40] data on the ground,
[1223.48 → 1224.82] not necessarily a full census,
[1225.40 → 1225.90] you can build
[1225.90 → 1226.90] a machine learning model
[1226.90 → 1228.14] that look at the time series
[1228.14 → 1229.02] of Sentinel-2
[1229.02 → 1230.34] and then gives you
[1230.34 → 1231.96] basically a crop type
[1231.96 → 1233.24] of a region.
[1233.58 → 1234.70] And then you can have
[1234.70 → 1236.20] a map at the national scale
[1236.20 → 1236.78] that the government
[1236.78 → 1238.50] can use for decision-making
[1238.50 → 1240.12] and basically having
[1240.12 → 1240.92] a better insight
[1240.92 → 1242.04] into what are farmers
[1242.04 → 1243.08] growing in this region.
[1243.38 → 1244.82] And this is a growing field
[1244.82 → 1245.58] in the AI
[1245.58 → 1246.74] and remote sensing board.
[1246.74 → 1248.00] And I want to pass it
[1248.00 → 1248.78] to Abba because he's
[1248.78 → 1249.98] working on a problem
[1249.98 → 1251.68] around crop type classification
[1251.68 → 1252.54] and how we deal
[1252.54 → 1253.90] with actually regions
[1253.90 → 1254.56] that we don't have
[1254.56 → 1255.42] good reference data.
[1255.58 → 1256.30] Abba, it would be good
[1256.30 → 1257.50] if you can talk about
[1257.50 → 1258.94] the synthetic data problem.
[1259.56 → 1260.38] Because we have
[1260.38 → 1261.26] limited data
[1261.26 → 1263.06] in a lot of regions,
[1263.40 → 1265.14] so limited level data,
[1265.78 → 1266.94] so what we were able
[1266.94 → 1268.06] to work on is
[1268.06 → 1269.70] using GANs,
[1269.78 → 1271.60] generative adversarial networks,
[1271.60 → 1274.88] to generate an image
[1274.88 → 1275.92] for each of the bands
[1275.92 → 1277.48] of the satellite images.
[1278.06 → 1279.06] So assuming we have
[1279.06 → 1281.00] just 2,000 labelled images
[1281.00 → 1282.46] of different regions,
[1282.86 → 1283.86] we can now generate
[1283.86 → 1285.18] much more than 2,000
[1285.18 → 1286.12] based on the data
[1286.12 → 1287.04] which we have.
[1287.16 → 1288.54] And that has proved
[1288.54 → 1291.04] to improve our classifiers,
[1291.42 → 1292.30] crop type classifier
[1292.30 → 1293.14] which we built.
[1293.42 → 1295.30] And it's still an ongoing work,
[1295.44 → 1296.26] but yes,
[1296.32 → 1298.22] it's provided good results
[1298.22 → 1298.66] for now.
[1299.12 → 1300.40] Yeah, so if I'm
[1300.40 → 1301.44] understanding right, Abba,
[1301.54 → 1303.04] that you are sort of
[1303.04 → 1304.24] using the GANs
[1304.24 → 1305.58] for data augmentation
[1305.58 → 1307.40] in the case of
[1307.40 → 1308.80] data scarcity.
[1309.20 → 1310.96] So do you take that
[1310.96 → 1312.54] sort of the actual
[1312.54 → 1314.10] observed imagery
[1314.10 → 1316.02] and use that sort of
[1316.02 → 1317.24] with your discriminator
[1317.24 → 1318.30] in this framework
[1318.30 → 1319.46] to create these
[1319.46 → 1320.38] augmented images?
[1320.68 → 1321.88] And could you describe
[1321.88 → 1322.42] a little bit,
[1322.52 → 1322.80] you know,
[1323.18 → 1324.00] was that kind of
[1324.00 → 1325.54] the initial solution
[1325.54 → 1326.86] that made sense to you?
[1326.88 → 1327.62] Or is that something
[1327.62 → 1329.30] you kind of stumbled on later?
[1329.30 → 1330.54] Could you describe
[1330.54 → 1331.66] maybe a little bit more
[1331.66 → 1332.94] of that process
[1332.94 → 1334.46] and how you came
[1334.46 → 1335.14] to that solution?
[1335.78 → 1336.18] Okay.
[1336.50 → 1337.38] It was a research
[1337.38 → 1338.58] which came off
[1338.58 → 1339.80] an existing paper
[1339.80 → 1342.12] which an MSG GAN
[1342.12 → 1342.82] was used.
[1343.48 → 1344.44] And we decided
[1344.44 → 1345.26] to make a few
[1345.26 → 1346.70] modifications on that
[1346.70 → 1348.40] to be able to take in
[1348.40 → 1350.10] all the possible
[1350.10 → 1351.70] bands which we have
[1351.70 → 1353.26] and generate them.
[1353.54 → 1354.36] The initial paper
[1354.36 → 1355.52] just had generating
[1355.52 → 1356.34] images without
[1356.34 → 1357.30] the labels, right?
[1357.30 → 1358.36] So we were able
[1358.36 → 1359.90] to modify it
[1359.90 → 1361.00] and also generate
[1361.00 → 1361.82] including with
[1361.82 → 1363.34] the labels as well.
[1363.96 → 1365.68] So that's basically
[1365.68 → 1367.64] the setup which we used.
[1368.08 → 1368.62] I'm curious
[1368.62 → 1369.34] as you're talking
[1369.34 → 1370.28] about GANs
[1370.28 → 1371.40] and the use of that
[1371.40 → 1372.42] and trying to augment
[1372.42 → 1373.42] data and stuff,
[1373.84 → 1374.72] have you kind of
[1374.72 → 1376.02] as a little bit
[1376.02 → 1376.80] of a random question
[1376.80 → 1377.32] thrown in,
[1377.62 → 1378.24] any thoughts
[1378.24 → 1379.60] on the use of simulation?
[1379.84 → 1380.50] We're seeing a lot
[1380.50 → 1381.12] of simulation
[1381.12 → 1382.12] starting to be used
[1382.12 → 1382.54] with that
[1382.54 → 1383.46] going forward
[1383.46 → 1384.18] in the space.
[1384.34 → 1385.12] And have you all
[1385.12 → 1386.06] gotten to that area
[1386.06 → 1386.66] or have you put
[1386.66 → 1387.02] any thought
[1387.02 → 1387.66] into what you
[1387.66 → 1388.16] might do
[1388.16 → 1389.14] in terms of
[1389.14 → 1390.04] data augmentation
[1390.04 → 1390.96] with simulation
[1390.96 → 1391.88] and GANs
[1391.88 → 1392.24] and such
[1392.24 → 1393.30] or not?
[1393.56 → 1394.34] Something on the GAN
[1394.34 → 1394.88] just to say
[1394.88 → 1395.68] that we have a website
[1395.68 → 1396.34] if you're interested
[1396.34 → 1396.92] to see some
[1396.92 → 1397.60] of those synthetic
[1397.60 → 1398.04] imagery,
[1398.52 → 1399.28] you can go to
[1399.28 → 1401.20] isthisplacereal.com.
[1401.48 → 1402.10] We have a game
[1402.10 → 1402.76] there you can see
[1402.76 → 1403.46] how good you can
[1403.46 → 1404.18] detect real
[1404.18 → 1405.50] from synthetic
[1405.50 → 1406.38] satellite imagery
[1406.38 → 1407.32] or fake imagery.
[1407.46 → 1408.12] We got kind of
[1408.12 → 1408.84] interested in this
[1408.84 → 1410.00] similar to the website
[1410.00 → 1410.44] that there is
[1410.44 → 1411.06] in the GAN board
[1411.06 → 1413.32] for thispersondoesntexist.com.
[1413.68 → 1414.16] But anyway,
[1414.26 → 1414.92] back to your question
[1414.92 → 1415.64] about simulation.
[1415.80 → 1416.74] So that is true.
[1416.82 → 1417.56] That is a growing
[1417.56 → 1418.96] kind of application
[1418.96 → 1419.98] in the generally
[1419.98 → 1420.74] air science
[1420.74 → 1421.70] geospatial sector.
[1422.00 → 1423.32] We haven't at Radiant
[1423.32 → 1424.74] touched on that space yet.
[1424.84 → 1425.46] We are not doing
[1425.46 → 1426.16] any simulation
[1426.16 → 1426.68] ourselves.
[1427.02 → 1427.60] But particularly
[1427.60 → 1428.46] for those who are
[1428.46 → 1429.30] working to
[1429.30 → 1430.50] kind of embed
[1430.50 → 1431.66] AI ML modelling
[1431.66 → 1432.98] into the general
[1432.98 → 1433.84] climate modelling
[1433.84 → 1435.02] in terms of like
[1435.02 → 1435.96] projecting what will
[1435.96 → 1437.00] happen with the
[1437.00 → 1437.60] warming world
[1437.60 → 1438.64] within like 10 years,
[1438.74 → 1439.20] 20 years,
[1439.30 → 1440.34] 100 year windows,
[1440.82 → 1441.52] they are basically
[1441.52 → 1442.28] relying on many
[1442.28 → 1443.08] of the simulations
[1443.08 → 1444.06] to fit it into
[1444.06 → 1444.68] the machine learning
[1444.68 → 1445.34] model part
[1445.34 → 1446.10] and train those
[1446.10 → 1446.44] models.
[1446.90 → 1447.44] That is a very
[1447.44 → 1448.02] growing field.
[1448.10 → 1448.62] There is a lot of
[1448.62 → 1449.00] research,
[1449.12 → 1449.74] a lot of kinds of
[1449.74 → 1450.82] interdisciplinary actually
[1450.82 → 1451.76] departments being
[1451.76 → 1452.88] established at universities
[1452.88 → 1453.84] to just work on
[1453.84 → 1454.74] that type of problem.
[1455.10 → 1456.44] How we can learn
[1456.44 → 1457.22] from the physical
[1457.22 → 1458.08] and the simulation
[1458.08 → 1459.48] world to teach
[1459.48 → 1460.24] the machine learning
[1460.24 → 1461.30] models to simulate
[1461.30 → 1462.16] that and be more
[1462.16 → 1464.12] scalable and hopefully
[1464.12 → 1465.12] more interpretable
[1465.12 → 1465.62] in the world.
[1465.76 → 1466.66] So it's a growing
[1466.66 → 1466.92] field,
[1467.08 → 1467.80] but we at Radiant
[1467.80 → 1468.60] haven't done anything
[1468.60 → 1469.22] in there yet.
[1469.22 → 1470.22] I'm interested,
[1470.42 → 1471.90] as I was sort of
[1471.90 → 1474.14] exploring the crop
[1474.14 → 1474.88] spotting or
[1474.88 → 1476.30] classification use
[1476.30 → 1477.30] case that you were
[1477.30 → 1477.72] highlighting,
[1477.84 → 1478.62] I noticed that
[1478.62 → 1480.30] there's a leaderboard
[1480.30 → 1482.20] on the Wendi site
[1482.20 → 1484.24] related to a spot
[1484.24 → 1485.50] the crop challenge.
[1486.02 → 1486.68] Could you talk a
[1486.68 → 1487.68] little bit about
[1487.68 → 1489.04] that and how
[1489.04 → 1490.92] you've decided to
[1490.92 → 1491.88] kind of utilize
[1491.88 → 1492.80] some of this
[1492.80 → 1494.52] competition leaderboard
[1494.52 → 1495.68] type of approach
[1495.68 → 1496.72] to look at some
[1496.72 → 1497.30] of these problems?
[1497.64 → 1498.30] Yeah, so this is
[1498.30 → 1499.16] actually one of those
[1499.16 → 1500.14] use cases that we
[1500.14 → 1500.94] work with a local
[1500.94 → 1501.40] partner.
[1501.58 → 1502.20] So in this case,
[1502.26 → 1503.56] it was the Western
[1503.56 → 1504.58] Cape Department of
[1504.58 → 1505.60] Agriculture in South
[1505.60 → 1506.00] Africa.
[1506.22 → 1507.56] So they do this
[1507.56 → 1508.62] agricultural census
[1508.62 → 1510.54] every decade or so
[1510.54 → 1511.24] because, as I
[1511.24 → 1512.00] mentioned, it is very
[1512.00 → 1512.76] extensive and
[1512.76 → 1513.80] expensive process.
[1514.20 → 1514.84] And they had done
[1514.84 → 1515.92] the recent one in
[1515.92 → 1517.10] 2017, 2018.
[1517.10 → 1517.76] So they had a
[1517.76 → 1519.34] high quality map
[1519.34 → 1520.58] of their state in
[1520.58 → 1521.58] terms of what crops
[1521.58 → 1522.12] are grown,
[1522.58 → 1523.44] specific field
[1523.44 → 1524.48] boundaries of each
[1524.48 → 1526.02] basically farmland,
[1526.44 → 1527.10] the crop type,
[1527.18 → 1527.90] and other kind of
[1527.90 → 1528.64] metadata like
[1528.64 → 1529.48] irrigation type
[1529.48 → 1530.06] and so on.
[1530.30 → 1530.70] And they were
[1530.70 → 1531.68] interested to see
[1531.68 → 1532.92] can this process
[1532.92 → 1534.20] be automated
[1534.20 → 1534.86] or at least
[1534.86 → 1535.88] semi-automized
[1535.88 → 1536.92] using satellite
[1536.92 → 1537.66] images so they
[1537.66 → 1538.18] can get an
[1538.18 → 1538.90] updated map
[1538.90 → 1539.52] every year.
[1539.70 → 1540.58] And what is the
[1540.58 → 1541.22] art of possible
[1541.22 → 1541.68] with that?
[1541.80 → 1542.50] So what we
[1542.50 → 1543.08] worked with them
[1543.08 → 1544.30] was receiving
[1544.30 → 1545.52] that data as a
[1545.52 → 1546.50] partner and then
[1546.50 → 1547.76] curating a high
[1547.76 → 1548.78] quality and diverse
[1548.78 → 1549.64] training data out
[1549.64 → 1550.00] of that.
[1550.16 → 1551.12] So we matched
[1551.12 → 1551.96] this kind of
[1551.96 → 1553.00] labels that they
[1553.00 → 1553.50] have collected
[1553.50 → 1553.98] on the ground.
[1554.06 → 1554.32] Those are
[1554.32 → 1555.54] practically what we
[1555.54 → 1556.08] call labels.
[1556.18 → 1556.54] You're on the
[1556.54 → 1557.24] ground, you collect
[1557.24 → 1557.94] the crop type,
[1558.32 → 1558.92] and because we
[1558.92 → 1559.56] match this with
[1559.56 → 1560.28] satellite imagery,
[1560.42 → 1561.10] that becomes the
[1561.10 → 1561.34] label.
[1561.84 → 1562.36] And then we
[1562.36 → 1563.66] basically match
[1563.66 → 1564.38] with corresponding
[1564.38 → 1564.96] time series.
[1565.10 → 1565.74] As Abba mentioned,
[1565.82 → 1566.44] in this type of
[1566.44 → 1567.20] problem, we use
[1567.20 → 1568.30] usually time series
[1568.30 → 1568.78] of imagery.
[1568.78 → 1569.38] It's not just
[1569.38 → 1570.62] one image and
[1570.62 → 1571.48] you classify a
[1571.48 → 1572.06] label for it
[1572.06 → 1573.14] because crops
[1573.14 → 1574.66] have a seasonality,
[1574.78 → 1575.18] they have a
[1575.18 → 1576.46] phenology, and you
[1576.46 → 1577.18] want to find that
[1577.18 → 1578.12] signature and then
[1578.12 → 1578.90] the model will be
[1578.90 → 1579.88] better able to
[1579.88 → 1580.88] decide if this is a
[1580.88 → 1582.12] wheat or a maize
[1582.12 → 1583.24] or a sorghum or so
[1583.24 → 1583.44] bond.
[1583.84 → 1584.92] So we basically
[1584.92 → 1585.70] curated that
[1585.70 → 1586.68] dataset and then
[1586.68 → 1587.88] to kind of
[1587.88 → 1588.92] crowdsource models,
[1589.08 → 1589.40] we run a
[1589.40 → 1589.86] competition.
[1590.56 → 1591.70] So getting some
[1591.70 → 1592.70] support from the
[1592.70 → 1593.88] GIG Fair Forward
[1593.88 → 1595.40] program, we ran
[1595.40 → 1596.54] this competition on
[1596.54 → 1597.42] Hindi platform and
[1597.42 → 1598.34] exposed the problem
[1598.34 → 1599.68] to a pool of
[1599.68 → 1600.48] talents that Hindi
[1600.48 → 1601.66] has to see who
[1601.66 → 1602.42] can build the best
[1602.42 → 1603.26] model for this
[1603.26 → 1603.68] crop type
[1603.68 → 1604.20] classification
[1604.20 → 1604.84] problem.
[1605.60 → 1606.24] And similar to
[1606.24 → 1606.68] any other
[1606.68 → 1607.40] competition, we
[1607.40 → 1607.92] had a training
[1607.92 → 1608.74] set and a test
[1608.74 → 1609.42] set and a test
[1609.42 → 1609.60] set.
[1609.82 → 1610.00] Basically,
[1610.14 → 1610.92] predictions were
[1610.92 → 1611.58] hidden.
[1611.58 → 1612.22] We use that
[1612.22 → 1613.48] for scoring and
[1613.48 → 1614.18] kind of defining
[1614.18 → 1614.88] that leaderboard
[1614.88 → 1615.48] that you saw.
[1615.88 → 1616.42] And people
[1616.42 → 1617.44] basically build
[1617.44 → 1618.00] their models.
[1618.20 → 1618.62] The incentive
[1618.62 → 1619.22] for them is
[1619.22 → 1620.26] getting exposed
[1620.26 → 1620.66] to a new
[1620.66 → 1621.02] problem.
[1621.18 → 1621.68] It's also a
[1621.68 → 1622.50] capacity development
[1622.50 → 1623.20] effort for us
[1623.20 → 1624.30] because many of
[1624.30 → 1625.06] the people in
[1625.06 → 1626.34] the AI community
[1626.34 → 1627.42] across Africa are
[1627.42 → 1628.06] eager for new
[1628.06 → 1628.50] problems.
[1628.96 → 1629.28] And I think
[1629.28 → 1630.10] geospatial and
[1630.10 → 1631.16] satellite imagery is
[1631.16 → 1631.70] one of those
[1631.70 → 1632.12] domains.
[1632.48 → 1633.30] So it's also a
[1633.30 → 1634.14] capacity development
[1634.14 → 1635.36] effort for us while
[1635.36 → 1636.32] it is a real-world
[1636.32 → 1637.08] problem-solving.
[1637.44 → 1638.02] It is a problem
[1638.02 → 1638.58] that a government
[1638.58 → 1639.48] agency is interested
[1639.48 → 1640.20] in and there is a
[1640.20 → 1641.06] good potential for
[1641.06 → 1641.26] it.
[1641.58 → 1642.22] So the
[1642.22 → 1643.12] winners basically
[1643.12 → 1644.00] are those three
[1644.00 → 1644.68] and the leaderboard
[1644.68 → 1645.20] that you see.
[1645.20 → 1646.02] They have built
[1646.02 → 1646.66] the best models
[1646.66 → 1647.20] in terms of
[1647.20 → 1648.06] accuracy score
[1648.06 → 1648.98] of detecting
[1648.98 → 1649.66] crop types
[1649.66 → 1650.46] in Western
[1650.46 → 1650.76] Cape,
[1650.84 → 1651.40] South Africa.
[1651.52 → 1651.94] And the models
[1651.94 → 1652.54] are all open
[1652.54 → 1652.76] source.
[1652.86 → 1653.24] We haven't put
[1653.24 → 1653.68] it on GitHub
[1653.68 → 1654.40] yet, but soon
[1654.40 → 1654.90] they will be.
[1655.24 → 1655.76] Yeah, so that
[1655.76 → 1656.56] is the scope
[1656.56 → 1657.60] of that competition.
[1658.58 → 1658.98] I'm wondering
[1658.98 → 1660.48] maybe, Joyce,
[1660.56 → 1661.16] as a member
[1661.16 → 1662.24] of the
[1662.24 → 1663.36] sort of wider
[1663.36 → 1664.56] research community
[1664.56 → 1665.46] in Africa,
[1665.46 → 1666.50] if you could
[1666.50 → 1666.90] give your
[1666.90 → 1667.86] perspective on
[1667.86 → 1669.94] how a research
[1669.94 → 1671.18] group like yours
[1671.18 → 1672.50] might think
[1672.50 → 1673.14] about using
[1673.14 → 1673.80] some of these
[1673.80 → 1674.72] tools that
[1674.72 → 1675.62] Radiant Earth
[1675.62 → 1677.22] is creating
[1677.22 → 1678.02] and what it
[1678.02 → 1678.56] might enable
[1678.56 → 1679.48] for you.
[1679.64 → 1679.94] And then
[1679.94 → 1682.00] maybe then,
[1682.20 → 1682.50] you know,
[1682.54 → 1683.34] if you have
[1683.34 → 1684.26] follow-up questions
[1684.26 → 1686.06] for Radiant Earth
[1686.06 → 1687.24] in those regards,
[1687.40 → 1688.44] feel free to take
[1688.44 → 1689.04] us wherever.
[1689.04 → 1690.14] Yeah, so I
[1690.14 → 1691.00] think this is
[1691.00 → 1691.48] interesting.
[1691.76 → 1692.14] I think the
[1692.14 → 1692.72] question, the
[1692.72 → 1693.48] example that I
[1693.48 → 1694.52] gave are about
[1694.52 → 1694.90] trying to
[1694.90 → 1695.26] understand
[1695.26 → 1695.96] deforestation
[1695.96 → 1696.48] is one of
[1696.48 → 1696.94] the practical
[1696.94 → 1697.54] problems that
[1697.54 → 1697.94] we are working
[1697.94 → 1698.40] on in the
[1698.40 → 1698.66] lab.
[1699.02 → 1699.48] And it was
[1699.48 → 1700.14] interesting to
[1700.14 → 1700.80] hear, have
[1700.80 → 1701.30] made thoughts
[1701.30 → 1701.80] on that.
[1702.16 → 1702.74] But also what
[1702.74 → 1703.20] is important
[1703.20 → 1703.92] is from the
[1703.92 → 1704.36] lab, we've
[1704.36 → 1704.88] been doing a
[1704.88 → 1705.46] lot of work
[1705.46 → 1706.38] around collecting
[1706.38 → 1707.64] data, around
[1707.64 → 1708.36] about the
[1708.36 → 1709.08] crops, some
[1709.08 → 1709.86] sort of crop
[1709.86 → 1710.32] mapping.
[1710.74 → 1711.34] And that's
[1711.34 → 1711.74] always the
[1711.74 → 1712.32] problem, trying
[1712.32 → 1713.36] to understand the
[1713.36 → 1714.10] ground truth and
[1714.10 → 1714.82] collect as much
[1714.82 → 1715.62] ground truth data
[1715.62 → 1716.30] as possible.
[1716.56 → 1717.06] Because if you
[1717.06 → 1717.70] want to use
[1717.70 → 1718.24] satellite imagery
[1718.24 → 1719.06] data, then the
[1719.06 → 1719.68] ground truth can
[1719.68 → 1720.16] act as a
[1720.16 → 1720.60] reference.
[1721.06 → 1721.70] And so I feel
[1721.70 → 1722.28] like the problem
[1722.28 → 1722.90] also that we
[1722.90 → 1723.82] can solve is now
[1723.82 → 1724.26] that we have
[1724.26 → 1724.90] the ground truth,
[1724.96 → 1725.44] can we be able
[1725.44 → 1726.12] to map that to
[1726.12 → 1726.54] the satellite
[1726.54 → 1727.74] imagery data and
[1727.74 → 1728.46] be able to
[1728.46 → 1729.70] build models that
[1729.70 → 1730.62] can easily be
[1730.62 → 1731.62] used for crop
[1731.62 → 1732.46] type mapping
[1732.46 → 1733.48] around different
[1733.48 → 1734.30] farms in the
[1734.30 → 1734.66] country.
[1735.06 → 1735.54] So there are
[1735.54 → 1736.48] several potential
[1736.48 → 1737.32] areas that
[1737.32 → 1738.06] really we can
[1738.06 → 1738.88] benefit from
[1738.88 → 1739.88] what Radiant
[1739.88 → 1740.24] Earth is
[1740.24 → 1740.94] providing and
[1740.94 → 1741.44] the kind of
[1741.44 → 1741.92] data that
[1741.92 → 1742.12] they are
[1742.12 → 1742.60] providing.
[1743.00 → 1743.34] But most
[1743.34 → 1744.54] especially since
[1744.54 → 1745.32] the Mario AI
[1745.32 → 1746.10] lab is located
[1746.10 → 1746.58] within a
[1746.58 → 1747.40] university, it
[1747.40 → 1747.68] really puts
[1747.70 → 1748.64] an opportunity
[1748.64 → 1749.36] for capacity
[1749.36 → 1750.12] building, right?
[1750.18 → 1750.58] Because that's
[1750.58 → 1751.12] how the lab
[1751.12 → 1751.46] grows.
[1751.72 → 1752.84] We have a lot
[1752.84 → 1753.64] of students who
[1753.64 → 1754.14] come in, do
[1754.14 → 1754.88] internship, and
[1754.88 → 1755.54] then get introduced
[1755.54 → 1756.02] to several
[1756.02 → 1756.98] concepts in
[1756.98 → 1757.58] machine learning
[1757.58 → 1758.18] and AI.
[1758.84 → 1759.60] And ML for
[1759.60 → 1760.18] Earth Observation
[1760.18 → 1760.80] is one of those
[1760.80 → 1761.46] concepts that we
[1761.46 → 1762.14] are starting to
[1762.14 → 1762.64] work on.
[1763.08 → 1763.66] And I know that
[1763.66 → 1764.36] earlier this year
[1764.36 → 1765.54] we had the ML
[1765.54 → 1766.48] boot camp that
[1766.48 → 1767.04] we organized
[1767.04 → 1767.82] together with
[1767.82 → 1768.82] Radiant Earth
[1768.82 → 1769.72] and Fair Forward
[1769.72 → 1770.58] as well.
[1771.00 → 1772.10] And so I think
[1772.10 → 1772.54] that's what I
[1772.54 → 1773.12] want to hear
[1773.12 → 1773.92] from Upped.
[1774.08 → 1774.52] I just saw
[1774.52 → 1775.20] recently that
[1775.20 → 1776.06] this had even
[1776.06 → 1776.80] moved into
[1776.80 → 1778.00] a tiny.
[1778.16 → 1778.70] So I think
[1778.70 → 1779.16] it's important
[1779.16 → 1779.74] for us to
[1779.74 → 1780.34] know if I
[1780.34 → 1781.50] were a student
[1781.50 → 1782.50] out there and
[1782.50 → 1783.04] I wanted to
[1783.04 → 1783.58] learn more.
[1783.90 → 1784.30] I understand
[1784.30 → 1784.88] there's Radiant
[1784.88 → 1785.54] Earth, yes
[1785.54 → 1785.92] there are
[1785.92 → 1786.84] tutorials, but
[1786.84 → 1787.22] I want to
[1787.22 → 1787.68] get a whole
[1787.68 → 1788.28] idea of
[1788.28 → 1788.90] what's Earth
[1788.90 → 1789.50] Observation,
[1789.94 → 1790.64] how do I get
[1790.64 → 1791.42] the data, but
[1791.42 → 1791.94] not just the
[1791.94 → 1792.52] data, how do I
[1792.52 → 1793.22] actually start to
[1793.22 → 1793.92] build my own
[1793.92 → 1794.26] model?
[1794.72 → 1795.62] For example,
[1795.80 → 1796.80] for a prediction
[1796.80 → 1798.14] of deforestation,
[1798.26 → 1798.78] how do I get
[1798.78 → 1799.12] started?
[1799.26 → 1799.54] And I know
[1799.54 → 1800.56] that Radiant
[1800.56 → 1801.14] Earth has been
[1801.14 → 1801.82] able to provide
[1801.82 → 1802.52] that opportunity.
[1802.52 → 1803.26] So, Ahmed, if
[1803.26 → 1803.80] you could speak
[1803.80 → 1804.86] more about this
[1804.86 → 1805.92] capacity development,
[1806.22 → 1806.62] that would be
[1806.62 → 1807.28] really great.
[1807.76 → 1808.28] Sure thing.
[1808.54 → 1809.06] When you think
[1809.06 → 1809.84] about the whole
[1809.84 → 1810.76] ecosystem of
[1810.76 → 1811.48] sustainable
[1811.48 → 1812.34] development goals,
[1812.42 → 1812.90] all the data
[1812.90 → 1813.56] being available,
[1813.66 → 1813.98] and as I
[1813.98 → 1814.60] mentioned, working
[1814.60 → 1815.08] with local
[1815.08 → 1816.06] partners, one
[1816.06 → 1816.52] of the missing
[1816.52 → 1817.26] pieces that we
[1817.26 → 1818.58] found is we
[1818.58 → 1819.16] need to train
[1819.16 → 1819.96] more individuals
[1819.96 → 1821.26] to be able to
[1821.26 → 1821.66] solve these
[1821.66 → 1822.38] problems because
[1822.38 → 1823.54] it is a new
[1823.54 → 1824.24] field, it is a
[1824.24 → 1825.30] growing field, it
[1825.30 → 1825.88] is an impactful
[1825.88 → 1826.48] field, but we
[1826.48 → 1827.28] need people to
[1827.28 → 1828.40] get trained how
[1828.40 → 1829.22] to use the data
[1829.22 → 1830.16] and generally
[1830.16 → 1831.06] starting with what
[1831.06 → 1831.84] is satellite imagery
[1831.84 → 1832.72] as Joyce mentioned.
[1832.94 → 1833.72] So, for that
[1833.72 → 1834.34] reason, one of
[1834.34 → 1834.96] the pillars of
[1834.96 → 1835.58] our work is
[1835.58 → 1836.28] really training
[1836.28 → 1836.92] and capacity
[1836.92 → 1837.44] development.
[1837.92 → 1838.40] So, earlier
[1838.40 → 1839.42] this year, back
[1839.42 → 1840.24] in May of
[1840.24 → 1841.50] 2021, actually,
[1841.86 → 1843.12] so we joined
[1843.12 → 1843.84] efforts with
[1843.84 → 1844.92] Joyce's team
[1844.92 → 1845.60] at May Career
[1845.60 → 1846.40] University and
[1846.40 → 1846.94] got support
[1846.94 → 1848.10] from the
[1848.10 → 1849.12] GIG Fair
[1849.12 → 1849.44] Forward
[1849.44 → 1850.40] program to
[1850.40 → 1851.04] run a
[1851.04 → 1851.36] training
[1851.36 → 1851.92] bootcamp
[1851.92 → 1852.88] focused on
[1852.88 → 1853.48] machine learning
[1853.48 → 1853.92] for Earth
[1853.92 → 1854.44] observation.
[1854.90 → 1855.14] And the
[1855.14 → 1855.96] target for us
[1855.96 → 1856.66] was there's
[1856.66 → 1857.50] a growing
[1857.50 → 1858.26] community of
[1858.26 → 1859.10] AI practitioners
[1859.10 → 1859.88] across Africa.
[1860.08 → 1860.36] I mean, we
[1860.36 → 1860.78] at Radiant
[1860.78 → 1861.18] have worked
[1861.18 → 1861.38] with,
[1861.38 → 1862.20] Data Science
[1862.20 → 1862.66] Africa,
[1862.92 → 1863.40] with Indaba
[1863.40 → 1863.82] teams,
[1863.94 → 1864.60] with Indaba
[1864.60 → 1865.20] X teams
[1865.20 → 1865.82] across different
[1865.82 → 1866.32] countries,
[1866.72 → 1867.08] and they're
[1867.08 → 1867.90] all AI
[1867.90 → 1868.50] people, but
[1868.50 → 1868.76] they're not
[1868.76 → 1869.30] exposed to
[1869.30 → 1869.62] the remote
[1869.62 → 1870.24] sensing board.
[1870.38 → 1871.08] So, the
[1871.08 → 1871.64] training was
[1871.64 → 1873.00] kind of outlined
[1873.00 → 1873.44] in a sense
[1873.44 → 1873.86] that let's
[1873.86 → 1874.58] start exposing
[1874.58 → 1875.26] them to what
[1875.26 → 1875.66] is satellite
[1875.66 → 1876.64] imagery, how
[1876.64 → 1877.18] you deal with
[1877.18 → 1877.76] this type of
[1877.76 → 1878.24] data, how
[1878.24 → 1878.86] do you access
[1878.86 → 1879.20] them?
[1879.46 → 1879.82] I mentioned
[1879.82 → 1880.54] APIs and
[1880.54 → 1881.20] the repositories,
[1881.32 → 1881.88] but practically
[1881.88 → 1882.32] how do you
[1882.32 → 1882.92] write a Python
[1882.92 → 1883.76] code to get
[1883.76 → 1884.32] that type of
[1884.32 → 1884.62] imagery?
[1885.06 → 1885.62] And then how
[1885.62 → 1886.60] do you curate
[1886.60 → 1887.02] a training
[1887.02 → 1887.74] dataset when
[1887.74 → 1888.10] you have a
[1888.10 → 1888.70] reference data
[1888.70 → 1889.18] on the ground?
[1889.18 → 1889.52] So, the
[1889.52 → 1890.12] lectures were
[1890.12 → 1891.08] kind of designed
[1891.08 → 1891.74] in that sense
[1891.74 → 1892.10] and we had
[1892.10 → 1892.68] around 40
[1892.68 → 1893.50] participants in
[1893.50 → 1894.00] that course.
[1894.48 → 1894.80] And then in
[1894.80 → 1895.44] the second week
[1895.44 → 1896.10] of that, we
[1896.10 → 1897.02] were working on
[1897.02 → 1897.78] practical use
[1897.78 → 1898.12] cases.
[1898.50 → 1898.90] How do you
[1898.90 → 1899.40] build a crop
[1899.40 → 1900.16] type classification
[1900.16 → 1900.72] model?
[1900.88 → 1901.24] How do you
[1901.24 → 1901.74] build a model
[1901.74 → 1902.54] for, for
[1902.54 → 1903.18] example, wind
[1903.18 → 1904.04] estimation from
[1904.04 → 1905.38] a cyclone using
[1905.38 → 1906.02] a game satellite
[1906.02 → 1906.80] imagery that we
[1906.80 → 1907.40] get regularly?
[1907.82 → 1908.50] And particularly,
[1908.84 → 1909.72] we were asking
[1909.72 → 1910.58] participants to
[1910.58 → 1911.18] also work on
[1911.18 → 1911.66] some of those
[1911.66 → 1912.72] exercises between
[1912.72 → 1913.10] lectures.
[1913.22 → 1913.62] So, it was
[1913.62 → 1914.60] hands-on and
[1914.60 → 1915.06] practical.
[1915.06 → 1915.28] Well, it
[1915.28 → 1915.78] wasn't just
[1915.78 → 1916.32] lectures.
[1916.98 → 1917.86] And I think it
[1917.86 → 1918.26] was a very
[1918.26 → 1919.62] successful training
[1919.62 → 1920.14] based on the
[1920.14 → 1921.26] feedback and the
[1921.26 → 1922.04] kind of survey we
[1922.04 → 1922.78] collected from the
[1922.78 → 1923.78] participants afterwards.
[1923.98 → 1924.42] And then we
[1924.42 → 1925.36] packaged that
[1925.36 → 1926.26] training program
[1926.26 → 1927.34] into an online
[1927.34 → 1928.12] course, which is
[1928.12 → 1928.96] now available on
[1928.96 → 1929.56] the ACTING
[1929.56 → 1930.34] platform, which
[1930.34 → 1930.92] is established
[1930.92 → 1931.56] by GIG.
[1932.00 → 1932.94] So, anybody can
[1932.94 → 1933.66] go through that
[1933.66 → 1934.48] course now on
[1934.48 → 1935.28] their own pace
[1935.28 → 1936.58] and basically start
[1936.58 → 1937.24] learning about
[1937.24 → 1938.06] Earth observations,
[1938.38 → 1938.92] the topics that
[1938.92 → 1939.60] I mentioned, how
[1939.60 → 1940.58] do you deal with
[1940.58 → 1941.28] machine learning in
[1941.28 → 1942.02] that sector and
[1942.02 → 1942.80] then building your
[1942.80 → 1943.30] own model.
[1943.30 → 1944.34] If you finish
[1944.34 → 1944.90] the course on
[1944.90 → 1945.50] ACTING, you can
[1945.50 → 1946.04] also get a
[1946.04 → 1946.46] certificate.
[1947.10 → 1947.74] And there's also
[1947.74 → 1948.80] a user community
[1948.80 → 1949.42] on our end.
[1949.50 → 1950.14] So, we have an
[1950.14 → 1951.26] open Slack
[1951.26 → 1951.82] workspace.
[1952.30 → 1952.84] The link is in
[1952.84 → 1953.44] that course.
[1953.84 → 1954.56] And it's basically
[1954.56 → 1955.38] Radiant ML Hub
[1955.38 → 1956.46] Slack workspace that
[1956.46 → 1957.38] anybody can join,
[1957.86 → 1958.60] ask questions,
[1958.98 → 1959.68] connect with other
[1959.68 → 1961.16] peers, share their
[1961.16 → 1961.88] experience or
[1961.88 → 1963.00] problem, or look
[1963.00 → 1963.66] for collaborators
[1963.66 → 1964.36] and others.
[1964.72 → 1965.64] So, those who
[1965.64 → 1966.38] participate in that
[1966.38 → 1967.04] course can also
[1967.04 → 1967.86] connect to others
[1967.86 → 1969.20] and basically get
[1969.20 → 1970.18] feedback from others.
[1970.76 → 1971.36] So, as you all
[1971.36 → 1972.00] have been talking
[1972.00 → 1972.92] about this for the
[1972.92 → 1973.26] last few
[1973.30 → 1974.40] minutes, it's a
[1974.40 → 1975.70] cool process and
[1975.70 → 1977.02] I find my mind
[1977.02 → 1977.92] kind of wandering
[1977.92 → 1979.06] back to earlier
[1979.06 → 1979.92] in the conversation
[1979.92 → 1981.48] and you've hit a
[1981.48 → 1982.12] couple of different
[1982.12 → 1983.78] use cases, but I'm
[1983.78 → 1984.48] starting to wonder
[1984.48 → 1985.54] how this could be
[1985.54 → 1986.48] applied to so many
[1986.48 → 1987.36] areas now that I
[1987.36 → 1988.20] understand how
[1988.20 → 1988.80] you're approaching
[1988.80 → 1990.06] and the tools that
[1990.06 → 1990.64] you're developing.
[1991.32 → 1992.14] And so, if you go
[1992.14 → 1993.02] back to kind of that
[1993.02 → 1994.76] notion of sustainable
[1994.76 → 1995.82] development goals,
[1996.14 → 1997.22] the SDGs and those
[1997.22 → 1998.42] kind of big problem
[1998.42 → 2000.18] areas that you're
[2000.18 → 2001.28] addressing some of
[2001.28 → 2002.40] those, I'm rather
[2002.40 → 2003.54] curious now, now
[2003.54 → 2004.32] that I understand
[2004.32 → 2005.36] which of those
[2005.36 → 2006.06] types of things
[2006.06 → 2007.06] you're hitting or
[2007.06 → 2008.14] planning to hit in
[2008.14 → 2009.40] the future and which
[2009.40 → 2010.48] might be aspirational.
[2010.62 → 2011.38] So, even if it's
[2011.38 → 2012.10] something that you
[2012.10 → 2012.90] have an interest in,
[2013.24 → 2014.38] your brain has been
[2014.38 → 2015.32] chugging on it for a
[2015.32 → 2016.08] while, and you know
[2016.08 → 2016.96] that might not be
[2016.96 → 2017.92] something that you're
[2017.92 → 2018.56] going to be able to
[2018.56 → 2019.84] address right away,
[2020.02 → 2021.32] I'd love to understand
[2021.32 → 2022.04] kind of what you're
[2022.04 → 2023.42] thinking about what's
[2023.42 → 2024.20] possible here.
[2024.36 → 2025.38] What types of things,
[2025.48 → 2026.38] what types of problems
[2026.38 → 2028.48] are achievable maybe in
[2028.48 → 2029.92] the short, medium, and
[2029.92 → 2030.88] long-term, long-term,
[2030.88 → 2031.50] maybe just being
[2031.50 → 2032.12] aspirational?
[2032.80 → 2033.60] Yeah, I'll share my
[2033.60 → 2033.88] feedback.
[2034.02 → 2034.74] I will feel free to
[2034.74 → 2035.54] jump in afterwards.
[2036.00 → 2037.84] So, think of geospatial
[2037.84 → 2039.12] as a horizontal sector.
[2039.62 → 2040.90] So, geospatial can feed
[2040.90 → 2041.98] into many, many
[2041.98 → 2043.68] vertical domains from
[2043.68 → 2044.62] agriculture, food
[2044.62 → 2045.94] security, land cover,
[2046.52 → 2047.58] surface water monitoring,
[2048.00 → 2048.74] drought monitoring,
[2048.90 → 2050.54] deforestation, ocean
[2050.54 → 2051.48] monitoring, and sea
[2051.48 → 2051.72] life.
[2051.82 → 2052.98] There are many aspects
[2052.98 → 2054.08] that geospatial as a
[2054.08 → 2055.14] horizontal sector can
[2055.14 → 2055.64] feed into.
[2055.90 → 2056.76] That's how we have
[2056.76 → 2058.08] established SHOP.
[2058.08 → 2059.34] So, it is agnostic
[2059.34 → 2060.18] to the application.
[2060.42 → 2061.56] But as a radiant
[2061.56 → 2062.58] team, we have
[2062.58 → 2063.38] limited capacity.
[2063.54 → 2064.04] So, we work
[2064.04 → 2065.20] ourselves on specific
[2065.20 → 2066.64] problems, which are
[2066.64 → 2067.58] particularly in the
[2067.58 → 2068.68] agriculture and food
[2068.68 → 2069.44] security sector.
[2069.54 → 2070.18] That has been really
[2070.18 → 2071.34] the prime kind of
[2071.34 → 2072.34] application area for
[2072.34 → 2073.28] us because of its
[2073.28 → 2074.18] impact across the
[2074.18 → 2074.94] development sector.
[2075.20 → 2075.98] It employs a
[2075.98 → 2077.08] significant portion of
[2077.08 → 2078.08] the labour across the
[2078.08 → 2079.72] developing regions, and
[2079.72 → 2080.62] it's a significant
[2080.62 → 2081.72] portion of the GDP,
[2082.40 → 2083.68] and then food security
[2083.68 → 2084.58] and human life is
[2084.58 → 2085.28] definitely another
[2085.28 → 2085.92] angle of that.
[2085.92 → 2086.52] So, for those
[2086.52 → 2087.66] reasons, we have
[2087.66 → 2089.30] been kind of doubling
[2089.30 → 2090.56] down our efforts into
[2090.56 → 2091.72] how we can better
[2091.72 → 2092.80] solve stakeholders
[2092.80 → 2093.88] on the ground to
[2093.88 → 2094.88] solve the problems
[2094.88 → 2095.62] related to that.
[2095.86 → 2096.96] The ambition and
[2096.96 → 2097.88] the end goal, if I
[2097.88 → 2098.60] want to think, okay,
[2098.68 → 2100.20] what is the kind of
[2100.20 → 2101.88] the ideal world, the
[2101.88 → 2102.72] utopia that we are
[2102.72 → 2104.22] thinking about is the
[2104.22 → 2105.40] kind of stakeholders,
[2105.66 → 2106.44] particularly in this
[2106.44 → 2107.56] case, governments, and
[2107.56 → 2108.10] to some extent,
[2108.20 → 2108.84] commercial sort of
[2108.84 → 2110.30] providing services, be
[2110.30 → 2111.54] able to say, oh, I'm
[2111.54 → 2112.84] in this region, I want
[2112.84 → 2113.30] to know what the
[2113.30 → 2114.10] farmers are doing, I
[2114.10 → 2114.84] want to provide the
[2114.84 → 2115.88] right recommendations,
[2115.92 → 2116.86] to them in terms of
[2116.86 → 2117.92] fertilizer application,
[2118.08 → 2119.14] the best crop type to
[2119.14 → 2120.70] grow, how to basically
[2120.70 → 2121.94] plant that, how much
[2121.94 → 2123.20] water you need, and
[2123.20 → 2124.02] maximize their
[2124.02 → 2125.00] production toward the
[2125.00 → 2125.72] end of the season.
[2125.90 → 2126.84] That addresses their
[2126.84 → 2127.74] economic kind of
[2127.74 → 2128.52] well-being, that
[2128.52 → 2129.56] addresses their food
[2129.56 → 2130.62] security, and the
[2130.62 → 2131.30] human well-being,
[2131.34 → 2132.28] because they have more
[2132.28 → 2133.38] nutrition and food to
[2133.38 → 2134.56] feed the society.
[2134.88 → 2135.44] And then we are
[2135.44 → 2137.30] utilizing our natural
[2137.30 → 2138.44] resources the best way,
[2138.50 → 2139.38] because that's another
[2139.38 → 2140.24] angle of this thing.
[2140.40 → 2141.58] If we are kind of
[2141.58 → 2143.06] over-planting in
[2143.06 → 2144.02] regions that are not
[2144.02 → 2144.70] suitable for that
[2144.70 → 2145.82] specific crop, we are
[2145.82 → 2147.10] killing the nutrition
[2147.10 → 2148.02] of the soil, and then
[2148.02 → 2148.68] down the road we are
[2148.68 → 2149.26] not going to have a
[2149.26 → 2150.16] sustainable agriculture.
[2150.70 → 2151.46] So really the end
[2151.46 → 2152.54] goal is supporting the
[2152.54 → 2153.06] governments and
[2153.06 → 2154.14] stakeholders to be able
[2154.14 → 2154.66] to do that.
[2154.94 → 2155.76] It needs a holistic
[2155.76 → 2156.78] approach, it is not
[2156.78 → 2158.40] just us doing that, but
[2158.40 → 2159.22] what we are trying to
[2159.22 → 2160.22] do is showing the art
[2160.22 → 2161.68] of possible, providing
[2161.68 → 2162.72] those benchmarks and
[2162.72 → 2163.96] access points, and
[2163.96 → 2165.04] providing the know-how
[2165.04 → 2166.00] and the skill sets to
[2166.00 → 2167.04] as many people as we
[2167.04 → 2168.38] can train, and then
[2168.38 → 2169.68] asking them to train
[2169.68 → 2170.40] others to be
[2170.40 → 2171.22] sustainable in the
[2171.22 → 2172.82] training ecosystem to be
[2172.82 → 2173.68] able to solve those
[2173.68 → 2174.42] type of problems.
[2175.22 → 2176.08] I would be curious
[2176.08 → 2177.56] just to sort of follow
[2177.56 → 2178.40] up on that.
[2178.62 → 2179.60] That was a very
[2179.60 → 2180.90] interesting kind of
[2180.90 → 2182.04] take on where
[2182.04 → 2183.66] geospatial sits sort of
[2183.66 → 2184.28] in the stack
[2184.28 → 2185.76] horizontally and what
[2185.76 → 2186.62] it can impact.
[2186.84 → 2187.74] I was wondering just
[2187.74 → 2189.22] for our listeners out
[2189.22 → 2190.14] there who, you know,
[2190.18 → 2191.22] with it being practical
[2191.22 → 2193.00] AI are very, or many
[2193.00 → 2193.78] of them are hopefully
[2193.78 → 2194.66] thinking about
[2194.66 → 2195.78] practical things, I
[2195.78 → 2196.42] was wondering if you
[2196.42 → 2197.60] could describe a little
[2197.60 → 2200.02] bit in more detail if
[2200.02 → 2201.14] people are excited by
[2201.14 → 2202.32] this podcast and they
[2202.32 → 2203.28] want to dig a little
[2203.28 → 2204.66] bit into the
[2204.66 → 2206.44] Radiant ML Hub.
[2206.80 → 2207.36] Could you just
[2207.36 → 2208.76] describe a little bit
[2208.76 → 2210.38] like what the API
[2210.38 → 2212.20] looks like for
[2212.20 → 2213.44] Radiant, the Radiant
[2213.44 → 2215.18] ML Hub, and the
[2215.18 → 2216.64] sorts of functions
[2216.64 → 2217.86] and things that you
[2217.86 → 2219.36] can do with the
[2219.36 → 2220.72] hub, and I see
[2220.72 → 2221.96] some sort of model
[2221.96 → 2223.12] extensions and that
[2223.12 → 2223.60] sort of thing.
[2224.36 → 2225.56] The Radiant ML Hub,
[2225.66 → 2226.40] just like I would
[2226.40 → 2227.66] mention, so now
[2227.66 → 2228.30] there's a model
[2228.30 → 2229.40] registry on it,
[2229.40 → 2230.86] and it has, it
[2230.86 → 2232.40] contains just brief
[2232.40 → 2233.78] tutorials on how to
[2233.78 → 2235.34] use the models, and
[2235.34 → 2236.22] also it has the
[2236.22 → 2237.22] datasets, right?
[2237.78 → 2239.40] So what, you could
[2239.40 → 2240.62] browse for different
[2240.62 → 2241.64] applications, so
[2241.64 → 2243.78] crops, wildfire, land
[2243.78 → 2245.34] cover, just different
[2245.34 → 2246.32] applications which you
[2246.32 → 2246.94] might want to use,
[2246.96 → 2247.88] then you get to see
[2247.88 → 2248.62] all the datasets.
[2249.42 → 2251.12] Now the API calls
[2251.12 → 2252.34] made, it's a bit
[2252.34 → 2253.44] direct as well,
[2253.58 → 2255.02] because it was made
[2255.02 → 2255.76] to be simple.
[2256.14 → 2257.12] In Python, you just
[2257.12 → 2259.24] from Radiant, ML
[2259.24 → 2260.20] Hub imports
[2260.20 → 2261.06] dataset, and then
[2261.06 → 2261.98] you specify the
[2261.98 → 2262.92] dataset which you
[2262.92 → 2263.24] want.
[2263.62 → 2264.16] For each of the
[2264.16 → 2265.16] datasets, it's a bit
[2265.16 → 2266.26] direct as well how
[2266.26 → 2266.84] to do that.
[2267.02 → 2268.06] You just proceed from
[2268.06 → 2269.42] there to build
[2269.42 → 2270.34] whatever model you
[2270.34 → 2271.28] want to build or
[2271.28 → 2272.36] analyze data.
[2273.00 → 2273.74] So it's a bit
[2273.74 → 2274.24] straightforward.
[2274.58 → 2275.46] It was made to be
[2275.46 → 2276.44] very simple for
[2276.44 → 2277.34] anyone to use.
[2277.68 → 2278.54] Everyone can view
[2278.54 → 2279.48] that as well on
[2279.48 → 2281.94] ml hub.ET, so you
[2281.94 → 2283.00] could register and
[2283.00 → 2284.22] download whatever
[2284.22 → 2285.70] datasets there and
[2285.70 → 2287.04] work with it as
[2287.04 → 2287.26] well.
[2287.26 → 2288.50] I'm wondering, as
[2288.50 → 2289.56] we sort of come
[2289.56 → 2291.02] to near to a
[2291.02 → 2292.50] close here, we've
[2292.50 → 2293.36] heard some, of
[2293.36 → 2293.88] course, very
[2293.88 → 2294.80] exciting things
[2294.80 → 2295.80] about Radiant
[2295.80 → 2296.54] Earth and the
[2296.54 → 2297.22] ML Hub.
[2297.64 → 2299.06] I wonder, Joyce, if
[2299.06 → 2300.86] you had a final
[2300.86 → 2302.26] closing question for
[2302.26 → 2303.28] the team as you're
[2303.28 → 2304.22] thinking about
[2304.22 → 2305.54] Radiant Earth, how
[2305.54 → 2307.36] it's impacting AI
[2307.36 → 2309.24] in Africa and going
[2309.24 → 2310.58] into this new year
[2310.58 → 2311.94] of work, do you
[2311.94 → 2312.94] want to maybe close
[2312.94 → 2313.76] us out with that?
[2313.76 → 2315.54] So I think also
[2315.54 → 2316.62] looking back at the
[2316.62 → 2317.46] training that we
[2317.46 → 2318.80] had, I think that's
[2318.80 → 2319.78] a very important
[2319.78 → 2321.20] thing for people to
[2321.20 → 2322.32] reflect about, that
[2322.32 → 2323.34] the resources are
[2323.34 → 2324.82] available, and also
[2324.82 → 2325.66] not that it's only
[2325.66 → 2326.46] for people in
[2326.46 → 2327.52] academia, but also
[2327.52 → 2328.58] people in industry,
[2328.80 → 2329.36] in policy.
[2329.56 → 2330.06] I remember during
[2330.06 → 2330.64] that training, we
[2330.64 → 2331.88] had people who had
[2331.88 → 2333.52] private startups that
[2333.52 → 2334.64] were looking around
[2334.64 → 2335.66] Earth observation who
[2335.66 → 2336.68] also benefited from
[2336.68 → 2337.42] the training that's
[2337.42 → 2337.90] available.
[2338.58 → 2339.32] So when I think
[2339.32 → 2340.34] about where AI is
[2340.34 → 2341.12] going in Africa, the
[2341.12 → 2341.84] things that we think
[2341.84 → 2342.64] about, one, is that
[2342.64 → 2343.44] there's capacity.
[2343.90 → 2344.54] And especially in
[2344.54 → 2345.42] a growing field,
[2345.86 → 2346.74] that like ML for
[2346.74 → 2347.70] Earth observation, so
[2347.70 → 2348.66] how do we train
[2348.66 → 2349.44] people, how do we
[2349.44 → 2350.20] build capacity?
[2350.78 → 2351.34] But then another
[2351.34 → 2352.02] thing that I also
[2352.02 → 2353.08] think about is the
[2353.08 → 2354.12] data, and through
[2354.12 → 2355.28] the Radiant ML
[2355.28 → 2356.48] Hub, the data,
[2356.76 → 2357.70] because Hamid has
[2357.70 → 2358.32] explained that they
[2358.32 → 2359.58] provide ML or AI
[2359.58 → 2360.56] ready data sets that
[2360.56 → 2361.38] people can be able to
[2361.38 → 2362.98] use for various, you
[2362.98 → 2364.06] know, solutions, or
[2364.06 → 2364.92] various problems that
[2364.92 → 2365.32] they have to
[2365.32 → 2365.94] encounter, you know,
[2365.96 → 2366.40] using Earth
[2366.40 → 2367.20] observation data.
[2367.58 → 2368.44] So I feel like that
[2368.44 → 2369.34] helps to close this
[2369.34 → 2370.16] gap that we've been
[2370.16 → 2370.98] struggling with of,
[2371.12 → 2371.56] okay, there's no
[2371.56 → 2372.60] capacity, or I'm not
[2372.60 → 2373.24] knowledgeable in that
[2373.24 → 2373.54] area.
[2373.76 → 2374.50] Okay, if I get that
[2374.50 → 2375.18] knowledge, then how do
[2375.18 → 2376.12] I gain access to the
[2376.12 → 2376.36] data?
[2376.44 → 2377.16] So the data is also
[2377.16 → 2378.22] provided, and there's,
[2378.54 → 2378.96] you know, there are
[2378.96 → 2380.36] tutorials, and it's a
[2380.36 → 2381.42] bit easy for people to
[2381.42 → 2382.56] follow through and
[2382.56 → 2383.96] practically build their
[2383.96 → 2384.96] ML, you know, models.
[2384.96 → 2387.14] So I think, I kind of feel
[2387.14 → 2388.66] like, I think, I think, I
[2388.66 → 2390.66] think, I think, I think, I
[2390.66 → 2391.44] think, I think there's
[2391.44 → 2392.20] something that I missed
[2392.20 → 2393.04] out that you think could
[2393.04 → 2394.14] be very important for us,
[2394.20 → 2395.38] for the AI community in
[2395.38 → 2397.04] Africa as we move into
[2397.04 → 2397.58] the new year.
[2397.70 → 2398.62] It would be exciting to
[2398.62 → 2399.54] hear your thoughts on
[2399.54 → 2399.78] this.
[2400.06 → 2400.74] Yeah, thank you.
[2401.06 → 2401.88] Yeah, thank you, Joyce.
[2401.96 → 2403.34] I mean, you hit it pretty
[2403.34 → 2403.58] well.
[2403.64 → 2404.48] This is about the
[2404.48 → 2405.28] community and the
[2405.28 → 2406.12] capacity, right?
[2406.12 → 2408.36] And we are acting as a
[2408.46 → 2409.02] what we call a
[2409.02 → 2410.12] collaborative agency,
[2410.60 → 2411.28] providing those
[2411.28 → 2413.06] resources and supporting
[2413.06 → 2414.38] the community to be
[2414.38 → 2415.56] helpful to their end
[2415.56 → 2416.48] users, which are
[2416.48 → 2418.26] decision makers, farmers
[2418.26 → 2419.62] on the ground, some
[2419.62 → 2420.34] people who are working
[2420.34 → 2421.62] at a sustainable kind of
[2421.62 → 2422.42] urban development.
[2422.88 → 2424.20] For us, the success of
[2424.20 → 2425.22] us is basically the
[2425.22 → 2426.22] success of those end
[2426.22 → 2427.12] users who are building
[2427.12 → 2427.90] those applications.
[2428.04 → 2429.12] So if they're more
[2429.12 → 2429.86] efficient, more
[2429.86 → 2431.06] productive in deploying
[2431.06 → 2432.04] solutions into their
[2432.04 → 2433.54] community, we are
[2433.54 → 2434.60] successful because we
[2434.60 → 2435.30] have been able to
[2435.30 → 2435.94] empower them.
[2435.94 → 2436.84] That's really how we
[2436.84 → 2437.34] look at this
[2437.34 → 2437.84] ecosystem.
[2438.42 → 2439.28] And we look forward
[2439.28 → 2440.64] to engaging with more
[2440.64 → 2441.58] partners, with more
[2441.58 → 2442.00] users.
[2442.36 → 2442.98] As Abba mentioned,
[2443.12 → 2443.86] everything on our end
[2443.86 → 2444.56] is open access.
[2444.72 → 2445.72] So feel free to start
[2445.72 → 2446.54] using the data.
[2446.94 → 2447.86] If you have data you
[2447.86 → 2448.48] want to contribute
[2448.48 → 2449.56] because ML Hub is
[2449.56 → 2450.92] an open repository, so
[2450.92 → 2452.28] you can access the data
[2452.28 → 2453.36] openly, but you can also
[2453.36 → 2454.24] contribute data.
[2454.62 → 2455.50] It is not just us
[2455.50 → 2456.62] publishing data in there.
[2456.70 → 2457.56] Many of the data sets
[2457.56 → 2458.84] are contributed by other
[2458.84 → 2460.12] providers and users.
[2460.62 → 2461.16] So if you have a
[2461.16 → 2462.12] benchmark data, you want
[2462.12 → 2462.84] to expose it to a
[2462.84 → 2464.38] broader community, please
[2464.38 → 2464.90] get in touch.
[2464.96 → 2465.68] You can publish your
[2465.68 → 2466.62] data on ML Hub.
[2466.92 → 2467.82] And we definitely are
[2467.82 → 2469.38] interested to expand the
[2469.38 → 2470.86] coverage of the data in
[2470.86 → 2472.42] terms of both geospatial
[2472.42 → 2473.86] coverage and the
[2473.86 → 2474.66] kind of application
[2474.66 → 2475.16] areas.
[2475.58 → 2476.66] And we will have more
[2476.66 → 2477.66] training and capacity
[2477.66 → 2479.46] development in 2022 and
[2479.46 → 2480.12] years beyond.
[2480.50 → 2481.38] If you have specific
[2481.38 → 2482.92] needs, you want to kind of
[2482.92 → 2484.42] get support from us, get
[2484.42 → 2484.80] in touch.
[2484.92 → 2486.36] The Slack workspace that I
[2486.36 → 2487.42] mentioned is definitely a
[2487.42 → 2488.52] good way to communicate
[2488.52 → 2488.94] with us.
[2489.00 → 2489.80] We also have support
[2489.80 → 2490.72] channel on our website,
[2490.72 → 2491.34] you can see.
[2491.84 → 2492.88] And we look forward to
[2492.88 → 2493.94] engaging more of those
[2493.94 → 2494.26] users.
[2494.46 → 2494.52] Yeah.
[2494.86 → 2495.84] Well, thank you all so
[2495.84 → 2496.08] much.
[2496.18 → 2497.38] Thank you, Joyce, for
[2497.38 → 2499.26] joining us again and for
[2499.26 → 2501.12] the Radiant Earth team for
[2501.12 → 2502.46] taking time out of their
[2502.46 → 2503.98] amazing work to have this
[2503.98 → 2504.56] conversation.
[2504.76 → 2505.72] It really is wonderful.
[2505.72 → 2507.88] And we'll include links in
[2507.88 → 2509.24] our show notes for those
[2509.24 → 2510.88] that want to jump off to
[2510.88 → 2512.76] the ML Hub to jump off to
[2512.76 → 2514.04] the open data sets and the
[2514.04 → 2515.12] competitions and the
[2515.12 → 2515.48] course.
[2516.12 → 2517.22] So please take a look,
[2517.48 → 2518.98] start to get involved in the
[2518.98 → 2519.40] new year.
[2519.78 → 2520.56] Thank you to you all.
[2520.68 → 2522.02] Have a wonderful rest of
[2522.02 → 2522.32] your day.
[2525.50 → 2526.54] That's our show.
[2526.76 → 2527.40] Thanks for listening.
[2527.92 → 2529.06] For more like this, check
[2529.06 → 2530.22] out our master feed.
[2530.38 → 2531.46] It is all Changelog
[2531.46 → 2533.56] podcasts in one easy to
[2533.56 → 2534.28] consume place.
[2534.28 → 2536.34] Let your podcast app snag
[2536.34 → 2537.62] everything we produce and
[2537.62 → 2538.84] then pick and choose which
[2538.84 → 2539.54] ones to listen to.
[2539.86 → 2540.88] Subscribe today at
[2540.88 → 2542.56] changelog.com slash master
[2542.56 → 2543.58] or just search for
[2543.58 → 2544.72] changelog master in your
[2544.72 → 2545.86] podcast app of choice.
[2546.14 → 2546.70] You'll find it.
[2547.18 → 2548.20] Special thanks to
[2548.20 → 2549.24] Break master Cylinder for
[2549.24 → 2550.76] providing our music and to
[2550.76 → 2551.94] our longtime sponsors
[2551.94 → 2553.86] Vastly, Launch Darkly and
[2553.86 → 2554.16] Linde.
[2554.70 → 2556.00] That's all for this week.
[2556.24 → 2556.98] We'll talk to you again
[2556.98 → 2557.48] next time.
[2564.28 → 2569.28] drought.
[2569.74 → 2570.64] Taught.
[2571.36 → 2572.70] Ja.
[2576.70 → 2577.66] Ha.
[2578.12 → 2579.64] Yeah.
[2579.64 → 2580.40] Ha.
[2580.86 → 2581.90] Ha.
[2581.90 → 2581.96] Ha.
[2582.10 → 2582.88] Ha.
[2582.88 → 2583.38] Ha.
[2583.38 → 2583.88] Ha.
[2586.02 → 2586.44] Ha.
[2586.44 → 2586.86] Ha.
[2586.86 → 2587.42] Ha.
[2587.42 → 2588.58] Ha.
[2588.58 → 2589.08] Ha.
[2589.08 → 2590.38] Ha.
[2590.38 → 2592.44] Ha.
[2592.44 → 2592.58] Ha.
[2592.58 → 2593.34] Ha.
