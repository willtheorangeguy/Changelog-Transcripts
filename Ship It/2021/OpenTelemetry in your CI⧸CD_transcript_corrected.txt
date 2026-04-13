[0.08 → 5.52] I'm your host, Gerhard Lasso, and you're listening to Ship It, a podcast about code,
[6.02 → 9.72] ops, infrastructure, and the people that make it happen.
[10.18 → 16.48] Yes, we focus on the people and what happens when their best ideas meet the real world.
[17.08 → 17.34] Why?
[17.74 → 23.02] Because that's how we learn, get inspired, and find out what is worth doing.
[23.26 → 29.52] Today, I'm joined by Cyril Leclerc, Product Manager, Lead on Observability at Elastic,
[30.00 → 33.36] and Oleg Finished, Principal Engineer at Cloud beast.
[33.80 → 36.34] It all started with Oleg's tweet back in July,
[36.64 → 42.28] in which he was promoting Akihito Kimchi's work on Jenkins Monitoring with Open Telemetry.
[42.66 → 45.28] This was done in the context of Google's Summer of Code,
[45.62 → 49.10] and there is a video with Akihito demoing this project in the show notes.
[49.38 → 51.42] As you may remember from episode 20,
[52.00 → 54.94] instrumenting our changelog.com pipeline is on my mind,
[55.24 → 58.62] and this conversation helped me clarify how I'm going to approach it.
[58.62 → 60.88] I have learned a lot from Oleg and Cyril,
[61.24 → 64.44] and if you're thinking of doing something similar, this episode is for you.
[64.94 → 68.70] Big thanks to our partners Vastly, Launch Darkly, and Linde.
[69.20 → 71.04] Thank you for the great bandwidth, Vastly.
[71.32 → 73.82] You can learn more at Fastly.com.
[74.54 → 79.40] Ship new features with confidence by getting your feature flags powered by LaunchDarkly.com,
[79.40 → 83.26], and thank you Linde for keeping our Kubernetes fast and simple.
[83.82 → 89.48] You too can run our infrastructure as we do by linode.com forward slash changelog.
[89.48 → 99.96] This episode is brought to you by Honeycomb.
[100.30 → 103.66] Honeycomb is built on the belief that there's a more efficient way
[103.66 → 107.10] to understand exactly what is happening in production right now.
[107.42 → 111.22] When production is running slow, it's hard to know exactly where problems originate.
[111.46 → 115.44] Is it your application code, your users, or the underlying systems?
[115.44 → 120.28] Teams who don't use Honeycomb scroll through endless dashboards guessing at what they mean.
[120.52 → 122.88] They deal with alert floods, guessing which ones matter,
[123.26 → 126.98] and go from tool to tool guessing at how the puzzle pieces all fit together.
[127.30 → 131.42] It's this context switching and tool sprawl that are slowly killing your teams and your business.
[131.82 → 134.94] With Honeycomb, you get a fast, unified, and clear understanding
[134.94 → 137.70] of the one thing driving your business, production.
[138.12 → 140.06] Honeycomb quickly shows you the correct source of issues,
[140.44 → 143.42] discover hidden problems, even in the most complex stacks,
[143.42 → 146.50] understand why you're at feel slow to only some users.
[146.96 → 149.38] With Honeycomb, you guess less and no more.
[149.82 → 154.30] Join the swarm and try Honeycomb free today at honeycomb.io slash changelog.
[154.58 → 157.26] Again, honeycomb.io slash changelog.
[157.26 → 174.30] We are going to ship in three, two, one.
[174.30 → 193.32] So, Akihito Kabuki presented Jenkins CI agents monitoring with open telemetry,
[193.68 → 196.40] and Eager, Pipkin, and Prometheus was included.
[196.40 → 200.96] And one of the goals, or like one of the reasons why I did that,
[201.36 → 205.16] was to minimize the downtime and set up costs of Jenkins agents.
[205.36 → 208.68] That was like one of the presentation, like the screenshots which I've seen.
[209.42 → 214.12] Now, Akihito couldn't join us today, but we have Cyril and Oleg joining us.
[214.62 → 218.50] And we'll be talking about open telemetry in your CI and why is it important.
[218.50 → 224.32] And I'm wondering what can you tell us about the presentation that Akihito gave back in July, I believe?
[224.64 → 225.44] I haven't seen it yet.
[225.58 → 226.66] Is it live? Can we watch it?
[226.78 → 227.38] Yes, it's live.
[227.56 → 232.78] So, it was a project within the Jenkins community as a part of the Google Summer of Code this year.
[233.44 → 238.48] Akihito was one of the students, and he chose visibility with open telemetry.
[238.78 → 242.00] Originally, the project was rather positioned towards Prometheus,
[242.30 → 244.96] but taking the recent developments and the ecosystem,
[244.96 → 251.04] we decided to press it with open telemetry and actually to try all three parts should time allow.
[251.38 → 253.98] So, metrics, visibility, and logs.
[254.12 → 256.54] For us, it was one of the missing parts of the puzzle
[256.54 → 259.68] because we already have open telemetry plugin for Jenkins.
[260.00 → 263.52] So, Cyril and many other contributors created it.
[263.76 → 267.74] But this plugin focuses on Jenkins controller as one of the instances.
[268.22 → 270.92] At the same time, Jenkins itself is a distributed system.
[270.92 → 275.58] It has agents, and actually agents may prove to be quite unstable,
[275.82 → 278.08] especially if you use multi-cloud environments,
[278.60 → 281.58] if you use various cloud provisioning, single-shot agents,
[281.70 → 283.32] which are just the day after the completion.
[283.74 → 288.12] So, it's essential to have some tracing and monitoring for these systems
[288.12 → 292.08] so that you can ensure that your CI environment is operational.
[292.70 → 296.40] And of course, if you can also verify that it's cost-effective, it would be super.
[296.40 → 302.26] Okay. So, this tracing was happening on the agents, not on the Jenkins master,
[302.74 → 306.22] so that when the jobs run, there will be visibility into the jobs
[306.22 → 310.24] and into the availability of the agents, of the Jenkins agents themselves.
[310.38 → 310.74] Is that right?
[310.94 → 311.42] Yes.
[311.86 → 312.10] Cyril?
[312.40 → 316.88] Yeah. So, here we have initiated an effort to provide visibility
[316.88 → 319.46] in the execution of the jobs themselves,
[319.98 → 326.46] where we were able to break down the duration of jobs on pipelines
[326.46 → 328.70] in the different steps of these pipelines.
[328.84 → 334.20] And also, we were able to track the time spent to allocate build agents.
[334.82 → 340.38] But then, we didn't have detailed visibility in the steps to allocate build agents.
[340.38 → 345.82] And so, we also had limited visibility to explain what kind of problems
[345.82 → 348.70] could have been happening when allocating a build agent,
[349.20 → 351.46] like cloud resources being unavailable,
[351.96 → 356.94] or maybe the Docker image you want to use being unavailable or broken, and so on.
[357.16 → 360.12] And this was an important focus of Antihero,
[360.46 → 363.24] which was to complement the existing traces we had,
[363.32 → 366.60] the existing visibility we had on the CD pipelines,
[366.60 → 371.60] detailing the agent allocation, which is on the agent communication,
[371.80 → 374.84] which are some fragile areas.
[375.26 → 375.72] That's a good summary.
[375.82 → 377.56] Okay. So, the talk is available online.
[377.62 → 378.46] We can go and watch it.
[378.64 → 381.26] I haven't watched it yet, but I will do right after this,
[381.38 → 383.68] because that's basically what started this conversation.
[384.18 → 388.12] And that made me actually think specifically about open telemetry
[388.12 → 389.74] in our CI-CD systems,
[390.28 → 393.38] and how open telemetry is like a nice unifier
[393.38 → 396.18] of all different CI and CDs that we have,
[396.18 → 400.78] because sometimes people recommend that CI is split from CD,
[401.28 → 403.26] but you still need to understand the unit as a whole.
[403.62 → 406.98] And then what happens when you switch between CDs or CI-CD systems?
[407.26 → 410.06] One day you use one, and six months later you switch.
[410.48 → 411.86] Do you lose all that visibility?
[412.40 → 414.86] Because the things that happen in your CI-CD,
[415.12 → 416.82] they kind of tend to stay the same.
[416.96 → 419.84] I mean, they may expand in the future and become more sophisticated,
[420.26 → 422.14] but the building blocks tend to be the same.
[422.14 → 426.16] So, with this context, why would you say that it's important
[426.16 → 429.34] that we use open telemetry in our CI-CD systems?
[429.68 → 430.52] Oleg, do you want to go first?
[430.64 → 430.78] Yeah.
[431.04 → 435.12] So, first, I would rather disagree with CI and CD statement.
[435.40 → 437.00] It's a subject for Holy War.
[437.24 → 440.54] Personally, I use quite old-style automation term,
[440.54 → 444.46] because CI-CD is a methodology, it might be culture,
[444.80 → 446.88] but when it comes to automation to tools,
[447.48 → 450.72] then actually CI and CD borders are quite blurry,
[450.96 → 452.94] and there are many other use cases, for example,
[453.04 → 456.36] for operations, for organization automation.
[456.68 → 457.92] All of that needs accessibility
[457.92 → 461.24] if you want to have your software delivery in place.
[461.38 → 462.40] It's not just CI-CD.
[462.40 → 466.42] And this is exactly where we can talk about open telemetry
[466.42 → 467.62] and other open standards,
[467.76 → 470.52] because if any system independently
[470.52 → 473.12] creates its own monitoring and observability,
[473.42 → 474.56] you basically get lost.
[474.98 → 477.54] So, when we talk about modern cloud native deployment
[477.54 → 478.46] with Kubernetes,
[479.06 → 481.88] you usually build your CI or CD system
[481.88 → 483.76] from dozens of different tools.
[484.30 → 486.48] Each of them may have different applications,
[486.76 → 488.34] them may have different interfaces,
[488.66 → 490.10] and then basically you end up
[490.10 → 492.38] with just trying to understand what happens.
[492.40 → 495.42] So, similarly to why Jaeger was introduced
[495.42 → 496.88] for cloud native applications,
[497.40 → 500.16] we need the same for CI, CD,
[500.56 → 502.36] and automation in the cloud,
[502.44 → 504.80] because we also need to glue information
[504.80 → 506.88] from these tools on multiple levels.
[507.26 → 508.74] So, it might be a CI server,
[508.92 → 509.76] it might be agent,
[510.00 → 512.10] it might be just a build tool like Maven,
[512.64 → 514.26] but we need all this information
[514.26 → 516.26] to understand how is our pipeline going.
[516.92 → 519.00] And now it's also important for audit,
[519.30 → 521.12] for supply chain security,
[521.12 → 523.52] and many other buzzwords that are emerging.
[524.04 → 526.18] But overall, you need data
[526.18 → 527.98] to verify what happens.
[528.50 → 531.20] And open telemetry is one of great opportunities
[531.20 → 533.88] to provide this data across the system.
[534.12 → 535.56] You said there's something fascinating
[535.56 → 537.52] about you disagreeing that CI and CD
[537.52 → 539.10] should be two separate systems.
[539.34 → 541.16] And I will want to come back to that.
[541.36 → 542.38] So, that's really important.
[542.60 → 543.86] Like, I've taken a mental note.
[544.36 → 545.96] But Cyril, why do you think
[545.96 → 547.62] that open telemetry is important
[547.62 → 549.40] for CI and CD systems?
[549.40 → 551.04] I will break down the point
[551.04 → 552.58] in two different themes.
[552.72 → 553.70] The first theme is,
[554.20 → 554.88] as you have said,
[554.92 → 556.12] there is a lot of visibility
[556.12 → 558.82] in having an end-to-end view
[558.82 → 562.14] of the execution of the CI and CD processes,
[562.50 → 564.38] where distributed traces
[564.38 → 566.12] is very valuable.
[566.12 → 569.16] And we see that distributed traces
[569.16 → 571.14] is a very good data structure
[571.14 → 573.38] to model the execution
[573.38 → 575.30] of CI and CD pipelines
[575.30 → 576.00] and processes.
[576.52 → 577.28] On exposing,
[577.66 → 578.96] meeting more practitioners
[578.96 → 580.56] with this proposal,
[580.72 → 581.90] we discover that
[581.90 → 584.32] all the data of the CD processes
[584.32 → 585.48] is a goldmine.
[585.64 → 586.00] Of course,
[586.12 → 587.20] CI and CD administrators
[587.20 → 588.52] are interested in this
[588.52 → 589.12] to troubleshoot
[589.86 → 591.10] on maintain up and running
[591.10 → 592.04] their platform.
[592.40 → 593.56] They also see benefits
[593.56 → 595.68] for sizing their platform.
[596.16 → 597.30] And then we see dev teams
[597.30 → 598.70] interesting in shortening
[598.70 → 600.48] their build cycles,
[600.78 → 602.86] in optimizing their unit tests,
[602.92 → 603.74] their flaky tests.
[604.24 → 605.72] We discover people
[605.72 → 606.92] doing cost accounting
[606.92 → 607.56] on platform,
[607.74 → 608.48] people doing,
[608.86 → 610.64] I've seen process optimization
[610.64 → 612.28] like digital transformation,
[612.64 → 613.40] agile transformation,
[613.62 → 614.24] DevOps transformation.
[614.46 → 615.14] You want to measure
[615.14 → 616.30] your lead time.
[616.70 → 617.00] And here,
[617.08 → 618.14] this is a source of data
[618.14 → 619.72] that is very interesting.
[620.50 → 621.52] So here we see
[621.52 → 622.68] a lot of value
[622.68 → 624.38] in capturing this data
[624.38 → 625.98] on distributed traces,
[626.12 → 627.34] which is often associated
[627.34 → 628.26] with open telemetry
[628.26 → 629.16] is very useful.
[629.66 → 631.82] Then what you said also
[631.82 → 632.92] that was very interesting
[632.92 → 633.44] for me is
[633.44 → 634.68] you say we want
[634.68 → 635.62] a unified view
[635.62 → 636.74] on CI and CD.
[637.34 → 638.58] And beyond this debate,
[638.68 → 639.76] is it different tools?
[639.90 → 640.94] Is it the same tools?
[641.42 → 642.84] Here is the distributed
[642.84 → 644.06] trace culture
[644.06 → 645.64] tells us that we can
[645.64 → 647.30] have an overall visibility
[647.30 → 649.00] across different phases
[649.00 → 650.48] of the cohesive unit.
[650.48 → 651.58] And so here,
[651.74 → 653.24] whatever people choose
[653.24 → 654.14] to structure
[654.14 → 655.76] their CI and CD phases,
[656.32 → 657.68] with this visibility
[657.68 → 658.76] on the process,
[658.82 → 659.50] we will be able
[659.50 → 661.14] to make this unified.
[661.44 → 662.46] Then when you talked
[662.46 → 663.82] about open telemetry,
[663.96 → 665.04] I think open telemetry
[665.04 → 666.92] is a great solution.
[667.58 → 668.00] First,
[668.10 → 669.92] it does distribute traces
[669.92 → 671.14] way well
[671.14 → 671.66] in a way
[671.66 → 672.42] that is standardized,
[673.08 → 674.52] popular for people.
[674.94 → 675.66] And also,
[675.88 → 676.66] open telemetry
[676.66 → 678.28] as the vision
[678.28 → 679.28] to provide
[679.28 → 682.02] unified semantic conventions,
[682.44 → 683.74] a common vocabulary
[683.74 → 685.54] to unify things together.
[686.04 → 686.76] And you said,
[686.92 → 688.66] I can have different CI
[688.66 → 689.58] on CD systems.
[689.58 → 691.08] And I remember this week
[691.08 → 691.78] I was talking
[691.78 → 694.24] with some CI platform administrators
[694.24 → 695.16] who told us,
[695.26 → 697.16] we don't use only Jenkins
[697.16 → 698.22] in our organization.
[698.40 → 699.10] Some other people,
[699.20 → 700.06] they use Build Kai,
[700.20 → 701.68] they use maybe other tools.
[701.68 → 703.32] And we want to have
[703.32 → 704.76] a holistic vision
[704.76 → 706.56] across all these
[706.56 → 708.74] where the CI platform
[708.74 → 710.24] is an implementation detail,
[710.36 → 711.18] which reminds me
[711.18 → 712.46] your Tiger conversation
[712.46 → 713.14] previously.
[713.72 → 714.28] These people,
[714.38 → 715.08] they are very interested
[715.08 → 716.60] in having an abstraction
[716.60 → 718.40] to look at the CD process
[718.40 → 720.06] rather than the details
[720.06 → 721.66] of each CI tool.
[722.22 → 723.30] On this culture
[723.30 → 725.66] of the open telemetry community
[725.66 → 727.54] of creating semantic conventions
[727.54 → 728.78] that spans across
[728.78 → 729.74] different tools,
[729.90 → 730.42] techniques,
[730.60 → 731.28] implementations,
[731.28 → 733.42] I think is a very good match
[733.42 → 734.44] with the problems
[734.44 → 735.22] we want to solve.
[735.76 → 737.24] So I saw these two dimensions,
[737.60 → 738.34] collecting data
[738.34 → 740.24] and also this culture
[740.24 → 742.08] of abstracting
[742.08 → 744.64] to provide a unified vision
[744.64 → 745.92] on top of different
[745.92 → 747.48] implementation details
[747.48 → 748.26] in some ways.
[748.90 → 749.90] So from the perspective
[749.90 → 752.64] of having a good CI-CD system,
[752.86 → 753.80] regardless whether it's one
[753.80 → 754.36] or multiple,
[754.78 → 756.26] which has a good
[756.26 → 757.98] open telemetry integration,
[758.50 → 760.30] what would that look like
[760.30 → 760.96] from the moment
[760.96 → 762.22] you push some code?
[762.46 → 764.08] What is like the perfect flow
[764.08 → 764.90] that you imagine
[764.90 → 765.96] that a system
[765.96 → 767.02] with good open telemetry
[767.02 → 767.76] would have?
[767.76 → 769.04] Yeah, so first,
[769.16 → 770.14] pipeline would include
[770.14 → 771.50] multiple tools in the chain.
[772.06 → 772.64] So for example,
[772.78 → 773.88] we push the code,
[774.00 → 775.62] it reaches firstly,
[775.94 → 777.76] whatever social coding system,
[777.88 → 778.62] let's say GitHub,
[778.90 → 779.40] GitLab.
[779.40 → 780.62] Even on this level,
[780.74 → 781.84] there are some events happening.
[782.14 → 782.44] Firstly,
[783.00 → 784.34] the system needs to process
[784.34 → 785.06] your request.
[785.24 → 786.20] It may apply some
[786.20 → 787.02] its own checks,
[787.12 → 787.48] for example,
[787.64 → 788.74] via GitHub actions,
[788.92 → 789.22] et cetera.
[789.74 → 790.70] And after that,
[791.10 → 792.60] our main CI starts
[792.60 → 793.60] or CD.
[794.28 → 795.02] So we invoke
[795.02 → 796.24] external service.
[796.46 → 796.68] Again,
[796.78 → 798.18] we may send webhooks
[798.18 → 799.84] to completely different instance.
[800.00 → 801.10] This instance provision
[801.10 → 803.00] whatever our build executor,
[803.12 → 804.40] it may be called the agent,
[804.70 → 806.04] it may be just a new
[806.04 → 807.68] whatever pipeline task
[807.68 → 809.02] definition in Teton
[809.02 → 810.12] in a separate container,
[810.28 → 810.84] it starts.
[811.48 → 812.72] And then we just start
[812.72 → 813.72] executing pipeline.
[814.22 → 815.26] And at this level,
[815.62 → 816.52] it's also not the end
[816.52 → 818.00] because then we invoke tools
[818.00 → 819.84] because nobody really
[819.84 → 821.10] builds software
[821.10 → 822.70] in CI or CD systems.
[822.92 → 823.88] It's external tools
[823.88 → 825.02] like Maven or Gradle
[825.02 → 825.64] doing that,
[825.76 → 826.40] you invoke them.
[826.88 → 827.58] So these tools
[827.58 → 828.56] are also complicated
[828.56 → 830.12] and you also need to have
[830.12 → 831.62] observability on this level.
[831.90 → 832.40] So basically,
[832.84 → 833.44] in the beginning
[833.44 → 834.20] of this pipeline,
[834.30 → 835.14] we should go through
[835.14 → 836.90] all these levels of tools
[836.90 → 838.02] and for each level,
[838.18 → 838.44] ideally,
[838.60 → 839.74] we need to have
[839.74 → 840.84] some data
[840.84 → 842.24] so that we can understand
[842.24 → 843.12] what happens,
[843.28 → 844.90] what are the cost blockers,
[845.08 → 845.56] for example,
[845.80 → 846.82] what are the obstacles
[846.82 → 848.22] our system experiences.
[848.94 → 850.46] And it gets complicated
[850.46 → 851.04] even more
[851.04 → 851.80] when we talk about
[851.80 → 852.36] prioritization.
[852.82 → 853.36] So basically,
[853.56 → 854.58] for each build,
[854.70 → 856.20] we need a distributed trace
[856.20 → 857.88] for going deep
[857.88 → 858.74] and hence,
[858.86 → 859.68] passing context
[859.68 → 860.36] through a level
[860.36 → 861.00] of the systems
[861.00 → 861.80] is essential.
[862.50 → 863.06] I wouldn't say
[863.06 → 863.76] that this question
[863.76 → 864.62] is fully resolved
[864.62 → 865.12] by now
[865.12 → 866.28] and I want to see
[866.28 → 867.10] much more happening
[867.10 → 867.72] on this state.
[868.06 → 869.16] But my expectation
[869.16 → 869.74] as a user
[869.74 → 871.34] to have full observability
[871.34 → 872.26] for pipeline
[872.26 → 873.64] as a single trace
[873.64 → 874.86] for all levels.
[875.24 → 876.30] And I'm looking forward
[876.30 → 877.22] to see a system
[877.22 → 878.54] that actually does that.
[878.68 → 879.30] So we understand
[879.30 → 880.38] when the pipeline starts
[880.38 → 881.80] and what happens
[881.80 → 882.56] at the beginning.
[882.76 → 883.86] The middle is always
[883.86 → 884.44] a bit hazy
[884.44 → 885.58] so we can leave it like that
[885.58 → 886.70] because it depends
[886.70 → 887.80] on what it needs to do.
[887.98 → 889.04] But I think that we all agree
[889.04 → 889.90] that when the pipeline
[889.90 → 890.66] ends,
[891.02 → 891.80] some artifact,
[892.14 → 893.06] maybe production artifact,
[893.06 → 894.38] need to be produced.
[894.38 → 894.78] Yes.
[895.20 → 895.56] Now,
[895.66 → 896.88] I know that some teams
[896.88 → 898.34] like their pipeline
[898.34 → 899.76] to end with code
[899.76 → 900.78] actually being deployed
[900.78 → 901.44] into production.
[901.64 → 902.66] What do you think about that?
[902.72 → 903.28] Do you think that
[903.28 → 904.32] that should be the last step
[904.32 → 904.84] of the pipeline?
[904.98 → 905.42] Do you think
[905.42 → 906.66] about this differently?
[907.16 → 907.34] Well,
[907.44 → 908.18] it depends on whether
[908.18 → 909.56] it's CI, CD pipeline
[909.56 → 910.84] because in CD pipeline
[910.84 → 911.98] we usually deploy
[911.98 → 913.26] as the last stage
[913.26 → 914.22] in CI pipeline
[914.22 → 915.36] even if we deploy
[915.36 → 916.00] the last stage
[916.00 → 916.78] is actually doing
[916.78 → 918.10] a lot of reporting
[918.10 → 919.30] and post-processing
[919.30 → 920.78] because it's not enough
[920.78 → 922.26] to deliver the software.
[922.26 → 922.98] we also need
[922.98 → 923.82] to do a lot
[923.82 → 924.86] of accounting work
[924.86 → 925.52] afterwards.
[925.82 → 926.46] We also need
[926.46 → 928.32] to process the results,
[928.48 → 928.92] compare them
[928.92 → 929.98] with previous runs,
[930.16 → 931.62] publish whatever coverage,
[931.76 → 932.46] test reports,
[933.04 → 934.40] and many of the things
[934.40 → 935.56] happen postpartum.
[936.00 → 937.00] Deployment is definitely
[937.00 → 937.42] important
[937.42 → 938.46] for any kind
[938.46 → 939.32] of modern pipeline.
[939.88 → 940.58] There are many
[940.58 → 942.32] other activities
[942.32 → 943.82] and task-heavy activities
[943.82 → 944.68] which still need
[944.68 → 945.22] to be delivered.
[945.68 → 946.16] And all of that
[946.16 → 947.16] involves many
[947.16 → 948.20] of external tools
[948.20 → 949.40] because you can
[949.40 → 950.82] deploy to other tools.
[950.96 → 951.54] For reporting
[951.54 → 952.54] you may use
[952.54 → 953.56] external tools
[953.56 → 955.10] like test trail
[955.10 → 956.72] it can be on-premise
[956.72 → 957.70] but still
[957.70 → 958.58] when something
[958.58 → 959.16] goes wrong
[959.16 → 960.06] you will need
[960.06 → 961.06] to access this data
[961.06 → 961.94] and you will need
[961.94 → 962.46] to understand
[962.46 → 963.04] where it went.
[963.26 → 963.90] What do you think, Cyril?
[964.02 → 964.70] I would like to
[964.70 → 965.94] come back to your question
[965.94 → 967.44] on what is the right way
[967.44 → 968.72] to instrument a pipeline.
[969.06 → 970.36] What we have discovered
[970.36 → 971.98] instrumenting
[971.98 → 972.80] Jenkins
[972.80 → 973.68] on Maven
[973.68 → 974.56] on Ansible
[974.56 → 975.88] is that
[975.88 → 976.80] instrumenting
[976.80 → 978.02] well your pipeline
[978.02 → 979.04] is a journey
[979.04 → 980.34] for the instrumentation
[980.34 → 980.72] people.
[981.24 → 982.08] We have to
[982.08 → 982.92] understand
[982.92 → 983.98] what are the right
[983.98 → 985.28] spans to capture
[985.28 → 986.62] in your pipeline execution
[986.62 → 987.46] to capture
[987.46 → 988.38] the right step.
[989.02 → 989.72] For example
[989.72 → 990.84] on Jenkins
[990.84 → 991.92] we had to iterate
[991.92 → 992.76] to capture
[992.76 → 994.24] the right spans
[994.24 → 995.32] to measure
[995.32 → 996.00] the time
[996.00 → 996.68] it was taken
[996.68 → 997.48] to allocate
[997.48 → 998.28] the build agent.
[998.68 → 999.46] Our initial
[999.46 → 1000.28] instrumentation
[1000.28 → 1000.96] did not capture
[1000.96 → 1001.44] it well
[1001.44 → 1002.64] so it was hard
[1002.64 → 1004.06] for CCD administrators
[1004.06 → 1005.30] to really
[1005.30 → 1006.10] narrow down
[1006.10 → 1006.88] their investigation
[1006.88 → 1008.02] to this specific
[1008.02 → 1008.42] phase
[1008.42 → 1009.28] on understanding
[1009.28 → 1010.22] and evolving
[1010.22 → 1011.00] across time.
[1011.66 → 1012.26] Another thing
[1012.26 → 1013.02] that was important
[1013.02 → 1013.40] for us
[1013.40 → 1014.58] was to iterate
[1014.58 → 1015.38] on the right
[1015.38 → 1016.20] attributes
[1016.20 → 1017.00] we extract
[1017.00 → 1017.72] from the pipeline
[1017.72 → 1018.22] execution
[1018.22 → 1019.60] that we attach
[1019.60 → 1020.38] to the spans
[1020.38 → 1021.64] so that you can
[1021.64 → 1022.84] get the right
[1022.84 → 1023.42] meaning
[1023.42 → 1024.34] of the data
[1024.34 → 1025.72] for your use case.
[1026.34 → 1027.08] We've seen
[1027.08 → 1028.36] that there is
[1028.36 → 1029.14] a troubleshooting
[1029.14 → 1029.80] use case
[1029.80 → 1030.32] troubleshooting
[1030.32 → 1031.18] of your pipeline
[1031.18 → 1031.68] execution
[1031.68 → 1032.78] so here maybe
[1032.78 → 1033.48] you need to
[1033.48 → 1034.08] capture
[1034.08 → 1034.42] well
[1034.42 → 1035.46] the GitHub
[1035.46 → 1036.26] access
[1036.26 → 1037.50] GitHub URL
[1037.50 → 1039.04] your Jira URL
[1039.04 → 1039.92] sometime
[1039.92 → 1040.84] you need to
[1040.84 → 1041.18] capture
[1041.18 → 1041.54] some
[1041.54 → 1042.26] organizational
[1042.26 → 1043.18] information
[1043.18 → 1044.38] if you want
[1044.38 → 1044.92] to be able
[1044.92 → 1046.00] to use
[1046.00 → 1046.56] this pipeline
[1046.56 → 1047.34] execution data
[1047.34 → 1047.98] to do some
[1047.98 → 1048.72] cost accounting
[1048.72 → 1049.56] then you need
[1049.56 → 1050.40] to associate
[1050.40 → 1051.02] attribute
[1051.02 → 1051.68] your pipeline
[1051.68 → 1052.10] execution
[1052.10 → 1052.68] to a team
[1052.68 → 1053.08] so maybe
[1053.08 → 1053.76] it's to understand
[1053.76 → 1055.00] what has caused
[1055.00 → 1055.56] your pipeline
[1055.56 → 1056.46] we are improving
[1056.46 → 1057.16] this on Jenkins
[1057.16 → 1057.72] at the moment
[1057.72 → 1058.90] how to understand
[1058.90 → 1059.70] what caused
[1059.70 → 1060.22] the execution
[1060.22 → 1060.96] of a pipeline
[1060.96 → 1061.48] to be able
[1061.48 → 1062.08] to attribute
[1062.08 → 1062.82] it to the right
[1062.82 → 1063.12] team.
[1063.48 → 1064.76] Same will be
[1064.76 → 1065.72] for using
[1065.72 → 1066.38] the pipeline
[1066.38 → 1067.26] execution data
[1067.26 → 1068.48] to understand
[1068.48 → 1069.46] the velocity
[1069.46 → 1070.06] of teams
[1070.06 → 1070.92] on the software
[1070.92 → 1072.06] delivery process
[1072.06 → 1073.62] in different
[1073.62 → 1074.88] CI platforms
[1074.88 → 1076.50] on your pipelines
[1076.50 → 1077.36] you have some
[1077.36 → 1078.14] concepts that are
[1078.14 → 1079.12] commonly used
[1079.12 → 1080.14] to define
[1080.14 → 1080.86] your business
[1080.86 → 1081.34] logic
[1081.34 → 1082.02] in Jenkins
[1082.02 → 1082.68] people commonly
[1082.68 → 1083.60] use what they
[1083.60 → 1084.12] call stages
[1084.12 → 1085.32] which is grouping
[1085.32 → 1086.16] of things
[1086.16 → 1086.72] it's maybe
[1086.72 → 1087.82] the CI build
[1087.82 → 1088.34] phase
[1088.34 → 1089.24] it's a QA
[1089.24 → 1090.20] validation phase
[1090.20 → 1091.14] it's a security
[1091.14 → 1092.18] validation phase
[1092.18 → 1092.98] and so here
[1092.98 → 1093.54] we need to
[1093.54 → 1094.12] capture the
[1094.12 → 1095.02] right attributes
[1095.02 → 1096.30] on this
[1096.30 → 1097.38] construct of
[1097.38 → 1098.14] the pipelines
[1098.14 → 1098.92] that are used
[1098.92 → 1100.42] for organizational
[1100.42 → 1100.90] grouping
[1100.90 → 1101.88] to be sure
[1101.88 → 1102.54] that the data
[1102.54 → 1103.62] will be useful
[1103.62 → 1104.68] downstream
[1104.68 → 1106.18] for the consumers
[1106.18 → 1107.06] the use case
[1107.06 → 1107.72] that will come
[1107.72 → 1108.16] one day
[1108.16 → 1124.86] what's going on
[1124.86 → 1125.16] shippers
[1125.16 → 1125.94] our friends
[1125.94 → 1126.78] at Vastly
[1126.78 → 1127.18] are running
[1127.18 → 1128.14] an amazing promo
[1128.14 → 1128.84] with massive
[1128.84 → 1129.36] savings
[1129.36 → 1130.18] on compute
[1130.18 → 1131.00] at edge
[1131.00 → 1131.78] they're inviting
[1131.78 → 1132.22] our entire
[1132.22 → 1132.72] listener base
[1132.72 → 1133.04] to move
[1133.04 → 1133.42] latency
[1133.42 → 1133.84] sensitive
[1133.84 → 1134.36] workloads
[1134.36 → 1135.02] to the
[1135.02 → 1135.46] edge
[1135.46 → 1136.10] with compute
[1136.10 → 1136.68] at edge
[1136.68 → 1137.02] free for
[1137.02 → 1137.60] three months
[1137.60 → 1138.56] plus up to
[1138.56 → 1139.50] $100,000 a month
[1139.50 → 1140.10] in credit
[1140.10 → 1140.76] for an additional
[1140.76 → 1141.44] six months
[1141.44 → 1142.96] this is a
[1142.96 → 1143.64] limited time
[1143.64 → 1144.38] offer so head
[1144.38 → 1145.50] to Fastly.com
[1145.50 → 1146.46] slash podcast
[1146.46 → 1147.56] as soon as you
[1147.56 → 1148.56] can to check it
[1148.56 → 1149.26] out and get all
[1149.26 → 1149.98] the details
[1149.98 → 1151.30] here's the TLDR
[1151.30 → 1152.52] Vastly's edge
[1152.52 → 1153.16] cloud network
[1153.16 → 1153.80] and modern
[1153.80 → 1154.26] approach to
[1154.26 → 1154.96] serverless computing
[1154.96 → 1155.86] allows you to
[1155.86 → 1156.68] deploy and run
[1156.68 → 1157.40] complex logic
[1157.40 → 1158.18] at the edge
[1158.18 → 1159.26] with unparalleled
[1159.26 → 1159.76] security
[1159.76 → 1160.72] and blazing
[1160.72 → 1161.18] fast
[1161.18 → 1161.70] computational
[1161.70 → 1162.18] speed
[1162.18 → 1163.16] scale instantly
[1163.16 → 1163.78] and globally
[1163.78 → 1164.98] reduce origin
[1164.98 → 1165.42] load
[1165.42 → 1166.24] get real-time
[1166.24 → 1166.84] observability
[1166.84 → 1167.86] and get seamless
[1167.86 → 1168.70] integration with
[1168.70 → 1169.10] you're existing
[1169.10 → 1169.72] tech stack
[1169.72 → 1171.16] head to Fastly.com
[1171.16 → 1171.94] slash podcast
[1171.94 → 1172.54] to get compute
[1172.54 → 1173.02] at edge
[1173.02 → 1173.54] free for three
[1173.54 → 1173.96] months
[1173.96 → 1174.92] plus up to
[1174.92 → 1175.96] $100,000 a month
[1175.96 → 1176.46] in credit
[1176.46 → 1176.94] for an additional
[1176.94 → 1177.62] six months
[1177.62 → 1178.78] once again
[1178.78 → 1179.84] Fastly.com
[1179.84 → 1180.68] slash podcast
[1180.68 → 1198.22] you mentioned
[1198.22 → 1199.18] Cyril about
[1199.18 → 1200.10] calculating
[1200.10 → 1201.34] or like the
[1201.34 → 1202.60] spans being
[1202.60 → 1203.16] worked out
[1203.16 → 1203.78] incorrectly
[1203.78 → 1204.64] when it comes
[1204.64 → 1205.30] to job
[1205.30 → 1205.78] allocation
[1205.78 → 1206.50] in agents
[1206.50 → 1207.52] and that was
[1207.52 → 1207.98] an interesting
[1207.98 → 1208.90] problem
[1208.90 → 1209.98] that I know
[1209.98 → 1210.94] that CCD
[1210.94 → 1211.42] administrators
[1211.42 → 1212.00] have
[1212.00 → 1212.52] there are many
[1212.52 → 1213.28] other problems
[1213.28 → 1214.36] so I'm wondering
[1214.36 → 1215.42] how does open
[1215.42 → 1216.36] telemetry help
[1216.36 → 1217.26] the CCD
[1217.26 → 1217.82] administrators
[1217.82 → 1218.38] which I think
[1218.38 → 1218.78] is a very
[1218.78 → 1219.50] important role
[1219.50 → 1220.40] it's not
[1220.40 → 1221.20] necessarily a
[1221.20 → 1221.62] person that
[1221.62 → 1222.06] does that
[1222.06 → 1223.06] it's maybe
[1223.06 → 1223.50] a role that
[1223.50 → 1224.28] many people
[1224.28 → 1224.62] share
[1224.62 → 1226.22] so how does
[1226.22 → 1227.54] this help
[1227.54 → 1227.76] them?
[1228.12 → 1229.00] So here was
[1229.00 → 1230.70] that continuous
[1230.70 → 1231.80] integration and
[1231.80 → 1232.56] continuous delivery
[1232.56 → 1233.16] pipelines
[1233.16 → 1234.54] gets more
[1234.54 → 1234.98] and more
[1234.98 → 1235.74] complicated
[1235.74 → 1237.10] with more
[1237.10 → 1237.52] complex
[1237.52 → 1238.30] orchestration
[1238.30 → 1238.86] not only
[1238.86 → 1239.56] getting source
[1239.56 → 1239.86] code
[1239.86 → 1240.50] and compiling
[1240.50 → 1240.96] it to
[1240.96 → 1241.58] create an
[1241.58 → 1241.94] artifact
[1241.94 → 1242.56] but now
[1242.56 → 1243.08] also
[1243.08 → 1244.40] creating a
[1244.40 → 1245.24] docker image
[1245.24 → 1246.02] going through
[1246.02 → 1247.10] security scanners
[1247.10 → 1248.66] triggering deployment
[1248.66 → 1249.50] in preview
[1249.50 → 1250.10] environments
[1250.10 → 1251.48] for integration
[1251.48 → 1252.26] tests or for
[1252.26 → 1253.20] human to test
[1253.20 → 1254.34] and this gets
[1254.34 → 1255.18] always more
[1255.18 → 1255.58] and more
[1255.58 → 1256.24] complicated
[1256.24 → 1257.80] involving more
[1257.80 → 1258.76] distributed
[1258.76 → 1259.42] systems
[1259.42 → 1260.04] everywhere
[1260.04 → 1261.36] so this was
[1261.36 → 1261.90] more and more
[1261.90 → 1262.56] complex to
[1262.56 → 1263.00] maintain
[1263.00 → 1263.90] up and running
[1263.90 → 1265.16] with some
[1265.16 → 1265.82] scalability
[1265.82 → 1266.32] problems
[1266.32 → 1266.74] that are
[1266.74 → 1267.56] very difficult
[1267.56 → 1268.26] because at
[1268.26 → 1268.66] some time
[1268.66 → 1269.08] of the day
[1269.08 → 1269.36] you have
[1269.36 → 1269.98] many teams
[1269.98 → 1270.76] needing to
[1270.76 → 1271.14] build
[1271.14 → 1271.78] and then you
[1271.78 → 1272.16] want to
[1272.16 → 1272.68] reduce
[1272.68 → 1273.68] your infrastructure
[1273.68 → 1274.40] for cost
[1274.40 → 1275.10] optimization
[1275.10 → 1276.38] these people
[1276.38 → 1276.82] they had
[1276.82 → 1277.58] a problem
[1277.58 → 1277.92] that was
[1277.92 → 1278.42] increasing
[1278.42 → 1278.90] and at the
[1278.90 → 1279.28] same time
[1279.28 → 1279.56] they had
[1279.56 → 1280.12] limited
[1280.12 → 1280.72] solution
[1280.72 → 1281.36] for this
[1281.36 → 1282.06] to help
[1282.06 → 1282.66] maintain
[1282.66 → 1283.32] troubleshoot
[1283.32 → 1284.34] these problems
[1284.34 → 1285.36] usually they
[1285.36 → 1285.82] are the last
[1285.82 → 1286.64] people to be
[1286.64 → 1287.52] noticed of a
[1287.52 → 1288.30] problem in
[1288.30 → 1288.98] an organization
[1288.98 → 1289.40] it's a
[1289.40 → 1289.92] deaf team
[1289.92 → 1290.60] who is under
[1290.60 → 1291.02] pressure
[1291.02 → 1291.68] who has
[1291.68 → 1292.34] this pipeline
[1292.34 → 1292.78] broken
[1292.78 → 1293.46] and they
[1293.46 → 1294.02] get very
[1294.02 → 1294.46] hungry
[1294.46 → 1295.28] they shout
[1295.28 → 1295.80] out people
[1295.80 → 1296.20] and it
[1296.20 → 1296.64] creates a
[1296.64 → 1296.88] lot of
[1296.88 → 1297.16] friction
[1297.16 → 1297.68] and so
[1297.68 → 1298.14] we felt
[1298.14 → 1298.44] these
[1298.44 → 1299.08] CI CD
[1299.08 → 1299.64] administrators
[1299.64 → 1300.40] deserve
[1300.40 → 1301.20] assistance
[1301.20 → 1302.26] something
[1302.26 → 1302.80] interesting
[1302.80 → 1303.30] that we
[1303.30 → 1303.70] observed
[1303.70 → 1304.08] as well
[1304.08 → 1304.40] is that
[1304.40 → 1305.06] observability
[1305.06 → 1305.72] says
[1305.72 → 1306.52] I need
[1306.52 → 1307.20] to be able
[1307.20 → 1307.74] to slice
[1307.74 → 1308.22] and dice
[1308.22 → 1309.02] my data
[1309.02 → 1309.64] in any
[1309.64 → 1310.06] dimension
[1310.06 → 1311.42] we saw
[1311.42 → 1311.88] when there
[1311.88 → 1312.40] is a
[1312.40 → 1313.02] CI CD
[1313.02 → 1313.48] platform
[1313.48 → 1314.12] problem
[1314.12 → 1315.04] you have
[1315.04 → 1315.42] to very
[1315.42 → 1315.74] quickly
[1315.74 → 1316.14] understand
[1316.14 → 1316.54] if this
[1316.54 → 1316.78] is a
[1316.78 → 1316.96] problem
[1316.96 → 1317.30] that is
[1317.30 → 1317.90] impacting
[1317.90 → 1318.64] just one
[1318.64 → 1318.90] team
[1318.90 → 1319.14] one
[1319.14 → 1319.62] pipeline
[1319.62 → 1319.94] maybe
[1319.94 → 1320.42] because
[1320.42 → 1320.86] Docker
[1320.86 → 1321.20] image
[1321.20 → 1321.74] used to
[1321.74 → 1322.02] build
[1322.02 → 1322.58] is broken
[1322.58 → 1323.62] or if
[1323.62 → 1323.92] it's a
[1323.92 → 1324.16] problem
[1324.16 → 1324.58] that is
[1324.58 → 1325.20] impacting
[1325.20 → 1325.94] a large
[1325.94 → 1326.42] part of
[1326.42 → 1326.62] your
[1326.62 → 1327.32] organizations
[1327.32 → 1327.74] maybe
[1327.74 → 1328.20] dozens
[1328.20 → 1328.68] of
[1328.68 → 1328.94] dev
[1328.94 → 1329.26] teams
[1329.26 → 1329.66] being
[1329.66 → 1330.08] blocked
[1330.08 → 1330.94] like
[1330.94 → 1331.30] your
[1331.30 → 1331.58] Docker
[1331.58 → 1332.04] registry
[1332.04 → 1332.48] is
[1332.48 → 1332.88] broken
[1332.88 → 1333.36] is
[1333.36 → 1334.60] unavailable
[1334.60 → 1335.76] or you
[1335.76 → 1336.18] have a
[1336.18 → 1336.44] GitHub
[1336.44 → 1337.04] outage
[1337.04 → 1337.92] so we
[1337.92 → 1338.44] wanted to
[1338.44 → 1338.76] provide
[1338.76 → 1339.42] tools to
[1339.42 → 1339.84] help
[1339.84 → 1340.44] CI CD
[1340.44 → 1341.06] administrators
[1341.06 → 1341.88] to be
[1341.88 → 1342.42] notified
[1342.42 → 1343.10] early of
[1343.10 → 1343.66] problems
[1343.66 → 1344.62] on being
[1344.62 → 1345.06] able to
[1345.06 → 1345.52] zoom in
[1345.52 → 1346.02] zoom out
[1346.02 → 1346.54] to understand
[1346.54 → 1347.16] if problems
[1347.16 → 1347.68] is impacting
[1347.68 → 1348.34] just one
[1348.34 → 1349.40] or everybody
[1349.40 → 1350.46] here it
[1350.46 → 1350.76] was a
[1350.76 → 1351.14] very good
[1351.14 → 1351.42] match
[1351.42 → 1351.74] with
[1351.74 → 1352.38] the
[1352.38 → 1352.88] problems
[1352.88 → 1353.10] that
[1353.10 → 1353.74] observability
[1353.74 → 1354.56] is solving
[1354.56 → 1355.16] at the
[1355.16 → 1355.52] moment
[1355.52 → 1355.86] with
[1355.86 → 1356.78] microservices
[1356.78 → 1358.14] architectures
[1358.14 → 1358.70] on all
[1358.70 → 1358.86] the
[1358.86 → 1359.24] investments
[1359.24 → 1359.68] that have
[1359.68 → 1360.04] been done
[1360.04 → 1360.28] on
[1360.28 → 1361.00] microservices
[1361.00 → 1361.62] architecture
[1361.62 → 1362.48] observability
[1362.48 → 1363.66] automated
[1363.66 → 1364.08] anomaly
[1364.08 → 1364.64] detection
[1364.64 → 1365.16] through
[1365.16 → 1365.58] leveraging
[1365.58 → 1366.26] statistics
[1366.26 → 1366.82] machine
[1366.82 → 1367.38] learning
[1367.38 → 1368.20] high
[1368.20 → 1369.18] cardinalities
[1369.18 → 1369.62] metric
[1369.62 → 1370.02] store
[1370.02 → 1371.00] all this
[1371.00 → 1372.08] could benefit
[1372.08 → 1372.68] a lot
[1372.68 → 1373.30] to
[1373.30 → 1374.20] CI CD
[1374.20 → 1374.82] administrators
[1374.82 → 1375.44] it was
[1375.44 → 1376.50] of the
[1376.50 → 1376.78] first
[1376.78 → 1377.22] problems
[1377.22 → 1377.72] we wanted
[1377.72 → 1377.94] to
[1377.94 → 1378.10] solve
[1378.10 → 1378.28] can you
[1378.28 → 1378.64] think of
[1378.64 → 1378.82] one
[1378.82 → 1379.22] example
[1379.22 → 1379.66] Oleg
[1379.66 → 1380.02] for
[1380.02 → 1380.38] an
[1380.38 → 1381.16] administrator
[1381.16 → 1381.78] that
[1381.78 → 1382.38] this
[1382.38 → 1382.74] tooling
[1382.74 → 1383.16] helps
[1383.16 → 1383.44] solve
[1383.44 → 1383.78] so
[1383.78 → 1384.18] for
[1384.18 → 1384.68] administrator
[1384.68 → 1385.20] when we
[1385.20 → 1385.62] talk about
[1385.62 → 1385.92] modern
[1385.92 → 1386.34] CI CD
[1386.34 → 1386.78] system
[1386.78 → 1387.18] it's
[1387.18 → 1387.52] basically
[1387.52 → 1387.84] a
[1387.84 → 1388.22] mesh
[1388.22 → 1388.48] of
[1388.48 → 1388.96] various
[1388.96 → 1389.46] asynchronous
[1389.46 → 1390.28] processes
[1390.28 → 1391.08] all these
[1391.08 → 1391.44] processes
[1391.44 → 1392.04] are loosely
[1392.04 → 1392.54] connected
[1392.54 → 1393.54] so even
[1393.54 → 1393.90] if we
[1393.90 → 1394.18] have
[1394.18 → 1394.58] one
[1394.58 → 1394.90] let's
[1394.90 → 1395.02] say
[1395.02 → 1395.46] mainstream
[1395.46 → 1396.06] pipeline
[1396.06 → 1396.40] which
[1396.40 → 1397.06] delivers
[1397.06 → 1397.48] you
[1397.48 → 1398.42] actually
[1398.42 → 1399.02] if you
[1399.02 → 1399.30] start
[1399.30 → 1399.72] looking
[1399.72 → 1400.30] under
[1400.30 → 1400.52] the
[1400.52 → 1400.74] hood
[1400.74 → 1400.96] you
[1400.96 → 1401.38] may
[1401.38 → 1401.70] notice
[1401.70 → 1401.96] that
[1401.96 → 1402.34] many
[1402.34 → 1402.78] events
[1402.78 → 1403.12] even
[1403.12 → 1403.34] in
[1403.34 → 1403.52] this
[1403.52 → 1404.06] supposedly
[1404.06 → 1404.82] one
[1404.82 → 1405.28] pipeline
[1405.28 → 1405.72] actually
[1405.72 → 1406.08] depend
[1406.08 → 1406.28] on
[1406.28 → 1406.64] other
[1406.64 → 1407.08] factors
[1407.08 → 1407.90] for example
[1407.90 → 1408.50] there might
[1408.50 → 1409.50] be provisioning
[1409.50 → 1410.08] of agents
[1410.08 → 1410.44] if we
[1410.44 → 1411.22] talk about
[1411.22 → 1411.82] the original
[1411.82 → 1412.36] work for
[1412.36 → 1412.88] monitoring
[1412.88 → 1413.48] and this
[1413.48 → 1413.80] agent
[1413.80 → 1414.34] provisioning
[1414.34 → 1414.82] doesn't have
[1414.82 → 1415.04] to be
[1415.04 → 1415.50] synchronous
[1415.50 → 1416.16] agents
[1416.16 → 1416.58] may be
[1416.58 → 1416.94] shared
[1416.94 → 1417.26] between
[1417.26 → 1417.70] different
[1417.70 → 1418.28] pipelines
[1418.28 → 1419.14] and hence
[1419.14 → 1419.70] various
[1419.70 → 1420.66] outages
[1420.66 → 1421.38] and issues
[1421.38 → 1421.98] also
[1421.98 → 1422.52] will be
[1422.52 → 1422.80] between
[1422.80 → 1423.40] multiple
[1423.40 → 1423.96] pipelines
[1423.96 → 1424.52] so being
[1424.52 → 1425.30] able to
[1425.30 → 1425.74] trace
[1425.74 → 1426.36] this event
[1426.36 → 1426.94] would help
[1426.94 → 1427.28] me as
[1427.28 → 1427.86] administrator
[1427.86 → 1428.54] to understand
[1428.54 → 1429.48] okay this
[1429.48 → 1430.10] agent is
[1430.10 → 1430.48] broken
[1430.48 → 1431.06] for example
[1431.06 → 1431.48] it has
[1431.48 → 1431.78] the wrong
[1431.78 → 1432.30] version of
[1432.30 → 1432.82] java due
[1432.82 → 1433.20] to whatever
[1433.20 → 1433.60] reason
[1433.60 → 1434.16] and then
[1434.16 → 1434.96] I can
[1434.96 → 1435.54] go back
[1435.54 → 1435.96] understand
[1435.96 → 1436.68] which pipelines
[1436.68 → 1437.32] were affected
[1437.32 → 1438.50] and restore
[1438.50 → 1439.24] them if
[1439.24 → 1439.54] needed
[1439.54 → 1440.92] and adjust
[1440.92 → 1441.64] my systems
[1441.64 → 1442.24] reschedule
[1442.24 → 1443.00] them so that
[1443.00 → 1443.82] my delivery
[1443.82 → 1444.76] continues and
[1444.76 → 1445.96] my development
[1445.96 → 1446.94] teams do not
[1446.94 → 1447.26] have those
[1447.26 → 1447.48] times
[1447.48 → 1448.06] just one
[1448.06 → 1448.54] example
[1448.54 → 1449.20] there are
[1449.20 → 1449.58] many like
[1449.58 → 1449.74] that
[1449.74 → 1450.06] that's a
[1450.06 → 1450.46] good one
[1450.46 → 1451.06] one thing
[1451.06 → 1452.34] that really
[1452.34 → 1452.80] got me in
[1452.80 → 1453.24] the past
[1453.24 → 1453.86] was caching
[1453.86 → 1454.62] in CI
[1454.62 → 1455.32] CD systems
[1455.32 → 1455.98] so when you
[1455.98 → 1456.30] have some
[1456.30 → 1456.88] basically some
[1456.88 → 1457.38] dependencies
[1457.38 → 1457.92] which have
[1457.92 → 1458.50] been cached
[1458.50 → 1459.34] and there's
[1459.34 → 1460.62] issues related
[1460.62 → 1461.44] to retrieving
[1461.44 → 1461.94] data from
[1461.94 → 1462.44] the cache
[1462.44 → 1463.64] it's so
[1463.64 → 1464.46] difficult to
[1464.46 → 1465.08] even understand
[1465.08 → 1465.48] that like
[1465.48 → 1465.82] where does
[1465.82 → 1466.20] this fit
[1466.20 → 1466.46] in my
[1466.46 → 1466.82] pipeline
[1466.82 → 1467.20] that's my
[1467.20 → 1467.58] pipeline
[1467.58 → 1468.02] depend on
[1468.02 → 1468.42] this other
[1468.42 → 1468.84] thing
[1468.84 → 1469.28] what is
[1469.28 → 1469.62] this other
[1469.62 → 1469.96] thing
[1469.96 → 1471.16] and does
[1471.16 → 1471.34] it just
[1471.34 → 1471.88] affect my
[1471.88 → 1472.36] pipeline
[1472.36 → 1472.68] did I
[1472.68 → 1473.38] mess up
[1473.38 → 1473.78] something
[1473.78 → 1474.10] in the
[1474.10 → 1474.40] caching
[1474.40 → 1474.88] maybe I
[1474.88 → 1475.18] running
[1475.18 → 1475.72] the wrong
[1475.72 → 1476.16] digest
[1476.16 → 1476.76] or maybe
[1476.76 → 1477.32] something
[1477.32 → 1478.10] just doesn't
[1478.10 → 1478.58] interact with
[1478.58 → 1478.86] the caching
[1478.86 → 1479.54] system properly
[1479.54 → 1480.86] that was so
[1480.86 → 1481.36] frustrating
[1481.36 → 1482.00] and you're
[1482.00 → 1482.16] right
[1482.16 → 1482.52] there's like
[1482.52 → 1483.30] all these
[1483.30 → 1484.16] changes that
[1484.16 → 1484.60] happen in
[1484.60 → 1485.08] pipelines
[1485.08 → 1486.20] and we don't
[1486.20 → 1486.64] know why
[1486.64 → 1487.08] they're broken
[1487.08 → 1487.62] we just know
[1487.62 → 1487.94] it doesn't
[1487.94 → 1488.24] work
[1488.24 → 1489.32] that doesn't
[1489.32 → 1489.64] tell me
[1489.64 → 1489.94] much
[1489.94 → 1490.68] and good
[1490.68 → 1490.84] luck
[1490.84 → 1491.30] debugging
[1491.30 → 1492.32] systems that
[1492.32 → 1492.62] you don't
[1492.62 → 1492.96] even know
[1492.96 → 1493.34] exist
[1493.34 → 1493.76] that's an
[1493.76 → 1494.06] interesting
[1494.06 → 1494.84] proposition
[1494.84 → 1495.48] right
[1495.48 → 1496.76] but you
[1496.76 → 1497.14] have to
[1497.14 → 1497.54] introduce
[1497.54 → 1498.26] these systems
[1498.26 → 1499.10] because caching
[1499.10 → 1500.16] is one of
[1500.16 → 1500.52] the most
[1500.52 → 1501.26] effective ways
[1501.26 → 1501.76] to reduce
[1501.76 → 1502.22] costs of
[1502.22 → 1502.78] your pipeline
[1502.78 → 1503.76] even if
[1503.76 → 1504.06] we talk
[1504.06 → 1504.62] about things
[1504.62 → 1505.16] like single
[1505.16 → 1505.96] short agents
[1505.96 → 1506.94] clean bills
[1506.94 → 1507.42] etc
[1507.42 → 1508.32] when it
[1508.32 → 1508.78] comes to
[1508.78 → 1509.42] real massive
[1509.42 → 1509.96] production
[1509.96 → 1510.54] pipelines
[1510.54 → 1511.14] we tend
[1511.14 → 1512.14] to actually
[1512.14 → 1513.26] simplify the
[1513.26 → 1513.70] things
[1513.70 → 1514.60] to application
[1514.60 → 1515.38] so that
[1515.38 → 1516.08] get better
[1516.08 → 1516.58] throughput
[1516.58 → 1517.20] because it's
[1517.20 → 1517.82] more important
[1517.82 → 1518.66] something
[1518.66 → 1518.94] something that
[1518.94 → 1519.54] identified
[1519.54 → 1520.38] also working
[1520.38 → 1520.88] on this
[1520.88 → 1521.58] visibility
[1521.58 → 1522.32] of CCD
[1522.32 → 1522.66] pipeline
[1522.66 → 1523.10] is that
[1523.10 → 1523.94] we often
[1523.94 → 1524.54] talk about
[1524.54 → 1525.26] the divergence
[1525.26 → 1526.10] between dev
[1526.10 → 1526.64] on ops
[1526.64 → 1527.80] dev wanting
[1527.80 → 1528.68] changing things
[1528.68 → 1529.32] all the time
[1529.32 → 1529.82] to deliver
[1529.82 → 1530.92] new features
[1530.92 → 1531.48] new business
[1531.48 → 1532.14] value on
[1532.14 → 1532.76] ops wanting
[1532.76 → 1533.30] stability
[1533.30 → 1534.66] we see that
[1534.66 → 1535.62] on the CCD
[1535.62 → 1536.14] platform
[1536.14 → 1536.90] we have the
[1536.90 → 1537.56] same challenge
[1537.56 → 1538.32] with CI
[1538.32 → 1538.98] administrators
[1538.98 → 1540.30] wanting a
[1540.30 → 1541.18] stable platform
[1541.18 → 1541.88] to keep it
[1541.88 → 1542.64] up and running
[1542.64 → 1543.28] because it's
[1543.28 → 1543.94] mission-critical
[1543.94 → 1544.78] for the company
[1544.78 → 1546.24] on dev teams
[1546.24 → 1547.02] wanting to
[1547.02 → 1547.68] onboard new
[1547.68 → 1548.16] projects
[1548.16 → 1548.62] with new
[1548.62 → 1549.00] needs
[1549.00 → 1549.80] new fancy
[1549.80 → 1550.84] requirements
[1550.84 → 1551.92] and we
[1551.92 → 1552.54] wanted to
[1552.54 → 1552.96] find
[1552.96 → 1553.68] assistance
[1553.68 → 1554.98] so that
[1554.98 → 1555.88] people could
[1555.88 → 1556.48] embrace
[1556.48 → 1557.04] changes
[1557.04 → 1558.06] with confidence
[1558.06 → 1558.84] and we felt
[1558.84 → 1559.56] that observability
[1559.56 → 1560.38] would be key
[1560.38 → 1561.04] to create
[1561.04 → 1561.66] this confidence
[1561.66 → 1562.46] to embrace
[1562.46 → 1562.94] changes
[1562.94 → 1563.72] on the CD
[1563.72 → 1564.22] pipelines
[1564.22 → 1564.90] that's a great
[1564.90 → 1565.46] point and it
[1565.46 → 1566.20] made me think
[1566.20 → 1566.98] of flaky
[1566.98 → 1567.78] tests when
[1567.78 → 1568.28] everything is
[1568.28 → 1568.88] fine and the
[1568.88 → 1569.54] CCD system
[1569.54 → 1570.36] still fails
[1570.36 → 1571.54] and you run
[1571.54 → 1571.86] it again
[1571.86 → 1572.18] and then it
[1572.18 → 1572.52] passes
[1572.52 → 1573.70] so I think
[1573.70 → 1574.02] flaky
[1574.02 → 1574.74] tests when
[1574.74 → 1575.02] it comes
[1575.02 → 1575.42] to
[1575.42 → 1576.08] code
[1576.08 → 1576.90] and developers
[1576.90 → 1577.64] tend to be
[1577.64 → 1578.56] very problematic
[1578.56 → 1579.78] especially for
[1579.78 → 1580.48] legacy code
[1580.48 → 1580.88] bases
[1580.88 → 1582.22] especially for
[1582.22 → 1582.72] distributed
[1582.72 → 1583.22] systems
[1583.22 → 1583.62] when you have
[1583.62 → 1584.30] tests, and you're
[1584.30 → 1584.98] testing distributed
[1584.98 → 1586.06] systems you have
[1586.06 → 1586.68] race conditions
[1586.68 → 1587.36] left right and
[1587.36 → 1587.60] centre
[1587.60 → 1588.88] so how does
[1588.88 → 1589.86] open telemetry help
[1589.86 → 1590.72] with flaky tests
[1590.72 → 1592.82] so this is in
[1592.82 → 1593.52] our radar
[1593.52 → 1594.82] to also add
[1594.82 → 1595.90] observability to
[1595.90 → 1596.60] unit test
[1596.60 → 1597.16] execution
[1597.16 → 1599.26] there is already
[1599.26 → 1600.06] a solution
[1600.06 → 1601.42] for go test
[1601.42 → 1602.40] it's written by
[1602.40 → 1603.34] Yang Logan
[1603.34 → 1604.12] who works at
[1604.12 → 1604.84] AWS where
[1604.84 → 1605.22] she has
[1605.22 → 1606.38] instrumented with
[1606.38 → 1607.32] open telemetry
[1607.32 → 1607.96] go test
[1607.96 → 1609.42] and we have
[1609.42 → 1610.10] the idea that
[1610.10 → 1610.92] it could also
[1610.92 → 1612.56] work on java
[1612.56 → 1613.60] unit test or
[1613.60 → 1614.20] any other
[1614.20 → 1615.36] language on
[1615.36 → 1615.86] that we could
[1615.86 → 1616.94] as well use
[1616.94 → 1618.06] distributed traces
[1618.06 → 1619.94] to visualize your
[1619.94 → 1620.56] unit test
[1620.56 → 1621.48] execution the
[1621.48 → 1622.36] duration on the
[1622.36 → 1623.06] outcome success
[1623.06 → 1624.58] failure on where
[1624.58 → 1625.44] I think open
[1625.44 → 1626.56] telemetry is very
[1626.56 → 1627.48] powerful is that
[1627.48 → 1629.00] every large
[1629.00 → 1630.00] organization has
[1630.00 → 1630.94] its flaky test
[1630.94 → 1632.08] detector implemented
[1632.08 → 1632.96] in some ways
[1632.96 → 1634.52] people tend to
[1634.52 → 1635.26] reinvent the wheel
[1635.26 → 1636.20] and with open
[1636.20 → 1637.14] telemetry with the
[1637.14 → 1638.54] open nature of
[1638.54 → 1639.56] its format
[1639.56 → 1641.36] then we have an
[1641.36 → 1642.24] opportunity to
[1642.24 → 1643.20] create a backbone
[1643.20 → 1644.74] of unit test
[1644.74 → 1646.20] results going
[1646.20 → 1646.88] through open
[1646.88 → 1648.10] telemetry channels
[1648.10 → 1649.16] which typically can
[1649.16 → 1649.78] be a Kafka
[1649.78 → 1651.16] streams than you
[1651.16 → 1651.70] will have dev
[1651.70 → 1652.30] ops team i
[1652.30 → 1653.62] think flaky test
[1653.62 → 1654.40] first not be
[1654.40 → 1655.22] something that an
[1655.22 → 1656.22] observability vendor
[1656.22 → 1657.92] will implement but
[1657.92 → 1659.30] maybe it will be
[1659.30 → 1660.02] DevOps team
[1660.02 → 1660.88] somewhere in an
[1660.88 → 1661.72] organization who
[1661.72 → 1662.98] will just connect
[1662.98 → 1663.86] to these Kafka
[1663.86 → 1665.00] streams of open
[1665.00 → 1665.92] telemetry traces
[1665.92 → 1667.58] create its own
[1667.58 → 1668.70] tool to process
[1668.70 → 1669.58] its flaky test
[1669.58 → 1671.14] report and share
[1671.14 → 1671.62] this with the
[1671.62 → 1672.66] community with this
[1672.66 → 1673.26] open source
[1673.26 → 1674.78] community nature i
[1674.78 → 1676.10] imagine that an
[1676.10 → 1677.08] open source solution
[1677.08 → 1678.76] will grow in the
[1678.76 → 1680.30] community leverage
[1680.30 → 1681.38] the fact that open
[1681.38 → 1682.20] telemetry is a very
[1682.20 → 1683.12] flexible architecture
[1683.12 → 1684.60] popular technology
[1684.60 → 1685.64] with open telemetry
[1685.64 → 1686.20] itself and the
[1686.22 → 1687.66] streaming like Kafka
[1687.66 → 1689.44] kinesis or google
[1689.44 → 1690.90] pub sub and so i
[1690.90 → 1691.50] see a lot of
[1691.50 → 1692.66] traction and i
[1692.66 → 1693.60] expect the solution
[1693.60 → 1694.82] to come soon in the
[1694.82 → 1695.74] community so I'm
[1695.74 → 1696.80] sold i definitely
[1696.80 → 1697.82] want open telemetry
[1697.82 → 1698.96] my CI city system
[1698.96 → 1700.04] how do I get it
[1700.04 → 1700.92] all like what do i
[1700.92 → 1702.14] do well in theory
[1702.14 → 1703.90] any system should
[1703.90 → 1704.80] include open
[1704.80 → 1706.24] telemetry or the
[1706.24 → 1707.58] Epis out of the
[1707.58 → 1708.96] box it doesn't
[1708.96 → 1709.50] happen at the
[1709.50 → 1710.30] moment because open
[1710.30 → 1711.04] telemetry is still
[1711.04 → 1712.16] emerging standard but
[1712.16 → 1713.26] how I would foresee
[1713.26 → 1715.48] it that basically any
[1715.48 → 1716.64] enterprise grade CI
[1716.64 → 1717.68] system would
[1717.68 → 1719.32] include a number of
[1719.32 → 1720.10] open telemetry
[1720.10 → 1721.36] collectors so that
[1721.36 → 1722.20] you can just connect
[1722.20 → 1723.40] to them and retrieve
[1723.40 → 1724.66] this information and
[1724.66 → 1726.18] it can be opt-in so
[1726.18 → 1727.34] that you set some
[1727.34 → 1728.38] flags for example in
[1728.38 → 1729.52] your Helen charts and
[1729.52 → 1730.86] then all your open
[1730.86 → 1732.06] telemetry collection is
[1732.06 → 1733.38] configured because it's
[1733.38 → 1734.58] again a building block
[1734.58 → 1735.86] if you need to do
[1735.86 → 1737.10] something complex to
[1737.10 → 1738.44] enable open telemetry
[1738.44 → 1739.78] that probably doesn't
[1739.78 → 1741.76] achieve its goal and
[1741.76 → 1742.80] once the technology
[1742.80 → 1743.76] measures I would
[1743.76 → 1744.62] rather expect that
[1744.62 → 1745.94] every tool just
[1745.94 → 1747.98] adopts that and it
[1747.98 → 1748.96] becomes a commodity
[1748.96 → 1750.42] for any system you
[1750.42 → 1751.36] run so what about
[1751.36 → 1752.56] today what CI city
[1752.56 → 1753.60] tool can I use today
[1753.60 → 1755.14] that has this out of
[1755.14 → 1756.22] the box wow that's a
[1756.22 → 1757.16] good question because
[1757.16 → 1758.62] actually almost none of
[1758.62 → 1759.22] the tools have
[1759.22 → 1760.38] serial ones yeah
[1760.38 → 1761.80] there are two CI
[1761.80 → 1763.24] platforms I am aware
[1763.24 → 1765.10] of who provide native
[1765.10 → 1765.90] open telemetry
[1765.90 → 1767.56] instrumentation and they
[1767.56 → 1769.96] are Jenkins and I am
[1769.96 → 1770.80] of course for the
[1770.80 → 1772.26] integration and also
[1772.26 → 1773.56] concourse CI what do
[1773.56 → 1774.84] we need to do to get
[1774.84 → 1775.66] open telemetry in
[1775.66 → 1776.94] Jenkins so you just
[1776.94 → 1778.50] need to install the
[1778.50 → 1779.82] Jenkins open telemetry
[1779.82 → 1781.28] plugin going through
[1781.28 → 1782.44] your Jenkins plugins
[1782.44 → 1784.32] manager and then you
[1784.32 → 1785.60] once Jenkins is
[1785.60 → 1786.50] instrumented with open
[1786.50 → 1787.44] telemetry you have to
[1787.44 → 1790.26] connect your Jenkins to
[1790.26 → 1791.50] an open telemetry
[1791.50 → 1793.54] endpoint backend which
[1793.54 → 1795.18] can be maybe elastic i
[1795.18 → 1796.82] work for elastic or
[1796.82 → 1798.10] maybe you can use
[1798.10 → 1799.30] Jaeger if you want to
[1799.30 → 1800.42] use Jaeger it's very
[1800.42 → 1801.76] popular open source
[1801.76 → 1802.94] distributed tracing
[1802.94 → 1804.40] visualization that has
[1804.40 → 1806.40] been created at Uber you
[1806.40 → 1807.50] will need to install a
[1807.50 → 1808.54] small component called
[1808.54 → 1809.74] open telemetry collector
[1809.74 → 1811.56] in between your CI
[1811.56 → 1812.72] platform on Jaeger
[1812.72 → 1814.18] because Jaeger don't
[1814.18 → 1815.16] speak natively open
[1815.16 → 1815.88] telemetry for the
[1815.88 → 1817.16] moment and then you
[1817.16 → 1818.64] are good to go in
[1818.64 → 1820.02] Jenkins with this open
[1820.02 → 1821.26] telemetry integration we
[1821.26 → 1822.38] have started with
[1822.38 → 1824.26] traces initially to
[1824.26 → 1825.46] trace pipeline execution
[1825.46 → 1827.18] we have also captured
[1827.18 → 1829.34] health metrics so you
[1829.34 → 1830.86] can also leverage our
[1830.86 → 1832.20] Jenkins open telemetry
[1832.20 → 1833.84] integration to capture
[1833.84 → 1835.62] the health metrics of
[1835.62 → 1837.26] your Jenkins CI platform
[1837.26 → 1839.44] route them to maybe
[1839.44 → 1842.02] Prometheus or maybe an
[1842.02 → 1843.10] open observability
[1843.10 → 1844.50] backend that support
[1844.50 → 1846.30] both traces on a
[1846.30 → 1847.86] matrix elastic being one
[1847.86 → 1849.28] I work for them but you
[1849.28 → 1850.28] will find many other
[1850.28 → 1852.04] vendors who also can
[1852.04 → 1853.50] consume all observability
[1853.50 → 1854.68] signals what about
[1854.68 → 1856.60] auto CLI from Equinix
[1856.60 → 1858.28] labs how could we use
[1858.28 → 1859.54] that to get some open
[1859.54 → 1860.90] telemetry in CI CD
[1860.90 → 1861.84] systems that maybe don't
[1861.84 → 1863.08] support if it's possible
[1863.08 → 1864.90] that's a great point as
[1864.90 → 1865.62] there were two
[1865.62 → 1866.86] initiatives that come to
[1866.86 → 1867.80] my mind I think the
[1867.80 → 1868.94] first one I saw what
[1868.94 → 1869.98] came from honeycomb
[1869.98 → 1871.40] where they created a
[1871.40 → 1873.02] small CLI to instrument
[1873.02 → 1874.60] some CI platform
[1874.60 → 1875.72] where the platform
[1875.72 → 1876.50] itself didn't
[1876.50 → 1877.52] instrument with hotel
[1877.52 → 1879.30] otherwise if you are on
[1879.30 → 1880.28] GitHub actions for
[1880.28 → 1881.64] example or maybe
[1881.64 → 1883.44] GitLab CI you would
[1883.44 → 1885.72] use hotel CLI as
[1885.72 → 1886.84] maybe a wrapper when
[1886.84 → 1887.84] you invoke your maven
[1887.84 → 1889.56] build as a wrapper when
[1889.56 → 1890.82] you use you invoke your
[1890.82 → 1892.62] Meg file also something
[1892.62 → 1894.34] even when you are inside
[1894.34 → 1896.22] Jenkins inside the CI
[1896.22 → 1897.06] platform that is
[1897.06 → 1898.26] instrumented with hotel
[1898.26 → 1899.90] traces its still very
[1899.90 → 1901.98] interesting to get more
[1901.98 → 1903.30] granularity in let's say
[1903.30 → 1904.92] Meg file because you
[1904.92 → 1906.38] discuss a lot of Meg files
[1906.38 → 1908.06] in ship it if you want
[1908.06 → 1909.20] granularity on what's
[1909.20 → 1910.02] happening in your Meg
[1910.02 → 1911.14] file you can in your
[1911.14 → 1913.10] Meg file drop some calls
[1913.10 → 1915.96] using the open CLI tool
[1915.96 → 1917.00] so that you get final
[1917.00 → 1917.98] granularity in your
[1917.98 → 1919.16] pipeline execution I'm
[1919.16 → 1920.10] probably a bit lazy
[1920.10 → 1921.40] because I just replace
[1921.40 → 1922.86] a shell on my agents
[1922.86 → 1924.50] so I modify shell on the
[1924.50 → 1925.50] docker images and
[1925.50 → 1927.08] hotel CLI is enabled by
[1927.08 → 1928.04] default there for
[1928.04 → 1928.80] screens okay
[1928.80 → 1929.32] interesting
[1929.32 → 1930.68] hackish, but it works
[1930.68 → 1931.64] do you have an example
[1931.64 → 1932.20] of how you do that
[1932.20 → 1932.82] that's very interesting
[1932.82 → 1933.56] I would like to check it
[1933.56 → 1934.68] out the code I don't
[1934.68 → 1936.02] have a code with me but
[1936.02 → 1937.34] yeah basically you can
[1937.34 → 1938.10] just take open
[1938.10 → 1939.66] telemetry you create a
[1939.66 → 1941.02] shell wrapper which
[1941.02 → 1942.56] just sends all the
[1942.56 → 1943.60] command worked in this
[1943.60 → 1944.28] shell to open
[1944.28 → 1945.80] telemetry and that's
[1945.80 → 1946.62] it okay it's wrapper
[1946.62 → 1947.66] which irritates all the
[1947.66 → 1948.68] environment and which
[1948.68 → 1950.12] is pretty transparent to
[1950.12 → 1951.50] your system as long as
[1951.50 → 1952.56] you use field scripts
[1952.56 → 1954.22] obviously if you use a
[1954.22 → 1955.70] mix let's say of bash
[1955.70 → 1957.12] python etc then you
[1957.12 → 1957.92] will have to instrument
[1957.92 → 1959.66] all of these tools which
[1959.66 → 1960.88] becomes a bit tricky but
[1960.88 → 1961.46] still possible
[1961.46 → 1963.20] you say Cyril in one of
[1963.20 → 1964.66] your talks that Jenkins
[1964.66 → 1966.08] in production is hard and
[1966.08 → 1967.06] I know a thing or two
[1967.06 → 1968.16] about that because many
[1968.16 → 1969.02] years ago we used to
[1969.02 → 1970.70] pair on getting cloud
[1970.70 → 1972.36] beast Jenkins in pivotal
[1972.36 → 1973.20] cloud foundry in the
[1973.20 → 1974.66] platform yeah that was
[1974.66 → 1975.74] like many years ago
[1975.74 → 1978.72] and I'm wondering today
[1978.72 → 1981.22] how would you run Jenkins
[1981.22 → 1982.18] in production what would
[1982.18 → 1983.44] you choose we use
[1983.44 → 1984.30] massively Jenkins
[1984.30 → 1986.32] at elastic we use it in
[1986.32 → 1988.00] conjunction with Kubernetes
[1988.00 → 1990.54] for our modern Jenkins
[1990.54 → 1992.58] platform I'm a bit
[1992.58 → 1994.10] further away from this but
[1994.10 → 1995.12] I think it is very
[1995.12 → 1996.46] important to leverage the
[1996.46 → 1998.44] flexibility of docker
[1998.44 → 2000.46] containers to let
[2000.46 → 2002.00] development team customize
[2002.00 → 2003.00] their build environment
[2003.00 → 2003.82] the way they need
[2003.82 → 2006.48] the way to offer the
[2006.48 → 2007.72] capability for dev teams
[2007.72 → 2008.86] to customize their build
[2008.86 → 2009.92] environment with docker
[2009.92 → 2011.64] combined with the
[2011.64 → 2013.94] orchestration needed by a
[2013.94 → 2015.04] CI platform and the
[2015.04 → 2016.26] scalability needed by a
[2016.26 → 2017.86] CI platform let me
[2017.86 → 2019.00] believe that you should
[2019.00 → 2020.24] leverage Kubernetes for
[2020.24 → 2020.92] this would you agree
[2020.92 → 2022.28] Oleg yes and no because
[2022.28 → 2023.88] you better deploy your CI
[2023.88 → 2025.22] system which would be
[2025.22 → 2026.16] similar to your target
[2026.16 → 2027.70] environment especially if
[2027.70 → 2028.68] you want to do integration
[2028.68 → 2030.60] tests and based on that a
[2030.60 → 2032.14] lot of depends so if you
[2032.14 → 2033.36] develop deploy cloud
[2033.36 → 2034.80] native applications then
[2034.80 → 2036.14] yeah most likely you will
[2036.14 → 2037.84] have to run Jenkins and
[2037.84 → 2039.34] Kubernetes, but it's not
[2039.34 → 2041.02] necessarily a case what i
[2041.02 → 2042.30] would like to say that if
[2042.30 → 2043.12] you talk about modern
[2043.12 → 2044.42] Jenkins management so
[2044.42 → 2045.46] everyone heard about
[2045.46 → 2046.86] Jenkins plugin hell and
[2046.86 → 2048.18] other things, and it's
[2048.18 → 2049.96] totally a case but these
[2049.96 → 2051.30] days you can fully manage
[2051.30 → 2052.16] Jenkins using
[2052.16 → 2054.34] configurations code and you
[2054.34 → 2056.24] create basically a CI CD
[2056.24 → 2057.72] pipeline for your
[2057.72 → 2058.64] automation system
[2058.64 → 2059.80] configuration as well you
[2059.80 → 2060.62] really have to be just
[2060.62 → 2062.04] Jenkins because it can be
[2062.04 → 2063.46] infrastructure as code yes
[2063.46 → 2064.38] I would definitely
[2064.38 → 2065.66] recommend packaging Jenkins
[2065.66 → 2067.20] into containers and there
[2067.20 → 2068.38] are tools for that there are
[2068.38 → 2069.44] helm charts so the
[2069.44 → 2071.10] operators provided by the
[2071.10 → 2073.20] Jenkins community but on
[2073.20 → 2074.66] the lower level you should
[2074.66 → 2076.36] always know what you run and
[2076.36 → 2077.66] you should be able to
[2077.66 → 2079.32] deploy staging and to
[2079.32 → 2080.84] verify your instance okay
[2080.84 → 2081.76] whatever is your target
[2081.76 → 2083.16] environment here something
[2083.16 → 2084.86] else on the way to build
[2084.86 → 2085.88] your continuous delivery
[2085.88 → 2087.56] pipelines and related to
[2087.56 → 2088.84] Jenkins it's a bit broader
[2088.84 → 2090.90] it's a topic you discussed
[2090.90 → 2092.18] last time when you met with
[2092.18 → 2093.22] the dagger people is it
[2093.22 → 2095.62] important to be able to run
[2095.62 → 2097.54] your CI pipeline to test it
[2097.54 → 2099.28] to develop it on your local
[2099.28 → 2101.22] computer there are two
[2101.22 → 2102.60] initiatives that struck me
[2102.60 → 2104.26] on this one was broad
[2104.26 → 2105.66] Johnson with his atomist
[2105.66 → 2108.00] company on one other is
[2108.00 → 2109.78] dagger who said it's very
[2109.78 → 2110.98] important to be able to test
[2110.98 → 2112.34] locally on the development
[2112.34 → 2114.44] cycle of the pipeline I think
[2114.44 → 2115.82] it's when you design your
[2115.82 → 2117.16] pipeline it's important to
[2117.16 → 2118.76] have as much as possible
[2118.76 → 2120.56] fragments that you can test
[2120.56 → 2122.56] locally so I believe in the
[2122.56 → 2124.52] ideas that you should have as
[2124.52 → 2126.60] little logic as possible in
[2126.60 → 2128.22] your CI proprietary
[2128.22 → 2130.08] orchestration language on that
[2130.08 → 2131.86] you should group these in
[2131.86 → 2133.76] typically make files to help
[2133.76 → 2135.54] the stability of the system
[2135.54 → 2136.98] Oleg firstly I agree that you
[2136.98 → 2137.80] should be able to test
[2137.80 → 2139.14] locally, but it doesn't mean
[2139.14 → 2140.98] that you cannot use pipeline
[2140.98 → 2142.48] definitions because many
[2142.48 → 2144.42] modern systems actually allow
[2144.42 → 2146.12] running pipelines locally it's
[2146.12 → 2147.40] not just Jenkins so for
[2147.40 → 2148.52] Jenkins we have Jenkins file
[2148.52 → 2150.34] runner for team city you can
[2150.34 → 2152.30] run contain DSL for GitHub
[2152.30 → 2154.78] there are projects as well and
[2154.78 → 2157.42] it basically poses this gap so
[2157.42 → 2158.54] if you have proper
[2158.54 → 2160.10] configuration management for a
[2160.10 → 2161.86] system if you can produce your
[2161.86 → 2163.24] production CD environment
[2163.24 → 2165.18] locally for example if you run
[2165.18 → 2167.74] the system in the container you
[2167.74 → 2169.50] can easily do local development
[2169.50 → 2170.98] and create corporate x pipelines
[2170.98 → 2172.56] so that's a good solution we
[2172.56 → 2173.64] will talk about pipeline
[2173.64 → 2175.04] development what it looks like
[2175.04 → 2177.16] but I would like to go back to
[2177.16 → 2179.44] the production question how would
[2179.44 → 2180.56] you deploy Jenkins in
[2180.56 → 2182.24] production so I think Cyril was
[2182.24 → 2183.88] mentioning Kubernetes you
[2183.88 → 2185.46] would deploy Jenkins a
[2185.46 → 2186.62] production deployment and you
[2186.62 → 2187.68] would manage Jenkins via
[2187.68 → 2189.56] Kubernetes and I imagine helm
[2189.56 → 2191.20] chart or operator what would you
[2191.20 → 2193.16] go Cyril which way I am not
[2193.16 → 2194.88] knowledgeable enough okay what
[2194.88 → 2196.54] about you like I would go with
[2196.54 → 2199.08] helm chart to be honest because
[2199.08 → 2200.70] helm chart allows being more
[2200.70 → 2202.10] flexible in terms of defining
[2202.10 → 2204.78] system okay operator has a lot of
[2204.78 → 2206.38] advantages if you want to build a
[2206.38 → 2207.98] reactive system so which is
[2207.98 → 2209.14] basically based on Kubernetes
[2209.14 → 2210.08] APIs
[2210.08 → 2212.04] text to some events automatically
[2212.04 → 2215.24] scales etc but for Jenkins to my
[2215.24 → 2217.20] experience it's not always needed
[2217.20 → 2219.52] it can be used in particular use
[2219.52 → 2219.86] cases
[2219.86 → 2223.38] so I would go with operators only if i
[2223.38 → 2226.18] was building highly available Jenkins
[2226.18 → 2227.98] solution where I would be managing
[2227.98 → 2229.76] controllers automatically
[2229.76 → 2232.42] provisioning them and if I had to
[2232.42 → 2234.28] share the context between them
[2234.28 → 2235.98] okay right now it's not quite
[2235.98 → 2238.50] possible with stock Jenkins so i
[2238.50 → 2240.10] would rather go after helm chart
[2240.10 → 2242.32] in that world where you deploy a
[2242.32 → 2243.28] where you have a production
[2243.28 → 2246.50] deployment of Jenkins using helm how
[2246.50 → 2248.92] would you configure the pipelines how
[2248.92 → 2250.10] do you configure Jenkins and then how
[2250.10 → 2251.36] would you configure for example the
[2251.36 → 2253.26] agents themselves where would that
[2253.26 → 2255.26] happen how that look like everything
[2255.26 → 2255.98] is code
[2255.98 → 2257.90] okay because currently if you talk
[2257.90 → 2259.58] about pipelines if you use Jenkins
[2259.58 → 2261.86] pipeline drop this all these
[2261.86 → 2264.12] technologies can be stored as code in
[2264.12 → 2264.86] your repository
[2264.86 → 2267.26] in parallel with your project so that
[2267.26 → 2268.96] when you build your project you have a
[2268.96 → 2270.98] pipeline, and you can test them all
[2270.98 → 2271.24] together
[2271.24 → 2273.46] and basically the same for agent
[2273.46 → 2274.02] definitions
[2274.02 → 2275.88] okay for example if you use Kubernetes
[2275.88 → 2278.06] plugin you can store agent definition
[2278.06 → 2280.52] again in the same repository so that
[2280.52 → 2282.64] you have your build system within your
[2282.64 → 2284.86] project, and it's portable, or you can
[2284.86 → 2286.94] have it separately if needed but still
[2286.94 → 2288.78] it should be defined as code somewhere
[2288.78 → 2290.96] and I would argue that actually the
[2290.96 → 2293.20] entire combination of Jenkins so for
[2293.20 → 2295.32] us it's a server itself login
[2295.32 → 2297.88] configuration pipeline libraries you use
[2297.88 → 2300.62] and the default pipeline building blocks
[2300.62 → 2302.24] all of them should be just one
[2302.24 → 2304.60] deliverable for the end system and
[2304.60 → 2306.28] this deliverable should be tested
[2306.28 → 2308.74] you know it's on ICD pipelines so there
[2308.74 → 2311.00] is much less opportunity for mistakes
[2311.00 → 2312.90] and end user pipelines
[2312.90 → 2315.08] from the perspective of code like
[2315.08 → 2317.70] config as code do you mean just
[2317.70 → 2320.16] config like YAML or some other format
[2320.16 → 2321.76] what it does that code look like
[2321.76 → 2323.62] yes so if you talk specifically about
[2323.62 → 2325.20] Jenkins pipeline yes historically it
[2325.20 → 2327.34] uses groovy DSL so it's groovy like
[2327.34 → 2329.98] language to some security and context
[2329.98 → 2332.18] requirements for failover, but it looks
[2332.18 → 2333.94] like groovy and there are multiple ways
[2333.94 → 2334.62] to define it
[2334.62 → 2337.08] so firstly it can be a scripted pipeline
[2337.08 → 2338.92] which is basically just root with a cell
[2338.92 → 2341.04] it can be declarative pipeline which
[2341.04 → 2343.54] gets us closer to obviously declarative
[2343.54 → 2345.80] syntax, but you can also deploy them as
[2345.80 → 2348.30] YAML these days okay so it's your choice
[2348.30 → 2350.44] how you actually implement them and
[2350.44 → 2351.84] Jenkins is a tool supports possible
[2351.84 → 2354.24] and would you configure Jenkins using
[2354.24 → 2357.08] the Kubernetes API or would you target
[2357.08 → 2359.66] the Jenkins master know directly how that
[2359.66 → 2362.36] works in my case I would rather use Jenkins
[2362.36 → 2365.40] for engine management because if you put
[2365.40 → 2367.66] it in Kubernetes, and it will be still a
[2367.66 → 2369.20] question how you actually retrieve
[2369.20 → 2371.98] these configurations into Jenkins and
[2371.98 → 2373.50] ultimately it doesn't matter because
[2373.50 → 2376.24] still a system in the same repository it
[2376.24 → 2378.26] doesn't matter how exactly it's deployed
[2378.26 → 2378.54] yeah
[2378.54 → 2380.16] you better get inside Jenkins just gives
[2380.16 → 2382.02] you more flexibility because if needed
[2382.02 → 2383.86] you can change on the flight without
[2383.86 → 2385.50] redeploying significant parts of your
[2385.50 → 2385.82] system
[2385.82 → 2399.24] hey shippers this episode is brought to
[2399.24 → 2401.70] you by our friends at Equinix metal if
[2401.70 → 2403.08] you want the choice and control of
[2403.08 → 2404.82] hardware with low overhead and the
[2404.82 → 2406.90] developer experience of the cloud check
[2406.90 → 2409.00] out Equinix metal deploying minutes
[2409.00 → 2411.44] across 18 global locations from silicon
[2411.44 → 2414.42] valley to Sydney visit metal.equinix.com
[2414.42 → 2416.58] slash just add metal and receive a hundred
[2416.58 → 2418.50] dollars in credit to play with again
[2418.50 → 2421.68] metal.equinix.com slash just add metal
[2421.68 → 2424.74] and by our friends at fire hydrant fire
[2424.74 → 2426.52] hydrant is the reliability platform for
[2426.52 → 2428.98] teams of all sizes with fire hydrant teams
[2428.98 → 2431.02] achieve reliability at scale by enabling
[2431.02 → 2433.50] speed and consistency from your service
[2433.50 → 2436.18] deployment to an unexpected outage here's
[2436.18 → 2437.30] the thing when your team learns from an
[2437.30 → 2439.18] incident you can codify those learnings into
[2439.18 → 2441.46] repeatable automated run books and these
[2441.46 → 2443.34] run books can create a Slack incident channel
[2443.34 → 2445.42] notify particular team members create
[2445.42 → 2448.10] tickets schedule a Zoom meeting execute a
[2448.10 → 2450.32] script or send a web hook here's how it
[2450.32 → 2452.44] works your app goes down an alert gets
[2452.44 → 2454.22] sent to a specific Slack channel which can
[2454.22 → 2456.34] then be turned into an incident that will
[2456.34 → 2458.36] trigger a workflow you've created already in
[2458.36 → 2460.94] a run book a pinned message inside slack
[2460.94 → 2463.24] will show all the details the JIRA or
[2463.24 → 2465.78] clubhouse ticket the Zoom meeting and all
[2465.78 → 2467.76] of this is contained in your dedicated
[2467.76 → 2469.90] incident channel that everyone on the team
[2469.90 → 2471.78] pays attention to now you're spending less
[2471.78 → 2473.28] time thinking about what to do next and
[2473.28 → 2474.80] you're getting to work actually resolving
[2474.80 → 2477.22] the issue faster what would normally be
[2477.22 → 2479.08] manual tickets across the entire spectrum
[2479.08 → 2481.18] of responding to an incident can now be
[2481.18 → 2483.50] automated in every single way with fire
[2483.50 → 2485.54] hydrant and here's the best part you can
[2485.54 → 2488.10] try it free for 14 days you get access to
[2488.10 → 2489.94] every single feature no credit card
[2489.94 → 2491.74] required at all that way you can prove to
[2491.74 → 2493.86] yourself and your team that this works for
[2493.86 → 2499.30] you get started at firehydrant.io again firehydrant.io
[2499.30 → 2519.40] so like I would like us to come back to the
[2519.40 → 2521.42] conversation that we started having, and we put a
[2521.42 → 2524.96] pin in it around separating the CI from the CD
[2524.96 → 2528.52] concern in your system right which gets code out
[2528.52 → 2530.88] into production what do you think about that do
[2530.88 → 2532.74] you think you should separate them or you
[2532.74 → 2535.44] shouldn't and why I would say that generally
[2535.44 → 2538.48] you should okay yes it might be
[2538.48 → 2541.36] still the same service per se in terms of
[2541.36 → 2544.92] deployment but logically CI and CD pipelines
[2544.92 → 2547.84] are significantly different, so there are
[2547.84 → 2549.64] different requirements there are different
[2549.64 → 2553.70] implementation paradigms so when you develop
[2553.70 → 2556.30] your delivery system you would rather split that
[2556.30 → 2559.16] so for example if you create a script you
[2559.16 → 2561.18] shouldn't write a built-in deploy or make
[2561.18 → 2563.86] file target you just create two ones with
[2563.86 → 2566.22] separate implementations and that you can
[2566.22 → 2568.94] maintain them separately and modify and test
[2568.94 → 2571.20] them separately if needed this is the main
[2571.20 → 2574.86] difference if you talk about CI CDs systems i
[2574.86 → 2578.40] would rather say it's implementation detail because what we want is that
[2578.40 → 2583.24] systems work for our use case if they work it's perfectly fine I know that
[2583.24 → 2589.78] in a previous episode we talk about using something like get have actions for the CI part which builds
[2589.78 → 2594.80] guess dependencies runs the tests and then something like argued for the
[2594.80 → 2599.64] deployment part where you have the artifacts and then argued just reconciles
[2599.64 → 2604.84] whatever runs in Kubernetes with the artifacts that were produced by our CI system and I thought that was a good idea
[2604.86 → 2609.34] what do you think Cyril something that comes to my mind here is that
[2609.34 → 2615.58] we are in a world where we want to automate more and more the deployment of what we produce
[2615.58 → 2621.58] so even if we decide to use two tools or maybe to put some boundaries for security
[2621.58 → 2629.18] constraints security of the supply chain process we still need a very automated way to trigger the deployment
[2629.18 → 2630.02] work through the previous mission and Processes Suzuki
[2633.96 → 2637.46] And in this sense I'm wondering if it's more alienation of tools for
[2637.46 → 2641.90] some reasons like the best tool for the job or security but your two
[2641.90 → 2645.62] processes remains completely connected together, maybe with a kind of GitHub GitHub approach
[2645.62 → 2650.12] where a GitHub manifest is sitting between the two processes.
[2650.12 → 2653.88] Git YAML manifest is sitting between the two processes,
[2654.72 → 2656.62] but the processes would remain
[2656.62 → 2658.70] integrated and connected together.
[2658.88 → 2662.02] Well, I can tell you what we changed about the whole changelog setup
[2662.02 → 2664.94] a couple of years back, where we decoupled, we used
[2664.94 → 2667.94] Concourse, by the way, to run the build, run the tests,
[2667.98 → 2670.66] and even deploy. That's what we used in the past. And we used Ansible
[2670.66 → 2674.14] in Concourse. That's what the setup was. And then I think
[2674.14 → 2677.08] 2019, if I remember correctly, we
[2677.08 → 2680.16] went to Manage CI. So we started using CircleCI
[2680.16 → 2683.10] for the build, steps, build,
[2683.20 → 2685.54] and test. And
[2685.54 → 2688.84] it stops currently today, depending on the branch.
[2688.92 → 2692.06] So the master branch is the one that produces a container image,
[2692.14 → 2695.30] which gets pushed to Docker Hub. And that's where the CI part
[2695.30 → 2698.10] stops. As for the CD part, we use
[2698.10 → 2701.28] something called Keyless. And we're meant to replace
[2701.28 → 2704.28] it, but that's what we even today, we make use of Keyless
[2704.28 → 2707.60] to watch the image. And when there are changes to the image,
[2707.64 → 2709.98] it will pull down the latest version automatically.
[2710.24 → 2712.34] There's nothing to be done. And it's because you always want
[2712.34 → 2714.40] to run the latest version. So in that
[2714.40 → 2716.52] world, we can have multiple copies
[2716.52 → 2718.36] of production, whatever that means.
[2718.68 → 2720.48] And all we have to do is tell it
[2720.48 → 2722.52] this is the artifact or artifacts
[2722.52 → 2724.32] that we want you to run.
[2724.64 → 2726.42] Whenever there's an update, run the latest.
[2727.08 → 2728.38] So we decouple the
[2728.38 → 2730.52] deployment concerns from the integration
[2730.52 → 2732.48] concerns, and we can change
[2732.48 → 2734.78] CI. We can produce those build artifacts
[2734.78 → 2736.60] whichever way we want, even locally
[2736.60 → 2738.70] if we really want to. Not a good idea,
[2738.78 → 2739.62] but it could be done.
[2740.44 → 2742.72] And it works. I'm not saying it's the best
[2742.72 → 2744.34] way, but it's what works for us.
[2744.46 → 2746.36] Yes, a good approach because CD system
[2746.36 → 2748.58] will be eventually more complex than
[2748.58 → 2750.10] CI, even in this case.
[2750.26 → 2752.38] Because it's nice to say that we just download
[2752.38 → 2754.58] our artifact, but when it comes, let's
[2754.58 → 2756.46] say, to fall over, fall over is a must
[2756.46 → 2758.40] for CD. Then, of course, various kinds
[2758.40 → 2759.64] of scalability concerns.
[2759.64 → 2762.56] Then you get a huge CD system.
[2762.86 → 2764.22] Having proper tools for that
[2764.22 → 2765.14] is definitely nice.
[2765.40 → 2766.44] This is a question for you, Oleg.
[2766.74 → 2768.40] What does your process of developing
[2768.40 → 2770.30] a CI CD pipeline look like?
[2770.46 → 2772.02] So in my case, I develop
[2772.02 → 2773.04] pipelines locally.
[2773.36 → 2774.78] I mostly use Jenkins.
[2775.12 → 2775.68] Surprise, surprise.
[2776.14 → 2778.20] I also use GitHub Actions quite a lot.
[2778.70 → 2780.48] In both cases, I run pipelines
[2780.48 → 2781.86] locally, verify them.
[2782.50 → 2784.34] And in both cases, I try to
[2784.34 → 2786.08] minimize the amount of code
[2786.08 → 2788.08] and business logic that goes to my
[2788.08 → 2789.78] user definitions, whether it's
[2789.78 → 2791.68] YAML or whether it's Jenkins file.
[2791.92 → 2794.22] Because I want to have a library
[2794.22 → 2795.04] of common steps.
[2795.34 → 2797.28] For example, if I deploy my application
[2797.28 → 2799.12] like published Docker Hub,
[2799.30 → 2800.60] it's just common step.
[2801.10 → 2803.00] Or if I build a Maven project,
[2803.00 → 2804.14] it's still a common step.
[2804.72 → 2806.54] So what happens usually is that
[2806.54 → 2808.08] there is a pipeline library that
[2808.08 → 2809.46] implements these steps.
[2809.92 → 2810.94] For these pipeline libraries,
[2811.18 → 2812.50] especially in Jenkins, you can create
[2812.50 → 2813.32] a test framework.
[2813.58 → 2814.62] You can verify them.
[2814.62 → 2817.38] And finally, I end up with my
[2817.38 → 2819.10] pipelines itself, just having
[2819.10 → 2820.92] several lines of code, which is
[2820.92 → 2822.46] basically configuration, not the
[2822.46 → 2823.72] pipeline definition itself.
[2824.32 → 2825.56] And all the pipeline exists
[2825.56 → 2827.60] separately as a separate deliverable,
[2827.76 → 2829.42] which is verified, which is
[2829.42 → 2830.82] tested against vendors,
[2830.98 → 2833.66] configurations, and which can be
[2833.66 → 2834.68] reduced quickly.
[2834.84 → 2836.60] Should I decide how to implement
[2836.60 → 2837.64] a different pipeline?
[2837.94 → 2839.52] For example, should I decide
[2839.52 → 2841.88] how I deploy the system or even
[2841.88 → 2843.02] how I build the system?
[2843.02 → 2844.60] And do you have an example that
[2844.60 → 2845.72] you can share with us for us to
[2845.72 → 2847.28] see what it looks like, the end
[2847.28 → 2848.38] result of that process?
[2848.78 → 2850.06] So one of the examples you can
[2850.06 → 2851.42] take a look at is Jenkins
[2851.42 → 2852.90] Infra slash pipeline library.
[2853.50 → 2855.18] So this is Jenkins pipeline library
[2855.18 → 2856.92] we use for building Jenkins
[2856.92 → 2857.36] components.
[2857.92 → 2859.72] We have something like 1800
[2859.72 → 2862.24] plugins available in our
[2862.24 → 2862.86] update centres.
[2863.38 → 2864.98] And basically we have two standard
[2864.98 → 2866.14] flows right now, Maven and
[2866.14 → 2866.64] Gradle.
[2866.98 → 2868.46] So for these flows, we offer
[2868.46 → 2869.28] pipeline library.
[2869.46 → 2871.04] It is very complex inside.
[2871.22 → 2872.34] So for example, there is common
[2872.34 → 2873.66] once they build plugin and has
[2873.66 → 2875.70] something like 300 lines in the
[2875.70 → 2876.40] pipeline library.
[2876.94 → 2879.32] But for end users like our
[2879.32 → 2881.00] Jenkins plugin developers and
[2881.00 → 2882.88] maintainers, they just get this
[2882.88 → 2884.96] build plugin step where they pass
[2884.96 → 2886.42] several options, like whether they
[2886.42 → 2888.16] want to build on Linux, Windows,
[2888.34 → 2889.86] which Jenkins core versions they
[2889.86 → 2890.78] want to test against.
[2891.10 → 2891.60] And that's it.
[2891.72 → 2893.32] So it's basically one or two lines.
[2893.52 → 2894.20] You can take a look.
[2894.34 → 2895.56] I will share the link later.
[2895.92 → 2898.54] It's all open source and all CIE is
[2898.54 → 2899.28] also accessible.
[2899.72 → 2900.12] Take a look.
[2900.12 → 2900.54] I will.
[2900.66 → 2900.78] Yeah.
[2900.82 → 2901.42] Thank you for that.
[2901.52 → 2903.56] And there is a test automation for
[2903.56 → 2905.06] both unit tests and integration
[2905.06 → 2905.80] tests there.
[2905.90 → 2906.20] Thank you.
[2906.28 → 2907.50] I'll definitely check that out.
[2907.56 → 2908.78] And I'll also include it in the
[2908.78 → 2909.20] show notes.
[2909.44 → 2909.64] Cyril?
[2909.86 → 2911.54] Listening to you, it reminds me
[2911.54 → 2913.14] something that I saw when I was
[2913.14 → 2914.70] working on continuous delivery,
[2914.90 → 2916.76] continuous integration, when I was
[2916.76 → 2918.18] product manager at Cloud Bees two
[2918.18 → 2920.66] years ago, is the importance of
[2920.66 → 2923.40] standardization of the processes.
[2923.40 → 2926.60] We should manage the CI process, CI
[2926.60 → 2928.32] pipelines, CI, CD pipelines of
[2928.32 → 2930.86] applications of microservices as
[2930.86 → 2932.56] a kettle, not as pets.
[2933.10 → 2935.68] I see the same question on
[2935.68 → 2937.86] observability, where the observability
[2937.86 → 2939.74] of your different applications on
[2939.74 → 2941.36] microservices in your organization
[2941.36 → 2944.02] should also be managed as a kettle
[2944.02 → 2945.24] rather than as pets.
[2945.76 → 2947.62] And I think this is a very important
[2947.62 → 2950.54] thing for your operations to remain
[2950.54 → 2951.06] sustainable.
[2951.06 → 2953.26] Speaking about important things,
[2953.60 → 2955.76] Dan Lawrence was saying this.
[2956.90 → 2959.22] Your build system should be at least
[2959.22 → 2960.82] as secure as your production
[2960.82 → 2961.40] environment.
[2961.60 → 2962.64] What do you think about that, Cyril?
[2962.74 → 2964.58] What I think about is, yes, we have
[2964.58 → 2967.02] seen it last year with supply chain
[2967.02 → 2968.58] attacks that have been visible.
[2968.86 → 2970.70] It's also something for which we are
[2970.70 → 2973.22] thinking about on the open telemetry
[2973.22 → 2975.00] instrumentation of the continuous
[2975.00 → 2977.34] delivery pipeline, where we see the
[2977.34 → 2980.30] importance of capturing audit trails
[2980.30 → 2983.70] of the CD processes, including the logs,
[2984.34 → 2985.72] as something critical.
[2985.96 → 2988.38] And we think that using open telemetry,
[2988.50 → 2991.44] it will be easier than ever to route
[2991.44 → 2993.96] all your audit trail of your release
[2993.96 → 2996.42] processes, build process of what you
[2996.42 → 2998.38] ship in production, to route them
[2998.38 → 3001.38] directly in this very secure, long-term,
[3001.54 → 3004.02] cost-effective storage, being your logs
[3004.02 → 3004.80] management system.
[3004.80 → 3007.36] It could be maybe an S3 bucket or maybe,
[3007.58 → 3009.66] let's say, your Splunk, Elastic, or you
[3009.66 → 3011.26] name it, a long-term storage.
[3012.04 → 3013.88] So this is what comes to my mind.
[3013.98 → 3015.50] And then there are some other
[3015.50 → 3018.20] requirements for the CCD companies,
[3018.38 → 3020.46] but I am less involved in this at the
[3020.46 → 3020.72] moment.
[3020.72 → 3022.24] How do you think about supply and chain
[3022.24 → 3024.76] security within the CCD space, Oleg?
[3024.76 → 3026.42] I definitely support this topic.
[3026.58 → 3027.92] It's very important.
[3028.38 → 3031.84] And when SolarWinds was announced one year
[3031.84 → 3034.02] ago, we actually had a Jenkins
[3034.02 → 3035.66] governance board meeting and then
[3035.66 → 3037.18] discussion at the contributor summit.
[3037.18 → 3039.82] And we decided to prioritize supply and
[3039.82 → 3041.70] chain security as one of the major
[3041.70 → 3043.38] topics for this year for Jenkins
[3043.38 → 3043.94] community.
[3044.64 → 3046.36] And if you have seen, there is a lot of
[3046.36 → 3047.66] activities on this front.
[3047.78 → 3049.30] For example, dependency updates.
[3049.54 → 3051.62] We invest quite a lot in tooling,
[3052.10 → 3054.24] in dependency scanning, in bills of
[3054.24 → 3054.94] materials.
[3055.28 → 3057.26] So currently we can produce S-bombs for
[3057.26 → 3058.48] companies if needed.
[3059.54 → 3061.44] And indeed, this is important.
[3061.60 → 3064.10] And it's important for us because we are
[3064.10 → 3065.50] a second-level supplier.
[3065.50 → 3067.24] We depend on so many libraries.
[3067.64 → 3069.22] We need to verify them, but we also
[3069.22 → 3071.64] need to provide a good level of trust
[3071.64 → 3074.20] so that users of Jenkins and of our
[3074.20 → 3076.02] systems can safely deliver their
[3076.02 → 3076.58] software.
[3077.12 → 3078.52] Something that comes to my mind here
[3078.52 → 3080.76] that I touched when I was working on
[3080.76 → 3082.98] CI and that I see also now that I work
[3082.98 → 3086.16] on observability is the importance of
[3086.16 → 3088.62] capturing the right information in the
[3088.62 → 3089.36] bill of material.
[3090.12 → 3091.86] And I think it's also an incremental
[3091.86 → 3092.38] journey.
[3092.82 → 3094.84] First, you build on your Docker
[3094.84 → 3096.30] environment, but if you don't capture
[3096.30 → 3100.12] exactly the hash of the Docker image that
[3100.12 → 3103.18] was used to run your build, it's too late.
[3103.26 → 3105.26] You will not be able to re-understand it
[3105.26 → 3106.16] 12 months later.
[3106.74 → 3108.48] And so I think there is an incremental
[3108.48 → 3109.04] journey.
[3109.38 → 3111.62] It's a continuous exercise to verify that
[3111.62 → 3114.82] the data you capture in your build are good
[3114.82 → 3117.12] enough to understand what actually happened.
[3117.12 → 3119.28] You mentioned the problem is the usage of
[3119.28 → 3119.98] cache system.
[3119.98 → 3123.48] Do I capture all the details to understand
[3123.48 → 3125.26] what artifact was retrieved from my
[3125.26 → 3126.10] caching system?
[3126.26 → 3127.08] Have I been poisoned?
[3127.94 → 3130.40] And this is a never-ending exercise in
[3130.40 → 3132.64] some ways to always capture the right
[3132.64 → 3133.94] metadata on your build.
[3134.36 → 3136.54] Is Captain Obvious involved in any of
[3136.54 → 3136.90] this, Oleg?
[3137.04 → 3139.50] Yes and no, because I'm currently building
[3139.50 → 3142.46] a prototype which integrates Jenkins,
[3142.84 → 3144.72] Open Telemetry, and Captain.
[3144.72 → 3147.40] But for me, the main objective is to actually
[3147.40 → 3149.48] expose more information about quality
[3149.48 → 3149.92] gates.
[3150.20 → 3152.66] So when we deliver software, we can verify
[3152.66 → 3155.42] that all items are basically delivered
[3155.42 → 3157.58] with all matching criteria.
[3157.86 → 3160.10] So currently, Captain is mostly built around
[3160.10 → 3161.96] cloud events, which is probably a topic for
[3161.96 → 3162.72] separate discussion.
[3163.36 → 3165.94] Captain exposes Open Telemetry metrics on
[3165.94 → 3168.48] its own, so you can understand what happens
[3168.48 → 3170.34] inside Captain when you analyze, for example,
[3170.50 → 3171.66] quality gates, etc.
[3171.66 → 3174.42] But it would also be great to have integration
[3174.42 → 3175.40] in other directions.
[3175.72 → 3179.18] So when CI-CD systems supply information about
[3179.18 → 3182.38] the status, metrics, and especially all
[3182.38 → 3185.22] deployment parameters, tools like Captain,
[3185.40 → 3187.66] so that they can make decisions whether the
[3187.66 → 3190.40] system is compliant with the expectations
[3190.40 → 3192.48] of our CI-CD admins.
[3192.70 → 3194.98] How can we follow up on what Captain is up
[3194.98 → 3195.60] to these days?
[3195.86 → 3197.32] Captain Obvious, specifically?
[3197.54 → 3200.12] Well, Captain Obvious, it was just Nick in
[3200.12 → 3202.00] my talk, which is coming soon.
[3202.44 → 3204.52] And yes, it's talk-driven development because
[3204.52 → 3206.96] I needed to implement a few bits for streaming
[3206.96 → 3207.80] events properly.
[3208.50 → 3210.94] So stay tuned, maybe announcement in a few
[3210.94 → 3211.22] months.
[3211.48 → 3211.54] Okay.
[3211.64 → 3214.30] Captain itself is basically a project, a member
[3214.30 → 3216.08] of Cloud Native Computing Foundation.
[3216.34 → 3218.48] It's currently a sandbox project.
[3218.64 → 3220.92] There are discussions about making it an incubating
[3220.92 → 3221.40] project.
[3221.52 → 3221.70] Okay.
[3221.94 → 3224.04] And it has quite vibrant community.
[3224.20 → 3227.06] There are meetings every week, including today,
[3227.26 → 3229.04] developer or user meetings.
[3229.04 → 3231.10] So if you want to join the community, you're
[3231.10 → 3231.84] welcome to do so.
[3232.12 → 3232.68] I just joined.
[3232.90 → 3233.68] That's a good shout out.
[3233.88 → 3234.02] Okay.
[3234.36 → 3236.60] So there's a question that I've been dying to
[3236.60 → 3239.00] ask since we began this recording.
[3239.66 → 3241.38] What made you move to Switzerland, Oleg?
[3241.58 → 3243.72] I moved to Switzerland because Cloud Vis is
[3243.72 → 3244.26] based there.
[3244.50 → 3247.12] Actually, I joined Cloud Vis when I was in Russia.
[3247.36 → 3249.72] But due to various non-technical reasons, it
[3249.72 → 3251.94] was more reasonable to have me in Switzerland than
[3251.94 → 3252.48] in Russia.
[3252.78 → 3254.26] And yeah, I got an opportunity.
[3254.60 → 3255.90] And Switzerland is a nice country.
[3256.12 → 3256.22] Right.
[3256.22 → 3258.82] For the record, I'm a big fan of Scandinavia.
[3259.08 → 3260.48] But Switzerland is good.
[3260.96 → 3261.62] And why not?
[3261.82 → 3262.42] I moved to there.
[3262.58 → 3263.64] How long have you been in Switzerland?
[3263.96 → 3264.70] How long have you been living?
[3264.84 → 3265.76] Five and a half years.
[3265.84 → 3267.68] So that's a long time to really appreciate the
[3267.68 → 3267.94] country.
[3268.04 → 3269.82] So like six months, and it's like the honeymoon
[3269.82 → 3270.24] period.
[3270.38 → 3270.54] Okay.
[3270.70 → 3272.92] I like this country and I like the city where I am
[3272.92 → 3274.92] because I'm in the French-speaking part.
[3275.60 → 3277.66] And there are a lot of advantages here.
[3277.76 → 3279.00] Which city are you in Switzerland?
[3279.28 → 3279.84] Norshotel.
[3279.98 → 3282.10] I think one of the advantages was you not needing
[3282.10 → 3282.86] a car, right?
[3282.90 → 3284.28] And you being very excited about that.
[3284.28 → 3285.82] Where the public transport is perfect.
[3285.92 → 3286.08] Okay.
[3286.44 → 3288.92] So as we are preparing to wrap this up, I'm
[3288.92 → 3290.96] wondering what is the most important takeaway
[3290.96 → 3292.16] for our listeners, Cyril?
[3292.36 → 3292.90] Thank you.
[3293.08 → 3297.08] The most important takeaway for me is the
[3297.08 → 3300.12] importance of the open source and standard
[3300.12 → 3304.74] nature of open telemetry to succeed to observe
[3304.74 → 3306.02] CCD pipelines.
[3306.02 → 3311.48] both to succeed in instrumenting these very, these very rich
[3311.48 → 3316.74] communities of tools involved in the CD processes and also
[3316.74 → 3321.20] communities that will consume all the observability data we
[3321.20 → 3325.28] produce, which are not only CI administrators, but as we have
[3325.28 → 3329.88] said, also developers for their pipelines, people doing cost
[3329.88 → 3333.86] accounting, people doing reporting on the delivery process.
[3333.86 → 3340.96] And on CCD data are gold mines that we succeed in exposing songs to the
[3340.96 → 3345.18] popularity of this open source standard, which is open telemetry.
[3345.18 → 3345.54] Okay.
[3345.66 → 3346.46] That's a good one.
[3346.60 → 3347.38] What about you, Alec?
[3347.42 → 3348.68] Let's support this statement.
[3349.10 → 3353.42] So data is the new oil, and it applies everywhere, including CCD world.
[3354.16 → 3358.38] And actually you can use this data and not just analyze it and optimize your
[3358.38 → 3360.18] pipelines, but also to make decisions.
[3360.18 → 3366.66] Because the same approaches as artificial intelligence, et cetera, they apply not only
[3366.66 → 3372.06] to production systems and use cases, not only to speed rating, but also to your CCD.
[3372.42 → 3377.92] Because once you analyze tests properly, once you can get better insights in tests and
[3377.92 → 3384.18] coverage, once you can show developers what are the issues, you can actually improve developer
[3384.18 → 3388.26] velocity a load, and you can reduce costs for your development.
[3388.46 → 3390.94] And more importantly, you can shorten your delivery cycle.
[3391.08 → 3396.98] So this data, which is exposed by open telemetry is essential to actually improving your pipelines
[3396.98 → 3397.92] to the next stage.
[3398.12 → 3402.94] The thing which gets me really excited is that regardless what system you're using, as long
[3402.94 → 3406.44] as you emit open telemetry events, you can get the same view.
[3406.44 → 3410.78] Even when you switch between systems, that gets me really excited because then you're
[3410.78 → 3412.76] free to pick mix and match.
[3413.00 → 3413.88] It doesn't really matter.
[3413.98 → 3415.56] Just pick the right tool for the right job.
[3416.06 → 3419.38] But we will understand the same things even when you move between systems.
[3419.64 → 3420.56] I think that's really exciting.
[3420.80 → 3422.06] Yeah, it's exciting.
[3422.34 → 3427.32] And when you operate with multiple systems in parallel, which is what's happening in the
[3427.32 → 3430.64] real life of not small organization or large organizations.
[3430.64 → 3436.22] I'm looking forward to it that foundations and various working groups start working on
[3436.22 → 3440.96] specific standards for open telemetry so that they actually standardize the events.
[3441.14 → 3443.52] Because right now it's still an open question.
[3444.00 → 3450.06] So it's a very idealistic view that every CI system exposes the same events, the same metrics
[3450.06 → 3450.94] and the same logs.
[3451.10 → 3452.48] It's not a case yet.
[3453.02 → 3455.32] And there is a lot of standardization work to happen.
[3455.86 → 3460.42] I see such work, for example, happening in the Continuous Delivery Foundation for CD events.
[3460.42 → 3464.32] But for open telemetry, I would like to see that as well.
[3464.52 → 3465.06] That's a good point.
[3465.16 → 3465.60] Yeah, you're right.
[3465.80 → 3466.88] It's still very early days.
[3466.94 → 3471.42] As you mentioned, this whole new ecosystem is still very young, right?
[3471.46 → 3474.18] It only just started maybe a year ago, two years ago.
[3474.34 → 3475.48] It's very recent anyway.
[3475.72 → 3478.78] Yeah, it's just a sandbox project in ICCF these days.
[3479.16 → 3484.56] But I hope that it will become incubating very soon because the adoption for open telemetry
[3484.56 → 3485.66] is already massive.
[3486.00 → 3488.52] And there are so many players on this space.
[3488.52 → 3492.88] So from my point of view, it's totally justified that it's transferred to incubating.
[3493.12 → 3496.36] Is there anything coming in the next six months that you want to share with us, Cyril?
[3496.58 → 3502.54] We have just donated the open telemetry Maven integration to the open telemetry community.
[3503.08 → 3505.48] So it's moving fast, and we get feedback.
[3505.64 → 3507.00] So we are progressing fast here.
[3507.06 → 3507.58] It's great.
[3508.22 → 3510.48] The open telemetry Ansible integration.
[3510.48 → 3515.52] We have donated the Ansible integration to the Ansible community itself.
[3516.20 → 3522.42] We are iterating at the moment, and we are rolling it out inside Elastic to really battle
[3522.42 → 3523.06] test this.
[3523.26 → 3524.94] So it's moving as well.
[3525.04 → 3530.18] So these are great milestones for us to expand the ecosystem of tools that we integrate.
[3530.36 → 3531.32] Oleg, what about you?
[3531.44 → 3533.60] It's kind of public and changing jobs.
[3533.82 → 3538.44] I still cannot announce what's the next one, but I'm sure it will be quite interesting.
[3538.44 → 3540.00] It's around open source.
[3540.42 → 3542.62] It's around observability as well.
[3543.44 → 3547.86] I will definitely keep working with Cyril and many other contributors in this area.
[3548.12 → 3549.04] Looking forward to that.
[3549.56 → 3551.04] We will keep working on Jenkins.
[3551.42 → 3557.60] I will be publishing my vision for Jenkins and some bits of the roadmap in the coming weeks.
[3558.22 → 3562.10] So that if you're interested to see Jenkins evolution, the community is strong.
[3562.26 → 3564.92] There are a lot of different developments happening in there.
[3564.92 → 3570.32] Yeah, I'm looking forward to seeing what we ship to the users in just a few months, maybe
[3570.32 → 3570.62] years.
[3570.80 → 3572.30] Well, this has been a great discussion.
[3572.64 → 3573.24] Thank you very much.
[3573.28 → 3575.88] There are so many things they need to go and check up on now.
[3575.98 → 3577.42] All very exciting things.
[3577.72 → 3582.08] And I look forward to what happens in six months in this space because it's really, really
[3582.08 → 3582.42] interesting.
[3582.56 → 3584.12] It just ties so many things together.
[3584.26 → 3584.88] I'm very excited.
[3585.32 → 3586.22] Thank you very much for today.
[3586.22 → 3586.96] Thank you very much.
[3587.08 → 3587.30] Thank you.
[3587.30 → 3593.40] Thank you for tuning in to another episode of Ship It.
[3593.76 → 3595.60] I enjoyed making it for you.
[3595.82 → 3598.94] This is just one of the podcasts for developers that we ship.
[3599.30 → 3602.76] Go to changelog.com forward slash master for the rest.
[3603.32 → 3609.32] You can join me and the rest of our community at changelog.com forward slash community.
[3609.92 → 3611.50] There are no imposters in our stack.
[3611.86 → 3613.10] Everyone is welcome.
[3613.10 → 3618.24] Huge thanks to our partners Vastly, Launch Darkly and Linde.
[3618.86 → 3622.18] Thank you, Break master Cylinder for all our awesome beats.
[3622.70 → 3623.80] That's it for this week.
[3624.12 → 3624.82] See you next week.
[3643.10 → 3653.00] Game on.
