[0.36 → 5.90] You are listening to Ship It, a podcast about operations, infrastructure, and Christmas
[5.90 → 6.36] presents.
[6.82 → 11.92] I'm your host, Gerhard Lazy, and today we have a special Christmas episode, which sums
[11.92 → 15.18] up two months of very early mornings and a few late nights.
[15.78 → 21.58] We have pull request 395, a CCD Lego set with Guillaume de Reville and Joel Longtime,
[22.46 → 28.70] continuous CPU profiling with Frederic Branch, which is PR396, as well as auto-restoring
[28.70 → 33.04] Kubernetes clusters with Dan Magnum and Mubarak Onus, PR399.
[33.84 → 38.62] While I initially intended us to have five Christmas presents in total, only three got
[38.62 → 39.38] delivered in time.
[39.84 → 44.16] We planned, worked hard, and eventually shipped the best version just in time for Christmas.
[44.88 → 49.76] My hope is that the latest additions to our changeup.com GitHub repository will help you
[49.76 → 52.36] just as much as they will help our 2022 setup.
[53.10 → 54.24] Merry Shipman, everyone.
[54.62 → 58.46] Big thanks to our partners Vastly, Launch Darkly, and Linde.
[58.70 → 60.56] Thank you for the great band with Vastly.
[60.80 → 62.78] You can learn more at Fastly.com.
[63.32 → 67.44] Ship new features with confidence by getting your feature flags powered by LaunchDarkly.com.
[67.92 → 70.92] And thank you, Linde, for keeping our Kubernetes fast and simple.
[71.38 → 75.28] Run your setup as we do via linode.com forward slash changelog.
[75.28 → 86.64] We are going to ship in three, two, one.
[86.64 → 107.18] The first present this Christmas is a CI CD Lego set that changelog.com is already using for production.
[107.18 → 114.16] The entire store, including code and screenshots, are available in our GitHub repository, cPullRequest395.
[114.68 → 120.72] Our new pipeline gets coding to prod at least twice as fast as before, and you can see it running in GitHub Actions.
[121.40 → 128.68] Since we recorded this, we made it over a minute quicker, which is a big deal when everything is taken less than five minutes in total.
[128.68 → 132.90] And there is one more pull request open, which will improve it even more.
[133.52 → 136.26] Check the name of the person that opened PR401.
[137.08 → 142.10] If you like the queue language and understand the potential of direct-to-cyclical graphs for pipelines,
[142.60 → 145.84] this present will take your CI CD to a whole new level.
[145.84 → 154.08] So in episode 23, we were talking to Sam and Solomon about this new universal deployment engine called Dagger.
[154.44 → 155.42] That's how it was introduced.
[156.08 → 163.02] And one of the things which I mentioned towards the end is that I would like to make it part of the changelog infrastructure.
[163.56 → 164.70] So, hi, Joel.
[164.88 → 165.62] Hi, King.
[166.32 → 166.58] Hello.
[167.26 → 167.80] How are you?
[167.84 → 168.52] How are you doing today?
[168.78 → 168.98] Good.
[169.16 → 170.06] Excited to be here with you.
[170.52 → 171.26] Yeah, same for me.
[171.26 → 173.80] How was it for you to work on this?
[173.92 → 178.94] Because we didn't have a lot of time, really, and we tried to squeeze it around all sorts of things.
[179.26 → 181.82] What was it like the last month working on this?
[182.42 → 183.12] Tell us about it.
[183.72 → 185.96] For me, it was fun.
[186.86 → 195.90] It gave me an opportunity to dig into Dagger and the tool and the way that we use it more than I had thus far.
[196.48 → 198.34] I'm relatively new to Dagger.
[198.34 → 202.80] So this was part of my learning about how our system actually works.
[203.76 → 215.60] And it was fun to kind of begin to grok how we use Q, how we use Build Kit, and how the layers and different file system states work together in those contexts.
[216.10 → 225.90] And it was also fun to work with you and Guillaume and try to figure out how to replicate what you've done in CircleCI inside of Dagger.
[225.90 → 234.86] Like you said, in part so that we could actually transition it over to GitHub Actions or wherever else you wanted to run it.
[235.04 → 235.16] Right.
[235.24 → 235.68] I got you.
[236.36 → 237.38] What about you, Guillaume?
[237.70 → 240.68] For me, it was really fun working with you.
[240.68 → 246.24] One of the things, maybe some of the headaches, because I didn't know CircleCI.
[247.00 → 250.98] And it's quite interesting to, because as I was helping you, I know Dagger.
[251.40 → 252.38] I don't know this technology.
[252.60 → 255.68] So to help you port it, I had to learn a lot of things, mix.
[255.82 → 256.62] I didn't get it.
[256.78 → 259.52] And we encountered a lot of issues along the way.
[259.52 → 265.32] And in order to tweak them, to fix them, you need to properly understand what you're doing.
[265.52 → 269.92] Because your config at the moment, the SULCI one, is quite a big one.
[270.30 → 273.24] And in order to port it, we need to understand it properly.
[273.56 → 274.50] But it was a lot of fun.
[275.08 → 276.60] That is actually my key takeaway as well.
[276.76 → 278.52] You know, I wasn't expecting to learn as much.
[278.76 → 281.02] I was hoping, but I wasn't expecting it.
[281.54 → 284.20] And then, you know, with you two, it was great.
[284.20 → 285.60] We went on such a journey.
[286.28 → 293.26] And I think what helped is that we didn't have a lot of time, but we had long gaps between us working together.
[293.66 → 298.04] So maybe it was like a couple of days, and then we got again for like half an hour or an hour or an hour.
[298.84 → 300.44] Joel, you're in Colorado.
[301.00 → 303.10] And Guillaume is in Paris, so he's like an hour ahead of me.
[303.34 → 306.80] I think that really helped, because we, in a way, we found a pace.
[307.26 → 309.14] And then we just bounced ideas off one another.
[309.44 → 311.70] And we bridged that gap really nicely, I think.
[311.70 → 322.90] Yeah, I think that's one of the things that I got out of this, too, is just where we are now and what's possible with Dagger today and some of the difficulties that we currently have.
[323.22 → 331.20] Interesting interactions between Q and Build Kit and how we're interpreting that Q and applying it to Build Kit states.
[331.78 → 338.90] And then kind of what we're doing with this new release, just what I'm seeing as being possible in that context.
[338.90 → 342.96] And just how much more intuitive and powerful it's going to be.
[344.16 → 351.22] So that was part of what was fun for me, was learning what our current state is while learning where we're headed.
[352.12 → 356.94] And seeing where that delta is actually going to be an immense improvement in the tool.
[357.90 → 360.12] So what does the new pipeline look like?
[360.36 → 363.64] We get and compile the dependencies, and we do this in parallel.
[363.64 → 365.32] So we do test and we do prod.
[365.82 → 367.46] The tests, we need to compile them.
[367.68 → 369.08] Then we use a cache.
[369.38 → 371.14] And this is something to do with the volumes, right?
[371.18 → 372.98] Like to copy all the layers.
[373.30 → 377.18] We don't need to go into too much detail, but it's Build Kit and Q working together.
[377.58 → 378.56] And then we run the tests.
[379.04 → 381.44] Before we can run the tests, we need to start the test database.
[381.86 → 382.74] It's an ephemeral one.
[382.78 → 387.72] It's just a container, PostgreSQL, because the tests are integration tests, some of them.
[388.00 → 388.94] So they need a database.
[388.94 → 392.22] And then we stop the database when the tests finish running.
[392.44 → 394.68] Now in parallel, we resolve the assets.
[394.96 → 398.10] These are like the CSS, JavaScript, all that in development.
[398.84 → 400.96] It's like a step towards production.
[401.20 → 402.28] Then we digest them.
[402.86 → 405.32] And that is one of the inputs to the production image.
[406.10 → 410.58] On the right-hand side, we have to compile the dependencies for production.
[410.94 → 412.40] We have the same caching mechanism.
[412.72 → 417.90] And this is like, it's a necessary step based on the current version of Dagger,
[417.90 → 420.40] which, by the way, this is something which will improve.
[421.66 → 423.22] And how do I know that?
[423.30 → 424.72] Well, Joel's been telling me all about it.
[424.74 → 426.82] And he's been very excited, right, to work on that.
[426.90 → 429.06] And maybe you want to mention a little bit about that.
[430.50 → 430.68] Yeah.
[430.86 → 436.48] So we're basically improving the DX, the developer experience,
[436.86 → 444.92] around the low-level interactions that Dagger has with Build Kit.
[444.92 → 450.28] So we're basically changing the API to Build Kit.
[450.48 → 456.62] Right now we have kind of an implicit, kind of spread all over the place API to Build Kit
[456.62 → 459.60] instead of our Q packages.
[460.80 → 464.50] And the changes that we're in the process of building out
[464.50 → 467.10] actually make that API much more explicit.
[467.10 → 468.00] Right.
[468.00 → 472.92] Kind of form like a low-level representation of the Build Kit API within Q,
[473.64 → 477.28] which then can be used by our packages or other packages
[477.28 → 481.12] to interact with Build Kit,
[481.38 → 487.46] the various file system states and actions on those file systems as well.
[487.46 → 490.84] So, yeah, I think this is going to get a lot better.
[491.68 → 493.58] We'll be able to actually use some of the features
[493.58 → 497.26] that we weren't able to use this time around of Build Kit,
[497.38 → 500.32] like mounting volumes in a much cleaner way.
[501.00 → 501.16] Okay.
[501.66 → 502.86] And then when that is done,
[503.16 → 506.76] the last step is to obviously assemble the image and push it to Docker Hub.
[506.94 → 509.38] The one step which we don't have here, and we would want
[509.38 → 514.94] is to Git commit the digest of the image that was deployed
[514.94 → 517.20] so that we can do like a proper Git Ops way
[517.20 → 520.36] so that rather than our production pulling latest,
[521.14 → 522.92] and, you know, there's like a couple of issues around that,
[523.02 → 526.04] I won't go into them, but we know we have to improve that.
[526.52 → 529.38] We would like Dagger in this case to make that Git commit.
[529.68 → 532.40] And I say Dagger, but now that I realize it could just be GitHub Actions.
[532.40 → 533.58] And why do I say that?
[534.16 → 535.38] Part of this pull request,
[535.72 → 536.96] we did the integration with GitHub Actions
[536.96 → 538.00] and we'll get to that in a minute.
[538.00 → 540.98] But first, I would like to show
[540.98 → 543.92] what the new pipeline looks like and what makes it better.
[544.24 → 548.78] So what are these green items here, Guillaume?
[548.88 → 550.02] How would you describe these?
[550.26 → 550.72] What are they?
[551.08 → 552.36] These are, I think it's actions.
[552.98 → 556.62] And so an action, it represents a step.
[557.08 → 560.02] So in general, it lies inside a definition in Dagger.
[560.46 → 564.38] And so how do you build a Dagger pipeline?
[564.68 → 567.60] You just assemble actions in and all together.
[568.00 → 570.84] And at runtime, we build a DAG.
[571.72 → 576.78] A little above, that's how you have like parallel dependency builds.
[577.12 → 577.38] Okay.
[577.56 → 578.34] What is an action?
[578.46 → 580.78] If you had to describe it, Joel, how would you describe an action?
[581.24 → 585.04] An action typically would be like a collection of build kit steps.
[585.04 → 587.52] So the people familiar with Docker,
[587.96 → 591.54] like a specific commands within a Docker file,
[591.88 → 597.96] like a copy or an exec, you know, an env, those sorts of things.
[598.82 → 603.42] They basically represent a stage within build kit.
[603.42 → 608.30] And typically one of these actions is going to be a set of those steps.
[608.88 → 612.60] So it might be a number of runs within a container, you know,
[612.72 → 615.86] evening a shell script or something along those lines,
[615.86 → 619.12] and then getting the kind of resulting file system state.
[619.12 → 621.48] They all run in the context of container, right?
[621.56 → 625.28] So when you think of a step, there is a container which gets created,
[625.54 → 628.86] that step runs, and there are some inputs and outputs for that one step.
[629.24 → 629.78] Is that correct?
[630.32 → 630.58] Yeah.
[630.72 → 632.48] Yeah, that's a great way of describing it.
[632.58 → 634.50] So you have a set of inputs.
[634.78 → 636.04] That could be a file system state.
[636.14 → 638.00] That could be a volume mount.
[638.08 → 639.64] It could be secret mounts as well.
[639.64 → 643.70] This is something that's a piece of build kit
[643.70 → 648.48] and some of the new features that Docker build got as a result of build kit.
[648.68 → 651.04] So you have all these inputs coming into this node,
[651.26 → 654.68] which is that file system state plus some action.
[655.76 → 659.16] And then something results from that.
[659.46 → 664.10] You know if you're doing an echo hello to world.txt,
[664.48 → 667.86] then that new file system state has that new file on top of it.
[667.98 → 668.18] Right.
[668.56 → 668.74] Yeah.
[668.74 → 672.20] So if you can see here, these steps, I mean, there's no cache, right?
[672.26 → 674.72] If you remember the Docker file, if you think about that,
[675.02 → 677.86] and how some of those commands could be cached,
[677.96 → 678.74] and then they're really quick.
[678.80 → 680.16] Like, for example, here, app image.
[680.54 → 683.66] You can think of it almost like, you know, like a command in the Docker file.
[683.78 → 686.02] So that is cached and takes 0.9 seconds.
[686.36 → 688.22] It just has to verify where it is in the cache.
[688.42 → 689.52] Now, these run in parallel,
[689.66 → 691.44] and we'll do a run for you to see what they look like.
[691.90 → 695.14] But this whole pipeline as a whole, even though it looks flat,
[695.42 → 698.46] it runs in parallel, and it takes 190 seconds.
[698.46 → 702.68] So it's a slight improvement over the three minutes and 38 seconds,
[702.76 → 703.40] which we had here.
[704.00 → 708.10] But you have to realize that these three minutes and 38 seconds will always be just that.
[708.52 → 709.08] It doesn't matter.
[709.54 → 710.56] I mean, this is using caching.
[711.48 → 715.28] But Dagger, if it does use the caching, if everything is cached,
[715.52 → 718.48] if it doesn't have to compile anything, it just has to run the tests themselves,
[718.80 → 720.30] it's five times quicker.
[721.08 → 722.54] And that is a huge speed up.
[723.00 → 726.62] So this pipeline run, all of it took 45 seconds,
[726.74 → 728.80] and the test took the longest 42 seconds,
[729.26 → 731.36] versus three minutes and 38.
[731.98 → 733.80] So much, much quicker.
[733.80 → 736.52] And by the way, this will run against any Docker daemon.
[736.66 → 737.70] That's the only requirement.
[737.84 → 738.48] You need Build Kit.
[739.02 → 741.54] And the easiest way of getting Build Kit is just in your Docker.
[741.64 → 742.38] It already has it.
[742.94 → 745.50] So there's no special CI setup required.
[745.60 → 748.44] You can run this anywhere, whether it runs the same way,
[748.60 → 749.80] whether it runs in GitHub Actions,
[750.50 → 752.20] CircleCI, or your local machine,
[752.36 → 753.18] which is really cool.
[754.12 → 757.48] The other very cool feature is that Open Tracing is built in.
[758.10 → 759.80] So what it means is that you can see
[759.80 → 762.40] what does the span look like
[762.40 → 766.14] for a cached run versus an unbaked run.
[766.20 → 767.92] And all you have to do is run Jaeger
[767.92 → 770.24] and have an environment variable.
[770.32 → 772.68] By the way, all this code, all integration is here.
[773.12 → 775.32] So if you look at pullRequest395, you can see all of it.
[775.92 → 777.80] So what we're seeing here is that this cached run,
[777.86 → 779.50] we can see compiling the dependencies,
[779.50 → 782.36] and you can see that some of these steps run in parallel.
[782.36 → 784.78] So devs compiled prod are still running
[784.78 → 788.54] while the test cache already started here.
[789.46 → 791.26] Same thing, image prod cache started here,
[791.36 → 792.72] assets, devs, so on and so forth,
[792.78 → 793.74] and tests, right?
[793.76 → 794.46] The tests are running,
[794.58 → 795.56] and we are already,
[796.52 → 798.22] we started building the production image.
[798.88 → 800.96] And that is the beauty of the pipeline, right?
[800.98 → 803.62] Like you want to run as many things as you can in parallel,
[804.44 → 807.14] and I do like optimistic branching, it's called in CPUs.
[807.28 → 809.20] And then when you get to the end of it,
[809.32 → 810.32] it's just like last step.
[810.44 → 811.94] You know, you assume that everything will just work.
[811.94 → 813.32] And that's what will make it really quick.
[813.72 → 815.46] So you can see what the cached run looks like.
[815.50 → 817.60] You can see that all these steps are really, really quick.
[818.08 → 819.36] The tests take the longest.
[819.70 → 823.36] And all in all, we're done in 47 seconds, 46.98.
[823.46 → 824.24] Let's be precise.
[824.82 → 825.02] Okay?
[825.32 → 828.32] I think that's one of the beautiful things about Dagger
[828.32 → 830.34] and our use of Build Kit too,
[830.44 → 835.30] is that because we're describing at a very fine-grained level,
[835.30 → 841.24] the relationships between these relatively fine-grained steps
[841.24 → 844.82] that might be, you know, within the context of an action.
[844.98 → 847.26] We can run many of those in parallel.
[847.68 → 850.16] So if you need to go run a bunch of things along,
[850.86 → 852.10] say, the assets pipeline,
[852.36 → 857.02] you can do that at the same time that you're doing stuff with mix.
[857.02 → 859.26] And then, like you said,
[859.40 → 861.86] you're basically waiting for both of those things to be done
[861.86 → 864.90] because those are inputs to some next stage.
[865.96 → 869.10] And you could imagine much more complicated versions of this as well,
[869.56 → 872.50] where you're going and building a ton of microservices in parallel.
[872.84 → 873.50] Yeah, exactly.
[874.62 → 876.12] What about the GitHub Actions integration?
[876.22 → 876.92] Well, this is a screenshot.
[877.04 → 877.70] This is what it looks like.
[877.74 → 879.18] We want to do like a point in time,
[879.42 → 880.86] and we can see how much quicker this is.
[880.96 → 882.54] But I would like to talk about this,
[882.72 → 884.28] and maybe Guillaume can run us through it.
[884.38 → 885.32] What does this look like?
[885.32 → 886.52] This is the GitHub Actions config.
[886.78 → 888.04] So what can you tell us about it, Guillaume?
[888.10 → 889.16] How do you read this?
[889.16 → 892.66] So it's like a normal GitHub Action.
[893.16 → 896.40] What I see here, you have environment variables,
[896.88 → 900.72] so Docker host, the hotel, so the Jaeger endpoint.
[901.30 → 901.60] Okay.
[902.14 → 904.28] And then you have a job, only one job,
[904.60 → 906.82] which is this name CI.
[907.32 → 908.30] It runs on Ubuntu.
[909.16 → 912.40] So you just check out the code for the context of the changes.
[912.40 → 916.82] And then you use basically Dagger here.
[917.32 → 917.96] The Dagger Action.
[918.08 → 918.34] Or Action.
[918.72 → 919.72] The Dagger Action, exactly.
[920.40 → 923.06] And then you configure the Tail scale Tunnel.
[923.16 → 925.48] I think it's for you, I believe.
[926.22 → 927.66] Yeah, because this Docker is remote.
[927.78 → 928.20] That's right.
[928.50 → 930.88] And it's the same Docker host, which I use locally.
[930.98 → 932.74] Like I don't run Docker locally.
[932.98 → 934.48] I just have a Tail scale Tunnel,
[934.56 → 935.88] which connects me to that host.
[936.04 → 938.70] And it's the same host that the CI uses.
[938.70 → 941.12] Now there's an improvement to be made there,
[941.18 → 942.94] and we'll get to that maybe at the end.
[943.12 → 945.00] But yeah, it's the same one.
[945.16 → 948.78] So if it runs locally, it will run exactly the same in CI.
[949.22 → 950.22] And that's really cool, I think.
[950.58 → 951.84] And what about this last step?
[952.20 → 954.58] Basically, it's the step you do when you run it locally.
[954.94 → 956.46] You just do a Dagger rep,
[956.84 → 958.96] and I presume you have an input,
[960.04 → 961.52] you have specified an input,
[961.70 → 963.60] which is a local folder.
[964.06 → 964.20] Yeah.
[964.24 → 966.74] And you don't have to specify it.
[966.74 → 967.14] That's right.
[967.22 → 968.98] So if you want to see the glue code,
[969.06 → 970.78] so the Dagger up, you're right.
[970.80 → 973.82] It's just a step which already takes some values
[973.82 → 974.88] that have been pre-configured.
[975.42 → 977.02] So those values are committed,
[977.34 → 978.74] including the secrets, by the way.
[979.66 → 981.54] I'm using this really cool thing called SOPS.
[981.70 → 983.12] You may have heard of it from Mozilla
[983.12 → 984.32] to encrypt all the secrets.
[984.74 → 986.76] So we have to set in terms of a secret,
[986.98 → 990.20] the H key for them to be able to be decrypted.
[990.36 → 992.30] Like if you think of it like the private key.
[993.14 → 995.30] And yeah, everything just works.
[995.30 → 996.90] So we commit secrets, right?
[997.48 → 998.42] We're crazy, I know.
[999.12 → 1000.32] No, actually it works really well.
[1000.46 → 1001.68] It's a done thing.
[1001.72 → 1003.26] And I waited for a long time to do this.
[1003.30 → 1003.88] I'm really excited.
[1004.12 → 1006.62] So this is what the glue code looks like locally.
[1007.82 → 1010.82] So it's basically what puts everything together.
[1011.90 → 1013.82] It is a make file.
[1014.10 → 1014.82] That's what we use.
[1014.88 → 1015.94] It just makes things easier.
[1016.00 → 1017.20] It just runs a bunch of commands.
[1017.20 → 1020.44] And what I would like to point out is, for example,
[1021.22 → 1022.72] the new CI package.
[1022.98 → 1024.18] So it declares new CI.
[1024.30 → 1024.92] This is a plan.
[1025.22 → 1025.72] Is that right?
[1026.06 → 1027.70] Is it called a plan or is it an environment?
[1028.10 → 1029.64] It's an environment in the current version.
[1030.06 → 1034.32] And we're transitioning to the name plan or DAG potentially.
[1034.52 → 1034.74] Right.
[1035.10 → 1035.84] Oh, that's a good one.
[1036.00 → 1036.48] DAG this.
[1037.64 → 1038.34] DAG this.
[1039.20 → 1040.70] It asked me to enter my username.
[1040.82 → 1042.34] This will be stored encrypted, by the way,
[1042.34 → 1044.82] because it's, no, this will be stored as text.
[1045.26 → 1045.94] Nothing secret.
[1046.08 → 1046.56] It's Gerhard.
[1046.64 → 1047.42] You already guessed it.
[1047.78 → 1050.26] And then it asks me for my Docker Hub password
[1050.26 → 1051.96] so that it can push the image.
[1052.48 → 1056.24] These are stored encrypted using SOPs locally.
[1056.44 → 1058.28] And then there's like a couple of things here.
[1058.36 → 1059.18] We'll skip over them.
[1059.26 → 1060.44] And then we provide the inputs.
[1060.96 → 1063.98] Those inputs are important because that's what the environment
[1063.98 → 1067.36] or the plan or the DAG, as Joel mentioned, calls it.
[1067.80 → 1070.30] So we have the app, which is basically the whole source code.
[1070.30 → 1072.80] There are a couple of things that we need from the environment,
[1072.94 → 1074.16] like the git shah, git author.
[1074.48 → 1074.68] Hmm.
[1075.08 → 1076.70] I don't think I fixed those.
[1076.78 → 1077.62] I need to fix them.
[1078.34 → 1078.66] Okay.
[1078.96 → 1079.20] Okay.
[1079.24 → 1080.72] This is something which still needs to improve.
[1080.78 → 1082.46] I just realized going through this now.
[1082.54 → 1082.70] See?
[1083.04 → 1083.40] So good.
[1083.48 → 1084.38] We're doing these things.
[1084.98 → 1085.70] So helpful.
[1086.38 → 1086.80] Cool.
[1087.04 → 1089.16] So then the Docker host, which is the remote one,
[1089.18 → 1090.30] it knows how to connect to it.
[1090.34 → 1094.18] And then it runs the same command that you've seen in GitHub Actions.
[1095.14 → 1095.46] Docker.
[1095.84 → 1096.04] Sorry.
[1096.52 → 1096.80] Docker.
[1097.52 → 1098.78] That's like a Freudian slip.
[1099.22 → 1099.58] Dagger.
[1099.58 → 1101.28] Dagger up.
[1101.64 → 1103.54] Log level debug environment CI.
[1104.54 → 1105.78] And that's exactly the same thing.
[1106.36 → 1108.88] The other part of this is obviously the CI queue.
[1109.36 → 1112.84] And this is like all the code that's actually like declares the pipeline.
[1113.12 → 1115.02] And what is this CI.queue?
[1115.10 → 1116.14] How would you describe it?
[1116.14 → 1121.96] It's basically the description of those various stages that we were describing earlier.
[1121.96 → 1124.86] So there's the app image.
[1124.96 → 1130.08] You have the test container or the test DB container definition prior to that.
[1130.74 → 1132.86] And then let's see.
[1132.96 → 1133.96] This is some of the...
[1133.96 → 1144.86] So depths is basically kind of helping copy the actual application, which is all the changelog.com source code into a container.
[1144.86 → 1145.78] Mm-hmm.
[1145.78 → 1157.46] And then we have some just queue variable or queue fields in essence that help us store some information about how we want to be mounting these dependency caches and build caches.
[1157.82 → 1158.42] Yep.
[1158.42 → 1161.16] So we also do the same thing for node modules.
[1161.16 → 1175.38] And then these depths compile, hashtag depths compile, is we're using that basically as a way to describe a kind of structure that we're then going to apply in a few other places.
[1175.80 → 1185.16] So you can see depths compile test actually uses that definition and specializes it with arms mix and test.
[1185.16 → 1191.30] And we do the same thing with dev and prod, if I remember correctly.
[1191.46 → 1193.08] Depths compile dev is right down here.
[1193.20 → 1194.20] So the only difference, you're right.
[1194.28 → 1201.26] The mix env is the same definition of depths compile with like, you know, something changed, actually added, right?
[1201.30 → 1202.62] Because it depends on stuff to it.
[1203.46 → 1203.70] Okay.
[1203.84 → 1204.74] And what is queue?
[1205.12 → 1208.02] So queue is a configuration language.
[1208.52 → 1213.14] It aims to be a better JSON, a better YAML.
[1213.14 → 1216.78] It stands for configure, unify, and execute.
[1217.32 → 1217.48] Yeah.
[1217.74 → 1222.90] And basically, I think Joe will be able to continue after that.
[1223.58 → 1223.96] Yeah.
[1224.30 → 1227.46] So like Guillaume said, it's a configuration language.
[1228.02 → 1236.66] And one of the things that I think is really lovely about queue is schema definition, data validation.
[1236.66 → 1244.76] And it basically allows you to create configurations that have types.
[1245.24 → 1248.80] So they can be type checked, preferably before you get to prod.
[1249.28 → 1249.66] Yeah.
[1250.88 → 1252.50] And that actually is true.
[1252.62 → 1253.46] It's how it works.
[1253.46 → 1259.16] I personally love that it is not whitespace dependent like YAML is.
[1259.32 → 1264.76] I've been a bit so many times by that with Helm and other various tools.
[1264.90 → 1266.08] Ansible comes to mind too.
[1267.20 → 1268.92] There are lovely things about those tools.
[1269.12 → 1275.20] And I've found myself bitten by that bug and a number of them.
[1275.20 → 1277.74] That's why YAML vaccine resonated with you, right?
[1277.74 → 1281.92] When I mentioned it, that's exactly what I meant because you had the bug multiple times.
[1282.06 → 1283.10] And damn it, it's not fun.
[1283.68 → 1283.98] Yeah.
[1284.24 → 1284.62] Yeah.
[1284.62 → 1292.12] I've had production deploys fail because an engineer added an environment variable and used tabs instead of spaces in a Helm chart.
[1292.48 → 1297.16] I prefer not having those sorts of problems that are avoidable.
[1297.56 → 1301.14] And queue is a really powerful tool for doing that.
[1301.14 → 1318.70] Just to kind of dig into the schema definition stuff a little bit deeper because I think it's useful to understand, you could basically define the shape of a particular configuration, including constraints on different fields.
[1318.70 → 1323.06] So if you want a good example of this might be like a Kubernetes deployment.
[1323.58 → 1329.72] So you can have a Kubernetes deployment with your API version, your kind deployment.
[1329.72 → 1339.48] And then you can, for instance, say, set the CPU field and actually set a constraint on that.
[1339.56 → 1342.54] You can set an upper bounds and a lower bound, et cetera.
[1342.54 → 1354.16] And then when any configuration from a developer or an SRE comes into that, if it doesn't match that specification, then to compile of the queue will fail.
[1354.66 → 1363.28] And so it'll allow you to fail at a much earlier stage, potentially even on a developer's local machine rather than once it gets to production.
[1363.28 → 1365.72] That's exactly what we've been using.
[1365.72 → 1373.52] We've developed a serverless package to easily deploy serverless functions on AWS.
[1374.34 → 1376.08] And that's basically what we used.
[1376.70 → 1377.84] So it's kind of useful.
[1378.20 → 1384.04] So sometimes you have like the names, they are forbidden characters and we just do it.
[1384.46 → 1389.52] We use these validations to avoid, to fail early.
[1389.52 → 1390.16] Yeah.
[1390.72 → 1390.98] Okay.
[1391.48 → 1393.86] So, yeah, there's a lot to explore here.
[1394.20 → 1395.96] I really, really like you.
[1396.02 → 1398.08] I have to say there's like so many great things about it.
[1398.44 → 1402.68] And it makes like not having the right inputs, not having the right values.
[1402.74 → 1404.92] It just really helps.
[1405.08 → 1408.58] Like the compiler errors for queue are perfect.
[1408.90 → 1411.40] And they steer you like in the right direction.
[1411.84 → 1414.88] And with Vim, there's like a good plugin, which kind of works.
[1415.30 → 1418.26] I can share it in the show notes, but it's good.
[1418.26 → 1420.66] I mean, it's much better than not having it.
[1421.12 → 1423.02] I'm sure that that can improve as well.
[1423.22 → 1427.78] There are some rumblings in the queue community around creating a language server as well.
[1428.06 → 1429.34] Ooh, wow.
[1429.36 → 1429.60] Yes.
[1429.60 → 1430.08] An LSP.
[1430.26 → 1431.04] I would love that.
[1431.42 → 1432.36] I would love that.
[1432.48 → 1432.64] Okay.
[1432.80 → 1433.08] Okay.
[1433.16 → 1433.38] Right.
[1433.46 → 1435.50] So, yeah, I'll definitely want to watch for sure.
[1435.74 → 1438.30] So what comes next?
[1438.30 → 1449.02] I think one thing that occurs to me is, at least as far as I remember, this is currently still using the Docker build.
[1449.02 → 1460.16] So you're actually pushing out the contents of a bunch of those steps to the Docker engine to actually then build the image.
[1461.12 → 1465.52] And with Europa and some of the improvements there, that should not be necessary.
[1465.52 → 1477.00] You should be able to just take the output of one of these stages and just add the information that you want on top of it and be off to the races and then be able to push that directly.
[1477.20 → 1486.50] Because right now what's happening is a bunch of the context is still having to be pushed from within Build Kit to Docker engine so that it can build the image.
[1487.26 → 1490.18] And that will not be necessary.
[1490.74 → 1491.14] Interesting.
[1491.80 → 1493.18] With some of the new Europa stuff.
[1493.18 → 1493.94] Okay.
[1494.60 → 1495.34] Sounds great.
[1496.48 → 1499.36] Anything to add, Guillaume, to that or something else?
[1500.20 → 1500.46] Yeah.
[1500.64 → 1507.22] I think that with Europa, as Joel mentioned earlier, the DX will be far better.
[1507.52 → 1515.58] Like what we're trying to do at the moment, if the people watch the PR with Europa, it's going to be, it will feel normal.
[1515.84 → 1516.00] Yeah.
[1516.04 → 1516.76] I think, yeah.
[1516.80 → 1517.96] I think that makes a lot of sense.
[1518.08 → 1519.74] Europa will make this a lot simpler.
[1519.74 → 1519.86] Yeah.
[1520.08 → 1524.70] And while we had like to jump through a couple of hoops, it just made it obvious they shouldn't be there.
[1525.08 → 1527.98] And so I'm really excited to adapt this to that new way.
[1528.24 → 1528.98] That will be great.
[1529.18 → 1530.86] And to see what improvements we can get.
[1530.94 → 1532.68] Because at the end of the day, that's what you care about, right?
[1532.82 → 1534.38] This looks not as good as it could.
[1534.64 → 1536.32] I mean, it works, right?
[1536.36 → 1537.26] And that's what you care about.
[1537.32 → 1537.82] Make it work.
[1538.40 → 1539.08] Make it right.
[1539.42 → 1540.40] I think that's what's happening now.
[1540.42 → 1541.08] We're making it right.
[1541.12 → 1542.16] And then we're making it fast.
[1542.16 → 1543.62] So I'm very excited about that.
[1545.26 → 1545.66] Okay.
[1545.74 → 1549.86] Well, I'm going to wish you both a Merry Christmas, even though this is like weeks before Christmas.
[1550.02 → 1553.12] But by the time listeners will be listening to this, it'll be Christmas.
[1553.94 → 1555.20] And Happy New Year.
[1555.60 → 1555.74] Thanks.
[1556.82 → 1559.14] It's been a lot of fun to work with you and Guillaume on this.
[1560.10 → 1563.50] It's been a nice opportunity to get to know you and get to know Guillaume as well.
[1564.34 → 1568.96] Like you mentioned, I live in kind of the Boulder, Denver area and Guillaume lives in France.
[1569.62 → 1574.22] And it was a good opportunity to bump into each other more regularly.
[1574.96 → 1575.32] Definitely.
[1575.54 → 1576.40] Right back at you again.
[1577.08 → 1577.80] Same for me.
[1577.90 → 1579.74] So I'm glad that this worked the way you did.
[1579.86 → 1580.98] I also had a lot of fun.
[1581.12 → 1581.70] Thank you very much.
[1581.90 → 1582.20] Thank you.
[1582.58 → 1583.12] Thank you.
[1583.12 → 1596.36] Our second present to you this Christmas is sharing my way of understanding CPU time used by Kubernetes workloads.
[1597.08 → 1605.30] Think near real-time flame graphs, as well as being able to compare CPU profiles for the same process at different points in time.
[1605.74 → 1611.02] If you're familiar with Brendan Gregg's book, Systems Performance, this goes really well with it.
[1611.50 → 1613.10] So why is this a big deal?
[1613.54 → 1616.60] And why was it more difficult to do this in the past?
[1617.10 → 1619.82] I know just the right person to unwrap this present with.
[1620.24 → 1624.08] Let me talk a little bit about why that's interesting, why that's useful.
[1625.00 → 1631.70] So profiling has kind of been in the developer toolbox ever since software engineering has existed,
[1631.70 → 1637.94] because we always needed to know, like, why is my program executing, and how is it executing the way it is?
[1638.60 → 1641.24] And so profiling has been around for a very long time.
[1641.24 → 1645.76] It's essentially us recording what the program is doing.
[1645.76 → 1656.16] And you can literally think of it as we're recording the stack traces that are happening, you know, 100 times per second.
[1656.16 → 1662.14] And that has kind of evolved over the years.
[1662.86 → 1670.34] And profiling used to be a very expensive operation to do, which is why you only did it when you really needed to.
[1670.34 → 1680.44] And so on thing that kind of changed the perspective was when we discovered sampling profiling.
[1680.44 → 1686.52] So in the olden days, the way that profiling worked is that we literally recorded everything that was happening in our program.
[1687.04 → 1689.18] And naturally, that's really expensive.
[1689.90 → 1694.56] And sampling profiles, profiling kind of go a different strategy and say,
[1694.86 → 1698.44] actually, we only need something that's statistically significant.
[1698.44 → 1706.78] And so instead of recording everything that's happening, as I said earlier, we only look at the stack traces 100 times per second.
[1707.04 → 1708.98] And that we can do incredibly efficiently.
[1709.54 → 1717.96] The reason why this is super useful and why being able to record stack traces with statistical significance is useful is that now we can say,
[1718.12 → 1721.54] this is where my program is spending time.
[1721.54 → 1726.18] And so that can be used to save money on your infrastructure.
[1726.62 → 1735.88] But also, you know, there are a lot of optimizations that you can only do if you have that type of depth of data to analyze.
[1736.18 → 1741.92] So you can actually down to the line number tell what is using your CPU resources.
[1742.26 → 1748.64] One really cool conversation that I had yesterday, this perfectly translates in the serverless world, right?
[1748.64 → 1755.88] Where you actually pay for basically every single CPU cycle that your serverless function is running.
[1756.24 → 1763.16] And any CPU second that you can cut off from that is money you're saving from your serverless bill.
[1763.72 → 1767.96] And so I think that's a really obvious value proposition.
[1768.40 → 1777.54] Because we simply have this data and are recording it always, we can actually reliably tell where we can optimize our code.
[1777.54 → 1782.14] So out of these three things, saving money, very important for some.
[1782.64 → 1784.78] Improving performance, I love that.
[1785.36 → 1787.76] Like shipping code fast, great.
[1788.28 → 1790.82] Making it better and improving it, I love that.
[1791.34 → 1795.44] And when things go wrong, understanding what exactly went wrong.
[1796.16 → 1800.90] What CPU, what disk, what network, where is the bottleneck from a system perspective,
[1801.16 → 1805.14] as well as obviously from like if you have microservices, between microservices.
[1805.14 → 1811.82] So ARCA helps us understand from a CPU perspective, where is the time spent, right?
[1811.86 → 1815.58] In the current implementation, the current version, that's what it tells us really, really well.
[1815.96 → 1817.08] So how about we try it out?
[1817.54 → 1820.42] We're going to run it in our production Kubernetes setup.
[1820.86 → 1822.14] Just like that, why not?
[1822.72 → 1826.36] Create namespace, apply the server, and apply the agent.
[1827.02 → 1830.70] And as I do this in the background, what is the difference, Frederick, between the server and the agent?
[1830.70 → 1836.94] The server is essentially the component that allows you to store and query profiling data.
[1837.72 → 1847.38] While the agent, the one and only purpose of the agent is to capture this data from your applications at super low overhead.
[1848.00 → 1852.10] And one of the really exciting technologies that we're using here is EPF.
[1852.10 → 1862.54] So because we know exactly what the format is that we're going to want this type of data in, we can, in kernel, you know,
[1862.60 → 1868.48] without having to spend all of this overhead of doing context switches from kernel space to user space,
[1868.70 → 1876.20] we can immediately record the stack traces in kernel and present it to ARCA agent.
[1876.20 → 1883.56] And then ARCA agent, it does some resorting in the data, but essentially it just sends that off to ARCA.
[1883.88 → 1885.88] And then from ARCA, you can actually visualize it.
[1886.18 → 1886.24] Okay.
[1886.64 → 1888.70] So we have the server and the agent.
[1889.44 → 1892.84] So let's port forward to the server, to the UI.
[1893.98 → 1898.40] And in our browser, localhost 7070, let's see what that looks like.
[1898.58 → 1904.12] One thing that I think is really important to mention, everything revolves around the PPF standard.
[1904.12 → 1908.16] This is kind of an industry standard format for profiling data.
[1909.28 → 1914.18] And so everything produces or works with PPF format.
[1914.40 → 1925.32] So you could send any kind of profile, like memory profiles that have been captured through some other mechanism to ARCA and analyze that as well.
[1925.64 → 1931.84] It's just that the agent today can only produce CPU profiles and continuously send those.
[1931.84 → 1936.58] The agent actually also produces PPF compatible profiles.
[1936.82 → 1938.40] And maybe we can have a look at that later.
[1939.36 → 1941.02] The server ingests those.
[1941.28 → 1949.88] And then one additional really cool feature, I think, is any query that you do in the ARCA front end, you can download again in PPF format.
[1950.18 → 1956.94] And then, you know, if you have any other sort of tooling around the PPF format, you can still use them and compose your workflows.
[1956.94 → 1961.82] Okay, we are on the server looking at all the CPU profiles.
[1962.02 → 1964.78] This is the profile coming from container ARCA.
[1965.30 → 1966.68] How do we read this?
[1966.94 → 1968.04] It's a CPU sample.
[1968.40 → 1969.36] We can see the root.
[1969.60 → 1970.80] That's the root span.
[1971.40 → 1972.90] What about all the other spans?
[1973.14 → 1973.70] What are these?
[1973.70 → 1975.58] This is what's called a flame graph.
[1975.86 → 1985.68] And every span that we're seeing here represents how much this span as well as all of its children make up in cumulative.
[1986.20 → 1988.92] So that's actually what the front end also says, right?
[1988.98 → 1990.12] The cumulative value.
[1990.94 → 1995.32] And essentially we're saying everything from this point onwards and further down uses up.
[1995.68 → 1997.70] In this case, you're hovering over one that says 11%.
[1997.70 → 2003.98] So, for example, we can see here in the middle, we can see runtime.gray object, for example.
[2004.26 → 2017.34] If we were able to optimize that gray object function, for example, and say for whatever reason we're able to optimize 100% of it away, we would actually be saving 15% of our CPU resources here.
[2017.34 → 2027.08] And in this case, you actually clicked a particularly interesting sample because we can see in our metrics above that we have these spikes sometimes.
[2027.30 → 2032.76] And we can very clearly see what it is that is causing the spike in this profile.
[2033.04 → 2036.40] We can see that it's garbage collection, right?
[2036.44 → 2040.06] A very classic thing that can use a lot of CPU resources.
[2040.48 → 2044.38] So this is garbage collection that happens in ARCA server, okay?
[2044.88 → 2046.42] So why does this garbage collection happen?
[2046.42 → 2052.46] Because of how Go works, you allocate objects in memory.
[2053.02 → 2066.50] And when you don't use them anymore, eventually the runtime will come around and see that this piece of memory is not in use anymore and kind of free that memory to the operating system so that anybody on the machine can use it.
[2066.50 → 2075.78] And in this case, essentially what we're seeing, because we have such a huge spike, that's telling us ARCA is doing a lot of allocations.
[2075.98 → 2083.08] It's allocating a lot of memory that then consequently is kind of thrown away and can be garbage collected.
[2083.08 → 2087.90] So it seems like there's probably some potential in optimizing allocations here.
[2088.00 → 2097.10] That said, having allocations is not a bad thing because at the end of the day, I can write a program that does absolutely nothing and does no allocations, right?
[2097.14 → 2098.24] But that's also not useful.
[2098.72 → 2103.52] Producing side effect is one of those things that as software engineers, we try to not produce side effect.
[2103.52 → 2108.30] But as it turns out, side effect tends to be the thing that's actually useful in the real world.
[2108.44 → 2110.18] That's when real work happens, right?
[2110.26 → 2114.42] Like these spikes are an artifact of real work happening.
[2114.42 → 2129.48] And if I had to guess without knowing too much, knowing what ARCA does behind the scenes, but not knowing all the details, I think that this is related to all those profiles being maybe read, being symbolized, or something happens in the background.
[2129.48 → 2135.28] So like reads a profile, builds whatever data structures it needs to build to get an output.
[2135.28 → 2142.40] And when that output is like that result, right, is achieved, then all the intermediary objects can be garbage collected.
[2142.50 → 2143.78] And I think that's what's happening here.
[2143.78 → 2151.80] The two major things are definitely what you already mentioned, symbolization, because this happens asynchronously as you have uploaded your profiling data.
[2151.98 → 2156.60] And then it's actually ingesting and writing that profiling data to its storage.
[2156.60 → 2160.94] This is something that because we're doing continuous profiling, it happens continuously, right?
[2161.20 → 2169.12] And every network request that we receive causes memory allocations because we read that from the network stack, right?
[2169.16 → 2170.78] And that causes memory allocations.
[2170.78 → 2176.04] Now, there are a number of optimizations that can be done to reduce this.
[2176.18 → 2178.72] And, you know, you can reuse buffers and stuff like that.
[2178.72 → 2183.78] And we'll get to all of that, but it's unlikely that we'll ever get to, you know, zero.
[2184.06 → 2186.56] But there's definitely lots of optimization potential here.
[2187.00 → 2187.24] Okay.
[2187.52 → 2191.52] I do have to say, looking at this flame graph, it's really amazing.
[2192.08 → 2206.58] Like if you remember how difficult this used to be in the past when you had to generate a prof and then use that prof or something similar that can read that profile to get this flame graph and then try and like slice and dice.
[2206.58 → 2209.50] Now, if I don't want this flame graph, I want a different one.
[2209.68 → 2210.80] I just click on it.
[2211.54 → 2212.44] And there you go.
[2212.94 → 2213.82] Database, Postgres.
[2213.96 → 2215.98] Let's see, what do we get from Postgres?
[2216.38 → 2216.62] Okay.
[2217.40 → 2219.38] So this is slightly a different view.
[2219.68 → 2223.40] This is a machine compiled binary, right?
[2223.70 → 2223.92] Right.
[2223.92 → 2226.70] So why do we see only these numbers?
[2226.84 → 2228.28] What are those numbers, first?
[2228.82 → 2229.92] Yeah, that's a perfect question.
[2230.12 → 2235.56] So these are the raw memory addresses that we obtained from the agent.
[2236.22 → 2248.36] And the reason why we're only seeing memory addresses is because most of the time when you, you know, install a package from, let's say, a Debian package or something like that.
[2248.36 → 2253.56] By default, these packages are distributed without debug information.
[2254.50 → 2260.48] And so they were intentionally removed from those binaries to reduce the size of the binary.
[2261.74 → 2267.90] And sometimes it can also have a performance impact, but usually it's just for size optimization.
[2267.90 → 2279.04] And in the case of Debian, for example, if you still want those debug symbols, the convention is that you, you know, let's say app get Postgres, right?
[2279.10 → 2286.38] The convention then is the package name is dash busy, debug symbols.
[2287.18 → 2296.16] And that downloads the debug symbols as a separate package, which can then again be picked up by the Parker agent as well.
[2296.16 → 2300.94] But in this case, we didn't have any debug information available.
[2301.52 → 2304.92] And so, yeah, this particular Postgres binary is stripped.
[2305.38 → 2307.54] And so it does not have this debug information.
[2307.80 → 2317.44] That said, there is a really cool project called Debug Info D, where the kind of distributions have come together and they're hosting these servers.
[2317.60 → 2319.26] We're using this build ID.
[2319.94 → 2323.24] You can request the debug symbols on demand.
[2324.04 → 2326.14] So this is great news, right?
[2326.16 → 2331.72] Because it means that you don't have to install these debug packages manually anymore.
[2331.98 → 2336.52] Parker can just go to this debug Info D server and retrieve it itself.
[2336.88 → 2337.72] That's the good news.
[2337.92 → 2341.02] The bad news is Parker doesn't have support for this just yet.
[2341.22 → 2343.72] We already have support for this plan.
[2343.86 → 2345.22] It just haven't gotten to it yet.
[2345.22 → 2350.48] So there's a good news and that bad news and that yet is the good news and that bad news.
[2350.56 → 2352.52] It's coming, but it's not there yet.
[2353.00 → 2354.26] So that's really cool.
[2354.78 → 2355.70] Yeah, I didn't know this.
[2355.78 → 2364.32] I knew about stripped binaries, but I didn't know about those build IDs and being able to use those build IDs to get the debug symbol for this particular binary from the server.
[2364.32 → 2365.06] That's really cool.
[2365.66 → 2367.02] Okay, so we've seen Postgres.
[2367.42 → 2368.98] What about Erlang VM?
[2369.24 → 2377.48] So this is our app, and we can see that we have Beam SMP all over the place, which is the name of the binary for the Beam Erlang VM.
[2377.48 → 2379.20] So we see the same thing here.
[2379.86 → 2394.38] Yeah, so this is kind of another variation of this, but the first kind of difference is this is not a binary that was compiled to machine-readable code, right?
[2394.78 → 2398.58] This is in the broadest possible sense interpreted code.
[2398.96 → 2405.12] The good news about Erlang is it actually has a just-in-time compiler.
[2405.12 → 2417.50] So what that means is even though it is technically an interpreted or a virtual machine, on the fly compiles parts of your code to actually machine executable code.
[2417.84 → 2423.18] So this is kind of good news again, because at least in theory, the same strategy can be applied.
[2423.48 → 2431.82] It just turns out that a lot of the strategies that these like dynamic languages or virtual machines tend to very subtly differ.
[2431.82 → 2439.72] And so we do have to essentially implement, you know, small pieces of runtime specific things.
[2439.90 → 2451.22] One thing that's actually really cool that I think Erlang does implement and, you know, like the Node.js runtime implements as well is something called perf maps.
[2451.22 → 2472.98] And this is something that many just-in-time compilers implement, where essentially the just-in-time compiler, because it generates or compiles this code on the fly, it can also write out this mapping from the memory address to the human-readable symbol.
[2473.64 → 2478.12] And that Parker agent can again pick up and symbolize on the fly.
[2478.12 → 2481.72] Okay. Now, I have tried this with Node.js.
[2482.04 → 2484.96] Unfortunately, we haven't gotten it to work with Erlang just yet.
[2486.64 → 2494.44] So there seems to be something specific that the Erlang VM does that we don't fully understand yet.
[2495.14 → 2502.24] But, you know, it's one of those things where language support is something that's always in progress.
[2502.24 → 2506.42] And hopefully we'll soon have like full support for the Erlang VM as well.
[2506.42 → 2509.52] Nice. So we can't really see that.
[2509.58 → 2512.70] But there's another thing which I haven't shown, the compare one, the compare view.
[2513.42 → 2515.48] So we can compare two profiles side by side.
[2515.66 → 2517.98] So we take a low one. I think that's how you like to start.
[2518.10 → 2523.44] You take a low profile on the left, and you take a high on the right, and it will compare them side by side.
[2524.14 → 2526.72] So how do we interpret when this loads?
[2526.78 → 2528.02] How do we interpret this result?
[2528.02 → 2531.64] Yeah. So this is going to be hard when we just see memory addresses.
[2532.40 → 2538.96] But essentially, anything that is blue has stayed exactly the same.
[2539.08 → 2545.04] It used exactly the same amount of CPU in the one observation as it did in the compared one.
[2545.74 → 2550.06] Anything that's green, the CPU cycles got less.
[2550.06 → 2555.16] I can actually see one very tiny one on the left somewhere in there.
[2555.38 → 2559.82] There's one that got very slightly better, 50%.
[2559.82 → 2565.90] It seems like it was two CPU samples before, and now it was only one.
[2566.64 → 2568.62] How do you know it was two CPU samples?
[2568.62 → 2574.76] So we see that the diff is minus one.
[2574.94 → 2575.32] Right.
[2575.92 → 2579.52] And the current sample is one.
[2579.92 → 2581.40] So that must have been two before.
[2581.62 → 2583.04] So that's CPU cycles.
[2583.62 → 2586.72] It's observations of stack traces.
[2586.96 → 2590.64] So we at most look at the process 100 times per second.
[2590.64 → 2598.12] And so that means 100 means one CPU core being used.
[2598.32 → 2602.44] So in this case, this is like 1%, like one millimole.
[2602.60 → 2603.24] Right. Okay.
[2603.66 → 2606.56] That was being used within those 10 seconds.
[2606.72 → 2606.96] Okay.
[2607.50 → 2610.48] So this one is slightly better.
[2611.08 → 2615.14] But this one, the Beam SMP, and I wish we knew what this was,
[2615.64 → 2618.68] or maybe this one, which is like just a memory address.
[2618.68 → 2622.90] This is 350% worse.
[2623.64 → 2626.74] So I can see, or I can think, I mean, even though this is very Christmassy
[2626.74 → 2629.80] and I like it, like red and green and, you know, it's very nice.
[2630.18 → 2633.36] It would be easier, like if we had used a different colour
[2633.36 → 2635.38] for the ones which have an infinity,
[2635.66 → 2637.40] I know maybe black or something like that,
[2637.46 → 2638.84] which they're like completely new.
[2638.92 → 2642.86] I like the diff idea, but a different number,
[2643.26 → 2645.16] sorry, different colour from the ones that are like,
[2645.20 → 2646.60] for example, this one plus 700.
[2646.60 → 2650.62] So this is just worse, but this is like brand new.
[2650.74 → 2653.74] This wasn't even like, didn't even happen in the previous sample.
[2653.88 → 2653.98] Yeah.
[2654.94 → 2655.26] Okay.
[2656.70 → 2658.44] I'm writing this down.
[2658.56 → 2658.74] Cool.
[2658.74 → 2664.16] So this is great to be able to see the difference.
[2664.62 → 2668.48] And I suppose, I'm just wondering if we were to take this memory address
[2668.48 → 2674.24] and if we were to look into that file, into that perf map file,
[2674.56 → 2677.30] would we be able to figure out what this is?
[2678.26 → 2679.64] It's possible.
[2679.64 → 2684.64] The problem is in this case, so we can look at the process
[2684.64 → 2689.20] and we can kind of go through the steps of what the Parker agent would do manually.
[2689.76 → 2695.80] And then we can try to see if we can figure out why this is not able to symbolize this.
[2695.92 → 2698.06] My theory is because of what we can see here,
[2698.82 → 2702.86] the way that this binary code was memory map,
[2703.16 → 2707.34] we weren't actually able to understand where it's mapped.
[2707.34 → 2713.38] So the way that this works is let's go back to our terminal, I would say,
[2713.88 → 2716.20] and we can inspect this actually,
[2716.56 → 2722.28] the way that binary code is memory mapped for the process.
[2722.74 → 2725.58] So we can again look into our proofs.
[2725.94 → 2728.16] This is where all the magic happens on Linux.
[2728.36 → 2728.54] Okay.
[2728.64 → 2730.36] So do we want to go like on the host?
[2730.76 → 2733.34] We can do the host or the container.
[2733.64 → 2734.38] Yeah, it shouldn't matter.
[2734.56 → 2735.12] Both should work.
[2735.22 → 2735.44] Okay.
[2735.44 → 2736.84] So yeah, let's go on the host.
[2736.84 → 2739.62] So we want to go on that.
[2739.80 → 2740.18] Let's see.
[2740.24 → 2742.12] We shall have the CD.
[2742.78 → 2743.30] There you go.
[2743.50 → 2744.10] That's the proc.
[2744.40 → 2744.62] Yes.
[2745.02 → 2745.28] Right.
[2745.80 → 2748.10] And here there's a file called maps.
[2751.02 → 2751.54] Yes.
[2752.68 → 2753.00] Yeah.
[2753.10 → 2755.30] So let's have a look at what it says in there.
[2755.30 → 2763.84] And the way that symbolization effectively works is that we take that memory address that we saw.
[2763.98 → 2764.28] Yes.
[2764.66 → 2770.98] And we try to find in which range within this file that memory address is from.
[2771.08 → 2771.90] So this one right here.
[2771.94 → 2772.18] Okay.
[2772.72 → 2773.92] So that's the memory address.
[2774.58 → 2776.76] So do we need to do 7FF?
[2776.76 → 2779.34] I mean, I can see something here, 7FF.
[2780.10 → 2792.54] Well, if you're able to search within your terminal, maybe we can, you know, it's a bit of a hack, but we can search for the address that you have copied.
[2792.54 → 2800.24] And we can just try to remove certain digits until we maybe get a match.
[2800.58 → 2800.66] Okay.
[2801.26 → 2802.40] So let's remove those two.
[2802.44 → 2807.18] And as we can see, the ranges don't have the 0x prefix here.
[2807.24 → 2808.90] So we're going to need to remove that.
[2809.38 → 2809.54] Okay.
[2809.54 → 2812.02] So yeah, this is an interesting one.
[2812.10 → 2814.82] And this is exactly why this is not working.
[2815.02 → 2818.36] So the way that this table works is that we have these ranges.
[2818.62 → 2827.32] And then it tells us on the very right, this is the binary that this executable code came from.
[2827.32 → 2841.98] And so actually the stack, I want to say this could be a, I don't know if it's necessarily a bug, but what can happen in some languages and in Go, this can happen as well.
[2841.98 → 2857.32] So sometimes when we do the stack, like the stack trace snapshots, when we retrieve them from EPF, sometimes the kernel does them a bit too tall, and we don't fully understand why.
[2857.74 → 2864.42] Like basically it, what it does is it goes back and walks the stack, and sometimes it walks too far.
[2864.42 → 2870.96] And in this case, it doesn't actually make sense that the stack contains executable code.
[2871.12 → 2873.90] That shouldn't be how things work.
[2874.58 → 2877.46] So it could be that this is just an artifact of that.
[2878.48 → 2888.82] But because it's also a virtual machine, maybe there's something happening that we don't understand, and we are actually executing code that is on the stack.
[2888.82 → 2897.78] It seems unlikely, but you know, it's one of those things where I'm not an expert on the Erlang VM, so I don't know for sure.
[2898.42 → 2898.48] Yeah.
[2898.64 → 2905.52] But like my intuition says that this shouldn't be possible just from like the way that processes work.
[2905.74 → 2906.28] Right, right.
[2906.72 → 2907.02] Okay.
[2907.50 → 2910.90] So this is like the Erlang runtime itself, right?
[2910.90 → 2913.34] How it executes code on the kernel.
[2913.78 → 2915.20] That's what we would need to know.
[2915.20 → 2920.48] So I think that we have a person that we can ask, which is Lucas Larson.
[2921.36 → 2934.54] So that is, even though he's very busy, I know, and he's focused like deep down on like some very gnarly problems in the world of Erlang, we can, you know, ask him.
[2934.74 → 2940.32] And if you're interested to follow what happens, I mean, this is like pull request 396 is what started this.
[2940.32 → 2946.22] I intend to keep, right, as many details as I can here and all the follow-ups.
[2946.74 → 2953.10] So yeah, this is a place to go, I suppose, to see what else has happened since this was recorded.
[2953.88 → 2957.24] So what I'd like to say is thank you very much, Frederick.
[2957.38 → 2957.66] My pleasure.
[2957.78 → 2959.34] For running us through ARCA.
[2959.34 → 2988.20] What we want to do is, first, fix this R.
[2988.20 → 2994.76] Damn it, someone can't type infrastructure as if my life depended on it.
[2995.66 → 2996.26] Right.
[2996.66 → 3009.98] So we want in 2022 for the changelog.com setup to use cross-plane to provision our Linde Kubernetes cluster.
[3009.98 → 3010.82] That's the goal.
[3011.32 → 3024.18] And the way we're thinking of achieving it is to follow this guide to generate a Linde cross-plane provider using the Terra Jet tool, which is part of the cross-plane ecosystem.
[3024.58 → 3028.10] And we can generate any cross-plane provider from any Terraform provider.
[3028.34 → 3028.54] Cool.
[3028.84 → 3030.02] So how are we going to do that?
[3030.44 → 3034.20] Yeah, I think, well, you know, there are a couple different parts here.
[3034.20 → 3043.08] In order to be able to test out anything that we generate, we're going to need a cross-plane control plane running somewhere.
[3043.08 → 3054.10] That being said, right, we need to generate and package up this provider to be able to install it in cross-plane and go through our package manager there.
[3054.74 → 3059.48] But it could be as simple as even just having a local kind cluster to start out.
[3060.04 → 3066.02] And, you know, after generating, using Go Run to just apply some CRDs and see if it picks them up correctly.
[3066.02 → 3067.58] That is a good idea.
[3067.98 → 3068.58] I like it.
[3068.92 → 3073.04] But I have found issues when I went from kind to something else.
[3073.88 → 3083.42] GKE, LIKE, any like real cluster, because they have, there are different things like RAC, for example, or different security policies or who knows what.
[3083.66 → 3089.34] So I like starting with like production, which is a bit weird because you would think like you start from development.
[3089.48 → 3090.84] But I like starting with production.
[3090.84 → 3097.68] What I'm thinking is I want to start with cross-plane installed in the production setup.
[3098.12 → 3106.90] And I can't remember this was episode 16 or 17, where I was saying that if there was a cross-plane 15, there you go.
[3107.22 → 3110.14] Gerhard has an idea for the changelog 22 setup.
[3110.40 → 3117.24] So the idea was to use a managed cross-plane, which would be running on the app out cloud.
[3117.24 → 3121.38] And with that cross-plane, that should manage everything else.
[3121.96 → 3123.22] So that is our starting point.
[3123.44 → 3124.60] That's what we're doing here.
[3124.98 → 3127.72] If we go to about cloud, there you go.
[3128.12 → 3129.10] Control planes.
[3129.46 → 3130.96] I have already created one.
[3131.34 → 3132.38] It's a Christmas gift.
[3132.88 → 3133.08] Nice.
[3133.42 → 3134.48] So this exists.
[3135.02 → 3137.84] I will contact you after my free trial.
[3138.96 → 3139.42] Sounds good.
[3139.56 → 3144.38] So just before Easter, I'll say, hey, Dan, is there like an Easter egg in here or something?
[3144.86 → 3145.10] Cool.
[3145.10 → 3147.58] We'll email you as a reminder.
[3148.92 → 3149.36] Cool.
[3150.00 → 3151.42] So we have a control plane.
[3151.66 → 3153.56] We have a Kubernetes cluster, which is this one.
[3154.00 → 3155.96] So K version.
[3156.26 → 3156.58] That's the one.
[3157.02 → 3163.22] Also, just a note, you'll want to make sure to clean up that token that was exposed there before you post this anywhere,
[3163.36 → 3167.56] because that'll give folks the ability to get a kubeconfig to your cluster.
[3168.36 → 3169.22] This token, yes.
[3169.32 → 3169.82] Thank you.
[3170.04 → 3170.72] Oh, yes.
[3170.88 → 3171.22] Oh, yes.
[3171.26 → 3173.24] That would be quite a Christmas gift, wouldn't it?
[3173.96 → 3174.70] Here we go.
[3174.70 → 3175.18] Right.
[3175.26 → 3176.28] You can have access to it.
[3176.36 → 3177.44] You can take everything down.
[3177.66 → 3178.90] That is a very good catch.
[3178.98 → 3179.36] Thank you.
[3179.58 → 3179.74] Cool.
[3180.22 → 3181.88] We have cross plane.
[3182.40 → 3183.30] We have access to it.
[3183.78 → 3185.62] And could we see the version?
[3185.76 → 3187.10] So I use canines.
[3188.12 → 3189.36] And I think you do, too.
[3189.54 → 3190.84] I've seen you use it a couple of times.
[3191.00 → 3191.58] It's a lot quicker.
[3191.70 → 3193.12] So these are all the pods.
[3193.60 → 3197.82] If I do D for describe, it's version 131.
[3198.10 → 3198.36] Cool.
[3198.74 → 3199.48] Is that good enough?
[3199.48 → 3199.96] Yep.
[3199.96 → 3200.58] That's good.
[3200.82 → 3208.50] Although, actually, by end of day today, you'll be able to get as recent as 151.
[3208.96 → 3220.52] But a nice policy here is also, and this will actually be rolling out today as well, we have patches, right, for minor versions.
[3220.52 → 3225.14] And your control plane will automatically receive the latest patch here.
[3225.48 → 3227.16] And you shouldn't see any disruption with that.
[3227.34 → 3231.40] So you'll actually get up to 1.3.3 if you kept this control plane around.
[3232.18 → 3232.20] Right.
[3232.32 → 3232.54] Okay.
[3232.54 → 3238.38] But to get Terra Jet to work, will I need a newer version of cross plane, or is 1.3 sufficient?
[3239.04 → 3242.26] 1.3 should be fine for what we're doing here.
[3242.58 → 3244.34] Terra Jet just basically generates the provider.
[3244.54 → 3247.30] So as long as the provider is supported, then you're good.
[3247.70 → 3247.90] Cool.
[3248.36 → 3248.60] Okay.
[3248.90 → 3249.90] We can connect to this.
[3250.24 → 3250.94] Everything is running.
[3251.36 → 3255.48] Shall we just follow these instructions and see how far we can get?
[3255.74 → 3255.98] Sure.
[3256.24 → 3257.04] Yeah, that sounds great.
[3257.04 → 3264.58] And a disclaimer for everyone at home, I am not intimately familiar with Terra Jet, actually,
[3264.68 → 3270.40] because we had another team of cross plane contributors who have worked on this.
[3270.84 → 3275.72] So I'm going to be learning as we go along here in terms of the actual generation process.
[3275.86 → 3276.46] This should be fun.
[3277.16 → 3277.70] That's amazing.
[3278.12 → 3279.42] So that is?
[3280.02 → 3280.48] That's correct.
[3280.60 → 3281.02] Move off it.
[3281.14 → 3281.30] Yep.
[3281.92 → 3282.22] Okay.
[3282.66 → 3284.08] And Hassan.
[3284.40 → 3284.60] Yep.
[3284.60 → 3285.20] Okay.
[3285.20 → 3285.66] Amazing.
[3285.66 → 3288.56] One of those folks are actually some of my coworkers at Upbound.
[3290.04 → 3295.68] And Move Office has been a cross plane maintainer with me for a number of years now.
[3296.44 → 3296.84] Amazing.
[3297.08 → 3297.32] Okay.
[3297.64 → 3297.76] Well.
[3298.08 → 3298.48] They're awesome.
[3298.62 → 3299.50] Thank you very much.
[3299.76 → 3300.78] Let's see how well it works.
[3300.86 → 3300.98] Right.
[3301.04 → 3301.46] My favourite.
[3301.66 → 3302.00] Let's see.
[3302.10 → 3302.98] Let's see what happens.
[3303.30 → 3303.48] So.
[3304.20 → 3304.46] Excellent.
[3305.42 → 3309.50] What follows next is an hour-long pairing session with Dan condensed into seven minutes.
[3309.78 → 3314.10] If you don't want to listen us two noobs figuring stuff out, skip ahead to the end
[3314.10 → 3314.44] result.
[3314.44 → 3318.60] When I talk it through with one of the Terra Jet creators, Mubarak Onus.
[3318.94 → 3319.72] Use this template.
[3320.68 → 3321.08] Okay.
[3321.72 → 3322.08] Why?
[3322.34 → 3325.64] If you're intending to, you know, make this an open source project, that's a way to get
[3325.64 → 3326.54] started right off the bat.
[3326.88 → 3328.32] So basically clone this, right?
[3328.42 → 3333.70] If you click the Provider Jet template there, it'll have a use this template button, which
[3333.70 → 3336.92] means you can just create a new repo right from it.
[3337.48 → 3337.84] Okay.
[3338.16 → 3339.10] Let's go for that.
[3339.28 → 3339.64] Awesome.
[3339.64 → 3340.38] Change log.
[3340.94 → 3341.26] Perfect.
[3342.04 → 3342.20] Cool.
[3342.26 → 3342.42] Okay.
[3342.86 → 3343.38] First step.
[3343.54 → 3344.26] Provider Jet Linde.
[3344.64 → 3346.12] Clone the repository CD.
[3346.42 → 3348.34] Replace template with your provider name.
[3348.96 → 3349.40] Okay.
[3349.80 → 3350.04] Yeah.
[3350.16 → 3351.34] So where was the template?
[3351.86 → 3355.36] So all you're doing here is you're specifying what you want your provider name lower and
[3355.36 → 3355.86] upper to be.
[3356.02 → 3360.32] And then these commands are going to replace all instances of template.
[3360.32 → 3361.42] Ah, I see.
[3361.52 → 3361.66] Okay.
[3361.72 → 3362.16] I'm with you.
[3362.26 → 3362.36] Okay.
[3362.44 → 3363.58] Replace all occurrences.
[3363.74 → 3364.00] I see.
[3364.10 → 3365.82] So now just basically run this command.
[3366.14 → 3366.44] Okay.
[3367.70 → 3373.56] I'm guessing that has to do with the name of the Terraform repo potentially.
[3374.70 → 3377.98] But it says the check that line in controller docker file.
[3380.66 → 3384.20] And so that looks like a broken link potentially.
[3385.80 → 3386.28] Found.
[3386.62 → 3386.90] Cool.
[3386.90 → 3388.74] So that is the link that we should use.
[3389.40 → 3394.60] So it sounds like that just the Terraform provider Linde is what we're looking for there.
[3394.68 → 3398.96] If I look in the Docker file here and see how Terraform provider source is used.
[3399.28 → 3400.24] It's adding this.
[3400.38 → 3401.62] I think it's.
[3402.42 → 3408.26] I am a little confused about the difference between Terraform provider source and Terraform
[3408.26 → 3411.44] download name here based on the Docker file that we're looking at.
[3412.00 → 3412.38] Yeah.
[3413.00 → 3415.64] Seems like they should be the same.
[3416.90 → 3417.30] Yeah.
[3418.50 → 3419.58] I think they should be the same.
[3419.64 → 3420.30] I think you're right.
[3420.86 → 3425.12] I think that might be getting Terraform itself and installing it.
[3427.16 → 3428.84] Let's see if there is a.
[3429.44 → 3430.84] Ah, yes, you're right.
[3430.96 → 3432.48] That is getting the Terraform itself.
[3433.06 → 3434.30] You're absolutely right.
[3434.30 → 3435.30] Okay.
[3435.30 → 3437.50] So this actually is the entire URL.
[3438.46 → 3438.82] Right.
[3439.46 → 3440.64] I think it's actually all of it.
[3442.08 → 3443.06] No, maybe not.
[3443.22 → 3444.34] Because look at the location.
[3445.08 → 3445.22] Yeah.
[3445.22 → 3447.54] It's just the URL prefix, right?
[3447.64 → 3448.24] So I think it's just.
[3448.24 → 3448.52] It's this.
[3448.72 → 3449.54] Yeah, exactly.
[3450.18 → 3450.50] Okay.
[3450.54 → 3450.78] Okay.
[3450.82 → 3451.46] That makes sense.
[3451.66 → 3451.84] Cool.
[3452.84 → 3453.22] Okay.
[3453.22 → 3454.90] So this is the changelog.
[3456.78 → 3458.78] This is Terraform provider Linde.
[3458.78 → 3460.94] And that's it.
[3461.34 → 3463.28] V4 GitHub, I think.
[3464.36 → 3464.62] Yeah.
[3464.90 → 3469.04] I'm confused a little bit about the V4 GitHub portion of that.
[3470.50 → 3471.90] Well, that was added there.
[3471.90 → 3474.36] So that means that there should be a GitHub.
[3475.42 → 3476.48] Not this one.
[3476.60 → 3477.52] This one, the changelog.
[3478.04 → 3482.74] It'd probably be helpful if we took a look at one of the.
[3483.48 → 3487.84] Potentially if some of the existing providers use this.
[3488.94 → 3489.04] And.
[3489.62 → 3490.74] So if we take this one.
[3491.24 → 3491.86] Is this public?
[3492.32 → 3492.80] It is.
[3493.34 → 3493.50] Cool.
[3493.60 → 3493.98] So GitHub.
[3494.72 → 3495.22] Look at that.
[3495.46 → 3496.06] GitHub is there.
[3496.46 → 3496.68] Yeah.
[3496.68 → 3499.62] So I think this is an example of.
[3500.38 → 3501.56] So I think you'd have.
[3501.90 → 3503.64] Linde instead of GitHub, right?
[3504.20 → 3504.52] Yeah.
[3505.06 → 3508.56] But I'm not sure where the V4 is coming from necessarily.
[3508.88 → 3509.78] I didn't see that there.
[3509.80 → 3510.28] Actually, yeah.
[3510.32 → 3511.10] It's V4 GitHub.
[3511.24 → 3511.94] That is interesting.
[3512.30 → 3512.72] You're right.
[3513.24 → 3514.32] I didn't see V4 either.
[3514.44 → 3515.26] So I've seen GitHub.
[3515.64 → 3516.86] I don't know where that's coming from indeed.
[3517.14 → 3517.32] Okay.
[3517.42 → 3518.60] So if we come back to this.
[3518.66 → 3518.80] Let me.
[3518.88 → 3520.00] Maybe I'm not reading this right.
[3520.32 → 3521.36] The way I understand it.
[3521.40 → 3523.46] It's actually the Linde Terraform provider.
[3523.96 → 3524.76] It's this one.
[3525.08 → 3526.18] That I'm linking to.
[3526.70 → 3526.80] Yep.
[3526.86 → 3527.32] This is it.
[3527.84 → 3529.46] This is what I think I need to provide.
[3529.58 → 3530.28] So it's.
[3530.84 → 3531.88] It's basically this.
[3532.60 → 3533.56] Well, I think actually.
[3533.70 → 3535.60] No, I think what you have potentially is right.
[3535.68 → 3535.86] Right.
[3535.90 → 3538.26] Because I believe this is pointing to.
[3538.92 → 3539.32] Well, no.
[3539.40 → 3541.68] Is it using the Linde?
[3541.78 → 3542.44] Hold on one second.
[3542.56 → 3542.84] Actually.
[3544.48 → 3545.42] This example.
[3545.64 → 3546.06] It was.
[3546.72 → 3547.56] Yeah, you're right.
[3548.14 → 3548.70] No, actually.
[3548.82 → 3549.02] No.
[3549.68 → 3550.30] Here we go.
[3550.64 → 3551.14] This is.
[3551.20 → 3552.22] This is helpful.
[3552.22 → 3555.40] So I'm dropping it in Zoom chat here.
[3555.40 → 3557.94] This tells us where integrations are coming from.
[3558.88 → 3561.04] Which is the Git repo.
[3561.38 → 3565.28] The org is called integrations that Terraform provider GitHub is in.
[3565.68 → 3566.30] And then GitHub.
[3567.38 → 3567.66] Eh.
[3567.66 → 3569.42] They don't have the V4 in there, though.
[3569.58 → 3569.70] Yeah, no.
[3569.70 → 3570.94] I don't know what that's coming from.
[3571.18 → 3571.44] But.
[3571.44 → 3575.60] So I think there was something here.
[3575.68 → 3577.46] There was something in the documentation.
[3577.62 → 3578.04] Where was it?
[3578.32 → 3579.36] I know what it is.
[3579.48 → 3579.70] It's.
[3580.10 → 3581.16] This is a Go package.
[3581.56 → 3584.10] And they have a V4 version.
[3584.56 → 3584.90] Right.
[3584.90 → 3588.02] And so that's just the import path for the Go package.
[3588.14 → 3593.50] So you can leave that out as long as the Linde provider is a normal Go package here.
[3594.12 → 3594.58] Look.
[3595.08 → 3596.64] That is the line.
[3596.90 → 3597.40] Mm-hmm.
[3597.66 → 3598.14] Downloading.
[3598.26 → 3599.06] Found downloading.
[3599.28 → 3601.12] So that pulls it from the right place.
[3601.64 → 3602.00] Okay.
[3602.72 → 3603.10] Great.
[3603.68 → 3608.14] If your provider is an old version, how do I know if it's using an old version?
[3608.92 → 3609.18] Oh.
[3609.60 → 3610.04] Okay.
[3610.12 → 3610.42] I see.
[3611.30 → 3611.98] I was confused.
[3612.10 → 3612.62] Go mode vendor.
[3612.62 → 3619.02] I believe you need an actual replace stanza down there at the bottom.
[3619.66 → 3620.12] You think?
[3620.56 → 3621.28] I believe so.
[3621.92 → 3622.22] Okay.
[3622.34 → 3623.18] This is a requirement.
[3623.44 → 3627.16] So the way I understand it, I need to replace this with this.
[3627.58 → 3628.06] No.
[3628.06 → 3633.14] I believe that you'll have a dependency there on HashiCorp Terraform plugin SDK.
[3633.90 → 3638.42] And then you'll have a replacement statement at the bottom of the Go mod that indicates you
[3638.42 → 3644.68] want to replace that dependency that's in your requirement with the fork there that Hassan has.
[3645.26 → 3645.52] Okay.
[3645.52 → 3650.06] So you're saying that all I need to do is comment out this line, this replaces.
[3650.90 → 3651.26] Yep.
[3651.34 → 3653.36] That should be what we're looking for here.
[3654.16 → 3654.58] Okay.
[3654.58 → 3657.26] I wasn't sure that Go mods supports this.
[3657.64 → 3657.90] Yep.
[3658.06 → 3658.42] But okay.
[3658.50 → 3658.76] Replace statements.
[3659.70 → 3659.96] Yeah.
[3660.34 → 3660.70] Okay.
[3661.00 → 3661.52] Go more tidy.
[3662.98 → 3670.02] I believe here is where we need to set up whatever the credentials are needed to talk to Linde.
[3670.54 → 3671.12] I see.
[3671.36 → 3675.04] So we may want to do the same thing that the Terraform provider is doing.
[3677.04 → 3677.64] But...
[3677.64 → 3678.94] I see what you mean.
[3679.02 → 3679.24] Okay.
[3679.32 → 3679.78] I'm with you.
[3680.08 → 3682.90] So the only thing that we really need is a key.
[3684.34 → 3685.12] To talk to Linde?
[3685.76 → 3686.02] Yeah.
[3686.20 → 3686.98] That's the only thing.
[3687.30 → 3687.62] Cool.
[3688.14 → 3693.56] I would call it CLI token because that maps it to what the Linde CLI expected to be.
[3693.56 → 3696.74] Is that what you use with Terraform to be able to authenticate?
[3697.60 → 3698.54] I don't know.
[3698.80 → 3700.56] Because I believe what we're doing here is...
[3701.42 → 3705.22] So we're taking things out of the provider config and then setting the environment variable
[3705.22 → 3705.94] based on that.
[3706.06 → 3711.86] So when the underlying Terraform plugin is invoked, it will utilize those credentials
[3711.86 → 3714.36] specified by the environment variables.
[3715.42 → 3715.68] Yep.
[3716.30 → 3716.88] Let's see.
[3717.30 → 3717.78] Linde token.
[3718.34 → 3718.66] Nice.
[3718.86 → 3720.44] So I'm guessing that's what we want there.
[3720.88 → 3721.78] That's what we want, yeah.
[3722.20 → 3723.42] Where does this key come from?
[3723.50 → 3723.96] So hang on.
[3724.00 → 3724.40] Let me see.
[3724.58 → 3724.98] Key username.
[3725.38 → 3726.46] Where does this key come from?
[3726.74 → 3730.12] You just deleted the variable that was key username.
[3730.34 → 3732.72] But you can name it whatever...
[3732.72 → 3732.92] Sorry.
[3733.14 → 3734.38] It was way up at the top.
[3734.38 → 3735.78] Ah, in token.
[3735.94 → 3736.22] I see.
[3736.34 → 3736.50] Okay.
[3736.88 → 3737.08] Yep.
[3737.28 → 3738.00] That sounds good.
[3738.42 → 3742.90] I also am going to have to wrap up here pretty soon.
[3743.10 → 3743.38] Okay.
[3743.70 → 3744.66] Let's wrap up now.
[3745.16 → 3745.44] Okay.
[3745.62 → 3746.76] Yeah, let's wrap up now.
[3746.84 → 3747.72] I think this was a good point.
[3747.94 → 3753.02] After the pairing session with Dan, I had a few more with Mubarak Onus, one of the Terra Jet
[3753.02 → 3753.56] creators.
[3754.02 → 3756.12] And then he joined me to talk about the end result.
[3756.36 → 3757.78] Yeah, I'm glad to be here.
[3757.94 → 3762.04] We had a couple of early mornings and I think I had a couple of late nights.
[3762.04 → 3763.90] So why did we do this?
[3763.90 → 3769.00] The reason why we did this is that we wanted our Kubernetes clusters to not be provisioned
[3769.00 → 3770.66] via UI or CLI.
[3770.96 → 3771.84] So no Click Ops.
[3772.56 → 3774.28] Dan, that was a great word.
[3774.42 → 3777.02] No Click Ops, no UI, and not even CLI.
[3777.18 → 3782.48] We didn't want to have a CLI that we need to like a command to type to provision a Kubernetes
[3782.48 → 3782.90] cluster.
[3782.90 → 3789.00] Now, that is not entirely true because obviously we still have to give it a config, but there's
[3789.00 → 3791.66] something that provisions the cluster for us.
[3792.40 → 3794.72] And that is Cross plane.
[3794.94 → 3796.02] But not just Cross plane.
[3796.20 → 3800.40] There's this secret source element, which I didn't know about until Dan mentioned that,
[3800.50 → 3801.66] hey, have you seen Terra Jet?
[3801.66 → 3803.68] That was your idea.
[3804.00 → 3810.22] Well, so you see in Cross plane ecosystem, there are many providers and not all of them have
[3810.22 → 3813.22] support for all APIs that clouds actually expose.
[3813.76 → 3813.96] Right.
[3814.14 → 3815.62] And one of the examples was Linux.
[3815.70 → 3817.26] We didn't have a provider at all.
[3817.26 → 3824.52] So the plan with Terra Jet was like, you know, the motivation was that let's build something
[3824.52 → 3829.52] that can utilize the whole like great Terraform community and the great work that they did.
[3830.04 → 3832.42] So that was how it came to be.
[3833.12 → 3839.80] Design a code generator and a generic controller that can take any Terraform provider and make
[3839.80 → 3841.96] up a Cross plane provider out of it.
[3842.30 → 3842.58] Right.
[3842.90 → 3845.24] So this is full circle happening.
[3845.24 → 3850.06] Marcus, if you're listening to this, this is what happened with your Terraform provider.
[3850.42 → 3853.24] I remember work with Marcus while he was still at Linde.
[3853.74 → 3859.32] We were using Terraform to provision the instances which were running Docker at the time to host
[3859.32 → 3861.52] the changelog.com website and the entire setup.
[3861.98 → 3865.92] Then that was the seed which created the Linde Kubernetes engine.
[3866.44 → 3869.06] Then Marcus joined Cross plane and Abound.
[3869.06 → 3876.64] And now using the Terraform Linde provider that Marcus started to provision Kubernetes clusters
[3876.64 → 3880.00] on Linde using the Terraform provider using Cross plane.
[3880.38 → 3881.64] Like how crazy is that?
[3882.24 → 3884.34] It just takes a while just like to wrap your head around.
[3884.48 → 3891.18] This was like years in the making, and we didn't even know it until a few months ago when Dan
[3891.18 → 3892.00] mentioned Terra Jet.
[3892.00 → 3893.74] I didn't even know that this thing existed.
[3894.28 → 3902.46] So that's what we're using as a generator for a Linde provider that uses Terraform.
[3902.90 → 3903.62] So, okay.
[3903.82 → 3907.98] How many providers have been generated with Terra Jet to date?
[3908.14 → 3909.16] And where can we see them?
[3909.16 → 3909.68] Yeah.
[3909.68 → 3916.68] So, today we have the providers for the big three, AWS, Azure, and GCP.
[3917.74 → 3923.22] And those three providers have 2,000 almost CRDs in total.
[3923.58 → 3923.70] Right.
[3924.44 → 3930.38] And then you can see like if you go to Cross plane, Cantrip, Org, you will see others like you know
[3930.38 → 3932.78] providers similar to like Jetliner.
[3932.86 → 3935.06] For example, we have Equinix, Equinix Metal.
[3935.06 → 3936.74] We have Scale.
[3936.98 → 3939.90] All of these are like you know completely bootstrapped by the community.
[3940.54 → 3945.16] So, I would say I think in total like seven or eight right now.
[3945.42 → 3945.68] Okay.
[3945.86 → 3946.04] Yeah.
[3946.04 → 3946.80] There's quite a few.
[3946.98 → 3948.04] Provider TFX, Equinix.
[3948.12 → 3948.86] I can see that.
[3949.12 → 3949.88] Provider Helm.
[3950.12 → 3950.86] Provider Servo.
[3951.94 → 3953.28] What else am I seeing here?
[3953.80 → 3954.82] Provider Jet AWS.
[3955.08 → 3956.16] This is an interesting one.
[3956.22 → 3959.74] So, even though you have an AWS provider, there's also a Provider Jet AWS.
[3959.94 → 3961.06] Do you know the story behind that?
[3961.06 → 3967.38] So, the Provider AWS, the one that calls APIs directly, has around 100 CRDs.
[3967.48 → 3967.72] Okay.
[3967.84 → 3970.36] Which means like you know it maps 100 services.
[3970.54 → 3972.60] But AWS has liked you know hundreds.
[3973.10 → 3979.12] So, if you look at that Jet AWS, you will see it has 765 custom resource definition.
[3980.20 → 3984.84] Which is like you know just too many for Kubernetes community at this point.
[3985.10 → 3987.62] I can imagine having so many CRDs in your Kubernetes.
[3987.62 → 3990.10] Like you wouldn't even know which one to pick.
[3990.20 → 3991.48] I mean there's just so many of them.
[3991.58 → 3991.74] Okay.
[3991.82 → 3992.56] So, that makes sense.
[3993.20 → 3995.04] So, and we added another provider.
[3995.22 → 3995.66] Haven't we?
[3995.88 → 3996.80] In the last week.
[3997.66 → 3997.90] Yes.
[3998.00 → 3998.84] That was amazing.
[3999.16 → 4000.98] Like 12 commits.
[4001.42 → 4004.98] That's all it took to generate a Provider Jet Linde.
[4005.02 → 4006.22] Which is in Cross plane Cont rib.
[4006.28 → 4007.80] This is by the way our gift to you.
[4007.86 → 4008.86] Our Christmas gift to you.
[4009.00 → 4012.54] If you want to provision Linde Kubernetes engine clusters using Cross plane.
[4013.26 → 4014.72] This is the modern way of doing it.
[4015.20 → 4015.42] Right.
[4015.46 → 4018.38] Because Mark has built a Cross plane provider for Linde.
[4018.72 → 4020.78] Which hasn't seen much maintenance I think.
[4020.94 → 4022.88] The last update was a year ago.
[4022.96 → 4023.64] Maybe a bit longer.
[4023.82 → 4025.96] And I don't think it's working with the latest Cross plane versions.
[4026.16 → 4027.42] Many things have changed since.
[4028.46 → 4030.08] So, this one we know it works.
[4030.66 → 4032.16] But it only has a single resource.
[4032.24 → 4032.42] Right.
[4032.88 → 4034.10] Because that's all that we needed.
[4034.10 → 4036.38] And that is the LIKE resource.
[4036.68 → 4038.52] Linde LIKE cluster.
[4039.32 → 4041.20] Now, if you want more resources.
[4041.92 → 4042.48] Contribute.
[4042.82 → 4044.48] It's an open source repository.
[4044.68 → 4045.52] Public to everyone.
[4045.74 → 4046.94] So, if there's anything missing.
[4047.14 → 4048.90] What I would like to see is a Linde instance.
[4049.40 → 4051.86] I would like to provision some Linde instances and VMs with it.
[4051.98 → 4054.62] So, that would be my request to anyone that's listening.
[4054.82 → 4055.02] This.
[4055.22 → 4055.82] Marcus maybe.
[4056.42 → 4057.08] What do you think?
[4057.24 → 4058.08] Or someone else.
[4058.62 → 4059.36] But anyway.
[4059.44 → 4059.84] It's there.
[4060.14 → 4062.12] I'm wondering what is coming next for Terra Jet.
[4062.12 → 4064.08] So, Terra Jet.
[4064.20 → 4066.12] So, when we first started with Terra Jet.
[4066.34 → 4068.02] We had hit a problem.
[4068.90 → 4071.78] With API server handling that many CRDs, actually.
[4072.18 → 4072.38] Right.
[4072.42 → 4074.46] When you install 700 CRDs.
[4074.84 → 4078.48] API server gets like unresponsive for like 40 minutes or something.
[4078.76 → 4081.06] Which like, you know, affects all the workloads.
[4081.36 → 4083.44] That it was supposed to schedule.
[4084.88 → 4086.72] So, we have fixed that problem.
[4086.94 → 4087.86] I mean, there was a patch.
[4087.96 → 4090.62] And we accelerated some of the processes in upstream.
[4090.62 → 4094.98] So, now we are able to use those Jet providers.
[4095.56 → 4099.64] And in January, we will have a big splash of announcements.
[4099.84 → 4100.14] Okay.
[4100.34 → 4103.68] That will announce AWS, Azure, and GCP providers.
[4103.78 → 4104.44] Jet providers.
[4105.06 → 4107.94] With their like, you know, API groups stabilized.
[4108.78 → 4109.84] Configures are stabilized.
[4109.96 → 4112.24] And API fields are stabilized.
[4112.34 → 4116.62] And then we will start making some of the resources version.
[4116.62 → 4117.96] Version V1, beta 1.
[4118.28 → 4118.54] Right.
[4118.54 → 4120.42] Which has like, you know, more guarantees around that.
[4120.52 → 4123.58] And then we will have conversion webhooks in cross-plane.
[4123.72 → 4130.02] Which will affect like, you know, how easily we can make a resource.
[4130.16 → 4134.12] Let's say that you're not happy with the implementation in Terraform provider.
[4134.66 → 4135.98] You can just switch it to native.
[4136.20 → 4136.48] Okay.
[4136.48 → 4139.14] With API calls directly to AWS.
[4139.58 → 4145.88] So, all this like, you know, new stuff that will allow community to bootstrap new providers.
[4146.12 → 4149.22] And like, you know, make upstream work with them.
[4149.60 → 4153.56] And then like, you know, it's just so many CRDs and built easily.
[4153.76 → 4153.94] Yeah.
[4154.02 → 4155.92] That you won't have a problem.
[4156.04 → 4157.54] Like, you know, hey, is this resource supported?
[4157.74 → 4158.94] Well, yes, probably.
[4159.32 → 4163.22] Instead of like, you know, let me take a look at how it would be to implement it.
[4163.22 → 4171.44] I do have to say, having gone from nothing, like I knew nothing about how to implement a cross-plane provider to using Terra Jet.
[4171.76 → 4173.04] That was really smooth.
[4173.24 → 4177.98] I think anyone that is determined to write a cross-plane provider doesn't exist yet.
[4178.34 → 4182.46] And there is a Terraform provider which exists, ours, and they can have it.
[4182.64 → 4183.70] Which is amazing to see.
[4183.86 → 4187.44] So, this is basically proof that your idea works.
[4187.62 → 4188.08] Yeah.
[4188.08 → 4196.96] I mean, in fact, we had a case where someone in the community, the provider scale you saw, that was actually written in six hours.
[4197.38 → 4197.90] There we go.
[4198.78 → 4199.18] Amazing.
[4199.56 → 4203.32] And also like, that was the hardest part that like bootstrap in the provider.
[4203.50 → 4213.28] If you, for example, decide to add an instance resource to Jetliner provider, it's like, you know, 10 or 15 lines of code as you see the like single configuration.
[4213.28 → 4214.02] That's right.
[4214.22 → 4215.34] So, all the commits are there.
[4215.44 → 4216.10] Go and check them.
[4216.18 → 4218.10] See what we've done for provider Jetliner.
[4218.42 → 4219.94] Again, it's very, very simple.
[4220.52 → 4225.96] So, what I would like to do now is show you how easy it is to actually do this.
[4225.98 → 4230.58] And I say show because we record video, and we may not have time to publish everything in time or ever.
[4230.74 → 4231.14] I don't know.
[4231.22 → 4232.60] You know, things can get very busy.
[4232.60 → 4235.84] But at least we'll do like a step-by-step process.
[4236.00 → 4247.00] There's a pull request, by the way, in the changelog org, the changelog.com repository, pull request 399, which has all the text, all the screenshots, everything on how to do this, all the links.
[4247.34 → 4248.84] So, this is what we're going to do next.
[4248.94 → 4256.26] We're going to install Cross plane, install the provider, and then provision the Linde Kubernetes engine cluster using this provider.
[4256.68 → 4257.60] Then we target it.
[4258.18 → 4259.82] And then we try something crazy.
[4259.82 → 4262.92] You know that I'm all for crazy, right, trying crazy things and see what happens.
[4263.12 → 4264.54] So, that's what we're going to do next.
[4265.02 → 4265.28] Okay.
[4265.54 → 4268.72] So, I am in the 2021 directory currently.
[4269.12 → 4273.56] And I'm going to do, I'm already targeting our production Kubernetes clusters.
[4273.70 → 4274.36] Oh, yes, of course.
[4275.06 → 4278.60] Mufasa, when I mentioned this to you first, like I develop in production.
[4279.28 → 4280.82] You laughed, but I'm serious.
[4281.36 → 4283.00] That's like the only thing that matters.
[4283.10 → 4284.60] If it's not in production, it's inventory.
[4284.92 → 4286.62] So, I don't like inventory.
[4286.80 → 4287.92] I like stuff being out there.
[4287.92 → 4291.84] So, make, in this case, LIKE cross plane.
[4292.26 → 4299.30] And what that does, that installs Cross plane version 1.5.1 using Helm straight into production.
[4300.02 → 4304.02] So, installing Cross plane two minutes later, it's done.
[4304.34 → 4305.38] That's how simple it is.
[4305.58 → 4308.66] The next step is make Cross plane Linde provider.
[4308.94 → 4309.98] And that's it.
[4310.18 → 4310.66] That's simple.
[4310.74 → 4313.30] That was really quick because the provider is tiny, right?
[4313.34 → 4316.70] Like 18 kilobytes, I've seen the image, which then pulls a bigger image.
[4316.70 → 4317.44] How does that work?
[4317.50 → 4317.96] Can you tell us?
[4318.74 → 4318.90] Yeah.
[4319.12 → 4326.64] So, the metadata image, it's an OCI image, where it has only the metadata.yaml that contains
[4326.64 → 4329.92] your CRDs and also some information about your package.
[4330.24 → 4337.46] Once it's downloaded by the package manager, it installs the CRDs and then creates a deployment
[4337.46 → 4339.92] with the image that you provided there.
[4340.44 → 4343.04] So, like, you know, that other image contains the binary.
[4343.04 → 4343.52] Okay.
[4343.52 → 4343.88] Okay.
[4344.22 → 4346.12] And which version did we install of the provider?
[4346.42 → 4349.52] Version 0.0.0-12.
[4349.72 → 4351.00] So, there's no tag for this.
[4351.06 → 4352.38] This is like a dev-only version.
[4352.82 → 4353.24] We trust.
[4353.40 → 4354.12] Dev in production.
[4354.66 → 4355.66] The dream is real.
[4356.28 → 4357.42] Production became dev.
[4357.80 → 4358.18] Great.
[4358.36 → 4359.52] So, okay.
[4359.56 → 4360.24] We installed it.
[4360.32 → 4361.02] We configured it.
[4361.06 → 4361.54] It's all there.
[4361.68 → 4364.98] So, how can we check that the provider's there?
[4364.98 → 4371.88] If we maybe get all the pods in the namespace cross plane system, because that's where everything
[4371.88 → 4376.20] gets installed, we see that we have cross plane installed.
[4376.32 → 4377.70] We have the cross plane RAC manager.
[4377.82 → 4378.58] These are two pods.
[4378.70 → 4380.86] And the third one is the Jellicoe pod.
[4381.44 → 4381.72] Cool.
[4382.14 → 4383.92] So, what can we do next?
[4384.14 → 4385.94] I'm using canines as a CLI.
[4386.04 → 4387.16] It just makes me...
[4387.16 → 4389.40] It allows me to do things really, really quick.
[4389.40 → 4395.30] So, if we go to look at all the aliases, which is control A for me, and I search for cluster,
[4395.72 → 4396.80] we see a new CRD.
[4397.64 → 4404.30] And the CRD is in the Linde jet cross plane IO V1 alpha 1 group.
[4404.46 → 4406.90] That's how we can provision new clusters.
[4407.10 → 4408.02] So, let's try that.
[4408.44 → 4411.94] If we go to cluster to list out clusters we have, we have no clusters.
[4412.12 → 4412.44] Great.
[4412.86 → 4416.56] Let's do make cross plane LIKE.
[4416.56 → 4419.50] All this does, I still have to run a command.
[4419.66 → 4419.88] Okay.
[4420.08 → 4420.34] Okay.
[4420.44 → 4421.56] I know what I mentioned earlier.
[4421.64 → 4422.52] There will be no commands.
[4422.96 → 4424.64] But this is a different type of command.
[4424.78 → 4431.92] I'm not telling the Linde API, hey, Linde, create me a LIKE instance.
[4432.28 → 4437.78] I'm telling cross plane to create on my behalf a LIKE instance.
[4438.18 → 4442.10] And there's something really cool about this, because cross plane will continuously reconcile
[4442.10 → 4444.06] what I ask of it.
[4444.48 → 4445.56] Like, how cool is that?
[4445.56 → 4450.32] So, that's, I think, my favourite cross plane features, which happens to be a Kubernetes feature
[4450.32 → 4450.72] as well.
[4450.94 → 4454.44] You know, declarative, you tell it what you want, and it will make it so.
[4454.56 → 4455.60] I love that story.
[4456.06 → 4456.42] Great.
[4456.62 → 4456.84] Okay.
[4456.90 → 4457.52] So, this succeeded.
[4458.46 → 4459.62] What are we seeing now?
[4459.62 → 4467.54] We are seeing that 42 seconds ago, a new LIKE 2021-1217, by the way, it's the 17th of December
[4467.54 → 4468.66] when we are recording this.
[4469.50 → 4474.44] It just uses the current date when this new cluster has been created, or it's, you know,
[4474.46 → 4476.04] it's asked to be created.
[4476.04 → 4481.40] So, if we go to the where do we have it?
[4481.52 → 4481.96] Linde.
[4482.92 → 4488.70] And if we go to our Kubernetes lists, we see a new cluster, which is Kubernetes version 1.22.
[4489.24 → 4489.76] Nice.
[4490.42 → 4494.14] I'm wondering, could it be our new production cluster for 2022?
[4494.14 → 4496.40] If you could see me, I'm winking.
[4496.76 → 4497.50] Yes, it will be.
[4498.66 → 4505.86] 1.22, Kubernetes 1.22, the first version of our production 2022 Kubernetes cluster.
[4506.36 → 4506.90] This is it.
[4507.78 → 4509.72] Because it's ready, it's synced.
[4509.90 → 4512.66] We have the external name, which is the which is the ID.
[4513.60 → 4514.68] The instance has booted.
[4514.78 → 4515.24] Great.
[4515.60 → 4515.96] Okay.
[4516.20 → 4517.02] So, did it work?
[4517.02 → 4521.74] Well, let's try to make a cross-plane LIKE kubeconfig.
[4522.90 → 4525.76] All these, by the way, are in our repo.
[4525.92 → 4526.80] You can check them out.
[4526.96 → 4529.34] Actually, do you want to tell us what happened behind the scenes?
[4529.48 → 4531.32] Like, how were we able to do this?
[4531.68 → 4531.86] Yeah.
[4532.78 → 4536.86] So, the cross-plane has this notion of connection detail secret,
[4537.24 → 4543.36] where it stores all the sensitive information you need to use that resource, if any.
[4543.36 → 4548.16] For example, we see that, like, you know, mostly in Kubernetes clusters,
[4548.58 → 4552.38] database instances where you have, like, a password or some other details.
[4552.56 → 4552.64] Right.
[4553.06 → 4557.88] And not in others, for example, VPCs, where you don't need any token or something to connect.
[4558.90 → 4566.56] So, here, what we see is that Terra Jet does this automatically using Terraform's TF state
[4566.56 → 4571.86] and exports it in its secret.
[4571.86 → 4578.68] And then we have added a custom configuration that will get that secret.
[4578.84 → 4580.80] You see the attribute.kubeconfig.
[4580.96 → 4584.86] That is automatically put here, taken from state.
[4585.08 → 4592.20] But the problem is that LENT Terraform provider actually base64 encodes the kubeconfig.
[4592.20 → 4598.54] So, you've got, like, you know, secret, base64 encoding, and then another encoding on top of that.
[4598.82 → 4603.18] What we did was to provide a custom configuration for Terra Jet,
[4603.64 → 4611.58] which takes one field from attributes and base64 decodes and puts it here,
[4611.76 → 4613.76] which makes it ready to use right away.
[4614.06 → 4620.58] With, like, you know, subject or other provider helm or provider Kubernetes controllers.
[4620.58 → 4625.44] So, while we can get the kubeconfig locally,
[4625.86 → 4630.16] and then we can use, like, subject or subject, whatever you want to call it,
[4630.26 → 4634.18] and use that kubeconfig to target that cluster,
[4634.42 → 4642.48] what we may want to do is let Cross plane provision other things inside this cluster
[4642.48 → 4646.82] so that we wouldn't necessarily need to give this kubeconfig away.
[4647.00 → 4648.44] It stays within Cross plane.
[4648.64 → 4649.72] You know, it's all there.
[4649.72 → 4654.12] Cross plane has it for it to be able to provision other things inside this cluster.
[4654.44 → 4658.76] And maybe this is the path where I lose access to Kubernetes clusters.
[4659.50 → 4660.04] Is that it?
[4661.56 → 4665.32] Like, it's more difficult for me to just, like, run commands against them.
[4665.64 → 4669.66] The idea being that this could be, like, a fully self-automated system.
[4670.00 → 4670.80] It creates itself.
[4671.02 → 4672.96] It provisions itself with everything it needs.
[4672.96 → 4677.40] It pulls down all the bits, including the application, the latest version of the changelog app,
[4677.74 → 4678.50] and it just runs.
[4678.64 → 4681.06] It updates DNS because it's like a self-updating system.
[4681.14 → 4686.54] So, this is one step closer to a self-updating, self-provisioning system.
[4686.90 → 4689.30] And that is a dream which I had many years ago,
[4689.30 → 4691.96] and I'm one step closer, and that makes me so happy.
[4692.28 → 4692.50] Okay.
[4692.86 → 4698.46] So, we have the kubeconfig locally, and I'm not there yet in that dream world.
[4698.56 → 4701.88] So, I'm still putting in the kubeconfig, pulling it down locally,
[4701.88 → 4705.62] and now going with canines targeting the new cluster.
[4705.62 → 4709.90] And what we see is that it's just like any regular cluster.
[4710.06 → 4710.48] There it is.
[4710.66 → 4711.58] Just the default pods.
[4712.14 → 4713.64] Four minutes ago, they were created.
[4713.90 → 4715.60] If we look at the node, it's the new node.
[4715.70 → 4717.84] It's version 1.22.2.
[4718.10 → 4721.78] So, the latest Kubernetes version on Linde currently.
[4722.34 → 4726.76] And I'm wondering what is going to happen if by accident,
[4727.16 → 4728.20] and I'm doing air quotes,
[4728.34 → 4731.66] if accidentally Jared deletes the cluster.
[4733.24 → 4734.24] I don't know, Jared.
[4734.34 → 4735.36] I just gave an example.
[4735.36 → 4738.96] You know, like we do crazy things together all the time.
[4739.10 → 4742.02] So, you know, you're like the first one when I'm thinking about someone
[4742.02 → 4744.84] deleting some changelog infrastructure.
[4745.12 → 4748.18] So, let's just click this delete button.
[4748.44 → 4749.58] Oh, pretend I'm Jared.
[4749.70 → 4750.28] What is it like?
[4750.36 → 4751.72] No, I don't recognize this cluster.
[4751.80 → 4752.62] Let me just delete it.
[4752.66 → 4753.72] It's just extra resource.
[4753.82 → 4754.76] So, let's delete the cluster.
[4755.08 → 4757.78] And yes, I confirm I want to delete it.
[4758.24 → 4759.20] And the cluster's gone.
[4759.74 → 4762.54] And luckily, I deleted the correct cluster.
[4762.60 → 4764.02] I haven't deleted our production cluster.
[4764.02 → 4766.00] But if I had deleted our production cluster,
[4766.46 → 4767.94] I mean, good luck setting everything up.
[4768.00 → 4769.86] There's like a lot of stuff to do, a lot of steps.
[4769.94 → 4773.00] And yes, we have like a make target, which puts everything together.
[4773.34 → 4775.12] And, you know, it's okay.
[4775.26 → 4776.90] But it's not as good as it could be.
[4777.24 → 4778.30] Yeah, Jared wouldn't do that.
[4778.38 → 4779.50] No, Jared wouldn't do that.
[4779.84 → 4780.66] No, he wouldn't.
[4780.66 → 4782.18] I do that all the time.
[4782.18 → 4784.20] You know, like, let's just take production down.
[4784.58 → 4785.14] You know, whatever.
[4785.26 → 4785.98] Let's see what happens.
[4785.98 → 4786.86] Just for the fun of it.
[4787.22 → 4791.86] So, what will this do behind the scenes with the new setup that we have?
[4791.98 → 4793.00] Can you tell us?
[4793.56 → 4793.82] Yes.
[4793.96 → 4800.26] So, what's going to happen is that the controller will reconcile and see that the cluster is not there.
[4800.26 → 4804.44] It's gone, which is like, you know, what happens when you first create the resource.
[4805.08 → 4810.12] The very first thing that a provider does is to check whether a resource is there and create it if not.
[4810.24 → 4810.34] Yeah.
[4811.06 → 4814.52] And it will be for the controller, it will be just like that.
[4814.58 → 4816.28] Hey, I checked the resource, and it's not there.
[4816.32 → 4817.38] So, I need to create it.
[4817.38 → 4821.86] So, it goes ahead and tries to create a new cluster.
[4822.18 → 4822.28] Right.
[4822.48 → 4824.78] And that takes 30 seconds, a minute.
[4825.08 → 4827.98] How long does it take for it to figure out that, hey, I'm missing a cluster?
[4828.36 → 4838.58] Well, so, because it doesn't get any events or anything in Kubernetes cluster, it will need to hit the long wait period, which is like, you know, one minute.
[4838.68 → 4838.86] Yeah.
[4838.86 → 4843.50] So, at most in a minute, it will recognize that change.
[4843.50 → 4849.04] Or, you can make a change on the custom resource, which will trigger a Kubernetes event.
[4849.40 → 4853.52] You go to that controller, and it will start all the processes there.
[4854.06 → 4857.40] So, I was trying to find this out to see where it's reconciling.
[4857.48 → 4858.34] It's finding it.
[4858.66 → 4860.22] I think I just missed it.
[4860.72 → 4863.10] The event, everything is synced now.
[4863.52 → 4863.72] Right.
[4863.78 → 4864.58] Everything's ready.
[4864.84 → 4865.68] The cluster's back.
[4865.82 → 4867.24] I mean, I just had to refresh the page.
[4867.48 → 4867.70] Nice.
[4868.02 → 4869.66] What about the Li nodes?
[4870.30 → 4871.34] Is it still there?
[4871.56 → 4872.48] It's offline.
[4872.48 → 4872.56] Offline.
[4873.20 → 4873.68] Interesting.
[4874.08 → 4875.36] I don't know why that's offline.
[4876.08 → 4885.92] So, when I deleted the cluster, whatever happened behind the scenes, maybe the node pool, the default node pool got deleted as well.
[4886.08 → 4886.78] Oh, it's booting.
[4887.02 → 4890.52] So, I think that the node was deleted as well.
[4890.76 → 4893.44] And this is like the worker VM.
[4893.92 → 4895.86] And the new one was created.
[4895.86 → 4902.92] So, deleting the cluster from the Linde UI, from the cloud, linode.com, it also deletes all the worker nodes.
[4903.28 → 4906.70] So, when the cluster gets recreated, it has to obviously recreate all the nodes.
[4906.78 → 4907.30] And there it is.
[4907.34 → 4908.00] It's back.
[4908.26 → 4908.46] Okay.
[4908.68 → 4909.76] So, everything here is ready.
[4909.88 → 4910.36] It's synced.
[4910.36 → 4918.16] Because while the cluster has been created, like the object, the cluster object, the node pool that's associated with it hasn't been finished yet.
[4918.22 → 4920.70] And I think that's where composite resources come in.
[4920.96 → 4922.12] Can you tell us a bit about that?
[4922.12 → 4931.72] So, in other cases where you have the node group as represented as a different resource, you can actually have like, you know, two resources in a single composition.
[4932.02 → 4932.16] Right.
[4932.54 → 4938.68] And additionally, just like you mentioned earlier, we can have more things installed there as well.
[4938.92 → 4943.58] Because like, you know, the dependencies that are resolved automatically, just like, you know, Kubernetes.
[4943.58 → 4948.22] So, for example, you would create your composite cluster resource.
[4948.66 → 4951.42] Cluster will be created, and node groups will be booted.
[4952.12 → 4953.42] And then the installations will start.
[4953.54 → 4953.64] Right.
[4953.68 → 4955.74] With provider kubeconfig or provider helm.
[4956.48 → 4962.40] So, like, you know, once your composite cluster CR reports ready, everything is ready.
[4962.52 → 4965.96] And like, you know, just back in its initial state.
[4966.08 → 4966.18] Yeah.
[4966.32 → 4971.80] So, it will just like, you know, revert it back to the original state, including all the things in composition.
[4971.80 → 4972.40] Okay.
[4972.58 → 4979.76] So, now what happened is we are targeting the same control plane, and we could see how the pods were being recreated.
[4979.92 → 4983.54] So, 90 seconds ago, 100 seconds ago, everything was created from scratch.
[4983.76 → 4989.52] We accidentally, air quotes again, deleted the cluster, cross plane, recreated the cluster.
[4989.80 → 4990.76] The node pool was recreated.
[4990.86 → 4992.02] The node pool had a single node.
[4992.54 → 4994.32] And then everything was put back on it.
[4994.38 → 4995.96] Like, by default, what's there?
[4995.96 → 5007.36] What we would have been missing, if, for example, if we had added any extra resources, like ingress nginx or external DNS or all the other components that we need, those would no longer be present.
[5007.52 → 5009.42] Because, let's be honest, we deleted the cluster.
[5009.80 → 5011.18] And that should delete everything in it.
[5011.36 → 5017.26] And this is, I think, where a human, i.e. me, would have come in and like run commands.
[5017.38 → 5019.86] Oh, I have to get production back, you know, because it was deleted.
[5019.86 → 5023.22] But how amazing would it be if cross plane could do this?
[5023.34 → 5028.90] So, it would know, oh, it's not just a cluster which I need, it's all this extra stuff that needs to be present in the cluster.
[5029.36 → 5030.56] Now, that is really exciting.
[5031.04 → 5032.00] Next year, right?
[5032.40 → 5033.10] I think we did enough.
[5033.12 → 5033.26] Yep.
[5033.42 → 5034.62] I think we did enough this Christmas.
[5035.34 → 5035.74] Cool.
[5036.22 → 5036.68] All right.
[5037.32 → 5040.32] So, what happens next?
[5041.00 → 5041.90] What happens next?
[5042.42 → 5046.26] Well, I think there are a couple of improvements that we can do.
[5046.26 → 5051.18] I already mentioned installing all like the base, having, I think, I think this is your idea.
[5051.32 → 5052.54] Can you tell us about your idea?
[5052.88 → 5054.82] Afar, this is really, perfect.
[5055.10 → 5055.82] The two compositions.
[5056.36 → 5059.82] So, maybe I can give a little summary about what composition does.
[5059.96 → 5060.06] Sure.
[5060.36 → 5062.68] Composition is, has two parts.
[5062.82 → 5067.20] One is XRD, similar to CRDs, where you define your own API.
[5067.62 → 5071.18] But with XRDs, you can define two different APIs.
[5071.18 → 5077.46] One is namespace and the other one is cluster scoped, which does not have any namespaces.
[5078.20 → 5087.88] So, what we usually see is that people create a composition with all the base system components in the same composition.
[5088.16 → 5090.12] Like, we call it batteries included.
[5090.12 → 5095.38] If you go to like, you know, platform references we have on the upbound org, you will see some of the examples.
[5095.90 → 5095.98] Right.
[5096.06 → 5106.06] Where we, for example, install Prometheus or like, you know, a few other tools that your platform team might want every cluster to have, like security agents.
[5106.36 → 5117.00] In this case, as listed there in the PR, you've got the cert manager, you've got a Grafana agent, and a few other components that you want to install.
[5117.00 → 5122.20] And then the other composition is usually the application itself.
[5122.58 → 5127.20] In that, in that composition, you would define like, you know, what changelog specifically needs.
[5127.44 → 5141.44] So that, for example, you would create a single cluster with that base composition and then refer to it from many namespaces in your seed cluster and from many applications that can be installed to that cluster.
[5141.60 → 5141.78] Right.
[5141.78 → 5148.58] So you would have like, you know, the cluster that is like, you know, managed in one namespace, maybe like, you know, changelog system.
[5148.68 → 5148.82] Yeah.
[5149.02 → 5150.12] With its own claim.
[5150.24 → 5153.78] Their claim is what we call like similar to PVC, percent volume claim.
[5153.84 → 5154.02] Yeah.
[5154.22 → 5154.98] That is namespace.
[5155.52 → 5169.32] So you would have that production cluster, but like, you know, different teams or developers in their own namespace, they would refer to that central production cluster in their claims that are defined again by you.
[5169.32 → 5169.48] Yeah.
[5169.54 → 5170.20] Via XRD.
[5170.20 → 5181.56] So it's about like, you know, publishing a new API instead of like, you know, we, instead of going through all the fields of the specific clouds, you would publish API with only because you want to be configured.
[5181.90 → 5182.18] Okay.
[5182.64 → 5183.62] That is really cool.
[5183.84 → 5185.30] I can hardly wait to do that.
[5185.40 → 5186.58] I mean, that is seriously cool.
[5186.58 → 5196.06] Like having all this stuff abstracted in a composition to just capture what it means for the entire changelog setup to come online would be so amazing.
[5196.68 → 5205.30] The other thing which would be also amazing is to move cross plane from being hosted on our cluster to be hosted on about cloud.
[5205.44 → 5211.18] Because the dream is there is a seed cluster somewhere, which is managed by someone else, in this case, about cloud.
[5211.18 → 5212.98] And the cross plane is there.
[5213.10 → 5215.08] We can define all the important stuff.
[5215.32 → 5220.98] And that is the seed, which controls all the other clusters, everything else, and not just clusters, other things as well.
[5221.48 → 5224.60] Again, I don't want to go too far with this idea, like blow your minds completely.
[5224.60 → 5227.98] But why doesn't it manage some fly IO apps?
[5228.32 → 5229.94] Or why doesn't it manage maybe some DNS?
[5230.34 → 5237.80] Or why doesn't it manage like other things from the seed cluster rather than because right now the external DNS is what we use in every cluster to manage its own DNS.
[5238.02 → 5238.82] And that's okay.
[5238.96 → 5240.18] We may need to do that.
[5240.44 → 5244.84] But what about a top level thing, which then, you know, seeds everything else?
[5245.10 → 5247.24] So that's something which I'm excited about.
[5247.78 → 5252.50] Well, I'm really looking forward to what we'll do together next year, move off with all this stuff.
[5252.50 → 5254.86] There's like so many improvements which we can drive.
[5254.98 → 5256.12] I'm really keen on that.
[5256.16 → 5256.88] It's the first step.
[5257.24 → 5264.48] But you as a listener, what I would say is have a look at the provider Jet Linde in the cross plane Cantrip org.
[5265.28 → 5267.06] See if, you know, it's helpful.
[5267.60 → 5270.28] And Merry Christmas and Happy New Year.
[5270.42 → 5271.22] Anything else to add?
[5273.42 → 5278.74] Yeah, it was great working with you for the last couple of days to get all these things done.
[5279.20 → 5281.04] And yeah, I'm honoured to be here.
[5281.36 → 5281.92] Thank you, Mubarak.
[5281.92 → 5283.16] It's been my pleasure.
[5283.34 → 5284.02] Thank you very much.
[5284.08 → 5284.70] See you next year.
[5288.58 → 5291.02] Thank you for tuning in to another episode of Ship It.
[5291.18 → 5294.06] This is just one of our podcasts for developers.
[5294.62 → 5297.58] Go to changelog.com forward slash master for the rest.
[5297.78 → 5302.74] You can join us via changelog.com forward slash community for free.
[5303.38 → 5307.70] The only cost is happiness credits if you choose to not interact with us.
[5308.16 → 5309.80] There are no imposters in our Slack.
[5310.18 → 5311.30] Everyone is welcome.
[5311.92 → 5315.86] Huge thanks to our partners Vastly, Launch Darkly and Linde.
[5316.52 → 5319.46] Thank you, Break master Cylinder for all our awesome beats.
[5320.10 → 5321.18] That's it for this week.
[5321.48 → 5322.28] See you next week.
[5323.02 → 5324.50] Actually, there's one more thing.
[5324.50 → 5326.84] Thank you for the great feedback, Alex.
[5326.84 → 5331.22] You're the reason why these episode outros will get extra love from now onwards.
[5332.06 → 5333.28] Keep shipping and improving.
[5333.78 → 5335.44] Inventory is overrated.
