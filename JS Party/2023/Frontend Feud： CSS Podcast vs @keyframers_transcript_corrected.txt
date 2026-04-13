[0.00 → 3.32] Please hold, your feud is important to us.
[7.68 → 10.32] This episode is brought to you by Sentry.
[10.52 → 12.32] They just launched Session Replay.
[12.46 → 17.36] It's a video-like reproduction of exactly what the user sees when using your application.
[17.86 → 20.66] And I'm here with Ryan Albrecht, Senior Software Engineer at Sentry,
[20.92 → 24.94] and one of the leads behind their Emerging Technologies team that built this feature.
[25.28 → 27.06] Ryan, what is this team all about?
[27.06 → 30.96] Emerging Technologies has been one of the greatest teams I've been working on in my career,
[31.32 → 33.06] and I think it's been highly successful.
[33.28 → 37.40] We just today launched Session Replay, and so it's a big celebration here,
[37.52 → 41.26] but I think that what we've built is going to be able to help all of our customers
[41.26 → 46.94] to solve their problems faster and really look at debugging and fixing issues in a new way.
[47.28 → 48.44] So what is Session Replay?
[48.72 → 51.90] Session Replay, it's a video-like reproduction of what your user saw.
[52.10 → 56.56] Instead of recording a video, we're recording the actual DOM nodes that appear and disappear on the screen,
[56.56 → 59.24] and then we can replay those to you in your own browser.
[59.50 → 63.40] So what this lets you do is you can actually see exactly what the user experienced in the application,
[63.84 → 67.22] take the guesswork out of trying to triage and what are the reproduction steps,
[67.40 → 71.98] stop at a point and inspect the DOM to see, you know, was this paragraph tag in the right spot?
[72.16 → 73.74] What are the CSS and the background colours?
[73.98 → 77.04] You can look at everything as if you were on that customer's machine.
[77.46 → 77.80] There you go.
[77.80 → 80.84] So if you've been playing detective, trying to track down support tickets,
[81.14 → 83.86] read through breadcrumbs, stack traces, and the like,
[84.10 → 89.02] trying to recreate the situation of a bug or an issue that your application has,
[89.08 → 92.28] now you have a game-changing feature called Session Replay.
[92.48 → 95.68] Head to Sentry.io and log into your dashboard.
[95.82 → 98.66] It's right there in the sidebar to set up in your front end.
[98.78 → 100.74] And if you're not using Sentry, hey, what's going on?
[100.92 → 103.64] Head to Sentry.io and use the code PART-TIME.
[103.64 → 106.28] That gets you three months for free on the team plan.
[106.60 → 110.02] Again, Sentry.io and use the code PART-TIME.
[131.16 → 133.24] Feud is important to us.
[133.24 → 138.80] This is JS Party, your weekly celebration of JavaScript and the web.
[139.46 → 141.78] Bandwidth for JS Party is provided by Vastly.
[142.12 → 144.02] Learn more at Fastly.com.
[144.30 → 147.06] And our podcasting platform is powered by Fly.
[147.66 → 150.62] Post your app servers and database close to your users.
[151.14 → 152.68] No ops required.
[153.20 → 155.40] Learn more at Fly.io.
[156.44 → 159.74] It's time to play Front End Feud!
[159.74 → 162.70] Welcome, friends.
[162.88 → 164.98] This is Front End Feud.
[165.12 → 168.18] Everyone's favourite award-worthy game show
[168.18 → 174.04] made by the award-winning JS Party podcast that you're listening to this very moment.
[174.04 → 175.60] I'm Jared Santo.
[175.60 → 180.50] And I'd like to thank all 100 of our savvy, tasteful, good-looking audience members
[180.50 → 184.60] for taking the time to take the survey, which makes this game possible.
[185.14 → 188.10] After dethroning the Shop Talk guys last time we played,
[188.30 → 193.88] Una Gravity and Adam Argyle are back from the CSS podcast defending their title.
[193.88 → 194.72] Welcome to the show.
[194.72 → 195.00] Woo!
[195.84 → 196.22] Thank you.
[196.32 → 197.86] Let's see if we can go two for two.
[199.02 → 200.00] We shall see.
[200.08 → 200.58] We shall see.
[200.70 → 201.54] And our challengers.
[201.68 → 204.80] We have David and Shaw from the Key framers show.
[205.00 → 205.54] Welcome, guys.
[206.24 → 207.42] Hey, thanks for having us.
[208.12 → 208.76] Ah, jinx.
[208.98 → 209.34] Jinx.
[210.78 → 213.18] They're already on the same page.
[213.28 → 214.12] This is a problem, Adam.
[215.52 → 220.34] That may not work if we're trying to sync up on what the audience is thinking, though.
[220.48 → 220.90] Exactly.
[221.36 → 221.78] That's true.
[221.78 → 225.84] Now, I've been told that it's customary in game shows to take a moment and get to know
[225.84 → 226.90] each of our contestants.
[227.84 → 232.38] But I didn't really have time to prep for this, so I asked our intern, Larry, to do some research
[232.38 → 235.36] and write up a question, one for each of you, which I will read now.
[235.52 → 239.90] So, Una, do you remember the first time you rode a bike without training wheels?
[240.56 → 240.76] Huh.
[241.60 → 243.38] Um, I do remember.
[243.76 → 244.08] All right.
[244.12 → 244.64] Thank you.
[244.92 → 249.26] Adam, who is your daddy and what does he do?
[249.26 → 251.20] I'm a cop, you idiot.
[252.88 → 253.70] Very good.
[254.08 → 255.66] David, I'm told you play the piano?
[256.30 → 256.66] I do.
[257.04 → 259.98] Where do you think Elton John gets those fancy outfits he wears on stage?
[260.46 → 261.28] Oh, I don't know.
[261.56 → 263.78] Um, probably coordinates with Billy Joel.
[264.02 → 264.62] I have no idea.
[265.18 → 265.92] Good answer.
[266.12 → 267.28] Shaw, do you like apples?
[267.98 → 268.24] Yeah.
[268.46 → 268.66] Yeah.
[268.80 → 269.42] They're pretty good.
[269.80 → 270.86] Well, I got her number.
[271.02 → 271.74] How do you like that?
[271.96 → 272.86] Larry, that's terrible.
[273.18 → 273.82] It's not even a question.
[273.82 → 276.30] Gosh.
[276.82 → 277.76] Let's just move on.
[277.82 → 283.74] Let's move on to our game, which, as you know, is not a game about how much front end
[283.74 → 286.90] or JavaScript or developer information you all have in your heads.
[287.14 → 293.28] It's how well you know the life of a developer, the choices, the answers that our listening
[293.28 → 297.20] audience put into those text boxes on the survey.
[297.30 → 298.24] So here's how it works.
[298.24 → 301.50] We have six rounds, of course, two teams.
[302.08 → 309.04] Each round has a game board in which we have a statement followed by the top matching answers,
[309.66 → 310.60] highest to lowest.
[310.94 → 317.02] Your job is to match the highest ranking answers, accumulate points, and the team with the most
[317.02 → 319.48] points at the end of six rounds wins.
[320.12 → 325.44] Now, each round starts with what we call an inter-face-off, because we love puns, and in
[325.44 → 330.84] which one person from each team steps up and gets to guess first.
[330.94 → 336.46] The person who matches the highest ranking answer on the board during that time gets
[336.46 → 341.84] to take the round, and their team plays that entire round until three strikes occur, at
[341.84 → 345.96] which point the other team can steal the points in the round with one guess.
[346.04 → 350.64] Now, there's no conferring between you and your teammate during the regular round, but during
[350.64 → 356.40] the steal, you all can talk, decide, and figure out which steal you're going to play.
[356.96 → 357.54] Any questions?
[358.26 → 359.78] When does Steve Harvey get here?
[361.56 → 362.62] You're looking at him.
[362.64 → 363.66] I'm your Steve Harvey today.
[363.76 → 364.74] I apologize in advance.
[365.44 → 367.06] This is as good as it's going to get.
[367.72 → 368.06] All right.
[368.20 → 371.90] First up in our inter-face-off, it is David versus Luna.
[372.06 → 372.84] Step right up.
[373.54 → 374.26] Woo-hoo!
[374.58 → 375.66] Woo-Hoo-hoo-hoo-hoo!
[375.66 → 376.16] Woo-Hoo-hoo-hoo!
[376.16 → 376.66] All right.
[376.66 → 383.84] Ladies first, Luna, we asked 100 JS Party listeners, which server-side JavaScript runtime
[383.84 → 387.82] do they expect to be using three years from now?
[388.02 → 390.34] What do you suppose was their response?
[391.46 → 392.14] Runtime.
[392.58 → 393.76] So is this like Node.js?
[394.18 → 398.92] Because that's been pretty popular for a long time and likely will continue.
[399.78 → 400.58] Is that your answer?
[401.40 → 401.74] Yes.
[401.84 → 403.14] That's my final answer.
[403.28 → 403.90] Final answer?
[404.08 → 404.84] Final answer.
[404.84 → 405.84] Survey says?
[406.66 → 410.20] That is the number one answer.
[410.56 → 416.28] So 43 of 100 said they would be using Node three years from now.
[416.36 → 418.68] So that means David does not get a chance.
[418.76 → 419.20] I apologize.
[419.40 → 420.24] But Luna stole the board.
[420.44 → 422.70] And now Team CSS Podcast gets to play.
[423.08 → 425.86] There are four total answers on the board.
[426.54 → 427.78] You've got the number one answer.
[427.94 → 429.66] And you now need to find the other three.
[429.76 → 435.28] I shall say, in order to make it on the board, an answer must have at least five responses.
[435.28 → 440.46] So you may match something that somebody said, but we had to have five people say it for it to make the board.
[441.12 → 443.90] So CSS Podcast is live.
[444.26 → 445.26] This is a hard one.
[446.30 → 447.44] It's Adam's turn.
[447.52 → 448.14] There's three left.
[448.22 → 449.06] You already have Node.
[449.32 → 453.64] Which server-side JS runtime do people expect to be using three years from now?
[454.12 → 457.36] The one I just built my site on top of, Dino.
[457.36 → 457.48] Dino.
[458.16 → 459.44] Show me Dino.
[460.42 → 461.44] It is on there.
[461.54 → 462.64] Let's find out where it is.
[462.94 → 464.38] You can't just rearrange letters.
[464.56 → 465.04] It's cheating.
[465.34 → 467.32] In fact, number two.
[467.50 → 471.08] 30 respondents said they'd be using Dino three years from now.
[471.14 → 471.56] Very good.
[471.70 → 472.26] So we go back.
[472.26 → 473.08] I got another one.
[473.14 → 473.86] Is this on Luna?
[474.40 → 475.88] Yeah, it goes back to her now.
[475.96 → 476.86] So you'll have another chance.
[476.98 → 477.80] It goes back to me.
[478.26 → 480.30] Yeah, it toggles back and forth until we get three strikes.
[480.58 → 481.62] You're halfway there.
[482.06 → 483.64] But there are two responses left.
[483.76 → 484.24] What do you think, Luna?
[484.72 → 485.40] Oh, God.
[485.40 → 485.94] I don't know.
[488.66 → 490.00] Server-side runtime.
[490.46 → 492.38] I don't even know if this is a server-side runtime.
[493.18 → 500.66] But I know that there is a tool that's been growing in popularity which has server-side rendering.
[500.66 → 505.58] I just don't know if this is a runtime or counts because it's a server.
[506.24 → 508.52] But this is what runs a server, right?
[509.28 → 514.56] Remember that the answers for this survey were completely based on the interpretation of the question
[514.56 → 516.22] by the survey taker.
[516.30 → 517.76] So they can take it however they want.
[518.24 → 521.66] I can't clarify what I meant because it meant something different to everybody.
[521.84 → 525.28] So go ahead and guess and just see what you can do.
[525.64 → 527.20] God, this is going to be wrong.
[527.78 → 529.12] This is going to be wrong.
[529.46 → 532.46] But for some reason, I'm thinking Site.
[532.54 → 533.92] But that's not a server-side runtime.
[534.56 → 535.28] But anyway.
[535.28 → 535.44] Anyway.
[535.94 → 537.00] Show me Site.
[538.56 → 539.00] Yeah.
[539.10 → 539.52] I'm sorry.
[539.62 → 541.54] But yes, that is incorrect.
[541.74 → 543.24] So you now have one strike against you.
[543.54 → 544.70] And we go back to Adam.
[545.28 → 545.88] I say bun.
[546.42 → 547.58] Show me some buns.
[547.90 → 549.02] Show us buns.
[550.30 → 551.46] Bun is on the list.
[551.54 → 553.84] Number four with seven responses.
[554.04 → 555.80] So now we have Note at number one.
[556.42 → 557.32] Dino at number two.
[557.52 → 558.70] Number three is a question mark.
[558.70 → 561.14] And bun with seven.
[561.24 → 562.10] You have one strike.
[562.50 → 564.20] So two more wrong guesses before a steal.
[564.60 → 565.42] You know we're back to you.
[566.46 → 566.94] Okay.
[567.18 → 572.34] So I'm thinking with things like Node being very popular,
[572.60 → 574.80] maybe people are thinking along those lines.
[575.74 → 579.42] So maybe people are thinking of like,
[579.78 → 582.76] everything I'm thinking of is a framework on top of a runtime.
[583.02 → 583.78] That's the problem.
[585.46 → 586.64] This is a hard one.
[587.02 → 587.34] Damn.
[587.34 → 588.50] My next thought goes to like,
[588.56 → 589.80] oh, what if it's something like Express?
[589.82 → 590.90] If they're thinking about Node,
[591.02 → 592.90] but they're not sure what the right answer is here.
[593.18 → 594.14] But that's not a runtime.
[594.46 → 597.48] It's a framework that you use on top of Node.
[598.50 → 599.64] Can I phone a friend?
[600.20 → 601.90] We will need some sort of guess.
[601.92 → 602.40] Different show.
[602.70 → 603.46] That's a different show.
[603.86 → 605.60] We do not have that kind of budget around here.
[605.98 → 606.74] What about Adam?
[606.82 → 607.52] Adam is my friend.
[608.34 → 608.76] He's here.
[608.84 → 609.86] Well, you can get one wrong.
[609.92 → 610.48] I'll be back to him.
[610.54 → 611.32] He gets another chance.
[611.40 → 612.94] So you can just guess whatever you like.
[613.26 → 614.38] Remember, it's what they said.
[614.38 → 615.44] It's not what is correct.
[615.84 → 616.36] That's true.
[616.36 → 617.64] So I'll guess Express,
[617.92 → 620.52] but I just know that's probably not it.
[620.70 → 621.48] Unless it is.
[621.60 → 622.54] Show me Express.
[624.42 → 625.46] It is not Express.
[625.66 → 628.98] I will say that there was at least one response that was Express.
[629.30 → 631.96] So you were not completely wrong,
[632.04 → 632.86] but not five.
[633.14 → 634.16] No, I was wrong.
[635.00 → 636.26] I knew that I was wrong.
[636.52 → 637.30] I was trying to throw you a bone.
[637.38 → 637.88] Two strikes.
[638.30 → 639.24] Back to Adam.
[639.42 → 640.12] Okay, this is it.
[640.14 → 640.88] You got one guess.
[640.98 → 641.94] You got one on the board.
[641.94 → 645.58] What do you think people said to this question about JS runtimes three years from now?
[645.82 → 646.06] Yep.
[646.94 → 649.50] I'm just going to go with the first one that I wrote down.
[649.72 → 652.82] Not sure if it's totally it, but maybe there are multiple terms,
[653.00 → 657.00] but it's either Cloudflare workers or edge workers in general.
[657.00 → 660.98] So just running your servers at the edge in a serverless function.
[661.38 → 661.82] Okay.
[662.30 → 663.82] Show us edge workers.
[665.74 → 666.62] I'm sorry.
[666.78 → 668.18] That is also not on the board.
[668.30 → 670.64] We now have an opportunity to steal.
[670.80 → 672.52] There are 80 points up for grabs.
[673.34 → 677.28] So key framers, guys, if you steal this, you get the 80 plus the correct answer.
[677.50 → 680.70] If you don't, the 80 goes to unit and Adam, and we move on.
[681.02 → 683.00] So you get one guess you can discuss together.
[683.66 → 684.36] Fingers crossed.
[684.36 → 685.32] That number three slot.
[685.40 → 685.94] What is it?
[686.02 → 686.50] What is it?
[686.94 → 687.22] All right.
[687.26 → 688.38] Well, what are you thinking, David?
[688.60 → 688.98] What are you thinking?
[688.98 → 691.52] I mean, I was also thinking Cloudflare.
[691.86 → 694.12] Cloudflare workers, too.
[694.64 → 697.86] But there has to be something else obvious that we're not thinking of.
[698.80 → 702.38] WebAssembly is the only thing that's coming to mind for me.
[702.54 → 703.00] You know what?
[703.14 → 703.46] Yeah.
[703.78 → 706.80] I think that's a let's go for it.
[707.24 → 708.14] That's a good guess.
[708.54 → 709.04] WebAssembly.
[709.34 → 709.92] Final answer.
[709.92 → 711.78] For the steal, WebAssembly.
[711.78 → 711.98] WebAssembly.
[714.54 → 720.08] I'm sorry, but it was not WebAssembly, which means CSS Podcast is awarded 80 points.
[720.24 → 721.42] See, this is the luck aspect.
[721.80 → 724.66] And we will now see what is that magical number three.
[724.84 → 726.56] It's not IONS, right?
[726.70 → 728.20] Is it Basel or something?
[728.42 → 733.06] One thing you have to know about JS Party listeners is they love to reject the premise of the question.
[733.38 → 733.72] None.
[734.04 → 734.98] The answer is none.
[734.98 → 737.84] They do not see themselves using a JS runtime.
[738.38 → 741.54] I was trying to answer with the rejection of the premise as well.
[742.58 → 743.02] Right.
[743.46 → 744.70] What if they just misspelled node?
[745.30 → 746.10] You know, it doesn't count.
[746.10 → 747.34] Ooh, also a possibility.
[747.52 → 748.94] Eight people misspelled node.
[749.18 → 751.10] They're just a few keyboard clicks away.
[751.20 → 752.96] Didn't one just show up, though, after Bun?
[753.06 → 757.96] Like, Bun got their funding, and I thought somebody else showed up recently that's like another fast job.
[758.00 → 760.92] And I couldn't remember what it was, but maybe I'm confusing it with.
[761.14 → 763.06] What about browser-based JS runtimes?
[763.72 → 764.68] No, it doesn't make the list.
[764.68 → 765.94] A few other runners-up.
[766.10 → 767.48] So three people said Remix.
[768.22 → 769.46] Two said Astro.
[769.68 → 770.90] One person said Ruby on Rails.
[770.90 → 772.62] Yeah, but those are frameworks.
[772.94 → 773.02] What?
[773.82 → 774.76] That's the same problem.
[775.12 → 775.80] Not runtimes.
[775.94 → 776.60] It's the same problem.
[776.74 → 781.78] And one person said an unreleased Go framework, which I think they're going to be releasing or something.
[781.94 → 784.24] But that's what they're going to be using three years from now.
[784.44 → 785.28] You heard it here first.
[785.52 → 786.48] So you heard it here first.
[786.80 → 787.18] All right.
[787.22 → 788.84] That brings us to round two.
[788.94 → 792.38] So after the first round, CSS Podcast holds on to their 80 points.
[792.38 → 794.76] We now move to round two.
[795.48 → 798.20] And our interface off is between Shaw and Adam.
[798.34 → 799.32] Step right up.
[801.32 → 801.76] Ooh.
[802.08 → 803.12] Brothers from another mother.
[803.22 → 803.54] Let's go.
[803.94 → 804.20] All right.
[804.26 → 806.06] We'll let Shaw go first on this one.
[806.26 → 810.34] The question is, every big tech company wants to hire you.
[810.88 → 812.44] Compensation is identical.
[813.46 → 815.10] Which do you choose?
[815.18 → 818.04] There are five answers on the board.
[818.16 → 819.58] Shaw, we go to you.
[819.58 → 821.34] Ah, man.
[821.94 → 822.82] That's tough.
[822.96 → 826.98] What does the audience think is the question.
[828.06 → 829.38] I'm going to go with Apple.
[830.06 → 830.88] Show us Apple.
[831.92 → 833.10] You are correct.
[833.22 → 841.36] And it is the number one answer with 21 respondents choosing Apple, which means, key framers, you get to play this round.
[841.86 → 844.04] And we go to David for another guess.
[844.72 → 845.16] Awesome.
[845.16 → 848.54] Well, running through the thing, Ming, whatever we want to call it.
[848.54 → 853.76] But I would say another one would be, I just came from Microsoft.
[854.26 → 856.54] So I don't know if that's the obvious one, though.
[857.28 → 860.24] Oh, oh, man, is OpenAI a big, you know what?
[860.28 → 862.14] Let's go with the obvious first, Microsoft.
[863.28 → 864.56] Show us Microsoft.
[865.62 → 867.78] Number two answer with 18.
[868.24 → 869.02] Very nice.
[869.64 → 870.60] Back to you, Shaw.
[870.70 → 872.40] We are now rolling in round two.
[872.40 → 875.76] I'm going to say Google is definitely on there.
[876.16 → 877.32] Show us Google.
[878.54 → 879.56] Number three answer.
[879.82 → 881.28] 13 points to you, sir.
[881.40 → 882.22] Very well played.
[882.38 → 883.22] Going down the list.
[883.34 → 884.96] Do I get extra points for going in order?
[885.64 → 886.76] You get kudos from me.
[886.94 → 889.02] You have the top three, four and five.
[889.12 → 893.06] Of course, it gets more difficult as you get further down because there are lots of big tech companies to guess from.
[893.62 → 894.20] David, what are you thinking?
[894.60 → 899.10] I was going to say Amazon, but that's like the only reason you would work there is for the compensation.
[899.60 → 900.04] No offence.
[900.04 → 904.06] But if it's identical, then you know what?
[904.10 → 905.02] Let's do Netflix.
[905.20 → 905.90] That's a big one.
[906.22 → 907.54] Show us Netflix.
[908.82 → 910.18] Number five answer.
[910.30 → 910.90] Very good.
[911.00 → 915.28] So you lost your purity in order, but you did not lose your purity in guesses.
[915.50 → 916.74] So you're four for four.
[916.74 → 916.82] Number four.
[917.62 → 918.72] There's one left.
[918.80 → 919.90] Number four is still open.
[920.02 → 921.00] Zero strikes against you.
[921.06 → 922.74] So you have three guesses at this before a steal.
[923.54 → 934.68] Man, I wouldn't want to work there, but Meta slash Facebook is probably on the list somewhere, mostly because of their React development.
[935.16 → 936.94] I'm sure people want to be a part of.
[937.38 → 938.42] Show us Meta.
[938.42 → 941.86] Strike number one.
[942.02 → 943.20] Not in the top five.
[943.40 → 944.00] David, back to you.
[944.06 → 944.90] Good on you, audience.
[946.18 → 946.76] All right.
[946.82 → 948.12] Let's go with the obvious.
[948.48 → 948.80] Amazon.
[949.26 → 950.10] Show me Amazon.
[951.86 → 952.26] What?
[952.46 → 955.44] Amazon had three, but didn't quite make the top five.
[956.12 → 956.52] Jeez.
[956.76 → 957.70] Now we have two strikes.
[957.78 → 958.84] We're down to our last guess.
[958.84 → 961.18] Luna and Adam, start thinking about a steal.
[961.50 → 961.72] Okay.
[961.76 → 962.92] What else is in the acronym?
[963.38 → 964.84] We've got...
[964.84 → 967.84] Man, I'm not even...
[968.42 → 970.22] I'm thinking of any other top companies.
[970.72 → 972.88] Am I allowed to help or are we on the same team?
[973.06 → 974.20] Not at this point.
[974.50 → 975.50] During a steal, you can help.
[975.98 → 976.30] Okay.
[977.00 → 977.30] Yes.
[977.40 → 978.56] It's not Amazon.
[978.96 → 979.92] It's not Meta.
[980.40 → 981.90] And GitHub's a part of Microsoft.
[982.26 → 983.14] So that...
[983.14 → 986.16] Did you combine audience answers into...
[986.16 → 986.54] Yes.
[986.70 → 987.54] GitHub is Microsoft.
[987.78 → 988.00] Yes.
[988.28 → 988.58] Okay.
[989.46 → 990.44] Ah, Geez.
[991.00 → 992.62] Let's go with OpenAI.
[993.42 → 995.72] I'm sure there's some interest out there.
[996.94 → 997.30] OpenAI.
[997.30 → 999.14] Is it in that number four slot?
[999.24 → 999.94] Survey says?
[1001.34 → 1002.98] No, it is not.
[1003.12 → 1005.68] I'm sorry, but you could not clear the board.
[1005.84 → 1010.84] And so now we have an opportunity to steal from CSS Podcast, and you guys can discuss.
[1010.96 → 1011.56] So what are you thinking?
[1012.82 → 1016.70] I'm thinking that this is a benefits-based answer, probably.
[1017.16 → 1018.42] That's kind of where my head's at.
[1018.60 → 1018.90] All right.
[1018.94 → 1021.76] I'm thinking about where everybody just left these big companies.
[1021.94 → 1022.76] Where did they all go?
[1022.76 → 1024.86] What was the number one spot?
[1024.92 → 1027.74] If you did work at Apple, Microsoft, Google, where'd you bounce?
[1028.58 → 1030.02] Who stole everyone recently?
[1030.56 → 1031.48] Apple fired no one.
[1032.54 → 1033.40] Apple fired no one.
[1033.46 → 1035.02] I think that's why they're on top, honestly.
[1035.22 → 1035.46] That's okay.
[1035.48 → 1036.20] Yeah, that might be.
[1036.64 → 1037.44] I think Shopify.
[1037.44 → 1040.40] You know, that's a good idea.
[1040.98 → 1042.30] What do you think of Spotify?
[1042.74 → 1043.76] That was also on my list.
[1043.90 → 1047.36] And the other one on my list here is Tercel, because they're so hot right now.
[1047.48 → 1050.06] Everyone's probably going to want to work there, and if compensation's good.
[1050.12 → 1052.24] But I wouldn't call that a big tech company.
[1052.70 → 1054.34] So this is hard.
[1054.44 → 1055.80] This is hard, because you only get one answer.
[1056.84 → 1058.78] I know a lot of great people that went to Shopify.
[1059.32 → 1060.66] I only know a couple that went to Spotify.
[1060.66 → 1063.62] But I can't say that they're doing better now than they were a year ago.
[1063.88 → 1064.60] I mean, nobody is.
[1066.12 → 1067.34] Not the people of the company.
[1067.86 → 1070.66] Spotify has those sweet, sweet benefits, just like Netflix.
[1070.96 → 1073.60] I think that people are thinking about the benefits with Netflix Answer, too.
[1074.04 → 1074.16] Yeah.
[1074.32 → 1075.84] Shopify was all stock, right?
[1075.90 → 1077.80] Because they're like the e-commerce backbone.
[1078.40 → 1079.50] Well, we're running out of time here.
[1079.56 → 1081.56] You're going to have to confer and pick one of these.
[1081.80 → 1083.24] All right, Adam, you pick.
[1084.00 → 1088.66] I'm going to say Shopify based on the stats of who and where.
[1088.86 → 1089.18] I don't know.
[1089.18 → 1089.78] Okay.
[1090.44 → 1095.36] For the steal and 61 additional points to add to your score, is Shopify number four?
[1097.10 → 1098.54] It is not.
[1099.28 → 1102.90] So we will award the 61 points to the key framers.
[1103.10 → 1103.32] To the none.
[1105.44 → 1106.64] Actually, I wrote self.
[1106.82 → 1108.16] I wrote myself on my thing.
[1108.24 → 1109.26] I should have remembered that, yeah.
[1109.84 → 1113.00] And I will say that you guys did not learn from last round, of course.
[1114.14 → 1116.02] 12 people said none.
[1116.52 → 1119.04] Should have sawed that one coming, but it's difficult.
[1119.60 → 1120.82] So three people said Amazon.
[1121.04 → 1122.12] Three people said Tercel.
[1122.54 → 1123.56] Three said Spotify.
[1124.18 → 1125.08] Three said Netflix.
[1125.40 → 1126.46] Two said Cloudflare.
[1126.68 → 1131.54] One said Adobe, presumably after they heard about Katy Perry's mushroom-filled fantasy land.
[1132.42 → 1135.42] And one said anyone that lets me write Ruby.
[1135.72 → 1138.48] And then one said the one with the least crazy CEO.
[1139.14 → 1141.56] So there are a few runners-up.
[1141.56 → 1145.24] I feel like there's one audience member that's really set on Ruby on Rails.
[1145.42 → 1146.16] I think so.
[1146.34 → 1147.04] For real, yeah.
[1147.38 → 1150.18] All the Ruby answers are coming in by one person.
[1150.48 → 1150.82] All right.
[1150.92 → 1153.54] So after two rounds, it's a tight game.
[1154.34 → 1158.20] CSS podcast with 80 key framers with 61.
[1158.46 → 1160.46] And we move now to round three.
[1160.46 → 1176.94] What's up, party people?
[1176.94 → 1180.94] This episode is brought to you by our new friends at Lolo Code.
[1181.34 → 1185.90] Lolo Code lets you build cloud-agnostic serverless apps that make it too easy to go from zero to one.
[1186.22 → 1189.80] If you're familiar with building serverless apps, you can think of Lolo Code as your backend,
[1190.18 → 1193.96] with a visual editor to let you think and build at the same time.
[1194.22 → 1195.30] No servers to worry about.
[1195.46 → 1196.90] This is serverless.
[1197.30 → 1200.82] And I'm here with Gabor NAD, software engineer at Lolo Code.
[1201.12 → 1201.56] Tell me, Gabor.
[1201.56 → 1203.32] What gets you excited about Lolo Code for developers?
[1203.96 → 1214.08] So Lolo Code is sort of all about the mentality of reducing the threshold and the pain of getting something from having an idea to actually having something in production.
[1214.38 → 1222.06] I think that a lot of developers that I know and that are out there know the sort of frustration of having an idea and wanting to prototype it.
[1222.24 → 1230.24] And it being a pretty difficult process of actually getting from, okay, I have an idea and actually having a stack, having code, having it deployed into a cloud or whatever.
[1230.24 → 1231.60] It takes quite a bit of work.
[1231.94 → 1237.10] And Lolo really focuses on minimizing the effort required for that process to actually take place.
[1237.40 → 1239.74] It's a low-code environment built for developers.
[1240.08 → 1246.42] So that actually means that you get to visualize the different nodes and the data flows between them in your application,
[1246.64 → 1251.36] which kind of makes the whole process of prototyping and the whole process of sketching out the architecture
[1251.36 → 1256.18] and getting a better understanding of what it is that you're actually building and how the whole thing functions
[1256.18 → 1259.82] much easier to understand while you're actually developing the application.
[1259.82 → 1265.78] So instead of having to spend hours with a whiteboard first, you can actually sit down and start sketching out your application
[1265.78 → 1271.32] by creating these nodes and creating these links between them while you're actually already doing the development work.
[1271.72 → 1272.04] Very cool.
[1272.12 → 1272.64] Thank you, Gabor.
[1272.94 → 1275.32] So Lolo Code is built for developers.
[1275.96 → 1276.90] Try it free today.
[1277.26 → 1278.40] No credit card required.
[1279.02 → 1280.82] Check them out at lolo.co.js party.
[1280.82 → 1284.82] Again, lolo.co.js party.
[1292.78 → 1295.36] Now, this round is a little bit different.
[1295.46 → 1297.30] We call this the inverted round.
[1297.56 → 1300.82] So we're just going to take turns team by team guessing responses.
[1300.82 → 1305.94] But the points at the bottom of the board are higher than the points at the top.
[1306.12 → 1311.66] So while you're trying to match the board, you're actually trying to match the least popular answer to get more points.
[1312.02 → 1318.96] The question that we asked our listeners, how many monitors do you use while coding?
[1319.12 → 1321.60] There are four responses on the board.
[1321.68 → 1326.24] And I will say the least popular response is worth the most points.
[1326.24 → 1326.28] Yes.
[1326.52 → 1328.90] So David and Shaw played the last round.
[1329.06 → 1331.16] Let's let Luna and Adam start this round.
[1331.24 → 1332.42] We're just going to go back and forth.
[1332.74 → 1333.72] And let's start with Luna.
[1333.90 → 1339.12] Go ahead and guess what you think people said when we asked them how many monitors they use while coding.
[1339.66 → 1343.10] Okay, so this is how many monitors they use, but the least popular answer.
[1343.36 → 1344.30] That's what you want to get.
[1344.40 → 1345.38] They're all worth points.
[1345.66 → 1349.50] So you can get the top score and get points, but you're going to get more points by getting the bottom score.
[1349.82 → 1351.16] Well, I know how many I use.
[1352.38 → 1354.66] I think what I want to go with is three.
[1354.66 → 1358.14] Like if they have two monitors and their laptop, that's going to hurt your neck.
[1358.20 → 1359.32] But I know people do it.
[1359.74 → 1361.34] So my answer is three.
[1361.54 → 1362.78] All right, show us three.
[1363.74 → 1368.30] Three is on the board, and it is in slot number three.
[1368.92 → 1369.22] Oh.
[1369.60 → 1374.20] 14 people use three monitors, which means you get 15 points for that response.
[1374.30 → 1375.18] I'll award those now.
[1375.64 → 1379.16] And now we'll go back to key framers and let's go to Shaw.
[1379.58 → 1381.66] How many monitors people use while coding?
[1382.12 → 1382.70] Let's see.
[1382.70 → 1392.48] If we're going the least popular, I'm going to say one is on there, but it's not going to be the top one.
[1392.80 → 1393.46] Show us one.
[1394.80 → 1398.06] Yes, one is on there and it's the number two response.
[1398.16 → 1399.44] So you get slightly fewer points.
[1399.52 → 1400.32] You still score 10.
[1400.84 → 1404.26] 35 people out of the 100 use one monitor.
[1404.36 → 1407.74] We'll award those points now and go back to CSS podcast.
[1408.10 → 1408.84] I'm team one.
[1408.84 → 1411.42] And we'll go to Adam.
[1411.66 → 1413.88] So we have one monitor is taken.
[1413.98 → 1414.96] Three monitors is taken.
[1415.08 → 1416.26] Those are the two and three slots.
[1416.38 → 1418.02] The one and the four are still available.
[1418.14 → 1420.68] Of course, the four is worth more than the one.
[1421.42 → 1421.84] What do you think?
[1422.14 → 1423.96] I'm going to go with the pattern we've seen.
[1424.30 → 1425.52] People are going to say none.
[1425.62 → 1426.32] They're going to reject it.
[1426.38 → 1426.78] I don't.
[1426.90 → 1428.40] So people say don't or none.
[1428.66 → 1429.48] They're just using their...
[1429.48 → 1430.68] No monitor coding.
[1431.00 → 1431.20] That's impressive.
[1431.20 → 1431.94] Just their laptop.
[1431.94 → 1433.60] I'm not using a monitor right now.
[1433.70 → 1434.24] Oh, yeah.
[1434.24 → 1434.76] So that's valid.
[1434.88 → 1434.98] Yeah.
[1435.06 → 1436.44] I'm assuming this is like...
[1436.44 → 1439.64] People are going to think of this as external monitors because it's impossible to...
[1439.64 → 1441.50] I guess it's not impossible to code without a monitor.
[1441.72 → 1443.78] But people are going to say none.
[1443.94 → 1445.16] Just whatever is built in or whatever.
[1445.26 → 1445.84] So that's my answer.
[1446.28 → 1446.62] Bold.
[1446.86 → 1447.52] Very bold.
[1448.24 → 1451.30] Did anybody say they code with no monitors?
[1452.60 → 1453.58] They sure did.
[1453.68 → 1454.60] One person.
[1454.74 → 1455.94] I mean, an assumption to the rule.
[1455.94 → 1456.16] Yes.
[1456.16 → 1457.38] Said zero monitors.
[1457.64 → 1461.22] And they said I am fully blind, and I do everything by touch.
[1461.22 → 1464.04] So they don't use a monitor because they can't see.
[1464.68 → 1465.46] Very cool.
[1465.68 → 1467.28] So you get 20 points for that.
[1467.74 → 1468.18] Congratulations.
[1468.68 → 1470.38] And the number one answer is still out there.
[1470.50 → 1471.28] So I'll award those.
[1471.36 → 1472.42] We'll go back to key framers.
[1472.86 → 1476.66] And we'll go to David for the last one out there.
[1477.02 → 1479.08] I think you can probably infer what it is.
[1479.26 → 1479.42] Yes.
[1479.42 → 1479.60] Two.
[1479.64 → 1479.90] Two.
[1480.14 → 1480.62] Yes.
[1480.66 → 1481.42] The number one answer.
[1481.50 → 1482.18] 16 monitors.
[1482.18 → 1482.72] Two monitors.
[1482.72 → 1482.94] Yes.
[1482.94 → 1483.30] 16.
[1483.62 → 1484.44] Two monitors.
[1485.08 → 1485.48] 50.
[1485.74 → 1488.84] Literally half of the people are using two monitors when they code.
[1488.94 → 1489.98] That's worth five points.
[1490.06 → 1490.80] We'll award those.
[1491.22 → 1493.96] And thus ends our inverted round.
[1494.10 → 1494.74] Good job, Adam.
[1494.88 → 1499.42] I didn't think anybody was going to get the zero on this one because it's so, so obscure.
[1499.74 → 1500.50] But there we go.
[1500.66 → 1500.92] All right.
[1500.94 → 1502.56] Let's head to round four.
[1504.92 → 1505.40] Okay.
[1505.70 → 1508.82] So beginning round four, we have key framers with 76.
[1509.28 → 1510.90] CSS podcast with 115.
[1511.50 → 1512.66] It's anybody's game.
[1512.78 → 1513.86] There's two more regular rounds.
[1513.96 → 1515.80] And then the last round is double points.
[1515.90 → 1518.94] So if you're behind, you have a big chance of coming back in round six.
[1518.94 → 1522.60] We asked 100 JS Party listeners to finish this sentence.
[1522.60 → 1525.50] I couldn't code without what?
[1525.64 → 1526.58] Without blank.
[1526.94 → 1528.68] We'll now have an interface off.
[1529.12 → 1532.32] We're back to David and Luna facing off.
[1532.48 → 1534.90] So Luna went first the first time, right?
[1535.04 → 1536.46] And we'll have David go first this time.
[1537.02 → 1539.16] David, there are six answers on the board.
[1539.72 → 1541.20] What couldn't people code without?
[1541.20 → 1546.64] I will say on this round and a few others, the responses vary but kind of mean the same thing.
[1546.72 → 1548.02] So we group in the categories.
[1548.20 → 1550.08] So if you hit a very specific thing, it's in a category.
[1550.22 → 1550.90] I'll let you know.
[1551.18 → 1552.78] And we won't count it as a guess.
[1553.30 → 1553.54] Okay.
[1553.66 → 1557.02] Well, I know that I can't code without coffee.
[1557.28 → 1558.94] I turned coffee into code.
[1559.34 → 1559.36] So.
[1559.54 → 1559.92] Okay.
[1559.98 → 1560.84] Show us coffee.
[1561.78 → 1562.66] It's on the board.
[1562.74 → 1563.52] Where is it on the board?
[1563.62 → 1566.78] It's at number four with 11 responses.
[1566.78 → 1570.58] So Luna does have a chance to match higher than that.
[1571.32 → 1573.52] What is something else that people can't code without?
[1574.14 → 1577.58] Continuing on the alliteration, I can't code without a computer.
[1578.10 → 1579.78] Without a computer.
[1579.96 → 1581.38] Taking it very literally.
[1581.68 → 1582.48] The math checks out.
[1583.32 → 1585.36] Did our audience take it as literally as that?
[1586.06 → 1587.16] They sure did.
[1587.26 → 1589.38] Number one answer was hardware.
[1589.74 → 1590.60] Whether it was a keyboard.
[1590.72 → 1591.46] People said keyboard.
[1591.62 → 1592.20] They said computer.
[1592.32 → 1594.84] They said electricity or internet.
[1594.84 → 1596.22] I was thinking electricity.
[1596.22 → 1598.08] We grouped all those together.
[1598.46 → 1600.58] And that's 23 people.
[1600.80 → 1603.74] So CSS podcast, you are playing this round.
[1603.92 → 1604.72] Adam, we go to you.
[1605.34 → 1606.86] There's still four slots open.
[1606.96 → 1608.64] What else can people not code without?
[1609.20 → 1609.40] Nice.
[1609.50 → 1610.38] We've crossed off a lot of my.
[1610.48 → 1613.38] Does a second monitor, is that in hardware?
[1613.60 → 1614.72] I kind of assume it would be.
[1615.00 → 1615.52] Second monitor.
[1615.60 → 1615.74] Yeah.
[1615.80 → 1617.00] Any sort of hardware is in there.
[1617.22 → 1618.90] Even no monitor is in there, I suppose.
[1619.40 → 1623.36] Knowing some of your listeners, I'm going to say TypeScript.
[1624.20 → 1625.28] Show us TypeScript.
[1626.78 → 1628.72] I'm happy to announce that that is incorrect.
[1629.40 → 1629.60] Yeah.
[1629.66 → 1630.80] I'm actually in the same boat.
[1630.90 → 1633.10] I don't need TypeScript, but I thought everyone else did.
[1633.26 → 1634.16] You've been overwhelmed.
[1634.64 → 1634.90] Yes.
[1635.06 → 1636.62] You've been influenced by Nick Geese.
[1636.90 → 1639.08] He's strong on the message, but no.
[1639.70 → 1641.20] We are out there still in force.
[1641.46 → 1643.24] Us regular JavaScript authors.
[1643.76 → 1644.08] All right.
[1644.12 → 1644.80] But that's a strike.
[1644.86 → 1645.46] So we go back to you.
[1645.46 → 1646.66] And now you got one strike against you.
[1646.96 → 1647.26] All right.
[1647.28 → 1648.80] I'm still on this literal train.
[1649.16 → 1651.92] I can't code without a text editor of some sort.
[1652.22 → 1653.22] Show us text editor.
[1653.22 → 1653.70] Yeah.
[1654.70 → 1655.10] Yeah.
[1655.22 → 1656.00] Number two answer.
[1656.20 → 1657.08] 22 responses.
[1657.98 → 1658.68] Some said editor.
[1659.00 → 1661.68] Some said specific editors like Vim, VS Code, et cetera.
[1661.84 → 1662.70] We put them all in one group.
[1663.44 → 1664.72] And that was number two.
[1664.84 → 1665.66] So we're back to Adam.
[1665.72 → 1666.30] One strike.
[1666.46 → 1669.72] You got half the board cleared, but it's still half up there.
[1669.80 → 1670.24] What do you think?
[1670.24 → 1672.60] It's getting tricky.
[1673.02 → 1673.84] You got this, Adam.
[1673.88 → 1677.58] I'd say hands, but you know, like, is that hardware?
[1679.66 → 1681.90] And I know that people can code without their hands, right?
[1681.94 → 1683.66] You're just like, no, I don't need hands to code.
[1683.74 → 1684.70] I'll code with my voice.
[1685.70 → 1688.50] You know, code in VR with your elbows or something.
[1688.60 → 1688.92] I don't know.
[1690.10 → 1692.18] I am going to say hands, fingers and hands.
[1692.36 → 1693.54] That's not grouped into hardware.
[1693.66 → 1694.78] I think that's kind of wetware.
[1694.86 → 1697.50] I don't know what kind of wear that is, but is it on there?
[1697.50 → 1699.92] Yes, it is.
[1700.00 → 1700.86] Oh, nice.
[1701.06 → 1702.18] Oh, I got lucky.
[1702.40 → 1703.00] Oh, man.
[1703.02 → 1704.34] I thought for sure I was going down.
[1704.62 → 1706.64] And it's in the general category of body parts.
[1706.94 → 1711.98] So this includes brains, hands, eyeballs, and other such things that you can't code without.
[1712.52 → 1713.30] At least some people cannot.
[1713.70 → 1713.94] All right.
[1714.00 → 1715.54] So that's still one strike.
[1715.62 → 1715.96] Back to you.
[1716.00 → 1717.50] Now we got two things left, three and six.
[1717.80 → 1718.22] All right.
[1718.22 → 1727.48] I'm thinking like people would probably say something like stack overflow or like a way to help them.
[1727.50 → 1728.22] Like get answers.
[1728.42 → 1730.12] So I'm going to say stack overflow.
[1730.42 → 1733.40] I don't know if that's been grouped into a larger section.
[1734.12 → 1737.48] Is stack overflow one of the things that people cannot code without?
[1738.52 → 1739.42] Yes, it is.
[1739.48 → 1741.52] And it's grouped into the generic thing of Google.
[1741.88 → 1744.32] Stack overflow, GitHub, web resources.
[1744.70 → 1745.02] Helpers.
[1745.24 → 1745.32] Yeah.
[1745.44 → 1746.10] 14 people.
[1746.28 → 1748.12] So the board is almost cleared.
[1748.18 → 1749.10] You got five of six.
[1749.20 → 1750.70] The last one is still on there.
[1751.24 → 1753.30] 76 points awarded so far.
[1753.46 → 1754.40] And one strike.
[1754.44 → 1755.80] He got two guesses at number six.
[1755.80 → 1756.56] Back to Adam.
[1757.22 → 1757.58] Okay.
[1757.68 → 1764.06] There are some silly ones on here, but I feel like another silly one is sitting there at number six.
[1764.54 → 1767.08] I could go really heady, you know, like purpose.
[1767.26 → 1770.24] But I don't think your audience people were like, I can only code with purpose.
[1770.36 → 1771.56] What are you trying to say about our audience?
[1771.70 → 1772.46] They don't have purpose.
[1772.46 → 1776.70] I'm a user-centric engineer.
[1776.88 → 1781.38] So for me, I'd be like, I can't code unless there's a user because otherwise I'm just coding into the ether.
[1781.56 → 1784.02] But again, heady, don't think anyone else is going to say that.
[1784.10 → 1785.42] It's a very Adam thing to say.
[1785.88 → 1786.82] You could be your own user.
[1787.46 → 1788.38] I could be my own user.
[1789.60 → 1795.14] I'm going to go with the only other thing on my list that maybe makes sense, which is funding, money, money.
[1795.38 → 1797.20] So you have to give me stuff to do this.
[1797.24 → 1799.20] I'm not going to do this for greenish.
[1799.20 → 1800.08] That's a good answer.
[1800.30 → 1800.42] Yeah.
[1800.70 → 1801.32] Compensation maybe.
[1801.40 → 1802.08] Show us compensation.
[1803.90 → 1805.04] Sorry, not on there.
[1805.46 → 1805.82] Compensation.
[1806.12 → 1807.08] I thought it was a good try.
[1807.22 → 1807.90] It was a good guess.
[1808.34 → 1810.16] But, you know, some of us just code for the love.
[1810.82 → 1811.44] Two strikes.
[1811.80 → 1812.36] That's true.
[1812.52 → 1812.96] Two strikes.
[1813.08 → 1813.78] Luna, back to you.
[1814.08 → 1815.22] I lose money when I code.
[1816.44 → 1817.64] That happens as well.
[1818.40 → 1819.18] Time is money.
[1821.00 → 1822.52] I don't think I have a better answer.
[1822.52 → 1829.24] But the place my mind went was, like, what are your physical needs when you're doing any task?
[1829.42 → 1831.14] And sleep is one of them.
[1831.34 → 1834.44] So maybe I can't code if I'm sleep-deprived.
[1834.50 → 1835.16] I need my sleep.
[1835.82 → 1836.80] Show us sleep.
[1838.76 → 1839.54] I'm sorry.
[1839.70 → 1841.72] Sleep is not on the list.
[1841.78 → 1845.42] But this provides opportunity to the key framers to get back in the game here.
[1845.96 → 1847.18] Lots of points to steal.
[1847.26 → 1847.70] We turn to you.
[1847.72 → 1848.46] You can discuss.
[1848.56 → 1849.34] It's number six.
[1849.34 → 1851.04] So not very many people said it.
[1851.50 → 1853.02] In fact, five said it.
[1853.12 → 1854.26] But what do you think they said?
[1854.32 → 1855.26] What was that last response?
[1855.34 → 1855.86] Go ahead and discuss.
[1856.60 → 1863.90] So, Shaw, one recent trend that's been all over Twitter and the Internets has been AI.
[1864.30 → 1865.14] ChatGPT.
[1865.58 → 1872.46] And I know that personally, I rely on it like a good bunch to do coding.
[1872.98 → 1873.38] Yeah.
[1873.78 → 1876.38] I think that's good.
[1876.38 → 1880.84] I don't know that the audience will be fully on that train.
[1881.16 → 1882.10] Don't underestimate me then.
[1883.38 → 1886.32] So, none is a possibility here.
[1886.60 → 1887.32] I couldn't code with no.
[1887.32 → 1888.38] That's always a possibility.
[1888.84 → 1888.96] Yeah.
[1889.18 → 1890.66] I reject your premise, sir.
[1890.92 → 1891.16] Yes.
[1891.42 → 1893.40] There's at least one response that's Ruby on Rails.
[1893.84 → 1894.40] Yeah.
[1894.74 → 1895.34] For sure.
[1895.78 → 1896.82] That's true.
[1896.82 → 1904.30] But a more realistic answer is probably like source control, like Git, that kind of thing.
[1905.00 → 1907.58] Or open source, like NPM.
[1908.42 → 1908.90] Hmm.
[1909.34 → 1912.20] So, we got AI on one hand and open source.
[1912.36 → 1913.66] Where do you think our audience is going?
[1914.12 → 1921.16] I feel like, you know, when asked this question, like a lot, I don't know, I'm still stuck on the ChatGPT thing.
[1921.50 → 1923.06] Or, you know, just, sorry, co-pilot.
[1923.36 → 1923.86] That's what I meant.
[1924.16 → 1924.42] All right.
[1924.42 → 1925.94] Let's go with it.
[1926.20 → 1928.02] Now, a quick metagame here.
[1928.32 → 1930.24] You know what if one of you is right and the other one is wrong?
[1930.32 → 1933.02] How are we going to feel that we go with one and not the other?
[1933.10 → 1934.60] Is this going to tear up the key framers?
[1934.66 → 1935.94] Just half the points.
[1936.20 → 1938.00] Could this be the end of the key framers as we know it?
[1938.14 → 1938.30] You know?
[1939.06 → 1941.64] The behind the band, you know, years from now.
[1941.80 → 1944.82] Like, what happened was this answer on Front End Feud?
[1945.16 → 1946.42] Well, let's see what it is here.
[1946.52 → 1948.82] You said GitHub.co-pilot.com slash AI helpers.
[1949.30 → 1950.78] Did our audience say that?
[1952.46 → 1953.92] I'm sorry, but they did not.
[1953.92 → 1954.44] Oh, man.
[1954.62 → 1955.36] I'm so sorry.
[1955.74 → 1959.16] But in order to keep the band together, I'll say Shaw was also wrong.
[1959.74 → 1964.30] And the correct answer, well, let's award these points here to CSS Pod.
[1964.70 → 1965.48] Terminal, right?
[1965.52 → 1969.74] And the correct answer was peace and quiet and muting all the things.
[1970.48 → 1971.80] And so they need to have quiet.
[1972.06 → 1972.36] Space.
[1972.48 → 1973.08] They need a space.
[1973.10 → 1975.40] So Luna was in the ballpark with her physical needs.
[1975.78 → 1978.62] Your sleep was a little bit outside what they were saying.
[1978.62 → 1979.84] Now, there were other responses.
[1979.84 → 1981.84] I guess you have peace when you're sleeping.
[1981.98 → 1982.46] Come on.
[1983.94 → 1985.10] You still got the points.
[1985.66 → 1986.06] You got the points.
[1986.06 → 1988.20] Just kidding.
[1988.42 → 1990.22] I thought that source control was a very good answer.
[1990.66 → 1991.56] I did, too, as well.
[1991.76 → 1993.44] Like, tooling in general, you would think.
[1993.78 → 1995.64] Although, editor's kind of on the fringe of that.
[1995.64 → 2000.40] But one person said patience and stubbornness, which I thought was funny because we asked for one thing.
[2001.20 → 2003.90] One person said wasting 50% of my time on meetings.
[2004.20 → 2005.26] And so they were pretty sour.
[2005.76 → 2007.10] And then talk about literal.
[2007.32 → 2012.20] The one thing I can't code without are the letters C, O, D, and E.
[2012.58 → 2014.90] So that was a snarky response, I thought.
[2015.60 → 2015.88] Okay.
[2016.42 → 2016.56] Wow.
[2016.56 → 2016.78] Yeah.
[2017.24 → 2018.76] So thanks, guys.
[2019.62 → 2019.94] All right.
[2019.98 → 2021.34] So thus ends round four.
[2021.66 → 2023.44] I'm surprised no one said programming languages.
[2023.88 → 2025.08] And there was no Ruby on Rails.
[2025.08 → 2029.88] So while it was a good guess, they got sick of answering that particular thing.
[2030.52 → 2034.14] After four rounds, we have CSS Podcast pulling away a little bit.
[2034.24 → 2037.64] It's still in play, but it's 191 to 76.
[2038.48 → 2040.12] Let's move to round five.
[2042.54 → 2043.34] All right.
[2043.80 → 2047.12] Oh, and it turns out, I forgot this, but round five is also inverted.
[2047.40 → 2050.30] So this will be just like round three, where we go back and forth.
[2050.38 → 2052.14] You're trying to match the bottom of the board.
[2052.14 → 2059.46] And the phrase they're matching against is my primary web browser is blank.
[2060.30 → 2062.34] My primary web browser is blank.
[2062.46 → 2064.06] Let's start with the key framers this time.
[2064.78 → 2065.68] And David.
[2066.10 → 2066.44] All right.
[2066.50 → 2068.24] The hot new one is ARC.
[2068.64 → 2070.78] I feel like there's a couple of people who've answered that.
[2070.94 → 2071.36] Okay.
[2071.88 → 2072.86] It is a great browser.
[2072.86 → 2073.66] Show us ARC.
[2074.88 → 2076.00] You are correct, sir.
[2076.12 → 2077.50] And it's near the bottom of the list.
[2077.58 → 2078.38] Number four.
[2079.00 → 2080.62] So you're awarded 20 points for that.
[2081.68 → 2082.68] Very nice answer.
[2082.76 → 2085.22] Now we go over to CSS pod, Luna.
[2085.86 → 2087.18] I'm just going to say Chrome.
[2087.46 → 2088.80] She's taking the easy points.
[2088.92 → 2089.60] Is Chrome on there?
[2089.68 → 2090.60] Of course it is.
[2090.72 → 2091.86] And it is number one.
[2091.86 → 2094.50] So you get five points.
[2095.02 → 2096.24] Back to key framers and Shaw.
[2096.40 → 2098.02] Oh, I didn't realize this was an inverted one.
[2098.10 → 2098.40] My bad.
[2099.14 → 2100.08] That was my fault.
[2100.26 → 2101.52] I thought it was a normal one.
[2101.86 → 2103.04] Five points is five points.
[2103.30 → 2105.08] I'm going to go Safari.
[2105.78 → 2107.56] I think that's probably toward the bottom.
[2107.70 → 2108.64] Show us Safari.
[2110.40 → 2110.76] Yes.
[2110.82 → 2113.04] It is the worst answer, which makes it the best answer.
[2113.46 → 2113.86] Yes.
[2114.06 → 2114.82] Six people.
[2115.06 → 2116.22] 25 points.
[2116.90 → 2118.00] I'm going to award those to you.
[2118.62 → 2119.60] The plot thickens.
[2119.60 → 2120.40] Adam, we're over to you.
[2120.48 → 2121.70] Two and three are still on the board.
[2122.20 → 2122.34] Yeah.
[2122.44 → 2122.78] Firefox.
[2124.04 → 2125.38] Firefox is on there.
[2126.24 → 2127.12] Number two.
[2127.56 → 2129.36] Ten points awarded to you.
[2129.98 → 2132.22] And key framers, can they swipe up?
[2132.32 → 2132.82] What's the word?
[2133.10 → 2133.56] Swoop up?
[2133.74 → 2134.22] Sweep up.
[2134.36 → 2134.90] That's the word.
[2135.00 → 2137.70] Can they sweep up these last 15 points?
[2138.14 → 2138.60] David's turn.
[2140.08 → 2141.04] What's in the middle?
[2141.88 → 2144.00] I mean, I have two good answers.
[2144.12 → 2144.92] One of them is silly.
[2145.02 → 2146.34] One of them is more realistic.
[2148.14 → 2149.88] But considering the audience,
[2149.88 → 2153.28] I'm going to say people gave a joke answer of Internet Explorer.
[2154.06 → 2155.82] That's a very interesting guess.
[2155.90 → 2156.68] Is it on there?
[2157.94 → 2158.30] No.
[2158.52 → 2159.62] They took this one seriously.
[2159.94 → 2162.96] You had the exact wrong time to go jokey.
[2163.34 → 2163.50] Luna.
[2163.94 → 2165.90] Oh, Microsoft Edge.
[2166.48 → 2166.74] Yep.
[2166.74 → 2168.78] The other one from Microsoft.
[2169.12 → 2170.24] Microsoft Edge.
[2171.82 → 2172.28] Oh.
[2172.70 → 2174.62] Not on the list.
[2175.26 → 2177.04] Back to key framers with Shaw.
[2177.24 → 2177.90] Come on, Shaw.
[2177.90 → 2183.30] Man, the only other one on my list right now is Brave.
[2183.54 → 2187.70] Given the tech audience, that seems to be a go-to.
[2188.64 → 2189.36] Is it on there?
[2189.60 → 2190.56] Show us Brave.
[2191.70 → 2192.22] Strong.
[2192.30 → 2192.92] Yes, it is.
[2192.96 → 2193.56] You found it.
[2193.56 → 2193.86] Nice.
[2193.86 → 2194.40] Number three.
[2194.56 → 2197.42] 16 people using Brave worth 15 points.
[2198.22 → 2200.16] And that concludes round five.
[2200.28 → 2201.48] Hey, it's a tight game.
[2201.60 → 2206.62] We have key framers with 136 CSS podcast with 206.
[2207.12 → 2208.28] There were a couple other answers.
[2208.38 → 2209.58] So four people said Edge.
[2209.96 → 2211.44] Two with Vivaldi.
[2211.92 → 2213.02] That's less than Safari.
[2213.18 → 2213.92] Should have been more points.
[2214.64 → 2215.72] Yeah, but it didn't make the top.
[2215.98 → 2216.42] Like it wasn't.
[2216.52 → 2217.88] It didn't have the requisite five.
[2218.26 → 2219.08] It's tricky.
[2219.26 → 2219.38] Wow.
[2219.38 → 2222.18] And there's one lonely opera user.
[2222.56 → 2223.22] Hi, opera user.
[2223.52 → 2223.88] Oh.
[2224.06 → 2224.32] Oh.
[2248.50 → 2249.08] Hey there.
[2249.08 → 2250.32] It's K-Ball from JS Party.
[2250.40 → 2253.10] And I want to talk to you about a new service I'm offering for engineers.
[2253.50 → 2257.68] As you advance from junior to senior to staff engineer or move into management, there comes
[2257.68 → 2261.32] a point where the skills that got you to where you are not enough to keep you moving
[2261.32 → 2261.70] forward.
[2261.96 → 2265.42] Where the answer to your question isn't on Stack Overflow because your problem has more
[2265.42 → 2268.60] to do with people and how to get them to make the right choices than about writing code.
[2269.14 → 2269.54] Congratulations.
[2270.02 → 2272.14] You've reached the border to becoming an engineering leader.
[2272.56 → 2275.92] If you're lucky, when you hit this point, you have a manager or senior peer that can help
[2275.92 → 2277.14] guide you through the transition.
[2277.14 → 2278.74] But most of us aren't that lucky.
[2278.94 → 2279.84] And that's where I want to help.
[2280.32 → 2283.76] Coaching engineers through the transition to becoming engineering leaders was the most
[2283.76 → 2285.28] satisfying part of my last job.
[2285.42 → 2287.30] And now I'm offering it as a paid service.
[2287.72 → 2291.20] Now, you may have never worked with a coach before, and you're not sure what it would look
[2291.20 → 2291.36] like.
[2291.48 → 2292.00] I get it.
[2292.14 → 2295.92] That's why I'm offering free exploratory sessions to try it out, learn what it's like
[2295.92 → 2297.64] and work through a challenge you're facing right now.
[2297.64 → 2302.28] So if you're curious, or you're feeling stuck, head over to ball.LLC slash coaching.
[2302.44 → 2305.44] You can learn more about what I'm offering and sign up for your free exploratory session.
[2305.74 → 2308.72] That's ball.LLC slash coaching.
[2308.72 → 2328.58] We now go to our final round and this one has twice as many points on the board.
[2330.92 → 2331.96] I love that music.
[2332.22 → 2332.62] Thank you.
[2332.62 → 2335.50] So round six, the final round, double score.
[2336.16 → 2337.88] We'll go back to our interface off.
[2337.92 → 2339.68] This time it'll be Shaw versus Adam.
[2340.54 → 2344.06] And please remind me who went first the first time so I can be fair.
[2344.42 → 2345.08] Was it you, Shaw?
[2345.22 → 2346.50] I think it was me.
[2347.20 → 2347.50] Okay.
[2347.96 → 2348.56] Does that sound right?
[2348.70 → 2349.36] I don't know.
[2349.54 → 2350.60] It was so long ago.
[2351.78 → 2354.80] Well, let's just assume you're correct and go with Adam.
[2354.80 → 2361.74] So the question, what one word sums up why you make software?
[2361.84 → 2364.68] And I'll say this is another one where we end up grouping some words together.
[2364.90 → 2366.58] That meant very similar things.
[2366.64 → 2368.38] But there are six answers on the board.
[2369.26 → 2370.12] It's anybody's game.
[2370.24 → 2373.38] Probably whoever wins this round wins this edition of Front of Feud.
[2373.44 → 2375.18] So no pressure, Adam, but you're up.
[2375.94 → 2378.78] Thank you for that no pressure warning.
[2379.04 → 2379.70] You're welcome.
[2380.12 → 2380.36] Okay.
[2380.40 → 2382.86] I'm just going to say it's for the love.
[2383.36 → 2384.68] It's not a maybe it's in the middle.
[2384.80 → 2385.10] I don't know.
[2385.26 → 2385.52] Love.
[2386.40 → 2386.72] Passion.
[2387.16 → 2387.36] You know?
[2387.42 → 2388.26] Show us love.
[2389.96 → 2390.62] I'm sorry.
[2391.12 → 2391.58] I'm alone.
[2391.84 → 2392.88] I'm alone in that, apparently.
[2393.24 → 2393.86] That hurts.
[2394.82 → 2395.42] No love.
[2395.66 → 2396.86] There's no love on this board.
[2398.02 → 2400.56] Shaw, that means it's wide open for you to take the round.
[2401.22 → 2401.58] Yeah.
[2401.68 → 2403.30] The opposite of love, money.
[2403.72 → 2405.40] I'm going to say is on there.
[2405.84 → 2406.58] Well played.
[2406.68 → 2407.26] Show us money.
[2408.14 → 2408.50] Yep.
[2408.50 → 2409.38] That one's on there.
[2409.50 → 2411.58] And it is in slot number two.
[2411.92 → 2412.06] Two.
[2412.52 → 2412.74] Wow.
[2412.74 → 2415.98] 15 people responded, which is worth 30 points.
[2416.18 → 2417.46] And you now take the board.
[2417.68 → 2419.04] So key framers will play this round.
[2419.54 → 2420.56] Number two is taken.
[2420.78 → 2422.70] One, three, four, five, and six are still out there.
[2422.80 → 2423.68] David, what do you think?
[2424.26 → 2427.26] For fun, enjoyment, pleasure, fun.
[2427.62 → 2431.92] Fun, enjoyment, pleasure, but notably not love, but fun.
[2432.08 → 2432.14] No.
[2432.58 → 2433.54] Is fun on there?
[2434.50 → 2435.80] Oh, number one answer.
[2436.70 → 2437.14] Yes.
[2437.26 → 2437.64] Joy.
[2437.96 → 2438.38] Fun.
[2439.04 → 2439.40] Enjoyment.
[2439.98 → 2440.62] Very good.
[2440.78 → 2441.00] Okay.
[2441.06 → 2441.74] One and two are gone.
[2441.82 → 2442.48] Shaw, back to you.
[2442.98 → 2445.54] To solve a problem, fulfill a need.
[2446.24 → 2449.04] Your second phrase kind of ruined it for me.
[2449.74 → 2450.86] Do I give it to him anyway?
[2451.18 → 2451.86] It's close.
[2452.64 → 2453.00] Yes.
[2453.14 → 2453.64] I'll give it to you.
[2454.82 → 2458.54] Number three was puzzles, challenges, and problem-solving.
[2459.50 → 2464.76] To fill a need was kind of like maybe moving beyond the whole challenge of it, but I'll give it to you.
[2464.86 → 2466.36] No, you need to solve a problem.
[2466.64 → 2467.18] Makes sense.
[2467.18 → 2467.66] Fair enough.
[2467.78 → 2468.14] Fair enough.
[2468.22 → 2472.64] Well, like I need some piece of software to do X, Y, Z, so I write it.
[2472.72 → 2473.00] Right.
[2474.12 → 2475.40] Yeah, see, that's further away.
[2475.52 → 2479.78] I think these people are thinking like the puzzle aspect, like the challenge of us.
[2480.30 → 2483.44] But you got problem-solving that's like literally in the list.
[2483.58 → 2484.32] I gave it to you.
[2484.44 → 2485.08] You're good to go.
[2485.58 → 2488.14] One through three, you have four through six on the board.
[2488.42 → 2489.16] No strikes yet.
[2489.24 → 2490.04] So, David, you're up.
[2490.04 → 2496.90] I know a lot of people, like besides it being a job, a lot of people just like automating stuff.
[2497.34 → 2498.92] So, I would say for automation.
[2499.38 → 2500.16] Show us automation.
[2500.16 → 2506.18] Ah, there were a couple that agreed with you, but not enough to make the board.
[2506.28 → 2507.32] So, there's your first strike.
[2507.58 → 2509.26] It's getting pressure filled at this point.
[2509.50 → 2511.22] You need three more to take the game.
[2511.58 → 2512.20] So, Shaw.
[2512.62 → 2513.48] Ah, Geez.
[2514.12 → 2516.10] So, it's one word, too.
[2516.26 → 2518.64] That makes things tricky.
[2519.94 → 2521.52] Like to help.
[2522.10 → 2523.24] Like helping others.
[2523.86 → 2524.86] That's two words, but.
[2525.52 → 2526.42] Show me help.
[2529.62 → 2531.76] Sorry, but help is not on there.
[2531.82 → 2532.90] Now, we're down to two strikes.
[2533.02 → 2534.14] We have one more guess.
[2534.24 → 2534.94] Three on the board.
[2535.08 → 2536.98] So, your back's up against it.
[2537.06 → 2537.96] But you can still do this.
[2538.04 → 2538.64] David, what do you think?
[2539.10 → 2539.46] Okay.
[2539.70 → 2541.88] So, some stuff is why you make software.
[2542.18 → 2543.14] You could do it for a job.
[2543.14 → 2544.10] You could do it for money.
[2545.32 → 2548.78] As a puzzle, I make software to.
[2549.96 → 2550.70] You know what?
[2551.02 → 2554.94] For which this is sort of a silly answer, but for fame.
[2555.22 → 2557.00] People want to, you know, be known.
[2558.66 → 2559.78] For the fame.
[2560.24 → 2562.40] Do JS Party listeners want the fame?
[2562.50 → 2563.02] Let's see it.
[2564.88 → 2567.94] I'm sorry, but they did not say fame.
[2568.14 → 2569.00] Pretty good guess.
[2569.52 → 2572.92] We have the steal available to you guys over there at the CSS pod.
[2572.92 → 2574.08] To retain your championship.
[2574.26 → 2576.40] You got three opportunities to drill it.
[2576.44 → 2576.80] What are you thinking?
[2577.22 → 2578.10] Oh, this is hard.
[2578.20 → 2580.26] I'm so glad they said a few that were on my list.
[2580.48 → 2582.66] Like, David, you and I were on the same page.
[2582.78 → 2584.14] And I was like, oh, they're going to win.
[2584.22 → 2585.10] And then I was like, oh.
[2585.30 → 2587.38] I expected more people to say automation for sure.
[2587.48 → 2587.62] Yeah.
[2587.68 → 2588.98] Automation was definitely on mine.
[2588.98 → 2589.60] Mm-hmm.
[2589.96 → 2592.10] So on mine, I have told a story.
[2592.82 → 2594.20] And I have loss.
[2594.32 → 2598.22] Just for the loss, I do it for the because I'm trying to think of what silly stuff people
[2598.22 → 2599.14] put in this, you know?
[2599.20 → 2601.26] I think that's the first one, the joy fun.
[2601.48 → 2601.68] Yeah.
[2601.70 → 2603.02] I would group that under joy.
[2603.66 → 2605.22] So that just leaves me telling a story.
[2605.38 → 2606.56] And that's, yeah.
[2606.72 → 2608.38] I don't know.
[2608.46 → 2609.20] This is a tough one.
[2610.32 → 2611.72] Because you got, yeah, ends meet.
[2611.90 → 2612.98] You know, you're just like making money.
[2613.08 → 2614.10] You got job security.
[2614.10 → 2618.32] So it's not like that one kind of wraps up, you know, family security or whatever.
[2618.44 → 2620.54] Like, I write software because it's like a stable tech job.
[2621.30 → 2622.00] Oh, maybe that's it.
[2622.08 → 2622.56] It's stable.
[2623.14 → 2624.92] Software is perceptively stable.
[2625.32 → 2625.56] I don't know.
[2625.84 → 2626.40] What do you think, Luna?
[2626.70 → 2628.14] Are we allowed to talk on this one?
[2628.26 → 2628.46] Yeah.
[2628.76 → 2629.36] This is a steal.
[2629.44 → 2630.54] Oh, I wasn't sure.
[2630.74 → 2631.00] Okay.
[2631.50 → 2634.42] I have some thoughts.
[2634.78 → 2637.52] I mean, my first thought is like, you know, the money, the benefits.
[2638.02 → 2639.76] That's probably included in the job.
[2640.16 → 2641.08] All those reasons.
[2641.08 → 2647.18] I also think like the impact of making software, you know, reaching people, kind of making a difference.
[2647.36 → 2654.10] Like the way that you can work on something that a lot of people use, it feels like there's purpose to it.
[2654.28 → 2654.40] Yeah.
[2654.42 → 2656.38] I'm wondering if that's in problem-solving.
[2656.56 → 2659.22] I was thinking the same thing, but I didn't know.
[2659.26 → 2662.94] But I don't think it is because the way Jared responded to that answer.
[2663.00 → 2663.96] Are you trying to read my eyes?
[2664.24 → 2664.48] Yeah.
[2665.78 → 2666.60] I'm over here.
[2666.78 → 2667.42] I'm on Reddit.
[2667.58 → 2668.82] So I'm not sure what you guys are talking about.
[2668.82 → 2677.02] I think that the logic aspect of it is like the challenge, but the impact aspect of it is like, why do you do that?
[2677.14 → 2678.12] Impact is a good one.
[2678.46 → 2678.60] Yeah.
[2678.78 → 2679.06] All right.
[2679.10 → 2679.84] Should we go with that?
[2680.48 → 2680.76] Yeah.
[2681.28 → 2682.94] Impact, making a difference.
[2683.74 → 2684.00] Okay.
[2684.08 → 2687.92] So to set the stage, we have key framers 136, CSS podcast 206.
[2688.10 → 2690.48] These points are theirs unless you can steal it.
[2690.92 → 2692.54] You have three opportunities on the board.
[2692.54 → 2694.62] You guessed impact.
[2694.76 → 2697.90] We've already had joy, money, puzzles.
[2698.50 → 2700.24] What else could be possibly on there?
[2700.36 → 2701.76] Is impact on the board?
[2704.40 → 2705.78] Yes, it is.
[2706.00 → 2709.34] It's grouped into satisfaction, accomplishment, and impact.
[2709.70 → 2711.10] So six people said that.
[2711.20 → 2712.10] That's 12 points.
[2712.20 → 2713.10] That's a steal.
[2713.28 → 2714.40] That's all the points.
[2714.66 → 2719.52] And once again, the CSS podcast defended this time their championship.
[2719.68 → 2720.26] You are the winner.
[2720.34 → 2721.32] Once again, congratulations.
[2721.32 → 2722.72] That made an impact, Luna.
[2722.92 → 2723.50] Well done.
[2730.04 → 2732.74] Let's clear the rest of this board just for the lulls.
[2732.82 → 2735.24] Number four was creativity.
[2735.36 → 2735.80] Oh, nice.
[2735.84 → 2736.04] Okay.
[2736.20 → 2737.36] Or craft or hobby.
[2737.46 → 2738.72] They do it as a hobby.
[2739.28 → 2740.72] Sometimes you're like, isn't that fun?
[2740.88 → 2742.58] Yeah, but they said the word hobby, not the word fun.
[2742.66 → 2744.68] So trying to keep some separate categories there.
[2744.90 → 2748.50] Number five, curiosity and interest.
[2748.50 → 2749.06] Huh.
[2749.60 → 2754.02] Again, somewhat related to problem-solving and challenges, but they were using these words.
[2754.52 → 2756.54] And so we let them stand on their own two feet.
[2756.62 → 2757.20] A couple other.
[2757.62 → 2758.84] Four people said love, Adam.
[2758.98 → 2759.46] Four people.
[2759.66 → 2760.32] So you were close.
[2760.46 → 2760.72] That's cool.
[2761.38 → 2765.36] Two people said passion, which maybe you could put in with love and make a category, but I didn't.
[2765.88 → 2767.14] Two people love the magic.
[2767.72 → 2769.04] That all feels like it goes together.
[2769.16 → 2770.10] One said laziness.
[2770.10 → 2771.24] Magic, love, passion.
[2771.24 → 2772.98] Yeah, laziness and automation.
[2773.34 → 2775.02] And of course, stubbornness is back.
[2775.24 → 2777.48] Our stubbornness answer reoccurs.
[2777.92 → 2780.90] So that rounds out our game.
[2781.04 → 2785.30] So at the end of six rounds, CSS Podcast 3.12, Key framers, you guys played a heck of a game.
[2785.36 → 2786.74] It came down to it at the very end.
[2786.92 → 2790.02] But at the end of the day, CSS Pod champs once again.
[2790.28 → 2790.68] Congrats.
[2790.98 → 2791.38] Great job.
[2791.56 → 2793.30] Good job, Sean, David.
[2793.66 → 2794.28] You killed it.
[2794.32 → 2794.66] Thank you.
[2795.32 → 2796.14] We won't be bitter.
[2796.14 → 2798.56] I still like your source control answer.
[2800.10 → 2800.68] Thank you.
[2800.86 → 2802.68] This audience just needs to get on board.
[2803.08 → 2803.40] They do.
[2803.60 → 2804.12] They really do.
[2804.30 → 2805.30] Especially the Ruby guy.
[2805.68 → 2806.28] The Ruby guy.
[2806.40 → 2807.64] Come on, Ruby guy.
[2807.80 → 2810.22] Well, I couldn't remember any run times at the beginning of this.
[2811.54 → 2812.48] I was stuck.
[2812.88 → 2813.52] That was tough.
[2813.86 → 2819.32] So at the end of the Super Bowl, they interview the winning team, and they ask them very heartfelt questions.
[2819.48 → 2821.66] And so I will do that now with Una and Adam.
[2822.00 → 2824.08] Adam, you put your heart out there today.
[2824.08 → 2826.32] You had some silly answers.
[2826.52 → 2828.76] You had some sarcastic ones that really hit.
[2829.32 → 2832.98] I felt like you really reverberated with our audience, if that's even the right word, which it's not.
[2833.66 → 2837.26] What was your emotion when you realized that this final answer was correct?
[2837.40 → 2838.18] What did you feel out there?
[2838.58 → 2839.16] Thanks, Jared.
[2839.26 → 2842.72] When I came into that final question, I was listening to Una.
[2842.94 → 2845.22] I was listening to all the options and I really just had to internalize it.
[2845.84 → 2846.92] That's me sipping Gatorade.
[2848.34 → 2849.02] But you know what?
[2849.02 → 2850.46] As soon as she said impact, I knew it.
[2850.52 → 2851.36] I felt it to my core.
[2851.54 → 2852.48] It was just so obvious.
[2852.48 → 2854.28] And so we went with that and then we won.
[2854.40 → 2854.88] Oh, yeah.
[2857.08 → 2858.68] I love Adam's football voice.
[2858.80 → 2859.92] Oh, he left the screen.
[2859.92 → 2860.28] He's gone.
[2860.28 → 2860.96] He's out of the frame.
[2860.96 → 2861.18] He's going to the end.
[2861.54 → 2861.76] Yeah.
[2862.96 → 2866.06] Una, you know, at the end there, we thought we had maybe a fumble.
[2866.24 → 2867.64] You didn't realize you could even talk.
[2867.88 → 2868.84] And so Adam's over there.
[2868.88 → 2869.78] You left him on an island.
[2870.00 → 2870.86] You know, no communication.
[2871.70 → 2873.20] He's fumbling and bumbling.
[2873.34 → 2874.78] He's saying things that don't make any sense.
[2874.86 → 2878.64] And then out of nowhere, at the very end, you swoop in and you bring your logic and reasoning.
[2878.64 → 2880.94] Like, what motivated you to swoop in at the end there?
[2881.38 → 2882.80] Well, I got to say, it's a team effort.
[2882.90 → 2886.12] I wanted to make sure my teammate had a platform, was able to get out, was on his mind.
[2886.22 → 2889.24] And honestly, I was just being a little silly at that moment.
[2889.60 → 2890.32] But here we are.
[2890.52 → 2892.32] All that matters is we made it in the end.
[2892.56 → 2893.78] We made it in the end, my friend.
[2894.20 → 2895.16] We ended up on top.
[2895.16 → 2895.88] She says, fun.
[2897.24 → 2897.52] Woo!
[2899.72 → 2900.32] I'm in a chair.
[2900.38 → 2900.78] I can't run.
[2900.78 → 2902.88] Very good.
[2903.12 → 2905.18] Well, I'd ask you what you were going to do with the winnings.
[2905.28 → 2908.32] But of course, there aren't any because this is a silly game show.
[2908.34 → 2909.04] We're going to Disneyland.
[2909.44 → 2911.04] Made by silly people on a silly podcast.
[2911.14 → 2911.88] Oh, we're not going to Disneyland?
[2912.18 → 2913.64] You can go to Disneyland if you like.
[2914.36 → 2919.34] It's just going to cost you quite a bit, I believe, as it's a hot place to travel these days.
[2919.50 → 2922.14] Well, Key framer guys, thanks so much for playing.
[2922.26 → 2924.30] David and Shaw, you were a valiant effort.
[2924.44 → 2925.52] We really appreciate that.
[2926.04 → 2930.12] Of course, CSS Podcast, you're invited back to defend your championship.
[2930.12 → 2935.54] The next time, as we asked 30 questions on this survey, and we only used six.
[2935.62 → 2938.98] So we have a lot left in the barrel, so to speak.
[2939.30 → 2942.24] And we don't have to nag our listeners to play some more games.
[2942.46 → 2943.86] So that's very cool.
[2943.94 → 2948.10] Of course, one of our listeners will be drawn at random for that Frees Party t-shirt.
[2948.30 → 2949.58] One of the people that took the survey.
[2949.70 → 2950.76] So stay tuned for that.
[2951.22 → 2952.38] We'll probably announce it in our Slack.
[2952.46 → 2954.42] And I'll also just email you if you're the winner.
[2954.82 → 2957.76] If you're not the winner, and you want some of that sweet, sweet swag,
[2957.94 → 2959.62] merch.change.com, of course.
[2959.62 → 2960.94] Go get yourself a t-shirt.
[2961.66 → 2963.02] But yeah, this has been Front End Feud.
[2963.08 → 2964.66] Another awesome battle.
[2964.86 → 2965.54] I've been Jared.
[2965.80 → 2966.64] This is JS Party.
[2967.48 → 2968.30] And thanks, you all.
[2968.56 → 2970.32] We'll talk to you next time.
[2970.94 → 2974.82] Book, book, book, book, book, book, book, book, book, book, book, book, book, book, book, book.
[2974.82 → 2990.64] If you had fun listening to this episode, check out the back catalogue.
[2991.02 → 2993.88] This is the sixth time we've hosted a feud.
[2993.88 → 3001.04] You can also find every dev game show we've ever played at changelog.com slash topic slash games.
[3001.54 → 3008.30] And on Spotify in my dev game shows playlist for those of you who like to mix your music and your pods.
[3008.74 → 3013.88] Like I mix my mashed potatoes, gravy, peas, turkey, corn, and everything else together at Thanksgiving.
[3014.68 → 3015.78] Actually, that does sound pretty good.
[3016.22 → 3018.30] Maybe I'll have to give Spotify one more look.
[3019.20 → 3020.08] Nah, I'm good.
[3020.08 → 3021.60] Oh, you're still here.
[3021.96 → 3023.66] Then let me thank our partners once again.
[3023.88 → 3027.46] Vastly and Fly, thank you for helping us make JS Party possible.
[3027.96 → 3033.94] And of course, our beat master in residence, BMC, that front end feud theme song is off the charts.
[3034.12 → 3034.52] Thank you.
[3034.92 → 3039.48] Next up on the pod, Daniel Thompson from the Tower Project joins the show.
[3040.12 → 3041.28] Have you heard of Tower?
[3041.50 → 3047.00] It helps you build smaller, faster, and more secure desktop apps with a web front end.
[3047.00 → 3050.06] Kind of like Electron, but with a few important advantages.
[3050.80 → 3051.72] Stay tuned for that.
[3051.88 → 3054.16] We'll drop it into your podcast feed next week.
