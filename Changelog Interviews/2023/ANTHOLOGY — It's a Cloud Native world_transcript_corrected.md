[0.00 → 7.98] Welcome back friends this week on the change law we are back at the Linux Foundations open
[7.98 → 13.76] source summit North America 2023 in Vancouver Canada.
[14.02 → 17.06] We have another anthology for you.
[17.24 → 20.34] This one is taking you to the cloud native world.
[20.44 → 22.70] This is after all a cloud native world.
[22.78 → 26.16] We're just all trying to operate in it on today's show.
[26.22 → 27.38] We're talking to Jeffrey Sika.
[27.38 → 30.50] Jeffrey is part of the CNCF.
[30.62 → 33.32] He works on the developer experience and programs.
[33.66 → 34.40] Eddie Zane ski.
[34.50 → 39.48] He's on the Kubernetes SIG CLI team helping to maintain the Kubernetes CLI.
[39.90 → 45.40] And also Jaron Schneider, co-creator of Dapper and founder and CTO at Diagram.
[45.90 → 46.76] But it's a big show.
[46.84 → 47.48] So let's get to it.
[47.56 → 51.52] A big thank you to our friends and partners at Vastly and Fly.
[51.74 → 54.82] This pod got to you fast because Vastly is fast globally.
[54.82 → 56.78] Check them out at Fastly.com.
[56.78 → 62.10] And our friends at Fly help us put our app in our database close to our users all over the world with no ops.
[62.40 → 64.50] Check them out at fly.io.
[64.50 → 80.28] I'm here with Tom Hu, dev advocate at Sentry on the Codec team.
[80.64 → 83.60] So, Tom, tell me about Sentry's acquisition of Codec.
[83.88 → 87.12] And in particular, how is this improving the Sentry platform?
[87.12 → 94.42] When I think about the acquisition, when I think about how does Sentry use Codec or conversely, how does Codec use Sentry?
[94.64 → 97.76] Like I think of Codec and I think of the time of deploying.
[98.00 → 100.16] When you're a software developer, you have your life to go.
[100.22 → 100.68] You write your code.
[100.74 → 101.30] You test your code.
[101.38 → 101.80] You deploy.
[102.18 → 103.44] And then your code goes into production.
[103.44 → 105.20] And then you sort of fix good bugs.
[105.50 → 108.84] And I sort of think of that split in time as like when you actually do that deploy.
[109.52 → 112.62] Now, where Codec is really useful is before deploy time.
[112.92 → 114.48] It's when you are developing your code.
[114.64 → 117.12] It's when you're saying, hey, like I want to make sure this is going to work.
[117.38 → 119.40] I want to make sure that I have as few bugs as possible.
[119.78 → 123.14] I want to make sure that I've thought of all the errors and all the edge cases and whatnot.
[123.64 → 125.74] And Sentry is the flip side of that.
[125.74 → 128.72] It says, hey, what happens when you hit production, right?
[128.76 → 131.58] When you have a bug, and you need to understand what's happening in that bug.
[131.82 → 133.32] You need to understand the surrounding context.
[133.38 → 135.92] You need to understand where it's happening, what the stack trace looks like.
[135.92 → 139.14] What other local variables, you know, exist at that time.
[139.14 → 140.34] So that you can debug that.
[140.64 → 143.02] And hopefully you don't see that error case again.
[143.26 → 146.38] When I think of like, oh, what can Sentry do with Codec?
[146.42 → 147.70] Or what can Codec do with Sentry?
[148.12 → 150.86] It's sort of taking that entire spectrum of the developer lifecycle.
[151.40 → 156.78] Of, hey, what can we do to make sure that you ship the least buggy code that you can?
[157.06 → 161.70] And when you do come to a bug that is unexpected, you can fix it as quickly as possible, right?
[161.86 → 164.76] Because, you know, as developers, we want to write good code.
[164.76 → 167.86] We want to make sure that people can use the code that we've written.
[168.18 → 170.08] We want to make sure that they're happy with the product.
[170.22 → 171.04] They're happy with the software.
[171.16 → 172.68] And it works the way that we expect it to.
[173.04 → 182.12] If we can build a product, you know, the Sentry plus Codec thing to make sure that you are de-risking your code changes and de-risking your software,
[182.58 → 186.68] then, you know, we've hopefully done the developer community as service.
[187.26 → 190.18] So Tom, you say bring your tests and you'll handle the rest.
[190.28 → 190.94] Break it down for me.
[190.94 → 194.42] How does a team get started with Codec?
[194.76 → 199.10] You know what you bring to the table is like testing and you bring your coverage reports.
[199.60 → 202.40] And what Codec does is we say, hey, give us your coverage reports.
[202.70 → 208.70] Give us access to your code base so that we can, you know, overlay code coverage on top of it and give us access to your CCD.
[208.70 → 216.80] And so with those things, what we do and what Codec is really powerful at is that it's not just, hey, like this is your code coverage number.
[216.80 → 223.70] It's, hey, here's a code coverage number and your viewer also knows and other parts of your organization know as well.
[223.70 → 227.68] So it's not just you're dealing with code coverage and saying, I don't really know what to do with this.
[228.04 → 233.16] Because we take your code coverage, we analyze it, and we throw it back to you into your developer workflow.
[233.72 → 236.68] And by developer workflow, I mean your pull request, your merge request.
[237.04 → 241.48] And we give it to you as a comment so that you can see, oh, great, this was my code coverage change.
[241.48 → 245.46] But not only do you see this sort of information, but your viewer also sees it.
[245.58 → 248.52] And they can tell, oh, great, you've tested your code, or you haven't tested your code.
[248.98 → 255.28] And we also give you a status check, which says, hey, like you've met whatever your team's decision on what your code coverage should be,
[255.34 → 257.78] or you haven't met that goal, whatever it happens to be.
[258.06 → 265.02] And so Codec is particularly powerful in making sure that code coverage is not just a thing that you're doing on your own island as a developer,
[265.48 → 268.78] but that your entire team can get involved with and can make decisions.
[269.26 → 270.18] Very cool. Thank you, Tom.
[270.18 → 277.28] So, hey, listeners, head to Sentry and check them out, Sentry.io, and use our code changelog.
[277.52 → 283.32] So the cool thing is, is our listeners, you get the team plan for free for three months.
[283.82 → 286.90] Not one month, not two months, three months.
[287.32 → 289.62] Yes, the team plan for free for three months.
[289.80 → 290.90] Use the code changelog.
[290.98 → 299.28] Again, Sentry.io, that's S-E-N-T-R-Y.io, and use the code changelog.
[299.28 → 302.20] Also, check out our friends over at Codec.
[302.42 → 304.38] That's CodeCov.io.
[304.80 → 307.48] Like code coverage, but just shortened to Codec.
[307.88 → 309.10] CodeCov.io.
[309.76 → 310.08] Enjoy.
[310.08 → 310.24] Enjoy.
[310.24 → 321.98] antisemitism hosting.
[321.98 → 322.72] Begins doing it.
[322.72 → 323.72] People doing this work Jaime.
[323.72 → 326.64] Let's go.
[328.76 → 329.56] They do everything.
[330.16 → 330.68] We're big.
[330.80 → 331.48] They let go.
[333.66 → 334.80] portfolios.
[334.80 → 337.16] They're not a union, or they hope to contribute to you.
[337.16 → 343.28] So we're here with Fee, but it's really Jeffrey.
[343.74 → 348.00] Yeah, full name is Jeffrey Sika, but pretty much everyone in the community calls me Fee.
[348.34 → 351.94] People even on emails say, hey, please talk to Fee.
[352.02 → 357.16] And it's probably like, okay, but why the heck is this person like Jay Sika at Linux Foundation?
[357.36 → 359.32] It's like, no, everyone calls me Fee.
[359.80 → 366.10] How did you, did you give yourself this Fee name or is it, you know, I mean, it's your handle.
[366.10 → 367.48] It is my handle.
[367.64 → 368.68] Self-inflicted wound here?
[369.32 → 370.88] No, no, not even.
[371.36 → 380.32] A buddy of mine at this point, like 25 years ago on ye old AOL Instant Messenger, misspelt my name once.
[381.16 → 381.54] Stuck.
[382.80 → 383.28] Jeff.
[383.98 → 384.26] GF.
[384.94 → 388.02] And then the Y was just like, you know, Fee is pretty harsh.
[388.48 → 392.38] Most people like, oh, Fee, because that's kind of like more of a pet name and smooth to say.
[392.86 → 394.58] Fun to say.
[394.58 → 395.24] So, yeah.
[395.32 → 396.08] What's your favourite peanut butter?
[397.00 → 397.54] All right.
[397.58 → 398.00] My mother.
[398.22 → 399.16] I was going to say, I thought your mom might have picked it.
[399.16 → 402.36] My mother called me Jiffy Jeff for my entire life.
[402.48 → 402.92] I knew it.
[402.92 → 403.74] And guess what?
[403.76 → 404.36] She's a choosy mom.
[404.72 → 405.72] All we bought was Jeff.
[406.76 → 408.52] The changelog sponsored by.
[410.08 → 410.48] Jiffy.
[410.68 → 411.08] Jiffy.
[411.44 → 412.28] So what do you do, Jeff?
[413.82 → 418.80] Recently, new title, shiny new title, head of projects at the CNCF.
[418.90 → 419.22] Okay.
[420.04 → 422.76] Most people, when they hear that, they go, wait, all of them?
[423.02 → 423.26] Yeah.
[423.40 → 423.94] And I'm like.
[424.00 → 424.80] I would think all of them.
[424.88 → 425.16] Yeah.
[425.48 → 426.12] Pretty much.
[426.12 → 431.02] Honestly, like what I'm really doing is I'm a community member first.
[431.02 → 433.22] I came up as a Kubernetes contributor.
[434.76 → 436.28] Been around for a while.
[436.88 → 438.78] So I know a lot of people.
[438.96 → 441.54] I know a lot of the communities and open source projects around it.
[441.76 → 445.60] So I can go and talk with them and figure out like, hey, what do you need?
[445.68 → 446.82] How can we help better?
[446.96 → 449.70] What can we do better to enable your project?
[449.98 → 451.44] New projects that are coming in.
[451.86 → 454.40] Hey, how can these projects potentially collaborate?
[454.40 → 459.52] Because like I'm an engineer first and then kind of, you know, schmooze, try to be nice
[459.52 → 460.26] to everyone second.
[460.68 → 465.72] So it's kind of hard to define my job and, you know, a job description, but it's really
[465.72 → 469.42] talk to projects, see what the CNCF is doing, make community happy.
[470.06 → 470.38] Gotcha.
[470.74 → 474.02] You take the requirements from the customers, and you give them to the developers.
[474.56 → 475.02] That's right.
[475.30 → 477.56] I joined a foundation, so I don't have to hear those words.
[477.56 → 485.58] What you do at MINATEC is you take the specifications from the customers, and you bring them down
[485.58 → 486.70] to the software engineers.
[486.88 → 487.12] Yes.
[487.26 → 487.66] Yes.
[487.80 → 488.68] That's right.
[488.86 → 490.64] I recently watched Office Space.
[490.82 → 491.74] I had to bring it in.
[491.74 → 493.14] How many projects are there?
[493.34 → 494.62] Again, 160.
[495.08 → 500.62] And right now, as of whatever today is, the 10th, May 10th, I think there's 12.
[500.62 → 506.86] So there is some number above like seven or eight that are currently getting voted on
[506.86 → 509.62] to be adopted into what's called the CNCF Sandbox.
[509.92 → 515.74] Think of it like proof of concept projects, projects that don't necessarily have a large
[515.74 → 518.02] community, and they're looking to build a community.
[518.58 → 521.90] They apply to the CNCF Sandbox and then those get voted in.
[522.00 → 522.12] Yeah.
[522.20 → 523.84] I talk with my hands as well.
[523.98 → 525.18] I'm somewhat Italian.
[525.56 → 526.36] I like it.
[526.44 → 527.04] I'm down with that.
[527.10 → 528.10] I talk with my hands too.
[528.56 → 530.60] I want to get super excited, and I'm super excited right now.
[531.04 → 534.12] So you got Sandbox, you got Incubation, you got Graduated.
[534.24 → 534.58] Oh, yes.
[534.84 → 535.12] Okay.
[535.36 → 538.44] So you're not all over all projects, but you are over most projects.
[540.92 → 543.06] Let's talk to people in the CNCF and see which...
[543.06 → 544.26] No, I'm...
[544.26 → 548.14] Honestly, it's over all projects because I'm interacting with projects at every different
[548.14 → 548.42] level.
[548.56 → 550.68] It's just, I don't want to say I'm in charge of all of them.
[550.80 → 551.92] That's not true at all.
[552.32 → 558.76] But I would say I communicate with all of them, and I'm trying to help the CNCF work with
[558.76 → 559.86] projects in a better way.
[560.22 → 560.48] Gotcha.
[561.18 → 562.52] Give us an example.
[562.64 → 564.40] How does that play out for recent?
[565.40 → 570.94] Recently, when I joined and one of the things that I've been really pushing for is a lot
[570.94 → 577.18] of the processes to grant projects access to cloud resources that are like group cloud
[577.18 → 582.80] resources under the CNCF, or we have license scanning software or services.
[582.80 → 587.08] We want to give those to the projects and then step out of the way.
[587.22 → 589.36] Hey, we don't want to be the bottleneck.
[589.92 → 594.38] But most of the way that we grant that access is still a manual process.
[594.38 → 596.40] Even though all of these things have APIs.
[596.90 → 602.04] Well, gee, you know, you look at what Kubernetes has done with their like community management,
[602.20 → 608.00] like creating a user group in Slack is memes aside, like laugh, laugh at home.
[608.00 → 610.36] You edit a YAML file.
[610.52 → 614.34] Oh, you're joining a GitHub group, or you've become like a SIG chair.
[614.48 → 615.70] You're editing a YAML file.
[615.82 → 619.38] And then once that file is committed, it's just Git Ops all the way down.
[619.38 → 623.62] Like your access gets granted in GitHub, your access gets granted in Slack, all of that.
[624.20 → 628.18] Why don't we do that for all of these services that the CNCF is like hosting?
[628.52 → 630.40] Right now, it's still Click Ops.
[631.08 → 636.78] That was cool when the like the foundation was 10 projects or 15 projects or at 160.
[637.66 → 638.56] 160 projects?
[638.88 → 640.46] And we're not slowing down.
[640.56 → 641.86] And 12 more being added.
[641.96 → 642.42] That's crazy.
[642.70 → 643.58] Those are up for vote.
[644.06 → 645.92] Those are up for TOC vote.
[645.96 → 647.04] How many get rejected?
[647.04 → 649.86] I actually don't have that off the top of my head.
[650.64 → 654.34] I would be willing to guess sandbox wise.
[654.46 → 658.90] It's probably 75% acceptance rate, but please do not hold me to that right now.
[658.90 → 659.54] Nine out of 12 are getting in.
[660.32 → 660.76] Don't.
[660.84 → 661.56] Hey, hey, hey.
[662.14 → 663.34] We're not naming names.
[663.74 → 665.98] What is the I guess, motivation?
[666.14 → 671.04] Probably might be the best word, but what does the CNCF do in terms of like you got 160 projects.
[671.38 → 672.38] What's the long-term goal?
[672.42 → 673.76] Is it to be bigger than that?
[673.76 → 677.16] Like what service do you provide to the cloud native world?
[677.28 → 679.50] Like what is it that you all do or hope to do?
[680.72 → 685.50] This is going to be interesting because if you ask different people in the CNCF, you might get a different answer.
[685.62 → 688.10] And there might be a canned response and I should know it.
[688.10 → 701.46] My answer is there is, aside from the couple stable patterns, like Kubernetes and the way that it has an API and like declarative over imperative stuff, everything's stable right now.
[701.72 → 703.36] Like that pattern is established.
[703.86 → 709.66] What things and what problems when consuming that pattern needs to be solved?
[709.66 → 718.16] What, like a good example was, okay, so now we can create all of these containers and orchestrate them in a meaningful way.
[718.28 → 720.12] But now we have a giant distributed system.
[720.76 → 723.68] What do we do in order to monitor that thing?
[723.82 → 725.18] Well, Prometheus came out of that.
[725.18 → 731.08] So this is a long-winded way of saying we have this, you know, foundational technology.
[731.26 → 737.44] At this point, we are accepting additional projects to help flesh out what cloud native actually means.
[737.64 → 740.36] And the definition itself is evolving.
[740.74 → 740.84] Yeah.
[740.92 → 743.30] Like we have a bunch of WebAssembly projects.
[743.38 → 744.14] Well, why is that?
[744.14 → 754.32] Because at its core, WebAssembly is, I don't want to say just another container runtime because that would be bad, but it is another like application runtime.
[754.82 → 756.28] You build it a different way.
[756.42 → 760.06] It has a very different like look and feel than a container.
[760.46 → 764.70] But still like that, that idea still fits into the pattern of cloud native.
[764.98 → 766.52] So that still solves a problem.
[767.38 → 769.84] So, Geez, what would I do?
[769.84 → 777.06] TLDR, we're accepting a bunch of projects because not all the problems or questions have been answered in what cloud native is.
[777.42 → 783.04] So you're attempting to and in many ways succeeding in defining the foundation of cloud native.
[783.20 → 783.32] Yeah.
[783.84 → 790.20] And everything was originally built on Kubernetes because that's what I guess was the founding project that really kicked off.
[790.42 → 792.22] So we come back from the Dan Kahn days.
[792.34 → 794.92] Like we were early CNCF days, Michigan.
[794.92 → 802.04] Dan Kahn, Dan, but like we were there when it was just, just two or three projects, you know, a very small CNCF, the original founding days.
[802.50 → 806.26] And as we see it grow and grow over time, you know, it's a lot of great stuff happening for open source.
[806.36 → 808.00] But, you know, you're on the inside.
[808.08 → 808.72] You see what's happening.
[808.80 → 810.76] You are in touch with all these projects.
[810.88 → 811.60] What is the mission?
[812.18 → 814.04] Like what is the end game for CNCF?
[815.42 → 816.90] Jeez.
[817.22 → 817.46] Three.
[819.22 → 821.54] Honestly, it's what is next?
[821.54 → 827.64] The definition of cloud native in a nutshell is really doing distributive computing repeatably.
[828.92 → 831.34] I mean, that's my definition in my old noggin, right?
[831.72 → 835.56] But that doesn't mean always use Kubernetes.
[836.68 → 837.12] Sure.
[837.28 → 837.86] Right now.
[837.94 → 839.18] Hey, Kubernetes is.
[839.62 → 841.14] I mean, you look at all the stats.
[841.70 → 844.10] Adoption's still like up into the right.
[844.18 → 845.00] It's a hockey stick.
[846.42 → 850.60] That doesn't necessarily mean it's going to be the same thing, or it's going to be the answer.
[850.60 → 853.06] So, like, what is the end goal?
[853.24 → 863.84] We don't really have an end goal aside from if you are doing some sort of distributed computing, like trying to solve or consume or build distributed computing, distributed platforms.
[864.40 → 868.66] How can we do it but make sure that how it's being done is in an open source way?
[869.02 → 872.12] Maybe Kubernetes, you know, goes by the wayside and something else comes up.
[872.12 → 879.62] Maybe there is some new, like, WebAssembly orchestration platform and then everyone starts adopting that.
[879.72 → 881.90] We want to make sure that that's still possible.
[882.46 → 891.96] Like, the reason why right now Kubernetes is like, I don't want to say flagship, but like, you know, the big thing that everyone thinks of with the CNCF is because of its popularity.
[891.96 → 894.64] Not because the CNCF is saying everyone use Kubernetes.
[894.94 → 906.80] If something else just starts shooting up into the right, we also want to be there to help enable them and make sure that the lessons we learned from Kubernetes just, again, hockey sticking up, can be learned over here.
[906.88 → 910.26] So they have an even better experience than, you know, Kubernetes had.
[910.44 → 912.10] And, like, it had a lot of growing pains.
[912.42 → 915.62] So let's not have another project repeat that.
[915.62 → 920.66] Do you all want all open source projects that support Cloud Native to be a part of the CNCF?
[921.04 → 921.84] Not necessarily.
[922.34 → 926.20] Well, that's probably not a good thing to say for, you know, me and my employer.
[926.32 → 929.62] But honestly, I think that would not...
[930.26 → 935.46] Part of the charter in the CNCF, specifically the TOC, is they are not kingmakers.
[935.92 → 944.34] The TOC, the Technical Oversight Committee, which is, like, elected positions, they're the ones that pick which projects get adopted, which projects aren't adopted.
[944.34 → 951.54] Like, they dictate who's in the CNCF, and then we, the staff, enable them, help, support, you know, do all that sort of thing.
[951.78 → 955.78] So, like, I'm coming at this as my opinion, man.
[956.76 → 962.32] Yeah, well, you know, that's just, like, your opinion, man.
[962.58 → 963.62] Honestly, I tangented.
[963.80 → 966.04] Like, I already forgot the original question.
[966.28 → 966.50] Right.
[966.64 → 968.56] We're all just over here in The Big Lebowski.
[968.56 → 969.26] I can ask it again.
[969.74 → 970.00] Please.
[970.32 → 972.60] I will do Big Lebowski references for the whole podcast.
[972.60 → 973.26] That's a problem.
[973.26 → 974.84] These guys are trying to joke on me.
[974.88 → 975.94] I'm trying to ask here.
[976.54 → 978.84] We're hoping you forget it so he doesn't have to answer it.
[980.50 → 982.78] I'm with you, but I'm just saying, like, he's trying to dodge it.
[983.04 → 983.66] Let's keep going.
[984.00 → 984.82] I'm just looking at my face.
[986.36 → 987.18] Let's try again.
[987.64 → 987.82] Sure.
[987.82 → 992.00] So, I'm curious if, because it seems like you've got a repeatable way to support projects.
[992.16 → 992.40] Yes.
[992.52 → 997.86] So, it makes sense that if it's supporting cloud native, and it's open source, you'd want it as part of your organization.
[998.04 → 998.70] I remember now.
[998.70 → 999.00] Yeah.
[999.36 → 1005.74] So, there's like, I will go back to, there's like my personal answer and then there's probably the party line.
[1005.82 → 1006.90] Can you give us the personal answer?
[1007.10 → 1010.82] The personal answer is I don't think that would be healthy for the ecosystem.
[1011.60 → 1016.02] Just, again, the tangent of the TOC and the fact that they say there are no kingmakers.
[1016.56 → 1017.28] Same thing.
[1017.28 → 1025.74] I also think that if all projects were in one foundation, that's probably not healthy for the ecosystem.
[1026.84 → 1029.74] Like, cloud native does not mean it is a CNCF project.
[1029.92 → 1034.60] There are plenty of other cloud native things that are not in the CNCF.
[1034.84 → 1035.08] Right.
[1035.22 → 1036.72] Like, there's Nomad.
[1036.82 → 1037.74] HashiCorp has Nomad.
[1037.84 → 1039.62] That's a container orchestration platform.
[1039.76 → 1042.28] There's still a lot of work being put in and around Nomad.
[1042.28 → 1048.42] They're an IPO company, though, so it makes sense why Nomad isn't there because that would be troublesome for their business.
[1048.68 → 1050.12] But Nomad is an open source project.
[1050.86 → 1053.68] There's a weight, though, to being a project in the CNCF.
[1053.74 → 1055.18] You have the CNCF landscape, right?
[1055.28 → 1055.42] Yep.
[1055.42 → 1058.28] So, by nature, you want to communicate what is and isn't.
[1058.58 → 1061.58] But at the same time, doesn't that give a weight to a project that is?
[1062.12 → 1070.86] Well, landscape is a bad example because the CNCF landscape has projects that aren't CNCF adopted or CNCF.
[1070.86 → 1071.26] That's true.
[1071.46 → 1071.92] I'll give you that.
[1072.10 → 1074.84] So, like, I was actually thinking Nomad might actually be on the landscape.
[1074.98 → 1075.50] I haven't looked.
[1075.84 → 1077.02] Well, let me give you this example.
[1077.16 → 1080.62] So, we've been here for eight hours, ten hours.
[1082.70 → 1086.48] I've talked to two people who have said,
[1087.02 → 1089.34] Hi, I'm X, and I'm with Project Y.
[1090.28 → 1091.54] We're in the CNCF.
[1093.06 → 1097.58] And it's like there's a clout to that.
[1098.02 → 1098.34] Yeah.
[1098.34 → 1099.02] Right?
[1100.06 → 1106.26] So, aren't the TOC then, I mean, they kind of are kingmakers in that sense, right?
[1106.38 → 1110.34] Like, they kind of, because they're the ones who decide who's in and everyone who says that they're in,
[1110.42 → 1111.88] now they're, like, cooler than they used to be.
[1111.88 → 1113.94] They can leverage the brand equity of the CNCF.
[1113.94 → 1114.30] Right.
[1114.30 → 1120.68] But in that case, the TOC isn't, like, picking one technology over another, at least with the sandbox.
[1121.16 → 1121.40] Okay.
[1121.44 → 1130.30] What's usually happening is they're judging maturity, whether it does fit, like, whether it is a cloud-native thing or not.
[1130.48 → 1130.80] Yeah.
[1130.80 → 1138.70] Like, if my transcoding software or, you know, some other random project that has nothing to do with cloud computing gets submitted to the sandbox.
[1138.76 → 1138.88] Sure.
[1138.88 → 1142.52] Which, that happens, TOC doesn't want that.
[1142.60 → 1143.46] Like, that's not the CNCF.
[1143.46 → 1145.42] Yeah, it makes sense that it has to be, like, inside the scope.
[1145.64 → 1146.84] So, there's a vulva rope.
[1146.92 → 1150.80] So, my personal opinion is I don't think that's healthy for the ecosystem.
[1150.98 → 1151.12] Sure.
[1151.12 → 1163.20] But that said, and I think the party line would be, if you want to be supported in the ecosystem and have the namesake of the foundation behind you,
[1163.50 → 1166.04] yeah, you probably want to join the CNCF.
[1166.82 → 1177.66] I also have feelings that, at some times, some projects probably should not have been, shouldn't have applied.
[1177.66 → 1184.66] But, again, that's why my personal opinions and the TOC are the people that vote on it.
[1184.96 → 1185.56] Not me.
[1185.70 → 1187.92] Your job is to support the ones that do make it in.
[1188.14 → 1188.38] Yep.
[1188.78 → 1190.54] However, they need support.
[1190.96 → 1198.46] And, honestly, projects that aren't in the CNCF but are in the landscape, I'm still, like, around to support and talk to.
[1198.46 → 1205.88] Because, again, I don't think this is necessarily a bad thing to have projects outside.
[1206.08 → 1212.00] Also, projects outside looking in could potentially spawn other projects that do want to come in.
[1212.38 → 1212.50] Sure.
[1213.22 → 1214.50] Do you like this job?
[1215.36 → 1215.58] Yeah.
[1216.24 → 1217.42] Best job I've ever had.
[1217.54 → 1219.64] And I'm not just saying that because of, you know.
[1219.80 → 1220.46] Because it's being recorded.
[1220.72 → 1224.70] Because it's being recorded, and I'm standing in, you know, a Linux Foundation event.
[1224.70 → 1225.18] No.
[1226.14 → 1234.16] My not-so-brief but, honestly, short resume career, I worked at the University of Michigan for 16 years and then Red Hat for three.
[1234.90 → 1237.56] And then I started here a year and a half ago.
[1238.16 → 1249.54] So, out of those, not getting into, like, different departments at the university, but out of those three, you know, areas, like, or places, Linux Foundation CNCF is the best.
[1249.64 → 1251.84] And your path came through contributing to Kubernetes?
[1252.24 → 1252.38] Yep.
[1252.38 → 1258.18] I actually did a little bit of contribution back in ye old days.
[1258.50 → 1262.70] Like, we're talking 2014 when it was just open sourced and still under a Google.
[1263.04 → 1265.58] Like, had to sign a Google CLA to contribute to it.
[1266.54 → 1272.48] Then my path at the university kind of took me away from it after probably a year.
[1273.12 → 1275.94] And then I started contributing again in early 2018.
[1275.94 → 1279.74] And wound up becoming a SIG UI chair.
[1279.98 → 1283.46] So, the Kubernetes dashboard that, you know, some people kind of dunk on.
[1284.90 → 1288.06] They were having, like, leadership issues.
[1288.76 → 1292.06] They just needed someone that could kind of come in and do more PM work.
[1292.12 → 1295.14] And also, I had a background in front-end work.
[1295.14 → 1298.54] So, I came in and, you know, just helped them out.
[1298.62 → 1300.80] Wound up becoming a SIG chair for a few years.
[1300.94 → 1303.02] And then I stepped down after I mentored someone up.
[1303.70 → 1304.82] It's a Cinderella story.
[1305.16 → 1305.44] Nah.
[1305.54 → 1306.64] It's a Cinderella story.
[1307.88 → 1309.44] So, you say you like this job.
[1309.66 → 1310.30] Love it.
[1310.52 → 1311.52] What do you like most?
[1311.76 → 1313.94] What is your favourite thing that you get to do every day?
[1313.94 → 1319.54] I feel like this job actually has a real impact on people's lives.
[1320.24 → 1326.90] When I worked at the University of Michigan, one of the things I did was informatics and, like, directly impacting patient care.
[1327.36 → 1328.80] I loved that.
[1329.20 → 1334.20] Like, I'm not saying patient care and open source are similar.
[1334.84 → 1341.30] But there is definitely, you know, that impact where I know that I have helped and, like, impacted other people's lives here.
[1341.30 → 1348.54] Similar to, like, being able to help someone's patient care just by supporting, like, a clinical app that I wrote that deals with their results.
[1349.02 → 1350.02] Different but same.
[1350.82 → 1354.40] That just gives me warm, fuzzy feelings because, I don't know, I'm weird.
[1355.32 → 1355.84] No, that's cool.
[1356.16 → 1357.38] Make the world a better place.
[1358.06 → 1358.36] Impact.
[1358.54 → 1359.42] Change lives.
[1359.66 → 1362.80] I was always taught to leave the world better than you found it.
[1363.38 → 1366.52] I'm one of those people that will make the bed in a hotel room when I'm leaving.
[1366.96 → 1368.70] I didn't know those people existed.
[1369.44 → 1369.90] They don't.
[1369.90 → 1372.68] It's, I'm, okay, so I'm a psychopath, apparently?
[1375.46 → 1377.00] It's the endowment effect.
[1377.28 → 1378.10] That's what this is.
[1378.66 → 1381.52] The endowment effect is that you don't wash your rental.
[1382.18 → 1382.54] Say what?
[1382.60 → 1384.34] You don't wash your rental car, for example.
[1384.86 → 1385.68] It's the endowment effect.
[1385.74 → 1388.64] If you own it, you think it's more valuable.
[1389.06 → 1390.50] And when you don't own it, you think it's less valuable.
[1390.54 → 1391.80] That's why we don't wash our rental cars.
[1391.90 → 1393.34] Yeah, but he makes his bed in his hotel room.
[1393.34 → 1393.42] I know.
[1393.64 → 1395.26] He's the anti-endowment effect.
[1395.42 → 1395.74] Okay.
[1396.40 → 1397.20] The anti-enter.
[1397.20 → 1401.34] Have either of you, I cannot, I can never remember like the social experiment or the
[1401.34 → 1405.38] dude that did this, but do either of you know about the shopping cart?
[1405.80 → 1407.96] Like, I don't even know what to call it.
[1408.18 → 1408.28] No.
[1408.68 → 1415.02] There's someone decided that you can tell whether a person was not necessarily good or bad,
[1415.02 → 1421.86] but more focused on the whole versus the self based on what they do in a grocery store parking
[1421.86 → 1422.14] lot.
[1422.82 → 1426.94] Do they put their shopping cart back where they are supposed to put it or not?
[1427.36 → 1429.06] And then you can watch people.
[1429.22 → 1433.30] And if other people will actually take the shopping cart like someone else's and put it
[1433.30 → 1436.64] away, it's like, they're the people that actually want to make the world a better place.
[1436.80 → 1436.98] Yeah.
[1436.98 → 1444.40] You know, in ye old days, supermarkets used to employ people that would walk your stuff
[1444.40 → 1444.92] Well, guess what?
[1445.00 → 1445.90] ATV still does it.
[1445.90 → 1446.20] Out to you.
[1446.28 → 1446.92] Do they still do that?
[1447.06 → 1447.56] Well, sorry.
[1447.80 → 1448.62] I spoke too soon.
[1449.10 → 1450.14] They do it for some.
[1451.02 → 1451.42] What?
[1451.58 → 1453.22] Well, usually for senior citizens.
[1453.34 → 1453.56] Okay.
[1453.72 → 1455.10] And like the pregnant people.
[1455.72 → 1457.00] I don't know about trendy people.
[1457.20 → 1457.58] No, pregnant.
[1459.58 → 1460.84] They're like, nice shoes.
[1460.96 → 1462.38] I'm going to walk your groceries out.
[1464.34 → 1465.08] Trendy people.
[1465.08 → 1467.64] Do you remember that back when the day?
[1468.14 → 1469.06] Were you around back then?
[1469.54 → 1474.90] I, yes, but I, kind of small town in Southeast Michigan.
[1475.32 → 1476.18] That never really happened.
[1476.42 → 1476.68] They never did that?
[1476.78 → 1480.74] We always, if like a senior citizen or someone that was, you know, needed help.
[1480.74 → 1482.44] There was a position called bagger.
[1482.76 → 1483.56] Wasn't it called bagger?
[1483.74 → 1483.92] Yeah.
[1484.10 → 1484.40] Yeah.
[1484.40 → 1486.50] I mean, they still had, like, they still have baggers.
[1486.50 → 1487.76] There's still baggers at my grocery store.
[1487.76 → 1490.36] Yeah, but the bagger would actually walk with you out to your car.
[1490.56 → 1490.94] Oh, no.
[1490.94 → 1492.58] And load the bags into your car.
[1492.58 → 1495.18] And then they'd take your cart, and they'd take it back.
[1495.70 → 1495.78] Yeah.
[1495.84 → 1499.48] Now that's called whoever, you know, delivers something to your car when you mobile order
[1499.48 → 1500.84] it from Target or like Pet Smart.
[1500.84 → 1501.62] I do miss those days.
[1501.70 → 1502.56] There's something about that.
[1502.62 → 1506.30] I think you're onto something, Jared, because what you said you'd like to buy your job and
[1506.30 → 1509.46] how you get to change lives is similar to this because, you know, you get to, every
[1509.46 → 1511.14] step of the way, you get the support, you know?
[1511.44 → 1511.70] Right.
[1511.76 → 1514.98] You get to make the process, the experience a little easier, a little bit better.
[1515.18 → 1515.40] Yes.
[1515.52 → 1517.92] The CNCF is the bagger position of open source.
[1518.04 → 1519.28] I see where this is going now.
[1519.28 → 1522.02] Well, I got mad respect for the CNCF.
[1522.18 → 1527.54] I think you've unified a diverse, if, let's hypothesize.
[1527.88 → 1533.86] If the CNCF did never exist, or it was never formed, how would, if cloud native was never
[1533.86 → 1535.36] termed or even if it is termed, doesn't matter.
[1535.78 → 1538.66] How would the world be if there was no CNCF to tie it all together?
[1539.22 → 1541.06] That's actually tough to hypothesize.
[1541.06 → 1551.96] So, one of the biggest benefits, like thinking at a super high level, is we're a neutral place
[1551.96 → 1558.54] for these large vendors to be able to collaborate and essentially make everything better for
[1558.54 → 1560.52] the consumer in a standardized way.
[1562.06 → 1564.24] Take that away, and what do you have?
[1565.02 → 1566.06] You have...
[1566.90 → 1567.74] Proprietary.
[1567.74 → 1570.06] Everything winds up being proprietary.
[1570.46 → 1571.28] No clarity.
[1571.90 → 1573.02] No focus on users.
[1573.92 → 1575.32] I mean, they'll focus on users.
[1575.32 → 1575.92] They'll focus on their users.
[1576.10 → 1579.46] So far as once they get you in there...
[1579.46 → 1579.86] Right.
[1580.42 → 1580.64] Silos.
[1580.64 → 1581.52] You're locked in.
[1582.20 → 1583.88] The like, major vendor lock-in.
[1584.70 → 1586.60] I think that's the biggest thing.
[1586.98 → 1587.26] Yeah.
[1587.78 → 1588.64] That's probably true.
[1588.90 → 1591.62] The vendor lock-in would be horrible.
[1592.36 → 1594.68] Like, I can't even imagine it.
[1594.68 → 1595.52] Yeah.
[1595.56 → 1605.58] And I'm trying to remember back in, like, Heroku, PHP, like, 2008, 2009 days of hosting,
[1605.70 → 1606.92] you know, web services.
[1607.42 → 1609.60] Everyone kind of had their own thing.
[1610.00 → 1612.66] But even then, it wasn't that bad.
[1613.18 → 1613.44] Yeah.
[1613.44 → 1615.54] Like, stuff made sense.
[1616.04 → 1621.54] But also, no one was really sticking around long enough to potentially have, I won't say
[1621.54 → 1625.52] a monopoly, but a lion's share to lock you in.
[1625.62 → 1627.84] So it doesn't make sense to shift elsewhere.
[1627.96 → 1628.42] Everything was...
[1628.42 → 1629.98] At that point, everything was VMs, right?
[1630.52 → 1630.72] Yep.
[1630.72 → 1631.32] So...
[1631.32 → 1631.82] Exactly.
[1632.98 → 1637.74] Hey, look, I can spin up a VM on my box, make sure it works, and then, I mean, ship the
[1637.74 → 1638.16] whole thing.
[1638.50 → 1639.70] Sucks, but doable.
[1640.50 → 1640.78] Sure.
[1641.44 → 1642.80] Jeff, I'm glad you talked to us, man.
[1642.94 → 1643.72] Dude, this is awesome.
[1643.72 → 1647.78] Thank you for sharing the story and the CNCF stuff and all that stuff.
[1647.78 → 1650.16] Shout out to Kara for dragging me away from the booth.
[1650.28 → 1653.58] Real quick, what's your favourite project, and what's your least favourite project?
[1653.70 → 1653.88] Go.
[1654.22 → 1654.96] Absolutely not.
[1655.00 → 1655.36] I refuse.
[1655.94 → 1657.12] This interview is over.
[1658.46 → 1660.50] Imagine me knocking over the microphone.
[1661.20 → 1662.78] Well, not the project, but the people.
[1663.06 → 1664.88] You know, tell us who's your favourite person and your least...
[1664.88 → 1665.30] I'm just...
[1665.30 → 1665.66] I'm messing.
[1665.92 → 1668.28] Oh, actually, I can at least tell you my favourite person.
[1668.38 → 1668.62] Okay.
[1668.62 → 1674.46] I had a coworker who was also a roommate who was also my best friend, and he's my best
[1674.46 → 1674.80] man.
[1675.08 → 1675.38] Oh, wow.
[1675.38 → 1676.36] Well, he was the best man at my wedding.
[1676.96 → 1679.86] We worked at the University of Michigan since the start.
[1680.14 → 1684.56] We both moved departments from pathology over to advanced research computing.
[1685.00 → 1685.42] Wow.
[1685.42 → 1686.88] I went to Red Hat.
[1687.00 → 1687.80] He went to Google.
[1688.46 → 1690.36] So my best friend's Bob Killen.
[1690.48 → 1691.70] Like, he lives down the street from me.
[1691.72 → 1692.16] That's cool.
[1692.38 → 1696.52] We are almost inseparable, except when I get to go to events and he doesn't.
[1697.14 → 1700.78] Trust me, if he was here, I would have been asking for another microphone because we just
[1700.78 → 1701.34] would have done that.
[1701.46 → 1702.76] We do have one more if we need it.
[1703.20 → 1703.32] So...
[1703.32 → 1704.78] Bob, come on.
[1704.80 → 1705.26] That's cool.
[1705.78 → 1706.56] Oh, if...
[1706.56 → 1707.56] Are you going to Keep Con Chicago?
[1707.80 → 1708.64] I'll drag him over.
[1709.92 → 1711.12] Let's talk off mic.
[1711.44 → 1712.24] I got ideas.
[1712.24 → 1714.12] All right.
[1714.18 → 1714.62] Thanks, Jeff.
[1714.90 → 1715.50] Thank you all.
[1732.28 → 1733.16] What's up, friends?
[1733.26 → 1736.20] I'm here in the breaks with one of our sponsors, Ray cast.
[1736.20 → 1740.78] I'm here with Thomas Paul Mann, the co-founder and CEO of Ray cast.
[1740.78 → 1744.72] So, Thomas, I recently moved from Alfred to Ray cast.
[1744.86 → 1750.40] I'm on the Preplan, loving the AI integrations and everything else helped me to be productive.
[1750.82 → 1753.90] Also helped you launch the Preplan recently on Change Law News.
[1753.98 → 1754.54] That was awesome.
[1754.92 → 1758.14] But what I want to know is why you built Ray cast in the first place.
[1758.54 → 1763.54] I think software, as we experience, is flawed and inefficient.
[1764.04 → 1766.36] And I know this is a pretty big and bold statement,
[1766.36 → 1770.30] but this is really where the idea from Ray cast comes from.
[1770.70 → 1773.62] Because when you think about it, when you interact with a computer,
[1773.98 → 1776.78] you have a certain action in your mind that you want to do.
[1777.10 → 1782.14] To perform that, you need to translate that into clicks and keystrokes on a computer.
[1782.50 → 1783.78] And that isn't really intuitive.
[1783.94 → 1785.70] That's not how we used to work.
[1785.76 → 1788.44] When we crap something in the real world, we just crap it and do it.
[1788.58 → 1791.32] There is no communication or something like that necessary.
[1791.32 → 1794.92] But somehow we got used to that this is how software works.
[1795.20 → 1796.10] And we work around that.
[1796.44 → 1800.96] It kind of works, but I feel really it's an inefficient way to use a computer.
[1801.46 → 1803.74] So with Ray cast, we re-envisioned that, and we said,
[1804.08 → 1806.76] what is if I could use all my tools in a single interface?
[1807.12 → 1807.86] They look the same.
[1807.96 → 1808.94] They behave the same.
[1809.30 → 1810.72] I'm super efficient at it.
[1810.78 → 1812.32] I just enter what I want to do.
[1812.66 → 1815.38] Everything is driven by the keyboard, which I'm used to as a developer.
[1815.68 → 1820.02] We basically started building exactly that and started with the basics of like,
[1820.02 → 1822.02] what if I could launch an application?
[1822.42 → 1823.58] That's an easy task, right?
[1823.82 → 1826.16] What if I could find a file that I'm looking for?
[1826.46 → 1827.24] Okay, that's nice.
[1827.50 → 1829.64] But at some point we reached in the threshold where we said,
[1829.76 → 1834.86] oh, but now I need to create a JIRA issue or see my assigned issues and change the status.
[1835.22 → 1836.80] That is where it gets fascinating.
[1837.26 → 1841.02] It quickly became clear to us like, wow, okay, there is actually demand for that.
[1841.02 → 1845.14] That was really the start of Ray cast where we felt this is something special.
[1845.32 → 1847.22] There are like so many people want to be more productive.
[1847.74 → 1849.84] They want to have a great tool that they can use.
[1850.02 → 1854.08] But they're also willing to put in a bit of work of maybe integrating with their own
[1854.08 → 1856.34] services that we don't have support for now.
[1856.96 → 1857.26] Okay, cool.
[1857.42 → 1861.82] So one of the things that stood out to me for your homepage when kind of learning about
[1861.82 → 1868.24] Ray cast and discovering what it can do, it says in big bold letters on the homepage,
[1868.64 → 1870.36] supercharge your productivity.
[1870.68 → 1872.76] Why is that the leading statement for Ray cast?
[1873.26 → 1873.42] Yeah.
[1873.42 → 1878.44] So for us, productivity is like, it's very hard to measure if you look down for it.
[1878.68 → 1880.60] People say they can do something faster.
[1881.18 → 1884.62] People say they're more productive, but it's very hard to quantify.
[1885.14 → 1890.70] So we thought, hey, we have a tool that generally just makes you more productive in many different
[1890.70 → 1891.14] ways.
[1891.14 → 1893.36] So it supercharges your productivity.
[1893.36 → 1894.92] It brings us to the next level.
[1894.92 → 1898.04] You like just can do things much faster than anybody else.
[1898.04 → 1900.52] You can interact with your tools quicker.
[1900.98 → 1903.14] You're basically like operating on a different level.
[1903.36 → 1907.44] There's always the saying of a 10x developer, which can do things a lot faster, right?
[1907.66 → 1913.06] So it goes along those lines where when you see people using a Mac with Ray cast, they use
[1913.06 → 1916.30] a Mac differently to somebody that uses a Mac without Ray cast.
[1916.70 → 1917.02] Okay.
[1917.02 → 1922.32] So if you're on a Mac and you want to be productive, you owe it to yourself to try Ray cast.
[1922.44 → 1923.24] You can try it free.
[1923.56 → 1925.38] Almost everything they have is free.
[1925.38 → 1929.48] I mean, lots, I mean, I told him Thomas, you kind of give away too much for free, but
[1929.48 → 1930.96] Hey, that's, that's their choice.
[1930.96 → 1931.28] Right.
[1931.52 → 1936.92] But if you want to be productive on a Mac Ray cast, if you're using a launcher for using
[1936.92 → 1942.94] spotlight or anything like it, Ray cast will take you to a whole new level.
[1943.20 → 1944.10] I'm using it.
[1944.18 → 1944.80] I love it.
[1945.00 → 1945.82] I think you should check it out.
[1946.06 → 1950.02] Go to Raycast.com again, Raycast.com.
[1955.38 → 1978.34] So the Kubernetes API, that's what you work on, right?
[1978.52 → 1979.46] I work on CLI.
[1979.58 → 1980.02] CLI.
[1980.02 → 1980.74] Oh, the CLI.
[1980.74 → 1980.94] Yeah.
[1981.14 → 1981.36] Okay.
[1981.42 → 1983.96] That's a, you know, it's an abstraction of that, right?
[1983.98 → 1986.04] You're actually interfacing with the API.
[1986.04 → 1987.92] We're probably the biggest consumer of the API.
[1987.92 → 1988.26] All right.
[1988.44 → 1988.70] Okay.
[1989.16 → 1989.78] What is that?
[1989.86 → 1990.48] How's it work?
[1990.68 → 1995.14] So are you familiar with how the Kubernetes project is broken up into special interest
[1995.14 → 1995.36] groups?
[1995.36 → 1995.66] School me.
[1995.82 → 1996.16] School me.
[1996.24 → 1996.38] Yeah.
[1996.38 → 1997.46] So we got SIG's.
[1997.66 → 1999.38] So basically every part of the Kubernetes code base.
[1999.38 → 2000.14] What does a SIG mean?
[2000.30 → 2001.08] Special interest group.
[2001.08 → 2001.60] Special interest group.
[2001.72 → 2001.96] Okay.
[2002.32 → 2004.42] And so we got a SIG for API machinery.
[2004.68 → 2008.22] They own the API and the stuff that runs on the master nodes.
[2008.54 → 2013.88] And so I work on SIG CLI, which is the SIG for the command line tooling, right?
[2013.88 → 2013.98] Okay.
[2013.98 → 2021.68] So Tube Control, Customize, GUI, which is a like GUI framework for Tube Control, a couple other
[2021.68 → 2022.46] subprojects.
[2022.46 → 2027.08] But yeah, so I've been working on that for like four years now, and it's a lot of fun.
[2027.30 → 2027.46] Yeah?
[2027.64 → 2027.88] Yeah.
[2028.04 → 2028.60] Tube Control, huh?
[2028.74 → 2028.98] Yeah.
[2029.08 → 2029.52] Is that official?
[2029.96 → 2036.34] Tube, well, you will notice throughout this talk, I say it many different ways on purpose.
[2036.48 → 2037.04] So you rotate.
[2037.28 → 2038.20] You just called me out early.
[2038.30 → 2038.94] You're a diplomat.
[2039.16 → 2042.10] So if you say Tube Cuddle here in a bit, it's on purpose.
[2042.40 → 2042.76] That's on purpose.
[2042.76 → 2044.38] We're also going to say Cub Eckel, so.
[2044.46 → 2045.04] Cub Eckel.
[2045.44 → 2045.92] Oh gosh.
[2046.60 → 2047.50] Who says Cub Eckel?
[2048.10 → 2048.78] Well, if you want to hit all the variations.
[2048.78 → 2049.84] People say Cub Eckel?
[2049.96 → 2050.20] Yep.
[2050.44 → 2051.76] Is it for fun or is it for serious?
[2051.76 → 2053.12] Well, I've heard both ways.
[2053.78 → 2054.12] Wow.
[2054.48 → 2055.38] Why not, right?
[2056.30 → 2059.96] If you can interpret something 17 ways, why not be 18?
[2060.16 → 2060.56] It's true.
[2061.10 → 2068.04] I just think that maybe Kubernetes is so complex and intimidating that whenever we have people
[2068.04 → 2070.92] on and talk about it, we just bike shed the Tube Cuddle thing.
[2071.86 → 2072.48] What do you think?
[2073.20 → 2073.60] Sure.
[2073.60 → 2076.64] I feel like you and I always end up right here talking about the Cube Control.
[2077.16 → 2077.68] For sure.
[2077.96 → 2084.30] I mean, you can go to cubecontrol.info, and it's a recording of Tim Hawken who originally
[2084.30 → 2086.16] wrote it saying how he pronounces it.
[2086.36 → 2087.70] I think we had Tim on the show back in the day.
[2087.70 → 2089.60] I talked to Tim forever ago, basically.
[2089.86 → 2090.50] The godfather.
[2090.64 → 2090.86] Yeah.
[2090.90 → 2092.10] When it first became a thing.
[2092.32 → 2092.58] Yeah.
[2092.66 → 2092.94] Nice.
[2093.44 → 2094.24] He was at Google then.
[2094.30 → 2094.88] Is he still at Google?
[2094.92 → 2095.60] He's still at Google.
[2095.60 → 2096.28] There you go.
[2096.28 → 2096.62] Yep.
[2096.86 → 2097.48] Good for you, Tim.
[2098.06 → 2098.42] Slay it.
[2098.90 → 2100.24] What should we know about the CLI?
[2100.34 → 2103.18] Like what's important with its development team, the SIG?
[2103.38 → 2104.22] Maintaining it.
[2104.40 → 2105.12] Maintaining it.
[2105.38 → 2105.64] Yeah.
[2106.24 → 2109.00] So one of the hardest things we have to do is say no to people.
[2109.10 → 2109.36] I bet.
[2109.36 → 2110.02] All day, right?
[2110.44 → 2115.60] I'm sure a lot of people have told you that, but everyone wants a short flag for everything.
[2115.94 → 2117.78] Everyone wants a long flag for everything.
[2117.88 → 2118.52] A lot of flags.
[2118.72 → 2121.56] Everyone wants every feature as a flag or command.
[2121.64 → 2123.24] What's the language of the CLI?
[2123.38 → 2123.86] It's all go.
[2124.16 → 2124.64] It's all go.
[2124.78 → 2125.02] Okay.
[2125.26 → 2125.58] Cobra.
[2126.10 → 2127.44] I've been doing a lot of Bash scripting.
[2127.54 → 2130.72] I'm like, you know, at some point I'm going to graduate from Bash to something else besides
[2130.72 → 2131.90] Bash, but it does a lot.
[2132.20 → 2132.46] Oh, yeah.
[2132.46 → 2136.52] Like Bash scripting is a lot of fun, and it's pretty powerful, but I feel like that my next,
[2136.72 → 2138.98] if I keep going in this direction, go.
[2139.62 → 2139.82] Yeah.
[2140.58 → 2142.38] I mean, I feel like I'm learning Bash, right?
[2142.50 → 2142.80] Okay.
[2143.00 → 2146.96] I've never sat down to properly learn Bash and you can do a lot with it.
[2147.06 → 2147.30] Yeah.
[2148.16 → 2152.18] And thank God for ChatGPT because I'm learning Bash left and right because of ChatGPT.
[2152.18 → 2158.58] It's somewhat esoteric in my history, but I think having GPT would make it super easy
[2158.58 → 2159.54] to accomplish a lot of things.
[2159.68 → 2160.10] It is.
[2160.10 → 2163.90] I mean, there's a lot you can, I mean, you can iterate quite a lot with it, which is
[2163.90 → 2166.72] a side tangent from crafting a CLI with Go, but.
[2166.78 → 2166.94] Yeah.
[2166.98 → 2170.12] But even the looping and the conditionals inside the loops, there's weird times when
[2170.12 → 2172.00] you use the square brackets, and you don't have to.
[2172.08 → 2172.88] And then there are the flags.
[2173.22 → 2175.98] There's like conditional flags inside the loops and stuff.
[2176.02 → 2177.74] How many square brackets do you use?
[2177.74 → 2177.84] Yeah.
[2177.88 → 2179.42] Multiple square brackets change things.
[2179.56 → 2181.18] It is esoteric, but powerful.
[2181.32 → 2181.82] Very powerful.
[2181.82 → 2182.74] And there.
[2182.98 → 2183.54] It's already there.
[2184.78 → 2188.14] And you use it just, when I tell you, I'm talking about me, you use it just infrequently enough
[2188.14 → 2190.28] that you always have to Google for the syntax.
[2190.48 → 2190.72] Oh, yeah.
[2190.80 → 2193.00] So, again, GPT's for the win on that one.
[2193.12 → 2193.80] Yeah, for sure.
[2194.08 → 2199.58] And on that note, I am very thankful because I've like, because, well, this isn't about
[2199.58 → 2204.44] ChatGPT necessarily, but I think it has flattened the world to like a lot of people who are like
[2204.44 → 2207.80] Go Curious or Bash Curious or Scripting Curious.
[2208.06 → 2208.68] Cube Control.
[2209.00 → 2209.36] Curious.
[2210.00 → 2210.92] Cube Cuddle or Cube.
[2211.36 → 2212.16] What was the other one?
[2212.86 → 2213.22] Cube Total.
[2214.00 → 2216.60] Cubical, Cube Control, Cube Ectal.
[2216.60 → 2217.04] Cube Ectal.
[2217.36 → 2218.00] Cube Ectal, yeah.
[2218.16 → 2220.48] Which is kind of cool to say, actually, Cube Ectal.
[2220.54 → 2221.44] You know what you want.
[2221.58 → 2224.10] You can describe what you want, but you can't quite get there.
[2224.14 → 2227.06] But if you learn enough, and then you can repeat yourself, you learn that stuff.
[2227.20 → 2227.36] Yeah.
[2227.52 → 2229.34] This episode brought to you by OpenAI.
[2229.46 → 2229.86] That's right.
[2229.98 → 2230.46] There you go.
[2230.58 → 2232.56] How many flags does Cube Control have?
[2232.58 → 2233.96] Oh, man, I can't tell you that.
[2234.04 → 2234.36] Gosh.
[2234.44 → 2235.06] We got a lot.
[2235.26 → 2236.66] We got a lot of subcommands.
[2236.94 → 2240.84] We got probably 20 subcommands, maybe more.
[2241.02 → 2243.16] And they all have lots and lots of flags.
[2243.16 → 2248.16] We basically have an entire framework just to add flags to the commands that they get instantiated.
[2248.16 → 2249.52] Oh, yes, the old flagging framework.
[2249.96 → 2250.20] Yeah.
[2251.02 → 2256.36] What's the biggest challenge that you said no, but maybe personally, maybe not as a team, but personally?
[2257.30 → 2259.38] You know, you've been on the project for four years.
[2259.76 → 2262.04] We didn't exactly hear about how you got there or anything like that.
[2262.04 → 2267.72] But what are challenges maintaining a project of that high demand and use?
[2268.52 → 2270.12] Definitely contributors, right?
[2270.12 → 2273.54] We have a saying on Kubernetes, chop wood, carry water.
[2274.20 → 2274.58] Say again?
[2274.68 → 2275.70] Chop wood, carry water.
[2275.78 → 2276.24] Chop wood, carry water.
[2276.24 → 2278.64] Kind of doing the unglamorous work that someone has to do.
[2278.64 → 2282.32] And we need people to just come do that, right?
[2282.40 → 2286.10] Triage issues, respond to open pull requests, review.
[2286.50 → 2294.90] And, you know, one of the things I encourage lots of new people to do is you don't have to be a reviewer for the Kubernetes project to go and review pull requests.
[2294.90 → 2300.98] It's just doing an initial pass of being like, oh, this is probably a better way to write this if statement.
[2301.18 → 2303.14] So you don't have like three else's under it.
[2303.22 → 2303.38] Right.
[2303.38 → 2304.48] It's just like little things.
[2304.74 → 2308.46] And so that's what I encourage a lot of new folks to do is just start reviewing code.
[2308.54 → 2309.92] Just start responding to issues.
[2310.24 → 2311.04] And, yeah.
[2311.28 → 2312.34] Just comment on the issue.
[2312.60 → 2312.84] Yeah.
[2313.70 → 2314.06] Just comment.
[2314.06 → 2316.22] Who's contributing to the CLI?
[2316.38 → 2317.48] Who's contributing to the CLI?
[2317.48 → 2319.72] Is it the sick team primarily or is it outside contribution?
[2320.12 → 2322.66] So I'm sure everything would say that.
[2323.12 → 2328.72] Well, it's probably the part of the oldest code base of Kubernetes itself, right?
[2328.74 → 2334.24] Because you build the API server and the node, and then you build the CLI at the same time to talk to everything.
[2334.58 → 2339.76] And so we got a lot of dragons that are there and a lot of stuff we come across.
[2340.14 → 2341.34] And so it's funny.
[2341.40 → 2344.44] People don't realize that Kubernetes is all JSON internally, right?
[2344.44 → 2347.76] You hear the Kubernetes and cloud native world complain about YAML.
[2347.78 → 2348.60] YAML, yeah.
[2348.60 → 2350.72] And Kubernetes doesn't know YAML internally.
[2350.72 → 2351.32] It's all JSON, huh?
[2351.32 → 2351.88] It's all JSON.
[2352.24 → 2353.00] That's news to me.
[2353.02 → 2356.10] So it goes JSON to YAML on the response.
[2356.34 → 2360.64] And then when it comes to the command line, we actually marshal it back to JSON.
[2361.00 → 2365.38] And then we have to go from JSON to figuring out what go type we have, right?
[2365.42 → 2367.36] So if it's a pod or a node or something.
[2367.74 → 2367.78] Right.
[2368.20 → 2377.72] And so that's a large chunk of the code that we maintain is just dealing with marshalling from format to format and then figuring out what go struct we have at the end of the day.
[2377.72 → 2379.40] Why don't you just go from YAML to go struct?
[2380.20 → 2381.30] From YAML to go struct.
[2381.68 → 2382.32] We could.
[2382.90 → 2384.40] That would just take one Marshall out of the list.
[2384.46 → 2384.88] It would.
[2385.40 → 2390.18] It's working with the Go YAML world is kind of interesting.
[2390.36 → 2391.98] We could probably talk about that for a long time.
[2392.10 → 2395.84] But we have a forked version of the Go YAML project.
[2396.30 → 2396.56] Gotcha.
[2396.56 → 2398.06] There are many different versions.
[2398.48 → 2403.60] And the project bundle is like three of them.
[2404.22 → 2407.74] One didn't like preserve comments or something in your YAML, right?
[2407.84 → 2414.14] So when you're dealing with client-side YAML for users, you want to keep their comments around.
[2415.00 → 2416.60] That's one of the problems with JSON, right?
[2416.66 → 2417.50] It's like no comments.
[2417.66 → 2418.60] No comments, right?
[2418.94 → 2421.48] So you got three Yams in there?
[2421.48 → 2425.56] We got a couple versions of the same library, yeah.
[2425.60 → 2428.34] We try to keep one, but YAML is a special case.
[2428.54 → 2428.86] Sure.
[2429.64 → 2431.08] You got to do what you got to do.
[2431.14 → 2431.58] I like YAML.
[2431.80 → 2432.52] It's not the worst.
[2433.22 → 2434.58] It's not as bad as people make out.
[2434.68 → 2434.98] No.
[2435.24 → 2436.44] I'd rather write YAML than JSON.
[2437.14 → 2437.34] Yeah.
[2438.10 → 2438.50] Agreed.
[2438.80 → 2439.82] For the most part.
[2440.00 → 2442.74] I feel like you can shoot yourself on the foot more with YAML.
[2443.14 → 2443.46] Yes.
[2444.42 → 2446.38] And complex YAML is very complex.
[2446.92 → 2448.14] But simple YAML is very simple.
[2448.58 → 2448.68] So.
[2448.82 → 2449.20] Yeah.
[2449.62 → 2450.42] I'm not against it.
[2451.12 → 2453.22] JSON might be easier to read if it's prettier.
[2454.30 → 2454.70] Yeah.
[2454.94 → 2455.34] Potentially.
[2455.58 → 2456.40] It's more verbose.
[2456.66 → 2456.92] Yeah.
[2457.00 → 2457.14] Yeah.
[2457.48 → 2461.80] You can see the invitations and the nesting a lot better than you might, I guess.
[2461.84 → 2463.76] I guess you can see either of those pretty easily, but.
[2464.34 → 2469.98] I like it in YAML because my editor can show me, like, the number of tab indents I have, right?
[2470.10 → 2470.44] Right.
[2470.44 → 2474.46] So he can, like, show me a one, two, three, and that's really nice to see.
[2474.60 → 2474.80] Yeah.
[2474.80 → 2475.08] Yeah.
[2475.08 → 2479.32] So that's your biggest challenge is this marshalling around YAML and contributors.
[2479.32 → 2479.76] Yeah.
[2479.76 → 2480.12] New contributors.
[2480.12 → 2480.44] No, contributors.
[2480.44 → 2480.76] Contributors.
[2480.98 → 2481.38] Contributors.
[2481.58 → 2481.74] Yeah.
[2481.86 → 2486.26] So we, people working on the project, I work with people from Google, Red Hat.
[2486.26 → 2491.26] We had someone from Shopify that fortunately just got laid off, pour some out.
[2493.48 → 2494.88] Bunch of Googlers, Red Haters.
[2494.90 → 2495.64] Don't pour your gin out.
[2495.86 → 2496.60] Don't pour your gin out.
[2496.66 → 2496.78] No.
[2497.86 → 2498.26] Water.
[2498.48 → 2499.14] Pour your water out.
[2499.28 → 2499.50] Yeah.
[2499.64 → 2503.62] And then we have people who come by, and they want to get involved in Kubernetes, and they're
[2503.62 → 2504.80] curious about things.
[2504.86 → 2507.20] And the CLI seems like a great entry point.
[2507.36 → 2507.48] Yeah.
[2507.48 → 2513.84] And as a project, we're still struggling with mentorship programs and onboarding.
[2514.10 → 2517.26] And one of the hard parts is maintainer burnout, right?
[2517.26 → 2522.80] Because we can, early on, I was very happy to sit down with someone for hours and just
[2522.80 → 2525.72] walk them through stuff, answer every question, help them write their code.
[2525.96 → 2526.20] Right.
[2526.38 → 2529.40] And then they make their one contribution, and then they disappear and they'll come back.
[2529.78 → 2532.42] And you do that enough times, and you're feeling really crispy.
[2534.06 → 2534.46] Yeah.
[2534.64 → 2535.18] It makes sense.
[2535.18 → 2538.34] Do you do videos?
[2538.64 → 2543.82] Do you find ways to not repeat yourself in that way so you can say, here's me telling
[2543.82 → 2545.28] you how to do these things and sit down with you?
[2545.34 → 2547.78] Maybe there's a video you could do or documentation.
[2548.08 → 2551.52] And that seems to be the easy, hey, why don't you just do documentation?
[2552.00 → 2555.80] But is there a way you can put down the wisdom, so to speak?
[2556.18 → 2560.56] From a mentorship perspective and succession planning, this is something that's big for
[2560.56 → 2565.08] maintainer month is how can you operate with balance as a team?
[2565.18 → 2566.02] As an individual.
[2566.46 → 2569.42] And then also how can you plan for succession when it's necessary?
[2570.42 → 2573.02] It's definitely something we're working through with the project.
[2573.64 → 2576.12] We have tons of developer documentation, right?
[2576.16 → 2578.06] Probably too much that people don't read, right?
[2578.08 → 2579.60] It's overwhelming when you first come in.
[2580.90 → 2583.22] Getting your development environment set up, right?
[2583.22 → 2585.66] It's so many moving pieces.
[2586.14 → 2589.28] And container runtime really only works well on Linux.
[2589.38 → 2591.84] And most people aren't running Linux as their OS.
[2592.22 → 2592.92] How dare them.
[2592.98 → 2593.26] Right?
[2593.80 → 2594.26] Linux.
[2595.08 → 2596.14] Linux for life.
[2596.14 → 2598.26] But it's something we're definitely trying to work towards.
[2598.42 → 2601.80] We want to make as much onboarding material as we can.
[2601.86 → 2603.16] We've had mentorship cohorts.
[2603.80 → 2607.60] But at the end of the day, it's very complex as a code base.
[2607.82 → 2607.98] Yeah.
[2607.98 → 2609.08] And it's just old.
[2609.22 → 2615.30] And there's so many, there's so much, we don't say tribal knowledge anymore.
[2615.56 → 2616.16] What do we say?
[2617.46 → 2619.08] Preconceived knowledge.
[2619.64 → 2621.70] Decisions that were made a while ago, right?
[2621.84 → 2625.60] And people come in headstrong, really wanting to help out and contribute.
[2625.76 → 2627.00] And it's like, well, we tried that.
[2627.04 → 2629.26] And here's why it didn't work six different times.
[2629.26 → 2632.66] And that is the hard part is the context and the history.
[2632.80 → 2634.52] How do we communicate that to new people?
[2634.82 → 2634.94] Right.
[2635.24 → 2638.02] What's the process to become a contributor long term?
[2638.54 → 2643.12] Like you put this time into this person, you walk to their code base, and they gave one
[2643.12 → 2644.46] contribution and never came back.
[2644.54 → 2647.74] What is the process to have a long term contribution plan?
[2647.86 → 2649.50] Is there a term of service?
[2649.60 → 2652.38] We hear from OSLO's like, hey, come for a term of service.
[2652.38 → 2655.14] That means maybe a year, maybe six months, maybe it's three years.
[2655.74 → 2657.44] You know, and then there's repetition in that.
[2657.44 → 2659.80] But how do you all plan that out?
[2660.02 → 2662.06] Is there a form and function around that?
[2662.56 → 2663.60] Do you know Mike McQuaid?
[2663.88 → 2664.04] Yeah.
[2664.32 → 2664.48] Yeah.
[2664.58 → 2667.56] So Mike McQuaid, he's the lead maintainer for Homebrew.
[2667.72 → 2672.24] And he's got a blog post that he wrote back in 2018 that's kind of resonated with me.
[2672.66 → 2675.40] It don't mentor first time contributors.
[2676.06 → 2677.44] Don't mentor second time contributors.
[2677.64 → 2678.72] Mentor third time contributors.
[2679.46 → 2684.82] And it's the idea that, like I explained, you get burnt out if you keep spending time on
[2684.82 → 2686.08] people who just don't come back.
[2686.08 → 2690.02] But if they've made two contributions, and they've come back for the third, it's like,
[2690.06 → 2690.46] all right, cool.
[2690.64 → 2691.38] Like you're in it.
[2691.44 → 2693.00] You've gone through the hard part, the weeds.
[2693.28 → 2695.44] Like we can grow you into a maintainer, right?
[2695.46 → 2698.94] Because that's the goal at the end of the day is to grow people into maintainers.
[2699.10 → 2700.44] We want as many as we can get.
[2700.72 → 2700.84] Yeah.
[2701.16 → 2704.92] What brings somebody back three times to the Kubernetes CLI, for example?
[2705.12 → 2706.18] Like what is it that brings them back?
[2706.24 → 2707.76] Is it because they have a vested interest?
[2708.12 → 2708.82] They're super curious.
[2709.00 → 2711.12] They have funded time interest.
[2711.22 → 2712.26] Their employer pays for it.
[2712.26 → 2715.60] Like what are the attributes of a person who comes back again and again?
[2716.06 → 2716.94] I don't have a good answer.
[2717.50 → 2718.26] I really don't.
[2718.40 → 2721.56] It's people who want to get involved and contribute back.
[2721.72 → 2724.44] And some people might be encouraged to get involved in open source.
[2724.52 → 2725.60] Some people want to learn Go.
[2725.78 → 2727.44] They want to learn Kubernetes in general.
[2727.44 → 2732.28] Yeah, it's we see people come for all different reasons.
[2732.40 → 2737.36] Some people really just want to build their resume and just want to build up their GitHub stats and show them that they've contributed.
[2737.72 → 2743.02] And so, yeah, it is hard to filter through and apply the right time to the right folks.
[2744.02 → 2746.40] So what do you think of this word?
[2747.00 → 2747.44] Rewrite.
[2747.90 → 2748.64] Do you like that word?
[2750.68 → 2751.58] It's a word.
[2752.98 → 2754.50] It's part of the English language.
[2754.50 → 2754.90] Okay.
[2755.42 → 2758.22] Have you ever considered it with the CLI?
[2759.44 → 2763.56] Like not throw one out and start new fresh, but start fresh alongside the one that exists.
[2763.58 → 2764.06] Oh, yes.
[2764.24 → 2764.68] The parallel.
[2764.98 → 2765.92] The old big rewrite.
[2766.08 → 2766.82] The parallel rewrite.
[2767.00 → 2769.26] Because, I mean, you got a lot of baggage, according to you.
[2770.00 → 2781.28] And that's perhaps scary, but maybe in an open source world, not so bad way of like, instead of just like trying to bring this one up to snuff, you just maintain it status quo and rewrite the sucker.
[2781.28 → 2781.72] Yeah.
[2782.12 → 2786.84] So we have an initiative that we've been rewriting commands to like our new pattern that's more concise.
[2787.12 → 2791.42] And, you know, we got like the options and the flags dangling off the command struct.
[2791.82 → 2794.20] And, you know, in a go world, it makes a lot of sense.
[2794.90 → 2796.98] From scratch is an interesting one.
[2797.84 → 2801.62] The Kubernetes project in a whole, we are terrified of breaking users.
[2801.62 → 2808.38] So the example that I like to give is I've been trying to get delete confirmation into the CLI for the longest time.
[2808.70 → 2812.78] When you delete a namespace in Kubernetes, you delete everything that was in that namespace.
[2812.88 → 2818.02] When you accidentally delete all namespaces in your cluster, you've wiped everything out, and you're going to have a bad time.
[2818.02 → 2825.22] And I could show you like tons of GitHub issues where people say, why was it so easy for me to make this mistake?
[2825.56 → 2825.60] Right.
[2825.82 → 2829.06] Why didn't it ask me, are you sure you want to blow everything away?
[2829.06 → 2835.32] And the reality is that we can't just start asking, are you sure you want to delete everything?
[2835.78 → 2838.54] Because your CI pipeline would break, right?
[2838.56 → 2839.72] We'd break everyone's build.
[2839.82 → 2844.42] People are updating their CI runs, and they don't know what version of the client they're using.
[2844.52 → 2846.00] They don't really read the release notes.
[2846.32 → 2847.78] And so that's just an example.
[2847.92 → 2850.40] Like I've been trying to get delete confirmation in since I started.
[2851.18 → 2852.70] Isn't that what SemVer is for?
[2852.98 → 2854.12] Major release.
[2854.32 → 2856.48] We don't want to do a major release for the project.
[2856.48 → 2860.92] As far as we know, right, we can barely get people to upgrade the minor versions.
[2861.82 → 2864.62] But majors are easier because people get excited.
[2864.86 → 2865.40] That's right.
[2866.38 → 2869.16] Is there something to learn from the way Linux is distributed?
[2869.60 → 2871.62] Like LTSs and versions?
[2872.14 → 2878.90] I mean, every time I do a new Ubuntu installation, it's 18, it's 22, it's 20.
[2879.40 → 2880.24] And I'm cool with that.
[2880.36 → 2881.22] There's an LTS.
[2881.82 → 2883.72] There's a spectrum of risk.
[2884.10 → 2884.78] It's clear.
[2884.78 → 2887.42] Is that a possibility with a CLI?
[2887.48 → 2888.60] This is a crucial piece.
[2888.96 → 2892.14] It's like the centrepiece for Kubernetes for the most part, right?
[2892.22 → 2894.68] It's the main consumer of the API.
[2895.06 → 2896.94] It's definitely the first thing you reach for, right?
[2896.98 → 2897.28] Right, yeah.
[2897.68 → 2899.56] There are two answers there.
[2899.68 → 2903.34] So the first one, LTS is actually something we just started talking about again.
[2903.50 → 2906.02] So we were on Rubicon in Amsterdam like two weeks ago.
[2906.46 → 2910.92] And Jeremy Rickard from Microsoft revived the talk around the working group for LTS.
[2910.92 → 2911.12] Yes.
[2911.58 → 2912.86] So we did it a couple of years ago.
[2912.98 → 2917.94] We determined that it wasn't something we wanted to do or support at the time or had the capability.
[2918.16 → 2920.12] So that just got revived two weeks ago.
[2920.12 → 2926.80] And then the other thing, Tube Control is versioned as part of the Kubernetes project itself, right?
[2926.90 → 2931.24] So 120, I can't release a separate version of Tube CTL.
[2931.32 → 2931.34] That makes it harder.
[2931.34 → 2931.98] That does, yeah.
[2932.06 → 2932.24] Right?
[2932.32 → 2935.58] So we do have a proposal out that probably needs to get revived.
[2935.68 → 2937.06] But that was something we wanted to do.
[2937.18 → 2940.58] But then you get the problem of the compatibility and SKU matrix.
[2941.12 → 2944.34] What version of the client is supported by what version of the API server?
[2944.34 → 2944.82] Yeah.
[2946.26 → 2947.78] Useful software gets upgraded.
[2948.64 → 2956.90] So if you, here's one thing we learned from GitHub and a lot of other things out there where it's like permission to mess up, permission to do something different.
[2956.90 → 2970.46] You know if you can release a different version of it in parallel that has what everybody wants, and it fixes all the problems and maybe internally it's easier to develop, and it's potentially easier to have contributors and easier to document.
[2970.72 → 2972.90] Like that has potential.
[2973.56 → 2978.24] There's an opportunity for that useful software just to get upgraded because, hey, this is just so useful.
[2978.58 → 2978.72] Yeah.
[2978.82 → 2979.96] This person is using it.
[2980.00 → 2980.96] That company is using it.
[2981.54 → 2985.56] And it's sort of like a social norm to upgrade because it's just useful.
[2985.56 → 2985.96] Right.
[2985.96 → 2992.92] The rewriting thing would probably get, like, it probably would be impossible to get through.
[2993.08 → 2993.24] Right.
[2993.30 → 2999.60] Because we do any significant changes to the project go through what we call the KEEP process, the Kubernetes enhancement proposals.
[3000.02 → 3005.54] And I could just see, like, opening a KEEP for rewrite, subject, and just like, no.
[3006.12 → 3007.00] It just gets closed.
[3007.14 → 3007.34] Right.
[3007.64 → 3007.80] Yeah.
[3007.82 → 3008.88] What if you already did it?
[3009.02 → 3010.12] What if we already did it?
[3010.24 → 3010.88] That's what I was thinking.
[3010.98 → 3011.72] I mean, it's not stuff.
[3011.72 → 3014.20] First time contributor shows up, I rewrote this.
[3014.20 → 3017.50] There's nothing stopping us or anyone from doing that.
[3017.50 → 3017.66] Yeah.
[3018.12 → 3024.42] The reality is we are changing the tires on a bus that's moving 1,000 miles an hour down the highway, right?
[3024.58 → 3024.76] Right.
[3024.76 → 3036.74] Maybe it actually turns into more like a yarn and NPM kind of situation where it's not you guys that rewrite it, but it's somebody else that comes alongside and says, well, we can write our own CLI against the Kubernetes API.
[3036.74 → 3038.50] And here's seven ways it's better.
[3039.62 → 3041.34] And, hey, who wants to use this?
[3041.42 → 3049.78] And I don't know if you can actually, you know, just side install that sucker and use maybe it's subject with C-U-D-D-L-E or something, you know?
[3049.84 → 3050.82] That's a conference now.
[3050.98 → 3051.44] Oh, it is?
[3051.56 → 3051.66] Yeah.
[3051.86 → 3052.20] Dang it.
[3052.20 → 3056.96] In a perfect world, the subject wouldn't exist, right?
[3057.00 → 3057.70] Why is that?
[3057.90 → 3062.48] Because it's, you can think of it like SSH for a server, right?
[3062.50 → 3064.88] Like I don't want my developers Ashing to my server.
[3065.08 → 3070.30] I don't want my developers pushing and making configuration changes to my production server.
[3070.52 → 3075.62] I want a trusted build entity that is applying these changes after they've been reviewed.
[3075.62 → 3079.44] And so it's just like, it's kind of giving a developer keys to the castle.
[3079.70 → 3080.70] And I'd rather if I...
[3080.70 → 3081.40] Deleting namespaces.
[3081.70 → 3081.92] Yeah.
[3082.08 → 3082.28] Right.
[3082.30 → 3085.72] Like I'd rather not have to give people the client in the first place.
[3085.80 → 3094.02] So I think instead of building one from scratch, I'd love to see us get to a point where the Git Ops tooling and all this other stuff is in a place where you don't need it in the first place.
[3095.12 → 3097.98] You can rewrite it in a different route.
[3098.26 → 3098.44] Yeah.
[3098.80 → 3099.60] You know, through...
[3099.60 → 3100.24] Write something else.
[3100.36 → 3102.66] In the Git Ops world, build that thing to make it obsolete.
[3102.94 → 3103.74] Yeah, that's fair.
[3104.14 → 3105.30] Then you can take a vacation.
[3105.62 → 3106.06] Yeah.
[3107.42 → 3107.82] Yeah.
[3107.94 → 3108.78] I would love one of those.
[3108.86 → 3112.24] What I like about this podcast is we look at things like Yarn and NPM.
[3112.80 → 3119.52] We look at, you know, we're not only in this cloud native specific world and, you know, sort of have tunnel vision.
[3119.64 → 3122.26] We sort of see outside all software.
[3122.44 → 3124.40] What was done here to solve that problem?
[3124.58 → 3128.08] And what was wise about that choice that we can apply here?
[3128.50 → 3131.94] You know, that's what I love about the conversation I think we get to have is that we...
[3131.94 → 3137.24] Jared and I have the luxury and the privilege to speak at software at large, really.
[3137.50 → 3137.74] Right.
[3137.80 → 3138.06] You know?
[3138.28 → 3141.72] Plus, we get to bike shed things but not actually be the person that has to go paint the bike shed.
[3141.80 → 3142.10] That's right.
[3142.26 → 3144.24] We can give you the idea of, hey, Eddie.
[3144.62 → 3145.22] We're like...
[3145.22 → 3146.04] Godspeed, bro.
[3146.04 → 3148.62] I told Eddie to rewrite the thing, and he just won't do it.
[3149.22 → 3150.92] I got a good one for you all then.
[3151.04 → 3154.30] So I also work on the build and test infrastructure for the project.
[3154.64 → 3160.56] And we're unique as a project in that we handle distribution of all of our own artifacts and binaries.
[3161.04 → 3163.40] And our artifacts aren't just binaries.
[3163.56 → 3165.60] They're containers and OCI images, right?
[3165.60 → 3169.12] So our CI bill is like $3 million a year.
[3169.62 → 3172.12] Google gives us $3 million of GCP credit.
[3172.30 → 3172.76] Shout out to them.
[3172.84 → 3173.28] Thank you, Tim.
[3173.42 → 3173.50] Wow.
[3174.42 → 3183.06] And I think it costs us like $250,000 a month for storage and network ingress and compute and egress.
[3183.82 → 3186.54] And we're working very hard to get that down, actually.
[3186.72 → 3187.60] We just...
[3187.60 → 3191.90] Amazon just also gave us a $3 million donation, and we set up a registry proxy.
[3192.06 → 3192.10] Yeah.
[3192.10 → 3192.72] Thank you, Amazon.
[3192.72 → 3198.86] Amazon and it's, you know, for a while it was everyone was downloading from our container registry
[3198.86 → 3203.40] because you can't just mirror a container registry like you can mirror a Linux kernel, right?
[3203.50 → 3206.28] And so I think some work can probably be done on that space.
[3206.38 → 3213.72] But that's a problem that we deal with that a lot of other projects don't deal with is we have to distribute in front the bill and host all this stuff ourselves.
[3214.54 → 3214.74] Hmm.
[3214.96 → 3215.68] That's a big bill.
[3215.88 → 3216.66] That's a hard problem.
[3216.84 → 3219.02] $3 million just for CI.
[3219.36 → 3219.58] Yeah.
[3219.58 → 3220.74] Have you tried R2?
[3220.74 → 3223.06] Free egress.
[3223.30 → 3226.40] We are talking to Cloudflare for a bunch of different things.
[3226.42 → 3226.94] They would love that.
[3227.04 → 3227.68] I assume so.
[3227.80 → 3227.90] Yeah.
[3227.98 → 3228.22] Yeah.
[3228.32 → 3229.36] Hopefully they help us out.
[3229.52 → 3229.72] Yeah.
[3230.00 → 3233.62] We want to do caching too with Cloudflare, right?
[3233.70 → 3234.68] Or Vastly or someone.
[3235.02 → 3235.22] Yeah.
[3235.70 → 3236.76] So shout out to them, please.
[3238.38 → 3239.24] We like them both.
[3239.64 → 3243.14] We're expensive, but we're very expensive as an open source project to support.
[3243.98 → 3244.62] And crucial.
[3245.08 → 3246.02] It's a cloud-native world.
[3246.40 → 3246.62] Yeah.
[3247.08 → 3248.12] Just trying to operate in it.
[3248.12 → 3251.44] You probably know our audience to some degree.
[3251.50 → 3252.42] What else is left unsaid?
[3252.50 → 3258.90] What else should our audience know about crafting the CLI and interacting with potential contributors?
[3259.54 → 3260.38] Maintainer hacks?
[3260.56 → 3261.04] Yeah.
[3261.26 → 3261.90] Maintainer hacks.
[3261.90 → 3262.34] Sure.
[3262.56 → 3262.94] Maintainer hacks?
[3262.94 → 3266.86] So my maintainer hack is that I triage new issues first.
[3267.76 → 3270.72] And people kind of, this is controversial, probably.
[3271.00 → 3273.90] A lot of people, you should start with the oldest issues and triage them.
[3274.06 → 3274.30] Yeah.
[3274.30 → 3279.42] We found that our newest issues are probably the most relevant just because we get hundreds
[3279.42 → 3281.50] of issues a week opened on the project, right?
[3281.86 → 3286.90] And we have, the way the Kubernetes repo works is we have the main OK repo, the Kubernetes
[3286.90 → 3288.02] slash Kubernetes repo.
[3288.28 → 3290.68] And then we have staging repos.
[3290.68 → 3293.22] So, so, so, so, cube CTL is a staging repo.
[3293.48 → 3297.16] So we don't actually accept pull requests to cube CTL as a repo.
[3297.36 → 3300.64] It has to be made to the main project in the staging directory.
[3300.64 → 3302.66] And that gets replicated to our repo.
[3302.92 → 3305.14] So we track issues in both places.
[3305.14 → 3306.48] And we take PRs in one.
[3306.72 → 3308.94] So we get issues all over the place.
[3309.02 → 3312.58] And I can barely keep up with the issues that are on my repo, let alone the main one.
[3312.82 → 3313.00] Yeah.
[3313.66 → 3316.06] First in, last out.
[3316.06 → 3316.94] Yeah.
[3317.02 → 3320.32] So I start with the newest ones because they're usually the freshest and most relevant.
[3320.60 → 3324.86] And a lot of times we can just close them right off the bat because it's a support issue
[3324.86 → 3325.56] or something else.
[3325.56 → 3326.72] Or a new flag, and you're just like, no.
[3326.86 → 3328.62] Or you're eight versions behind.
[3328.72 → 3330.00] Please upgrade and try again.
[3330.32 → 3330.50] Right.
[3331.12 → 3333.96] Or it's an issue that's like, help, I just deleted my whole namespace.
[3334.64 → 3335.00] Right.
[3335.52 → 3335.92] Yeah.
[3335.96 → 3337.74] That one is really hard to...
[3337.74 → 3338.76] Sorry about that.
[3338.76 → 3343.06] Can I send you a bottle of gin or commiserate with you?
[3343.56 → 3344.98] So we do have plans for that.
[3344.98 → 3346.74] So we have been working on trying to get that in.
[3347.46 → 3349.12] What is your day like with issues?
[3349.20 → 3356.32] Like how many hours a day, either directly in issues or procrastinating, do you spend
[3356.32 → 3356.94] on issues?
[3358.08 → 3358.44] Wow.
[3358.64 → 3359.22] What a call-out.
[3359.40 → 3359.80] Surprise.
[3359.92 → 3361.52] Kubernetes isn't my full-time job.
[3361.64 → 3361.98] Okay.
[3362.24 → 3363.16] Oh, I thought it was.
[3363.30 → 3364.00] No, I do.
[3364.38 → 3365.16] When I was...
[3365.16 → 3366.68] I used to work on the EKS team at Amazon.
[3366.90 → 3369.18] So I would spend most of my days on Kubernetes.
[3369.18 → 3373.92] And now I do stuff with supply chain security and some other projects like SIG Store.
[3374.10 → 3375.34] It's an open SSF project.
[3375.76 → 3375.86] Yeah.
[3376.62 → 3382.48] But yeah, so we have a bug triage once a month that we go through where we'll go through as
[3382.48 → 3382.76] a group.
[3382.82 → 3386.64] And the idea behind this was that knowledge transfer of where we can talk through the
[3386.64 → 3388.90] history and the context that people don't have.
[3388.98 → 3390.62] And we invite lots of new people.
[3390.62 → 3394.64] So if you're listening, and you want to get involved, join us for our bi-weekly, our bi-monthly,
[3395.04 → 3396.50] our once a month bug scrub.
[3396.78 → 3398.26] We have bi-weekly SIG meetings.
[3398.78 → 3402.88] And we have from twice a week to every other week to once a month.
[3402.88 → 3403.88] I have a Kubernetes meeting every Wednesday.
[3404.40 → 3406.28] So it's bug triages once a month.
[3406.38 → 3408.28] And then our general SIG meeting is twice a month.
[3408.34 → 3408.58] Gotcha.
[3408.70 → 3408.88] Okay.
[3409.04 → 3410.06] And so join us for that.
[3410.22 → 3413.12] It's Kubernetes, GitHub.com slash Kubernetes slash community.
[3413.36 → 3416.04] And then the SIG CLI folder right at the top, it has meetings.
[3416.60 → 3419.06] So it's all public agenda, and it's all recorded.
[3419.06 → 3420.92] So 9 a.m.
[3420.94 → 3421.72] Pacific time.
[3422.46 → 3422.86] Cool.
[3423.14 → 3423.66] There you go.
[3423.94 → 3425.76] Well, thanks for talking to us, Eddie.
[3425.80 → 3426.00] Yeah.
[3426.04 → 3426.96] Thanks for having me, you all.
[3427.52 → 3428.12] It was a blast.
[3428.64 → 3429.30] Let's play Zelda.
[3429.86 → 3430.48] Let's play Zelda.
[3432.46 → 3433.78] That was awesome, guys.
[3433.94 → 3434.26] Yeah, man.
[3434.28 → 3434.76] Thanks so much.
[3434.90 → 3435.32] That was fun.
[3446.38 → 3448.34] This is a Changelog News Break.
[3449.06 → 3453.94] Even legendary computer scientist Donald Knuth is playing with ChatGPT.
[3454.58 → 3459.68] Inspired by a conversation he had with Stephen Wolfram, Knuth asked it 20 questions and wrote
[3459.68 → 3461.60] up his analysis of its responses.
[3462.28 → 3464.92] His questions are interesting.
[3465.28 → 3467.22] Much more intentional than anything I come up with.
[3467.72 → 3471.34] He asks things like, does Donald Trump eat beetle nuts?
[3471.34 → 3475.94] Write a sonnet that is also a haiku.
[3476.72 → 3478.92] What is the most beautiful algorithm?
[3479.68 → 3480.36] Stuff like that.
[3481.32 → 3484.68] He then provides the answers verbatim and his conclusions.
[3485.14 → 3486.98] Here's my favourite thing he has to say about it.
[3486.98 → 3492.60] Quote, I find it fascinating that novelists galore have written for decades about scenarios
[3492.60 → 3497.94] that might occur after a, quote, singularity in which super-intelligent machines exist.
[3498.20 → 3503.12] But as far as I know, not a single novelist has realized that such a singularity would
[3503.12 → 3509.20] almost surely be preceded by a world in which machines are 0.01% intelligent and in which
[3509.20 → 3513.90] millions of real people would be able to interact with them freely at essentially no cost.
[3513.90 → 3515.42] End quote.
[3516.66 → 3522.96] Despite this game of 20 questions, Knuth does not plan on continuing his generative AI research.
[3523.62 → 3528.60] He says he's going to spend his time developing concepts that are authentic and trustworthy.
[3529.04 → 3534.26] You just heard one of our five top stories from Monday's Changelog News.
[3534.60 → 3539.44] Subscribe to the podcast to get all the week's top stories and pop your email address in
[3539.44 → 3543.78] at changelog.com slash news to also receive our free companion email
[3543.78 → 3547.02] with even more developer news worth your attention.
[3547.40 → 3550.88] Once again, that's changelog.com slash news.
[3550.88 → 3577.34] Where should we begin?
[3578.10 → 3578.48] Dapper.
[3578.82 → 3579.22] Dapper.
[3579.42 → 3580.16] Let's begin with Dapper.
[3580.16 → 3580.62] All right.
[3580.70 → 3582.28] Open source CNCF.
[3584.82 → 3585.22] Graduated.
[3586.14 → 3586.90] No, not yet.
[3587.02 → 3587.38] Not yet.
[3587.50 → 3588.08] Okay, sorry.
[3588.22 → 3588.86] It's incubating.
[3589.26 → 3589.66] Incubating.
[3589.92 → 3590.10] Yeah.
[3590.36 → 3593.84] We will graduate at some point, but we're not rushing it.
[3594.04 → 3597.06] We'll make sure we get the most out of the CNCF incubating stage.
[3597.92 → 3602.50] We are doing lots of things in the CNCF, integrating with other projects.
[3602.90 → 3606.86] We really want to make sure we have this core integration with all the other CNCF projects
[3606.86 → 3608.10] before we graduate.
[3608.10 → 3609.10] Okay.
[3609.10 → 3609.14] Okay.
[3609.14 → 3613.56] So, yesterday you said you started Dapper at Microsoft?
[3613.56 → 3614.42] Microsoft, yes.
[3614.42 → 3614.78] That's correct.
[3614.78 → 3615.60] And you're working for them.
[3615.94 → 3616.22] Yep.
[3616.22 → 3618.74] And you built Dapper as an open source project?
[3619.28 → 3619.68] Correct.
[3619.68 → 3622.24] And then, well, first, what was it?
[3622.38 → 3624.10] And then, tell that story.
[3624.24 → 3625.60] What was Dapper when you built it then?
[3626.36 → 3627.26] And what happened next?
[3627.26 → 3627.86] Yeah.
[3628.00 → 3633.36] So, in 2018, I was at Microsoft, and I was working for the Azure CTO called MarkoSyndvich.
[3633.80 → 3639.56] That was an incubations team whose job was basically to look for bleeding-edge technologies
[3639.56 → 3646.32] and come up with innovative open source technologies that could really give Microsoft a boost in the ecosystem.
[3647.18 → 3650.28] And, yeah, I was mostly working on open source.
[3650.50 → 3655.82] I was contributing to Kubernetes, Terraform, a bunch of other projects along that line.
[3655.82 → 3660.72] And then, I met someone called Mark Russell, who today became the co-founder of my company, SIGRID.
[3661.28 → 3668.98] And we were looking into how can we improve the lives of application developers, not necessarily DevOps or infrastructure people,
[3669.28 → 3671.54] on top of Kubernetes in the cloud-native space.
[3671.88 → 3676.98] Because, you know, the ratio between a DevOps engineer and application developer is 10 to 1 in the favour of an application developer.
[3677.32 → 3680.22] And we call them the silent majority of cloud-native, right?
[3680.22 → 3689.44] Because if you look at the CNCF ecosystem, most of it is, you know, around, like, how do you do Git Ops and Ops and, you know, security and supply chain and CCD.
[3689.64 → 3694.82] But there is no one out there that's really solving the problems of, like, core distributed systems challenges.
[3695.16 → 3702.12] And this is why we came up with Dapper as this core tool that developers can use to focus on their business logic and not distribute the systems issues.
[3702.12 → 3702.60] Okay.
[3703.40 → 3704.22] A core tool.
[3704.48 → 3709.22] So developers can focus on their business logic and not distributed systems problems, is that what you said?
[3709.40 → 3709.50] Yeah.
[3709.96 → 3712.40] What are the distributed systems problems?
[3712.72 → 3712.92] Yeah.
[3713.18 → 3714.54] And how does Dapper deal with them?
[3714.60 → 3720.10] So, for example, as a developer, you have to make sure that your application is, first, secure, and second of all, reliable.
[3720.10 → 3728.82] And that usually translates into a lot of boilerplate code that you, as a developer, need to write on your own to basically make your application more secure wherever it's running.
[3729.16 → 3733.70] And Dapper will basically give you the security and reliability features out of the box immediately.
[3734.34 → 3735.78] And then you have to write state.
[3735.86 → 3737.26] You have to manage state at scale.
[3737.56 → 3741.86] You might be writing to Radio or Dynamo DB or Cassandra or Google Firebase.
[3741.86 → 3749.88] But if you have multiple services writing the same data all at once, you are probably going to want something like first-rate wins or last rate wins.
[3750.36 → 3754.50] And you're going to have to do Pub Sub and leader election and config management and secret management.
[3754.84 → 3762.06] And all of these infrastructure things really add up when all you want to do is focus on your business logic so that you can ship your feature out and get your next promotion.
[3762.06 → 3762.32] Right?
[3762.68 → 3762.80] Right.
[3762.80 → 3774.62] And so Dapper really gives developers these APIs that give them all these Pub Sub event, async eventing paradigms and service-to-service invocation and stateful management paradigms.
[3774.74 → 3777.02] They can focus on what matters most to them.
[3777.40 → 3779.58] So do you describe it as a framework or a toolkit?
[3780.12 → 3782.96] Yeah, I think a framework is a good definition of it.
[3783.06 → 3785.78] It's an API that you call, so it doesn't compile into your code.
[3786.12 → 3787.30] It's a sidecar architecture.
[3787.50 → 3789.62] So there's a process running next to your application.
[3789.62 → 3800.98] You talk to it via HTTP or gRPC, which makes Dapper really inclusive because if you're a developer coming from Python, Java, C Sharp, Rust, whatever language, as long as it can talk HTTP, it can talk to Dapper.
[3801.30 → 3801.54] Okay.
[3802.36 → 3806.04] And so there are a bunch of client libraries probably for different languages that talk to Dapper?
[3806.28 → 3807.16] Yeah, there are.
[3807.34 → 3812.40] They make the development experience nicer, but if you want to, you can just drop to HTTP and gRPC directly.
[3812.50 → 3812.70] Sure.
[3813.24 → 3813.40] Yeah.
[3813.40 → 3821.08] All right, so I have my business logic, and then it's calling over to Dapper and telling Dapper to store some data, give me some data.
[3821.88 → 3825.36] Yeah, handle state that's for you, do Pub Sub between services.
[3825.36 → 3825.56] Yeah.
[3825.56 → 3834.28] But then the nice stuff for ops people is that no matter where you're running, you can basically tell Dapper to work with the infrastructure of choice for your team.
[3834.62 → 3838.76] So Dapper doesn't replace a state store or a Pub Sub or a configuration store.
[3838.92 → 3847.74] It actually has this component model concept where you can plug it in to work with whatever database or Pub Sub or secret store your cloud's running.
[3847.74 → 3857.30] So we have 100 of these community-contributed components that we maintain, and as a DevOps person, you can say, hey, if I'm running Google Cloud, I'll have Dapper work against Firebase.
[3857.60 → 3861.32] We're running on-prem, it'll work against Regis, and as a developer, you get really consistent API.
[3861.86 → 3867.66] So in a multi-cloud environment, you write your code once, and you can basically configure Dapper to work against whatever infrastructure you're running.
[3868.10 → 3868.70] That sounds cool.
[3868.78 → 3870.68] Is there like a Dapper stack?
[3870.68 → 3876.28] Is there like a default set of these are the plugs that we recommend you plug in, but you can plug in whatever you want?
[3876.78 → 3878.46] Yeah, you can basically plug in whatever you want.
[3878.58 → 3879.86] So that's a perfect question.
[3879.98 → 3881.78] We have the concept of a pluggable component.
[3882.26 → 3893.38] So, for example, if you are using Dapper to talk to some proprietary system that you can't contribute upstream back to Dapper, we have a way for you to write that plug in and run it on your own.
[3893.78 → 3895.66] But we also have maturity level.
[3895.66 → 3901.00] So we have alpha components, beta components, stable components, and we recommend people use stable components for production.
[3901.42 → 3903.06] Other than that, you're free to do whatever you want.
[3904.02 → 3908.78] Dapper will make sure that all the best practices are really encapsulated in the API calls for you.
[3909.52 → 3909.64] Huh.
[3910.70 → 3916.98] So how did Dapper escape Microsoft, or how did you escape Microsoft with Dapper, or...
[3916.98 → 3918.02] It wasn't an escape at all.
[3918.18 → 3918.96] Or maybe you just left.
[3919.38 → 3923.16] Yeah, so Dapper was open-sourced first in October 2019.
[3923.40 → 3924.22] It really picked up.
[3924.22 → 3933.98] So we have a lot of end-user adopters today, from IBM to Microsoft to Alibaba Cloud, NVIDIA, NASA is running Dapper in outer space, as we speak, by the way.
[3935.04 → 3935.46] That's cool.
[3935.58 → 3936.78] I think that's the coolest use case of Dapper.
[3936.78 → 3937.44] That's good, right?
[3937.72 → 3937.96] Yeah.
[3938.08 → 3939.68] It's like the ultimate edge deployment, right?
[3939.84 → 3940.04] Yeah.
[3940.46 → 3941.20] Which is nice.
[3941.64 → 3942.94] And so it really picked up.
[3943.04 → 3944.58] We saw a lot of community contribution.
[3944.58 → 3953.04] Then we decided that we're going to give it to our foundation because we want to really make sure that it grows and that we bring other vendors in, other companies.
[3953.04 → 3955.76] So it arrived in the CNCF.
[3956.40 → 3959.92] We were, I think, the first or second project to make it straight into incubating.
[3960.12 → 3965.72] We skipped the sandbox phase because we already had a lot of end-user adoption, a lot of contributions coming in.
[3965.72 → 3969.42] And, yeah, since then, the project really took off.
[3969.54 → 3974.28] And at some point, VCs basically came up to me and were like, hey, you know what?
[3974.44 → 3975.68] How about you spin off Microsoft?
[3975.92 → 3977.60] We think there's going to be a good business here.
[3977.60 → 3979.96] And I basically told all of them no.
[3980.18 → 3982.68] So I was focused on my career at Microsoft.
[3982.88 → 3992.20] And Mark, my co-founder of Dapper and Dy grid also, which is our company, was also busy having Dapper really take off the ground.
[3992.20 → 3996.12] And a year later, we were having a hallway conversation.
[3996.28 → 4000.00] We were like, look, we think Dapper can have a much broader future.
[4000.58 → 4003.98] And we have our own vision for distributed systems and where this can go.
[4004.34 → 4006.30] And this needs to happen outside of Microsoft.
[4006.94 → 4009.42] So, yeah, we basically started Dy grid.
[4009.62 → 4012.80] We left Microsoft in very good terms.
[4012.90 → 4015.02] We're still very friendly with all the people there.
[4015.42 → 4017.60] Microsoft's doing an awesome job on the project.
[4017.60 → 4020.82] They're contributing to the project along with Alibaba and Intel.
[4021.20 → 4026.14] They're the main contributors who are on the Dapper steering committee alongside us, Dy grid.
[4026.66 → 4028.90] And, yeah, it's been a fun ride.
[4029.90 → 4037.30] It's pretty cool to be able to start a project inside of Microsoft, work on it at Microsoft, for Microsoft, donate it.
[4037.40 → 4038.02] Or I don't even donate.
[4038.12 → 4038.68] It's not the right word.
[4038.86 → 4041.64] When you CNCF something, is it donated?
[4041.80 → 4042.46] Yeah, it is donated.
[4042.46 → 4043.10] It is the right word.
[4043.30 → 4043.66] It's the right word.
[4043.82 → 4043.92] Yeah.
[4043.92 → 4046.00] Okay, donate it to the CNCF.
[4046.00 → 4054.74] And then start a company around it that builds on it or around it or for it after that as a startup.
[4054.94 → 4055.78] It's a managed version of it.
[4055.90 → 4056.08] Yeah.
[4056.64 → 4056.84] Yeah.
[4057.26 → 4058.48] That's a beautiful world, man.
[4058.62 → 4059.22] That sounds, yeah.
[4059.34 → 4060.88] You were kind of saying no for a while.
[4061.38 → 4062.42] Yeah, for a long while.
[4062.46 → 4067.24] I was, like, so focused on building Dapper into Azure services, like Microsoft Managed Services.
[4067.88 → 4070.04] They have a service that integrates Dapper.
[4070.18 → 4071.44] So, that's what I was working on.
[4071.44 → 4076.90] And I was, like, I always thought I would be, like, an entrepreneur and start my own company at some point.
[4077.28 → 4079.30] But I didn't see it coming at that point in time.
[4079.38 → 4081.92] So, I told the VCs, yeah, it's not for me right now.
[4082.06 → 4082.24] Right.
[4082.24 → 4083.78] But some of them persisted.
[4083.92 → 4086.70] And in the end, yeah, we took it and went.
[4087.10 → 4088.58] So, what turned the no into the yes?
[4088.66 → 4091.48] Was it a deal you couldn't turn down from a VC?
[4091.76 → 4093.98] Or was it your partner that was, like, come on, let's do this?
[4094.34 → 4095.48] It was a combination of things.
[4095.56 → 4097.80] I think mostly we saw Dapper really take off.
[4097.90 → 4103.42] And we figured out, yes, there can be a business model, especially around helping enterprises operate it on Kubernetes.
[4104.24 → 4108.46] You know, Kubernetes is a complex piece of software to operate.
[4108.56 → 4113.92] And so, we really saw the struggle of developers operating Dapper on top of Kubernetes.
[4114.10 → 4115.46] And we knew we had something to give there.
[4115.70 → 4117.72] This is not something we could have done with Microsoft.
[4117.72 → 4129.96] But also, ultimately, our vision is to come out with a distributed systems API platform that developers from serverless platforms and really platforms from all types of compute can leverage.
[4130.40 → 4130.48] Right.
[4130.52 → 4131.62] So, it's like serverless Dapper.
[4131.84 → 4133.32] You can run it outside of Kubernetes.
[4133.48 → 4134.64] You can run it whatever you want.
[4134.76 → 4134.98] Okay.
[4135.08 → 4136.74] And to do that, it needs to be multi-cloud.
[4137.00 → 4142.08] And so, that was another reason why we thought we'd leave Microsoft and start it with our own company.
[4142.22 → 4145.18] We really want to build our vision of distributed systems through the Dapper APIs.
[4145.84 → 4146.14] Okay.
[4146.14 → 4149.88] What year was that when you started the Diagram?
[4149.98 → 4151.06] It was January 2022.
[4151.90 → 4154.16] So, a year ago, plus and change.
[4154.66 → 4154.98] Yes.
[4155.42 → 4156.32] That's some nice logos here.
[4156.40 → 4157.96] You got IBM Research.
[4158.32 → 4160.46] This is for your company, Diagram.
[4160.74 → 4163.00] IBM Research, Intel, Microsoft.
[4163.36 → 4164.24] Hey, makes sense.
[4164.30 → 4165.04] You did that integration.
[4165.82 → 4172.92] Alibaba Cloud, Huawei, Bosch, Ignition Group, Tencent.
[4172.92 → 4176.06] I mean, these are like major enterprise players.
[4176.44 → 4176.64] Yeah.
[4176.78 → 4180.94] There are a lot of other players who have not come out as public adopters yet.
[4180.94 → 4184.38] Really, some of the biggest names in the industries.
[4184.38 → 4191.64] And what's fascinating about Dapper is that it was adopted by the tech-savvy enterprises before it was adopted by startups, for example.
[4192.10 → 4193.54] And you usually see it the other way around.
[4193.66 → 4193.76] Yeah.
[4194.02 → 4199.62] You know, as a company offering commercial products on top of Dapper, we're not complaining.
[4199.98 → 4200.92] That works out really well for us.
[4200.92 → 4201.96] That sounds great for you guys.
[4201.96 → 4203.08] Why do you think that was?
[4203.14 → 4206.24] Is it because it solves enterprise scale problems?
[4206.74 → 4207.18] Yes.
[4207.32 → 4216.54] I think startups, what's most important to them is to make sure that they deliver on their business, which means they want their infrastructure to be as reliable as possible.
[4216.54 → 4221.20] So they're not as, you know, likely to take on new bets and new technologies.
[4221.36 → 4231.26] But enterprises, on the other hand, they have resources, and they look at new technologies as a way to go to market faster, reach the market faster and really outpace their competition.
[4231.48 → 4233.08] So they're much more open to new tech.
[4233.08 → 4239.82] And I think also it's coming from Microsoft really gave it like the enterprise stamp that made people feel really comfortable adopting it.
[4240.52 → 4243.66] Why is it important to have a managed version of Dapper?
[4244.42 → 4244.66] Yeah.
[4244.80 → 4247.90] So if you're on Kubernetes, for example, you need to manage Dapper yourself.
[4248.30 → 4250.74] And as a developer, you just talk to the Dapper APIs.
[4250.86 → 4251.20] It's easy.
[4251.58 → 4255.20] But as an ops team, it's really difficult to babysit the control plane, you know.
[4255.54 → 4262.70] On Kubernetes, every type of technology that has a control plane that manages a data plane, like a service mesh, you know, Into, Linked, Consul, Dapper.
[4262.70 → 4263.54] It's no different.
[4264.00 → 4265.28] It's really troublesome.
[4265.62 → 4268.06] It's a lot of cognitive overhead for infrastructure teams.
[4268.44 → 4274.68] You need to upgrade, downgrade, do certificate renewals, you know, monitor, observe the infrastructure.
[4275.12 → 4278.90] So we basically do it for you and we take all of that pain away for you.
[4279.14 → 4281.66] And then the other product we're coming out with is serverless Dapper.
[4282.08 → 4285.74] So using Dapper outside of Kubernetes on whatever compute platform you want.
[4286.22 → 4290.42] Browser, Wasm, Edge, Google Cloud Run, AWS Lambda.
[4290.42 → 4292.94] And whatever compute you're running on, you'll be able to use Dapper.
[4293.40 → 4295.82] Is it a problem of scale that makes you want to go managed?
[4295.98 → 4303.50] Or is it like if I'm a small team with, let's say, a three-node Kubernetes cluster, is managing Dapper, myself, my ops team, not a big deal, right?
[4303.72 → 4303.94] Yeah.
[4304.18 → 4308.14] If you're a small operation, then managing Dapper yourself will probably be something that you should be able to do.
[4308.14 → 4310.98] It's once you go too much, much bigger.
[4311.32 → 4313.46] Huawei size, IBM research size.
[4313.46 → 4315.98] Well, slightly smaller than that, too.
[4316.12 → 4321.52] Like we have perfect end users for Diagram, like Sharper Image, for example.
[4322.04 → 4323.02] They're a mid-sized company.
[4323.28 → 4330.42] They wrote their own application platform, and they replaced it with Dapper internally because they want to really repeat on something that was standard.
[4331.46 → 4335.02] And they're a five-person development team, I think.
[4335.14 → 4338.74] And they're using our services to manage it because, you know, they're a small team.
[4338.88 → 4340.30] They want to focus on their business logic.
[4340.38 → 4341.88] They want to focus on managing Dapper.
[4341.88 → 4344.22] So this also helps smaller teams.
[4344.56 → 4344.68] Yeah.
[4345.38 → 4349.16] Can you speak to the reluctant founder journey to some degree?
[4349.24 → 4350.68] Like you said you eventually wanted to be an entrepreneur.
[4350.84 → 4351.66] You just wasn't sure when.
[4351.82 → 4352.00] Yeah.
[4352.24 → 4355.26] And speak to the I have this open source project.
[4355.48 → 4358.98] I incubated it, or I am incubating it inside CNCF.
[4359.40 → 4362.14] Why incubate or donate to the CNCF?
[4362.20 → 4364.28] Like what does that benefit the project?
[4364.54 → 4365.76] You speak to all those details.
[4365.96 → 4368.48] For those listeners out there thinking, you know, I'm you.
[4368.62 → 4370.16] I'm a version of you at some point.
[4370.22 → 4371.20] I may do something like this.
[4371.20 → 4372.32] Why did you take this route?
[4372.66 → 4374.18] Why did this donation make sense?
[4374.28 → 4377.10] And this whole route makes sense for your, I guess, your journey?
[4377.56 → 4377.72] Yeah.
[4377.78 → 4381.16] So we donated Dapper to CNCF while we were at Microsoft.
[4381.48 → 4385.00] And the reason, the main reason why we did that was to really gain new contributors.
[4385.26 → 4386.42] Dapper had a lot of contributors.
[4386.42 → 4389.56] But being vendor neutral is something that's really important.
[4389.56 → 4403.90] You know if it's a project that spins out of Microsoft or AWS or Google, and it remains under their proprietary, you know, licenses or control, then users of other clouds might not feel so much inclined to take a bet on it.
[4403.90 → 4407.92] Because they will go like, oh, it's a Microsoft thing, or it's an AWS thing, or it's a Google thing.
[4407.92 → 4419.32] But when you donate to CNCF, you get this vendor neutrality, and you gain these new audiences of contributors who are coming in from, you know, every walk of life, every cloud platform or technology that contribute to your project.
[4419.32 → 4428.74] So your end users grow, your contributor audience grows, and people see that this is really something that can adhere to many users from many cloud platforms.
[4428.94 → 4431.04] We didn't want it just to become an Azure thing.
[4431.50 → 4433.92] So primary benefit is vendor neutral.
[4434.08 → 4434.36] Yes.
[4434.58 → 4438.38] And new contributors because you're seen as a level playing field, no bias.
[4438.64 → 4439.02] Correct.
[4439.24 → 4439.40] Right.
[4439.46 → 4440.72] No corporate overlord necessarily.
[4440.90 → 4441.06] Yeah.
[4441.50 → 4441.74] Okay.
[4442.54 → 4444.46] How has that benefited Diagram?
[4444.46 → 4451.62] How has that benefited your company in terms of like commercializing this open source, your journey to get venture-backed funding?
[4451.92 → 4457.72] Like how has that helped in all ways the business angle of, has it been a lot easier, I suppose, to do this route?
[4458.20 → 4463.48] So, you know, there are a lot of commercial entities that back open source projects that are not CNCF projects.
[4464.30 → 4465.74] You know, I can name many.
[4465.74 → 4478.26] But I think the one major benefit of being in the CNCF was looking at the contributor growth since we joined because Apr picked up a lot of new contributors ever since we joined.
[4478.36 → 4484.22] And when you pick up new contributors, eventually it translates into end users, which translates into new business.
[4484.22 → 4488.04] So, yes, that makes commercializing it easier.
[4488.30 → 4498.04] You have to spend less time working on the open source project than you would have if it wasn't in CNCF because you get this awesome power of the open source contributions helping your project.
[4498.20 → 4501.92] Where otherwise we would need to like fund a really, really large team to work on open source.
[4502.16 → 4502.28] Right.
[4502.90 → 4504.72] What's the license of Apr itself?
[4505.00 → 4506.96] And is there anybody else who can do a Diagram?
[4507.22 → 4508.66] Could like Jared and I get like, you know what?
[4508.70 → 4510.54] Hey, we're leaving here today, and we're going to compete.
[4510.80 → 4511.90] Yes, you can definitely do that.
[4512.08 → 4513.06] Apr is Apache 2.
[4513.06 → 4515.26] That's mandated by the CNCF.
[4515.62 → 4520.06] So all CNCF projects are under an Apache 2 license, which is very flexible in how you commercialize it.
[4520.30 → 4521.24] You can do whatever you want.
[4521.30 → 4522.80] You can start your own service around it.
[4523.34 → 4525.54] Apr and any other project in the CNCF.
[4525.80 → 4531.28] So you're competing on, I guess, your ability to do the managed service the best, right?
[4531.28 → 4531.48] Yes.
[4531.48 → 4536.88] So if somebody comes out and competes with you, they compete on the same, they have the same Apr core or whatever it might be.
[4537.04 → 4538.98] They can spin up a version of that.
[4539.06 → 4542.84] No, it wouldn't be cool necessarily to do that, but they could.
[4542.84 → 4543.50] It's possible.
[4543.78 → 4544.40] Yeah, definitely.
[4544.76 → 4546.22] And, you know, we welcome competition.
[4546.68 → 4551.02] Look what's happening with Argo, the CNCF project that picked up on a lot of traction.
[4551.52 → 4554.72] CCD side, there are multiple companies trying to commercialize it today.
[4555.46 → 4556.80] Microsoft's commercializing Apr.
[4556.80 → 4559.88] I actually built Apr into a managed service.
[4560.02 → 4566.10] So I kind of, in a way, created some of my own future competition, which is pretty cool.
[4566.28 → 4569.92] You know, the Microsoft people are great and competition is good because it makes everyone better.
[4569.92 → 4585.80] But, yes, we believe that in Diagram, because Mark and me, my co-founder, created the Apr project, and we're core maintainers of the project, and we're also on the Apr steering committee alongside Alibaba, Intel, and Microsoft, then we have a very good, you know, overview into the project.
[4585.80 → 4589.44] And we have a very good understanding of the technical aspects of it.
[4590.06 → 4592.00] But you didn't name yourself Apr Inc.
[4592.60 → 4594.42] Yes, yes, we didn't.
[4594.54 → 4595.20] For two reasons.
[4595.34 → 4597.46] One is, well, a legal requirement.
[4597.72 → 4600.16] We can't because Apr is under trademarks of CNCF.
[4600.16 → 4602.54] So that limits you.
[4602.84 → 4611.30] But even if it didn't have that limitation, we still wouldn't do that because we don't want to tie the fate of our company to, you know, one single project.
[4611.70 → 4613.78] At some point, Diagram will eclipse Apr.
[4614.14 → 4617.70] Apr is an amazing framework helping a lot of developers out there today.
[4617.98 → 4621.34] And we will be invested in it for as long as the company lives.
[4621.48 → 4623.60] That's a promise to anyone out there listening to this.
[4623.60 → 4629.82] But we will also want to give, you know, our own take about distributed systems that might not necessarily have something to do with Apr.
[4630.10 → 4634.58] Our core at Diagram is to make application developers more successful, whatever they're doing.
[4634.66 → 4636.60] And Apr is one way of doing it, and there may be others.
[4636.60 → 4645.12] And so, yeah, we name yourself Diagram because that's an architectural term that helps buildings be built, you know, faster and more reliably.
[4645.26 → 4646.06] And that's what we want to do.
[4646.12 → 4650.28] We really want to enable architectural patterns for application developers to be better.
[4650.28 → 4655.82] Is there a parallel to Apr or a comparable that people may know about?
[4656.44 → 4661.56] Yeah, so Apr is really polyglot in that you can talk to it from any language.
[4661.80 → 4668.46] I think if you look at, like, individual programming languages, you'll find equivalents like Spring, for example, for Java.
[4668.64 → 4670.14] Or Spring Cloud, right?
[4670.22 → 4673.54] So it's like a Java framework that gives you all of these developer primitives.
[4673.80 → 4675.10] It's like Apr for Java.
[4675.38 → 4675.60] Right.
[4675.60 → 4677.04] And you have Micro for Go.
[4677.04 → 4681.00] So, yeah, those are the immediate two that I can think of.
[4681.56 → 4682.20] That helps.
[4682.64 → 4690.50] So are there drawbacks to the polyglot style versus, I mean, I'm sure there are, but HTTP works pretty well.
[4690.88 → 4691.70] Yeah, it does.
[4691.70 → 4697.42] I mean, like, if you're writing a very extremely low-latency application, Apr might not be for you.
[4698.22 → 4698.60] Right?
[4698.64 → 4700.96] Because you still have an extra network call.
[4700.98 → 4701.16] Right.
[4701.16 → 4709.58] And so, like, if you're writing a trading application, and need, like, I don't know, microseconds of latency, Apr might not be a fit for you.
[4709.88 → 4715.58] But we do believe that, you know, in that terms, performance is good for, you know, 90% plus of use cases.
[4715.58 → 4726.38] Another reason why Apr might not be for you is if you need really, really specific features from, like, Kafka, AWS, Dynamo DB, because Apr is an abstraction layer on top of this infrastructure.
[4726.78 → 4731.80] In many cases, it adds features that you don't find on top of these cloud services, which is really helpful.
[4732.18 → 4735.24] But in some cases, you won't find the feature that you're looking for.
[4735.44 → 4735.52] Yeah.
[4735.52 → 4738.32] So if you need something really esoteric, Apr might not be the best fit.
[4738.62 → 4739.04] Makes sense.
[4739.12 → 4741.98] Lowest common denominator across what you're trying to do.
[4742.76 → 4743.10] Cool.
[4743.50 → 4744.18] Anything else?
[4744.84 → 4748.24] Future, is the project mature in terms of feature set?
[4748.34 → 4750.78] Or is it, like, you got huge plans for Apr?
[4750.96 → 4751.28] Yeah.
[4751.42 → 4752.28] And you feel like it's kind of done?
[4752.34 → 4753.18] We have huge plans.
[4753.32 → 4755.86] We've recently added workflows, which is really nice.
[4755.86 → 4766.34] So very, you know, workflow as code type of programming model where you can tell your code, hey, sleep for 100 years and then kick off this process, and it'll be reliable and secure.
[4766.92 → 4771.90] And we're adding cryptography APIs, blob streaming APIs, document store APIs, SQL APIs.
[4772.28 → 4774.22] There's a whole world of APIs getting added to Apr.
[4774.22 → 4778.16] We have eight today, and we're going strong on 12, I want to say, in the next year.
[4778.70 → 4778.96] Awesome.
[4779.50 → 4779.98] Very cool.
[4780.44 → 4780.80] Thanks, Jaron.
[4781.16 → 4781.64] Thank you.
[4781.84 → 4782.54] Thanks for having me.
[4782.70 → 4783.22] Thank you.
[4783.90 → 4784.18] Jaron.
[4784.72 → 4785.16] Jaron.
[4785.36 → 4785.76] Jaron.
[4786.16 → 4786.62] My bad.
[4786.70 → 4787.12] Thanks, Jaron.
[4787.18 → 4787.72] My bad, Jaron.
[4790.98 → 4793.88] Okay, that completes our transition to Apple.
[4794.08 → 4795.42] I mean, well, that's the wrong announcement.
[4795.48 → 4795.82] My bad.
[4795.82 → 4803.86] That completes our Open Source Summit North America 2023 in Vancouver, Canada coverage.
[4804.30 → 4815.84] Big, big, big thank you to our friends over at GitHub for sponsoring our efforts to get there and get all this awesome hallway track coverage and bring it back.
[4815.86 → 4818.04] Cut it up and make it awesome.
[4818.04 → 4821.28] And then share it with you because, well, we love you.
[4821.28 → 4826.22] Okay, so if you want to give us some feedback on this episode, the link is in the show notes.
[4826.34 → 4828.40] But one more thing.
[4828.46 → 4834.54] Coming up next, speaking of Apple coverage, we have our Friday show coming up.
[4834.54 → 4837.08] The next change log and friends.
[4837.08 → 4842.34] We have Mike McQuaid joining us for WWDC coverage.
[4842.68 → 4845.74] Vision Pro, all the updates, everything.
[4845.74 → 4850.22] And then next week on this show, we're talking pass keys.
[4850.46 → 4852.96] It's going to be such a fun conversation.
[4853.12 → 4856.14] If you want to know about pass keys, come back next week.
[4856.62 → 4857.48] We've got something for you.
[4858.00 → 4858.56] But that's it.
[4858.56 → 4859.40] This show is done.
[4859.52 → 4866.38] Big thank you to our friends over at Vastly, over at Fly, and also our friends at Type Sense.
[4866.92 → 4874.28] And of course, the infamous and also famous brake master cylinder because those beats, well, they're banging.
[4874.82 → 4875.40] That's it.
[4875.62 → 4876.32] This show's done.
[4876.78 → 4877.32] We'll see you tomorrow.
[4877.32 → 4877.38] We'll see you tomorrow.
