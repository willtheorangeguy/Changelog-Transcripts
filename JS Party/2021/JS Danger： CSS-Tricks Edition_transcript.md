[0.00 --> 4.84]  It used to be a trickier aspect of CSS, but Flexbox and Grid have made it trivial to pull off.
[5.14 --> 5.58]  Floats.
[6.86 --> 8.42]  Not what we were after there.
[9.28 --> 10.90]  I can see where you got this.
[11.58 --> 13.02]  Jeff, first deal.
[13.60 --> 14.96]  What is aspect ratio?
[16.24 --> 17.48]  Not quite, right?
[18.22 --> 18.70]  Miriam.
[19.20 --> 20.70]  I'm going to go with what is layout.
[21.32 --> 22.96]  Well, that's such a generic thing to say.
[26.96 --> 27.44]  Layout.
[27.66 --> 28.68]  It's a large aspect.
[28.68 --> 30.28]  It's the Holy Grail.
[31.10 --> 32.30]  Not what we're looking for.
[32.38 --> 32.62]  Sorry.
[32.92 --> 33.80]  It's not what we're looking for.
[35.00 --> 36.88]  We have to read our minds as well as get it right.
[37.72 --> 39.66]  Just because everybody's risking it all.
[39.72 --> 40.78]  I'm going to say columns.
[41.56 --> 43.14]  Also not what we're looking for.
[43.60 --> 44.04]  Nice.
[44.74 --> 45.98]  It's a question from hell.
[46.10 --> 46.88]  Welcome, everyone.
[47.14 --> 48.22]  Welcome to the red.
[50.12 --> 52.68]  Bandwidth for Change Log is provided by Fastly.
[52.98 --> 54.86]  Learn more at Fastly.com.
[55.10 --> 57.40]  Our feature flags are powered by LaunchDarkly.
[57.40 --> 59.48]  Check them out at LaunchDarkly.com.
[59.72 --> 61.56]  And we're hosted on Leno cloud servers.
[61.96 --> 65.46]  Get $100 in hosting credit at Leno.com slash Change Log.
[65.46 --> 67.66]  What's up, JS Party people?
[67.78 --> 72.54]  Have you ever wondered if you could be offering a faster, less buggy experience for your customers?
[73.08 --> 83.76]  Well, with Raygun Error and Performance Monitoring, you have all the information you need at your fingertips to quickly find and fix errors and performance issues across your tech stack down to the line of code.
[83.76 --> 92.58]  Raygun makes it easy to monitor the impact of your performance improvements, quickly identify issues across web and mobile apps, and see how your code performs in the hands of your customers.
[93.06 --> 96.64]  This saves you time, this saves you money, and this saves your sanity.
[97.00 --> 101.60]  Head to Raygun.com to join thousands of customer-centric software teams who use Raygun every single day.
[101.92 --> 105.78]  Again, Raygun.com to give them a try with a free 14-day trial.
[105.78 --> 129.50]  This is JS Party, a weekly celebration of JavaScript and the web.
[129.74 --> 134.02]  Follow the show on Apple Podcasts, Spotify, or your favorite podcast app.
[134.02 --> 136.84]  We are also on Twitter at JSParty.fm.
[136.96 --> 139.10]  And did you know, we have a worldwide website.
[139.36 --> 144.18]  Dig into the back catalog, comment on episodes, and a whole lot more at JSParty.fm.
[144.34 --> 146.34]  All right, hey, it's danger time, y'all.
[151.18 --> 153.62]  Welcome, everyone, to JS Party.
[153.82 --> 155.90]  I'm Jared Danger Santo.
[156.46 --> 159.18]  And today we have a very special treat for you.
[159.88 --> 162.64]  Our Don't Call It Jeopardy game show is back.
[162.64 --> 165.70]  And we're joined by the team behind CSS Tricks.
[165.80 --> 168.76]  Maybe you've heard of it, csstricks.com.
[169.30 --> 171.84]  And they're going to face off and see which one's the best.
[172.00 --> 172.86]  Chris Coyer is here.
[172.96 --> 175.04]  Chris, thanks for coming on JS Party.
[175.48 --> 176.24]  Oh, I can't wait.
[176.36 --> 177.10]  Thanks for having me.
[177.72 --> 178.86]  And do you like to live dangerously?
[179.46 --> 180.62]  That's my middle name.
[181.58 --> 182.80]  No, that was my middle name.
[182.86 --> 183.56]  Didn't you hear my intro?
[184.14 --> 184.60]  Dang it.
[184.92 --> 187.12]  We also have Sarah Drasner here.
[187.42 --> 188.94]  Sarah, do you have a competitive spirit?
[188.94 --> 195.32]  I do, but not as much as Chris, who has broken both of his wrists in the last two years.
[198.32 --> 199.70]  Chris, how'd you break your wrist, man?
[200.26 --> 201.72]  I was mountain biking.
[201.90 --> 204.06]  And I was really just competing against myself, really.
[204.28 --> 206.86]  And it was my elbows, which I'm not sure if which is worse.
[207.12 --> 209.68]  But I could type with the elbows thing.
[209.78 --> 211.34]  So I'm saying it was a little better, maybe.
[211.90 --> 214.28]  Yeah, and he was putting your articles the whole time.
[214.28 --> 217.48]  Sounds like you do like to live dangerously after all.
[217.48 --> 218.60]  Editing those was something else.
[220.62 --> 222.96]  That voice you hear is Jeff Graham.
[223.08 --> 223.96]  Jeff, welcome to the show.
[224.28 --> 224.52]  Hi.
[224.78 --> 225.28]  Nice to be here.
[225.72 --> 229.26]  And I've wondered, have you ever considered suing Instagram for a trademark infringement?
[230.80 --> 231.74]  I think so.
[232.08 --> 235.18]  Once or twice, but for probably different reasons than you're thinking.
[236.32 --> 237.76]  What are you thinking?
[238.84 --> 240.50]  Well, just they're using your name, man.
[240.60 --> 241.44]  That's your name, Graham.
[241.66 --> 242.16]  They're using it.
[242.16 --> 243.52]  Oh, sure.
[243.52 --> 244.54]  Okay, yeah, yeah.
[244.94 --> 250.06]  Well, you know, I hold exclusive copyright on the H and the extra A that's in there as well.
[250.54 --> 251.34]  So I'm all good.
[252.26 --> 254.86]  And we are also joined by Miriam Suzanne.
[255.20 --> 255.52]  Hello.
[255.86 --> 256.28]  Welcome.
[256.56 --> 257.92]  Did you bring your trivia skills with you?
[258.40 --> 258.78]  Nope.
[262.02 --> 267.72]  Well, then you'll fit right in because we are here to have some fun and to play JS Danger.
[267.92 --> 270.14]  This is very much in the Jeopardy! style.
[270.14 --> 275.36]  So we will do a round-robin selection of squares from the game board.
[275.58 --> 278.78]  And there are two rounds and then a final trouble round.
[278.88 --> 280.42]  First round is called trouble.
[280.42 --> 283.30]  And there are four categories.
[283.80 --> 285.40]  Each category has a theme.
[285.92 --> 288.32]  We will take turns selecting a square.
[288.70 --> 290.74]  If you get it right, you get the points from that square.
[290.96 --> 293.92]  If you get it wrong, it goes to the next person in line.
[294.04 --> 295.28]  They have a chance to steal.
[295.28 --> 300.16]  So if it's Chris's turn, Sarah will have a chance to steal, then Jeff, then Miriam, and so on.
[300.78 --> 302.40]  If you steal, you get the points.
[302.50 --> 305.72]  If you miss the steal, you also go negative.
[305.94 --> 307.06]  So be careful with the steals.
[307.80 --> 312.04]  Let's go ahead and take a look at our categories, and I'll describe what their themes are.
[312.14 --> 314.86]  So the first one is called Project People.
[314.86 --> 320.70]  And this is where you are trying to match coders with the projects that they started.
[321.40 --> 324.64]  The second category is called Movies Worth CSSing.
[325.58 --> 328.90]  These are movies with CSS-related things in their titles.
[330.80 --> 333.20]  Category three is called Tricky CSS Sites.
[333.36 --> 338.54]  These are websites that aren't CSS tricks, and yet people still somehow learn CSS from them.
[338.90 --> 341.28]  The next category is called Bleeding Edge.
[341.28 --> 344.42]  These are newish browser features.
[345.62 --> 346.26]  So there you go.
[346.32 --> 347.50]  Chris, the board is yours.
[347.62 --> 348.30]  Please pick a square.
[348.80 --> 349.90]  Oh, I get to kick it off.
[349.96 --> 350.60]  That's exciting.
[351.16 --> 353.64]  Oh, I'm going to take Bleeding Edge for 100, please.
[354.20 --> 355.10]  Bleeding Edge for 100.
[355.64 --> 359.96]  Some animations can cause dizziness and nausea in people with vestibular disorders.
[360.52 --> 361.74]  Media queries to the rescue.
[362.16 --> 364.92]  Do I have to form my answer in the form of a question or whatever?
[365.18 --> 365.76]  You can try.
[366.96 --> 369.80]  What is prefers reduced motion?
[370.64 --> 371.82]  That is correct.
[373.48 --> 374.80]  100 points to you, sir.
[374.86 --> 375.66]  Very well played.
[375.66 --> 377.30]  The snowball is going.
[377.76 --> 378.02]  Yeah.
[378.18 --> 378.86]  There you go.
[379.02 --> 379.50]  Now we're playing.
[379.60 --> 380.08]  We're having some fun.
[380.16 --> 380.82]  Sarah, you are up.
[380.92 --> 381.54]  Please pick a square.
[382.36 --> 382.80]  Oh.
[383.74 --> 386.96]  I'm interested in the Movies Worth CSSing for 100.
[387.54 --> 388.90]  Movies Worth CSSing.
[389.04 --> 394.30]  Keanu Reeves infiltrates a gang of bank-robbing surfers in this 1991 cult classic.
[394.90 --> 397.66]  Isn't it breaking...
[398.20 --> 399.64]  Point Break?
[400.20 --> 401.14]  Point Break.
[401.14 --> 403.50]  You pulled it out somehow at the last second.
[403.92 --> 404.32]  Wow.
[406.32 --> 406.72]  Incredible.
[407.60 --> 408.04]  Jeez.
[408.50 --> 408.90]  Excellent.
[409.36 --> 409.68]  Excellent.
[409.78 --> 411.72]  And it was there because Break was in the title?
[411.94 --> 412.60]  Like...
[412.60 --> 413.10]  Or what?
[413.24 --> 413.72]  Or Point?
[413.86 --> 414.94]  Yeah, like Break Points.
[415.30 --> 416.36]  Oh, Point Break.
[416.36 --> 416.68]  Break.
[416.88 --> 417.64]  There you go.
[417.98 --> 418.32]  Okay.
[418.38 --> 419.10]  Thank you.
[419.50 --> 419.88]  Okay.
[420.10 --> 420.84]  Jeff, your turn.
[420.94 --> 421.58]  Please pick a square.
[421.58 --> 423.78]  I'm going to keep it going right there.
[423.88 --> 424.92]  Movies Worth CSSing.
[425.00 --> 425.24]  300.
[426.18 --> 427.80]  Somehow our squares got mixed up there.
[427.94 --> 429.38]  300 is in the 200 spot.
[429.54 --> 430.92]  I'm going to go ahead and blame Nick for that.
[431.70 --> 435.72]  In the colorful future, even though it's my fault, a cab driver, who is Bruce Willis,
[435.90 --> 440.08]  unwittingly becomes the central figure in the search for a legendary cosmic weapon to
[440.08 --> 443.96]  keep evil and Mr. Zorg, played by Gary Oldman, at bay.
[443.96 --> 446.92]  Oh, good lord.
[448.80 --> 450.30]  I'm going to have to pass on that one.
[450.50 --> 451.22]  I have no idea.
[451.36 --> 452.78]  I'm just not Bruce Willis savvy.
[453.12 --> 453.52]  Steal.
[453.90 --> 454.44]  Oh, wait.
[455.12 --> 455.44]  All right.
[455.52 --> 457.14]  So pass gets you negative 300.
[458.02 --> 459.66]  And Miriam gets a chance to steal.
[460.12 --> 460.70]  Would you like to steal?
[460.94 --> 462.12]  What is the fifth element?
[462.66 --> 463.78]  That is correct.
[463.94 --> 464.16]  Oh!
[464.88 --> 465.66]  Very good.
[465.72 --> 466.28]  Very good.
[466.38 --> 467.32]  A successful steal.
[467.56 --> 468.06]  Good job.
[468.32 --> 469.56]  And you now get the board.
[470.16 --> 473.06]  I guess I'll jump back over to Bleeding Edge for 200.
[473.96 --> 475.82]  Bleeding Edge for 200.
[476.56 --> 482.88]  This experimental CSS property allows animations to be driven by a container's scroll position.
[483.24 --> 486.40]  What is animation scroll timeline?
[489.38 --> 491.40]  Scroll timeline?
[491.86 --> 492.76]  Yeah, scroll timeline.
[492.88 --> 493.44]  We'll give it to you.
[495.22 --> 496.30]  Very good.
[497.14 --> 498.28]  I heard animation.
[498.42 --> 499.16]  I'm like, that's not right.
[499.22 --> 499.96]  But then you kept talking.
[500.08 --> 501.10]  I'm like, that sounds pretty good.
[501.96 --> 502.84]  All right.
[502.84 --> 503.54]  Very good.
[503.54 --> 504.68]  So you're in the lead.
[504.76 --> 505.40]  Looping back around.
[505.48 --> 506.16]  Chris, it's your turn.
[506.22 --> 506.84]  Please pick a square.
[507.46 --> 508.86]  Bleeding Edge for 300, please.
[508.88 --> 509.30]  All right.
[509.34 --> 509.78]  Here we go.
[509.84 --> 511.10]  They're going after the Bleeding Edge.
[511.60 --> 514.26]  This modern image format is optimized for web environments.
[514.84 --> 520.30]  It boasts better image compression than WebP, JPEG, PNG, and GIF with a hard G.
[521.56 --> 522.74]  It's A-V-I-F.
[524.22 --> 524.88]  I'm sorry.
[524.96 --> 525.68]  That's incorrect.
[525.86 --> 527.94]  It may also be true now that I'm thinking about it.
[527.94 --> 530.22]  But it's not the one that was on the website.
[530.70 --> 531.06]  Okay.
[533.76 --> 536.26]  Anybody like to steal a non-AVIF answer?
[536.92 --> 537.98]  That was my answer.
[538.52 --> 538.82]  Okay.
[538.92 --> 539.32]  Mine too.
[539.96 --> 541.14]  Maybe you guys can school me.
[541.32 --> 546.16]  So this was according to caniuse.com, and the feature's called JPEG XL.
[546.82 --> 547.06]  Oh.
[547.62 --> 548.22]  Is anybody familiar?
[548.22 --> 548.64]  Ooh.
[549.48 --> 551.14]  My answer's more right.
[551.14 --> 553.32]  All right.
[553.54 --> 554.66]  I'm going to defer to Chris.
[554.76 --> 555.96]  Let's go ahead and give him the points.
[557.98 --> 560.22]  Because you're probably more right than I am.
[561.50 --> 562.66]  Thank you very much.
[563.12 --> 563.84]  I'm not cheating.
[564.10 --> 565.00]  I'm really right.
[565.24 --> 565.56]  Okay.
[566.68 --> 567.38]  I agree.
[567.48 --> 567.84]  I agree.
[568.38 --> 569.24]  Everybody agrees?
[569.40 --> 570.12]  He got it right.
[570.32 --> 570.68]  All right.
[572.12 --> 576.12]  What's funny is we were test driving this before the show, and Nick also went through these
[576.12 --> 576.44]  questions.
[576.54 --> 577.88]  And he also said A-V-I-F.
[577.88 --> 580.72]  So that's why I was like, hmm, maybe I got it wrong there.
[581.14 --> 582.18]  All right.
[582.52 --> 583.38]  Sarah, your turn.
[584.62 --> 588.12]  I want to do tricky CSS sites for 100.
[588.12 --> 588.32]  All right.
[588.90 --> 589.86]  For 100.
[591.28 --> 595.26]  Often atop CSS-related search results, but that doesn't mean devs love it.
[595.90 --> 596.50]  Ooh.
[596.88 --> 598.66]  I can picture it in my mind.
[600.00 --> 601.72]  The green site.
[605.16 --> 605.80]  Green.
[607.60 --> 608.12]  Oh.
[608.98 --> 609.54]  Oh.
[609.74 --> 610.40]  Time to out.
[611.14 --> 611.70]  Sorry.
[612.18 --> 612.96]  Tip of your tongue.
[613.14 --> 615.30]  Jeff, do you know what site we're referring to?
[616.26 --> 617.76]  What is W3 schools?
[619.50 --> 619.90]  Yes.
[620.04 --> 620.96]  That's it.
[621.80 --> 622.70]  Go on.
[623.42 --> 625.40]  I'm picturing it in my mind.
[626.20 --> 626.50]  Yes.
[626.56 --> 628.08]  We all have it burnt into our retinas.
[628.30 --> 628.92]  You got green.
[629.06 --> 629.70]  That's absolutely.
[630.44 --> 630.68]  Yeah.
[631.20 --> 631.82]  Okay, Jeff.
[631.84 --> 632.18]  Your turn.
[632.26 --> 632.86]  Please pick a square.
[633.46 --> 633.68]  Oh.
[634.28 --> 635.04]  Leading Edge 400.
[635.64 --> 636.44]  Leading Edge for 400.
[636.44 --> 642.46]  The new cookie store API has a more modern interface than document.cookie and can also be used in these.
[643.32 --> 647.36]  What is custom properties?
[647.36 --> 649.82]  I'm sorry.
[649.90 --> 650.68]  That's incorrect.
[651.00 --> 651.88]  Miriam, would you like to steal?
[652.84 --> 653.24]  No.
[653.72 --> 654.32]  I would not.
[654.66 --> 655.52]  Chris, would you like to steal?
[656.18 --> 656.52]  No.
[656.52 --> 656.78]  I don't know.
[656.84 --> 658.42]  I don't really understand the question.
[658.68 --> 658.92]  Okay.
[659.26 --> 659.74]  That's fine.
[660.00 --> 660.18]  Skip.
[660.44 --> 660.78]  Skip.
[660.88 --> 661.64]  Sarah, would you like to steal?
[662.14 --> 664.86]  We're not talking about local storage, are we?
[665.84 --> 667.48]  Is that a steal or a question?
[670.04 --> 672.62]  I'm not supposed to tell you that until you submit a steal.
[673.66 --> 675.74]  I would say probably skip the steal, maybe.
[679.70 --> 680.60]  Nobody is stealing.
[680.74 --> 682.22]  Let's go ahead and show the answer.
[682.38 --> 684.00]  They can also be used in service.
[684.06 --> 684.76]  Was it a web worker?
[684.76 --> 685.86]  Oh, a service.
[686.04 --> 686.18]  Yeah.
[686.90 --> 687.58]  Tough one.
[688.02 --> 690.50]  Jeff, so far, selecting the difficult ones.
[690.64 --> 691.16]  Let's move on.
[691.16 --> 693.48]  So you can't use a regular cookie in a service worker.
[693.72 --> 694.20]  TIL.
[694.76 --> 695.16]  Go ahead.
[695.88 --> 696.60]  Miriam, your turn.
[696.68 --> 698.16]  Please select a category.
[698.66 --> 701.94]  Let's do tricky CSS sites for 200.
[702.44 --> 702.84]  Okay.
[703.40 --> 706.92]  Browser support tables for modern web technologies, including CSS.
[707.58 --> 708.90]  What is can I use?
[709.72 --> 710.64]  You got it.
[711.74 --> 712.82]  And or MDN.
[715.56 --> 717.36]  There's some crossover there now, isn't there?
[718.24 --> 718.78]  All right.
[718.84 --> 719.56]  You got that one.
[719.62 --> 720.68]  We're back to Chris.
[721.16 --> 723.94]  I'll take tricky CSS sites for 300.
[724.20 --> 724.58]  Okay.
[724.72 --> 725.28]  Here we go.
[726.06 --> 729.90]  This site demonstrates what can be accomplished by only changing the CSS.
[730.72 --> 731.44]  Oh, yeah.
[731.56 --> 732.66]  The Zen Garden.
[733.16 --> 734.08]  CSS Zen Garden.
[734.94 --> 735.74]  That's right.
[736.50 --> 739.20]  Well, that's like one for us old friends.
[739.20 --> 740.74]  That is an old school, isn't it?
[741.44 --> 741.66]  Yeah.
[741.66 --> 743.66]  There's a new version of it.
[744.06 --> 745.30]  Style Stages.
[745.80 --> 746.04]  Really?
[746.04 --> 746.14]  Oh.
[746.86 --> 747.26]  Yeah.
[747.82 --> 749.86]  By, is it Stephanie behind that?
[750.06 --> 750.74]  Stephanie Yaggles?
[751.26 --> 751.66]  Nice.
[752.10 --> 752.88]  I'll have to check that out.
[752.94 --> 756.70]  There's a, they kind of like re, revitalized the Zen Garden too at one point.
[756.74 --> 759.12]  And you could like actually like submit pull requests to it instead.
[759.22 --> 760.04]  Oh, oh, sorry.
[761.04 --> 762.02]  Let's get back to the game.
[762.56 --> 762.82]  Not yet.
[762.82 --> 763.04]  Cool.
[763.42 --> 764.14]  We can chit chat.
[764.24 --> 764.62]  No big deal.
[765.26 --> 765.54]  Okay.
[765.60 --> 766.36]  Whose turn was that?
[766.50 --> 767.38]  I think I'm next.
[767.58 --> 767.82]  Maybe.
[768.60 --> 769.72]  Miriam just got it right.
[769.78 --> 770.02]  Right?
[770.14 --> 770.36]  Okay.
[770.46 --> 771.30]  So back to Chris then.
[771.52 --> 772.98]  Or no, I, I got it right.
[772.98 --> 773.88]  Or you got that right.
[774.00 --> 774.64]  So Sarah's turn.
[774.64 --> 774.84]  Oh, I got it.
[775.08 --> 775.68]  Very good.
[775.76 --> 775.94]  Okay.
[776.04 --> 776.68]  Sarah was correct.
[777.86 --> 779.68]  God, Chris just trying to feel.
[779.84 --> 780.50]  I really.
[782.78 --> 784.64]  We haven't done Project People yet.
[784.74 --> 785.74]  So I'll do that one for.
[785.80 --> 786.46]  All right.
[787.42 --> 788.54]  Matt Molenweg.
[789.54 --> 789.74]  WordPress.
[790.52 --> 791.12]  Very good.
[792.32 --> 794.70]  That feels like a softball.
[795.24 --> 797.08]  Well, that is a 100 point question.
[797.84 --> 798.50]  Yeah, that's true.
[799.34 --> 799.78]  Okay.
[800.02 --> 800.46]  Jeff.
[801.36 --> 802.70]  It's going to keep going in the red.
[803.00 --> 803.76]  Bleeding Edge 500.
[804.36 --> 805.40]  It kind of likes to bleed.
[805.48 --> 806.02]  What can we say?
[807.40 --> 814.10]  This CSS property sets whether an element's background extends underneath its border box, padding box, or content box.
[814.78 --> 816.48]  What is border box?
[817.60 --> 818.16]  Oh, I mean.
[819.38 --> 819.82]  No.
[820.10 --> 820.74]  Go ahead and.
[820.80 --> 821.54]  You can change it.
[821.72 --> 822.40]  You have a better guess?
[822.68 --> 823.02]  No.
[823.08 --> 824.08]  Go right ahead.
[825.36 --> 825.98]  All right.
[826.02 --> 826.54]  Sorry, Jeff.
[826.78 --> 827.84]  Go further in the red.
[828.08 --> 828.76]  Miriam for the steal.
[828.76 --> 830.74]  What is background clip?
[832.70 --> 833.46]  That's correct.
[834.14 --> 835.42]  Thanks for that, Jeff.
[835.42 --> 838.08]  Miriam is the benefactor of Jeff.
[838.08 --> 840.14]  First debuted in 1997.
[840.14 --> 843.54]  That's why it was new-ish.
[845.32 --> 845.98]  Fair enough.
[846.06 --> 846.40]  Fair enough.
[847.10 --> 849.04]  That was Jeff's turn, so it's Miriam's turn.
[850.66 --> 851.52]  Yeah, okay.
[852.16 --> 853.78]  Tricky CSS sites for 400.
[853.78 --> 860.78]  Launched in 2005 when a small team of idealists set out to create a new free community-built online resource for all web developers.
[861.60 --> 863.72]  What is web platform docs?
[865.20 --> 865.64]  No.
[866.42 --> 866.60]  Hmm.
[867.08 --> 867.36]  Hmm.
[867.46 --> 867.78]  Chris.
[868.76 --> 870.68]  I'm not going to steal because that was my guess.
[871.16 --> 871.60]  Okay.
[871.88 --> 872.26]  Sarah.
[872.60 --> 875.56]  This may be too late to be accurate, but GeoCities?
[877.24 --> 877.88]  I'm sorry.
[877.96 --> 878.94]  That's not correct either.
[879.04 --> 879.34]  Jeff.
[881.34 --> 882.28]  Dig out of that hole?
[882.28 --> 882.36]  Okay.
[884.74 --> 890.10]  I have a guess, but I kind of like that someone's joining me in the red, so I'm just going to leave it.
[891.68 --> 892.08]  Okay.
[892.38 --> 893.66]  Let's see what the answer was.
[895.36 --> 896.10]  Oh, NBN.
[896.58 --> 898.10]  That was it.
[898.50 --> 899.14]  There it was.
[899.50 --> 899.94]  2005.
[900.40 --> 901.48]  It's been that long ago.
[901.48 --> 902.22]  Idealists.
[902.82 --> 904.30]  Large company of Idealists.
[904.46 --> 906.58]  That's according to their own about page right there.
[906.64 --> 906.94]  Okay.
[907.14 --> 907.32]  Okay.
[907.62 --> 908.52]  Those are not my words.
[909.32 --> 909.76]  All right.
[909.88 --> 912.88]  So that was, it's always hard to remember whose turn it is.
[912.94 --> 913.86]  Who said that one?
[914.88 --> 915.58]  Oh, that was mine.
[915.74 --> 915.98]  All right.
[916.02 --> 916.78]  So we're back to Chris.
[917.44 --> 917.74]  Chris.
[917.82 --> 918.06]  Okay.
[918.06 --> 920.10]  Tricky CSS sites for 500.
[920.32 --> 920.72]  All right.
[920.78 --> 921.60]  He's going back to the well.
[921.66 --> 922.74]  Got to take the lead here.
[923.50 --> 927.70]  This site shows you CSS alternatives for common JS UI components.
[928.16 --> 928.52]  Oh.
[931.06 --> 932.68]  And I have to guess, right?
[932.76 --> 933.40]  That's correct.
[933.52 --> 934.20]  You have to guess.
[934.52 --> 935.50]  I have to guess.
[935.50 --> 940.46]  Is it like, you may not need JS or something like that?
[940.54 --> 941.44]  You don't need JS.
[941.44 --> 941.92]  Wow.
[942.24 --> 943.18]  Way to pull it out.
[943.32 --> 943.86]  Look at this.
[944.08 --> 944.18]  Yes.
[944.98 --> 948.26]  How did you pull that one out?
[948.34 --> 949.14]  Excellent job.
[949.94 --> 951.06]  All right, Sarah, your turn.
[951.18 --> 951.84]  Pick a square.
[952.72 --> 954.50]  Let's do Project People for 200.
[954.92 --> 955.42]  Okay.
[956.54 --> 957.54]  Another softball.
[957.70 --> 958.46]  John Rezig.
[959.20 --> 959.96]  Jake Rezig.
[961.52 --> 962.40]  There you go.
[963.06 --> 963.96]  Jeff, it's your turn.
[963.96 --> 965.60]  I knew the last one too.
[969.28 --> 969.84]  Jeez.
[970.22 --> 971.54]  Let's go Project People 300.
[972.42 --> 972.76]  Okay.
[974.12 --> 975.52]  David Hennemeyer Hansen.
[976.14 --> 977.08]  That was a base camp.
[977.98 --> 979.26]  Open source project.
[979.64 --> 980.66]  Ruby on Rails?
[981.58 --> 982.14]  Yes.
[982.22 --> 982.44]  Yes.
[982.50 --> 983.02]  There you go.
[984.62 --> 985.52]  Very good.
[986.96 --> 988.00]  Now we're scooting along.
[988.10 --> 988.74]  Miriam, your turn.
[989.12 --> 990.88]  Movies worth CSSing for 200.
[990.88 --> 998.20]  A young Peruvian bear travels to London in search of a home in this 2015 animated comedy.
[999.60 --> 1000.92]  What is Paddington bear?
[1002.48 --> 1003.60]  You got it.
[1003.68 --> 1004.18]  Very good.
[1004.86 --> 1005.24]  Wow.
[1005.64 --> 1007.06]  Marginnington.
[1007.06 --> 1014.20]  Chris, your turn.
[1015.62 --> 1017.74]  I'll take Project People for 400.
[1018.62 --> 1020.26]  Drys Boytart.
[1020.94 --> 1021.76]  Oh, no.
[1021.98 --> 1023.28]  And I have to guess again.
[1023.56 --> 1024.84]  I'm sorry, Drys.
[1024.88 --> 1025.76]  I don't know you.
[1026.10 --> 1026.48]  Let's see.
[1026.60 --> 1027.46]  Think of Project.
[1028.20 --> 1029.40]  That's something.
[1030.94 --> 1032.30]  Oh, does everybody know it?
[1032.30 --> 1033.02]  I feel dumb.
[1034.30 --> 1035.24]  It's MooTools.
[1035.24 --> 1038.36]  I'm sorry.
[1038.46 --> 1038.96]  That's incorrect.
[1039.96 --> 1041.26]  Sarah, would you like to steal?
[1041.78 --> 1042.56]  Can I say no?
[1043.02 --> 1043.66]  You can say no.
[1043.82 --> 1044.54]  Yeah, you can say no.
[1044.72 --> 1045.18]  Okay, wait, wait.
[1045.26 --> 1046.26]  I'm going to make a guess.
[1046.66 --> 1046.86]  Okay.
[1047.80 --> 1049.16]  We did CMSs.
[1049.70 --> 1051.16]  What if he's like Drupal?
[1051.62 --> 1052.04]  Drupal?
[1053.96 --> 1054.88]  You got it.
[1055.64 --> 1056.44]  Nice work.
[1056.68 --> 1057.46]  You just came up.
[1057.72 --> 1058.70]  That was nice.
[1059.28 --> 1059.64]  Wow.
[1060.28 --> 1060.64]  Wow.
[1061.14 --> 1062.58]  I thought you were going further in the red there.
[1062.90 --> 1063.30]  Congratulations.
[1063.46 --> 1063.96]  That was excellent.
[1063.96 --> 1064.84]  All right.
[1064.94 --> 1066.12]  And it's now your turn as well.
[1067.10 --> 1067.76]  Oh, again.
[1067.98 --> 1068.38]  Oh, okay.
[1068.70 --> 1069.00]  Oof.
[1069.22 --> 1069.84]  Project People.
[1070.58 --> 1071.10]  All right.
[1071.54 --> 1073.82]  For 500, Mr. Doob.
[1074.04 --> 1074.62]  Oh, yeah.
[1075.18 --> 1077.02]  Mr. Doob does 3JS.
[1078.26 --> 1079.16]  That's right.
[1079.64 --> 1079.96]  Wow.
[1080.14 --> 1080.56]  Very good.
[1080.62 --> 1081.88]  I'm pulling it together.
[1082.40 --> 1082.50]  You are.
[1082.68 --> 1083.38]  You're on the come back.
[1083.48 --> 1085.42]  You're now tied for second place with 800.
[1085.56 --> 1086.26]  Chris has 800.
[1086.46 --> 1087.42]  Miriam has 1,000.
[1087.86 --> 1088.52]  Jeff, it's your turn.
[1088.78 --> 1089.70]  I'll take Movies Worth.
[1089.82 --> 1090.74]  Yes, I've seen 400.
[1090.74 --> 1091.14]  400.
[1091.14 --> 1091.70]  400.
[1092.36 --> 1097.18]  Two powerful mutants, Charles Xavier and Eric Lencher, joined together to stop a ruthless
[1097.18 --> 1101.16]  dictator from thrusting Russia and the U.S. into nuclear war.
[1101.52 --> 1102.88]  Oh, gosh.
[1104.68 --> 1107.20]  It's like so showing that I don't watch movies.
[1107.90 --> 1108.38]  Ah.
[1109.96 --> 1110.48]  Jeez.
[1110.76 --> 1111.42]  I'm sorry.
[1111.52 --> 1112.02]  I'm going to pass.
[1112.40 --> 1112.80]  Okay.
[1113.92 --> 1115.14]  Miriam with a chance to steal.
[1115.14 --> 1118.68]  Let's go with who are the X-Men.
[1119.32 --> 1121.06]  Is that X-Height Men?
[1123.52 --> 1126.26]  We're going to have to say no on that one.
[1126.32 --> 1127.38]  You're close, but you're not.
[1127.66 --> 1128.24]  You're not on.
[1129.20 --> 1129.60]  Chris.
[1131.04 --> 1133.82]  That's going to pass because it's X-Men related.
[1134.22 --> 1134.48]  Yeah.
[1134.60 --> 1134.88]  Sarah.
[1135.60 --> 1136.84]  X-Men First Class.
[1136.92 --> 1137.76]  X-Men First Class.
[1138.32 --> 1139.34]  That's what I was going to say.
[1139.34 --> 1139.62]  Whoa.
[1143.24 --> 1144.96]  Storming back to take the lead.
[1145.98 --> 1146.48]  All right.
[1146.48 --> 1146.78]  Incredible.
[1147.20 --> 1150.24]  And that leaves us with just movies worth CSSing for 500.
[1150.40 --> 1153.24]  This is Miriam's turn, or is this Chris's turn?
[1153.24 --> 1153.58]  Yeah.
[1153.72 --> 1154.68]  Yeah, that's me, I think.
[1154.70 --> 1155.08]  That's you.
[1155.22 --> 1155.32]  Okay.
[1156.42 --> 1156.64]  Yeah.
[1157.30 --> 1158.30]  Who started the X-Men one?
[1158.44 --> 1159.86]  That was Jeff.
[1159.88 --> 1160.08]  Jeff.
[1160.08 --> 1161.32]  Yeah, so it's Miriam's turn.
[1162.24 --> 1162.88]  All right.
[1162.94 --> 1164.32]  Last one on the board for round one.
[1164.42 --> 1168.74]  Steven Spielberg directs Whoopi Goldberg, a black Southern woman struggling to find her identity
[1168.74 --> 1171.52]  after suffering abuse from her father and others.
[1171.90 --> 1173.66]  What is the color Rebecca Purple?
[1175.14 --> 1176.16]  You got it.
[1176.72 --> 1177.26]  Wow.
[1177.56 --> 1178.08]  Wow.
[1178.38 --> 1178.98]  Very good.
[1179.18 --> 1179.72]  Well done.
[1180.72 --> 1182.90]  Thus concludes round one.
[1183.60 --> 1184.48]  Let's look at the board.
[1185.30 --> 1188.78]  We have in first place with 1,200 points, Sarah Drasner.
[1189.78 --> 1192.16]  Following close behind is Miriam with 1,100.
[1192.92 --> 1194.40]  Chris in third with 800.
[1194.88 --> 1198.30]  And Jeff still bleeding after those bleeding edge choices.
[1198.70 --> 1199.70]  Negative 1,200.
[1199.70 --> 1200.52]  Don't worry, Jeff.
[1201.02 --> 1202.68]  Double troubles just around the corner.
[1203.48 --> 1205.04]  A real comeback for Sarah.
[1205.86 --> 1206.34]  Yeah.
[1206.34 --> 1206.92]  That was amazing.
[1207.16 --> 1208.08]  Pulling Jerupo out.
[1210.16 --> 1211.24]  That was clutch.
[1212.04 --> 1212.88]  Well done, everyone.
[1213.52 --> 1214.10]  Except Jeff.
[1214.28 --> 1214.46]  You didn't.
[1217.04 --> 1219.52]  I just hope my boss isn't watching.
[1219.52 --> 1223.64]  Don't we all.
[1223.64 --> 1224.50]  We all.
[1224.50 --> 1225.12]  I love you.
[1238.18 --> 1241.20]  This episode is brought to you by Sourcegraph.
[1241.60 --> 1244.08]  Sourcegraph is code search for every developer and team.
[1244.34 --> 1247.58]  Easily search across all the code that matters to you and your organization.
[1248.02 --> 1248.98]  Find example code.
[1249.22 --> 1250.30]  Explore and read code.
[1250.56 --> 1251.40]  Debug issues.
[1251.40 --> 1252.60]  and so much more.
[1252.88 --> 1255.72]  And I talked with Byung Liu, CTO and co-founder of Sourcegraph
[1255.72 --> 1258.42]  and asked him to share what code search is,
[1258.56 --> 1260.76]  what developers and teams are missing out on
[1260.76 --> 1262.62]  and how Sourcegraph provides code search
[1262.62 --> 1263.94]  to every developer in the world.
[1264.22 --> 1266.96]  If you've worked inside a Google or a Facebook
[1266.96 --> 1269.20]  or any one of these really big,
[1269.42 --> 1271.38]  well-respected technology companies,
[1271.52 --> 1274.10]  chances are you've used something like code search before
[1274.10 --> 1276.72]  and you know the value that it provides to your team.
[1276.78 --> 1278.72]  You know that almost every single engineer
[1278.72 --> 1282.26]  inside these organizations uses it on a daily basis.
[1282.46 --> 1284.16]  If you've never had that experience,
[1284.50 --> 1287.16]  chances are you may not know what you're missing out on.
[1287.40 --> 1289.96]  You know, the term code search sounds a lot like,
[1289.96 --> 1292.18]  you know, grep or the search inside your editor
[1292.18 --> 1293.64]  and that's what a lot of people think
[1293.64 --> 1294.54]  when they first hear it.
[1294.60 --> 1296.30]  But it's really about much more than that.
[1296.40 --> 1298.74]  It's really about connecting you as a developer
[1298.74 --> 1302.46]  to the broader universe of code and code-related data
[1302.46 --> 1305.12]  that's relevant to you, that you need at hand
[1305.12 --> 1307.38]  in order to enter that, you know, magical flow state
[1307.38 --> 1309.06]  of, you know, being in your editor,
[1309.56 --> 1312.22]  writing code quickly, making rapid progress
[1312.22 --> 1314.10]  towards that feature bug fix that you're working on.
[1314.22 --> 1316.20]  It's really about making all that contextual information
[1316.20 --> 1318.34]  accessible at your fingertips.
[1318.80 --> 1319.86]  And what that means is,
[1319.96 --> 1321.48]  think about every single repository,
[1321.66 --> 1324.14]  every single file and every single language,
[1324.48 --> 1325.74]  every single diff
[1325.74 --> 1328.38]  and every single open source dependency
[1328.38 --> 1330.04]  or maybe closed source dependency
[1330.04 --> 1331.48]  that's shared across your organization.
[1331.48 --> 1334.30]  All that is searchable through a single text box.
[1334.80 --> 1335.62]  And that's really powerful
[1335.62 --> 1337.98]  because it means all this friction is eliminated
[1337.98 --> 1339.40]  between you and understanding
[1339.40 --> 1340.40]  that broader world of code.
[1340.50 --> 1342.14]  You don't have to clone stuff down to your local machine.
[1342.28 --> 1343.98]  You don't have to mess around with editor config.
[1344.40 --> 1346.34]  You don't have to be constantly bugging
[1346.34 --> 1347.64]  people on other teams
[1347.64 --> 1349.40]  who may not even know who you are
[1349.40 --> 1351.18]  in order to teach yourself
[1351.18 --> 1352.84]  how all that code works.
[1353.24 --> 1354.30]  What Sourcegraph is,
[1354.30 --> 1357.44]  is really a way for the rest of us,
[1357.50 --> 1358.76]  the people who don't work inside
[1358.76 --> 1360.50]  the Googles, the Facebooks,
[1360.50 --> 1362.88]  to get a tool that gives us access
[1362.88 --> 1365.64]  to that sort of information readily
[1365.64 --> 1366.82]  and at our fingertips.
[1366.82 --> 1369.26]  It's really about bringing this type of tool
[1369.26 --> 1371.22]  that a lot of the larger technology companies
[1371.22 --> 1372.48]  have developed and invested
[1372.48 --> 1373.96]  hundreds of millions of dollars
[1373.96 --> 1375.92]  into making for the productivity
[1375.92 --> 1376.80]  of their own engineers
[1376.80 --> 1378.14]  and making that accessible
[1378.14 --> 1380.12]  to every single developer in the world.
[1380.30 --> 1380.78]  All right.
[1380.80 --> 1382.10]  If CodeSearch powered by Sourcegraph
[1382.10 --> 1384.04]  sounds like something you and your team can use,
[1384.16 --> 1385.98]  head to info.sourcegraph.com
[1385.98 --> 1386.88]  slash changelog
[1386.88 --> 1387.98]  and click the button that says
[1387.98 --> 1389.04]  try Sourcegraph now.
[1389.24 --> 1390.18]  You can install it locally,
[1390.50 --> 1391.38]  deploy it to a server,
[1391.38 --> 1392.38]  or to a cluster.
[1392.76 --> 1393.54]  They have a quick start guide
[1393.54 --> 1394.54]  that takes less than five minutes
[1394.54 --> 1396.02]  to install Sourcegraph using Docker,
[1396.18 --> 1397.84]  so it's too easy to give it a try.
[1398.10 --> 1400.42]  Again, head to info.sourcegraph.com
[1400.42 --> 1401.48]  slash changelog.
[1421.38 --> 1428.86]  Now this is double trouble.
[1429.02 --> 1431.20]  All point values are doubled,
[1431.64 --> 1433.62]  so it's a good chance to come back
[1433.62 --> 1435.68]  or fail terribly.
[1436.68 --> 1439.46]  So the first column category is,
[1439.62 --> 1440.72]  oh, node, you didn't.
[1440.88 --> 1443.24]  These are obviously node-related questions.
[1443.82 --> 1445.90]  The second category is called frameworks.
[1445.90 --> 1449.84]  These are CSS frameworks in their own words,
[1450.06 --> 1452.40]  so how they describe themselves in their homepage.
[1453.92 --> 1455.28]  Actual CSS tricks,
[1455.42 --> 1456.58]  those are, you know,
[1456.70 --> 1458.60]  hacks that devs have to do to get stuff done.
[1459.16 --> 1461.14]  And then the last one is called divitis.
[1462.00 --> 1462.58]  On this one,
[1462.64 --> 1465.52]  we've taken HTML elements,
[1465.96 --> 1467.96]  which were semantic,
[1468.18 --> 1469.48]  and we've replaced them with divs,
[1469.50 --> 1470.84]  and you have to figure out
[1470.84 --> 1472.42]  which element it originally was.
[1472.42 --> 1473.72]  Oh, my God.
[1473.88 --> 1474.74]  That's cool.
[1475.54 --> 1476.86]  Also, Miriam has a leg up
[1476.86 --> 1478.50]  on the frameworks category.
[1479.44 --> 1480.16]  Do I?
[1481.46 --> 1483.56]  You a framework aficionado?
[1483.78 --> 1484.34]  I don't know.
[1484.76 --> 1485.60]  She made one.
[1486.14 --> 1488.02]  I guess that counts.
[1488.38 --> 1488.70]  Okay.
[1489.38 --> 1490.64]  That's one more than I've made.
[1492.00 --> 1492.60]  And let's see.
[1492.64 --> 1493.46]  We finished off with Miriam,
[1493.58 --> 1495.08]  so I guess we'll go back to Chris.
[1495.22 --> 1496.20]  Chris, go ahead and get a start.
[1496.28 --> 1496.60]  Round two.
[1497.28 --> 1499.32]  Okay, let's try divitis for 200.
[1499.32 --> 1500.16]  All right.
[1500.16 --> 1503.18]  So, div, name equals please.
[1503.48 --> 1504.60]  Press me, end div.
[1505.88 --> 1506.96]  I hope it's a button.
[1508.24 --> 1509.40]  You got it.
[1510.10 --> 1511.20]  All right, we go to Sarah.
[1511.80 --> 1516.32]  I'm going to try actual CSS tricks for 200.
[1516.74 --> 1519.10]  You can use multiple background images
[1519.10 --> 1521.82]  and nested divs to achieve the rounding effect
[1521.82 --> 1523.60]  possible with this one property.
[1524.26 --> 1525.62]  Rounding effect like,
[1526.42 --> 1528.32]  well, I guess you can't tell me.
[1528.52 --> 1529.98]  Remember that it's a hack,
[1529.98 --> 1531.74]  so this is something that people did
[1531.74 --> 1533.02]  before the property existed.
[1534.02 --> 1534.32]  I see.
[1534.88 --> 1535.84]  Is it CSS gradient?
[1537.24 --> 1537.68]  Nope.
[1538.18 --> 1538.74]  Jeff to steal.
[1539.54 --> 1540.60]  What is border radius?
[1542.34 --> 1542.98]  That's it.
[1543.60 --> 1544.60]  Oh, I was thinking.
[1545.14 --> 1545.60]  All right.
[1545.62 --> 1547.18]  Good memories of the sliding doors.
[1547.74 --> 1548.32]  Oh, yes.
[1548.70 --> 1549.10]  Nice.
[1549.82 --> 1550.94]  Jeff began his comeback,
[1551.16 --> 1552.04]  and now your turn, Jeff.
[1552.10 --> 1553.40]  You get to pick a square.
[1553.40 --> 1554.42]  All right.
[1554.50 --> 1555.74]  Let's keep digging out.
[1556.16 --> 1557.14]  Frame words for 200, please.
[1557.52 --> 1558.68]  Frame words for 200.
[1558.68 --> 1560.72]  Simple and flexible HTML.
[1560.86 --> 1561.90]  CSS is on JavaScript
[1561.90 --> 1563.88]  for popular user interface components
[1563.88 --> 1564.70]  and interactions.
[1565.22 --> 1566.10]  From Twitter.
[1567.08 --> 1568.22]  What is bootstrap?
[1569.74 --> 1570.70]  There you go.
[1571.46 --> 1572.34]  And we go to Miriam.
[1573.12 --> 1575.54]  Let's do actual CSS tricks for 400.
[1576.26 --> 1577.52]  Many people aren't clear
[1577.52 --> 1578.96]  why this fixes anything,
[1579.28 --> 1580.50]  but they reach for it anyways
[1580.50 --> 1581.56]  when things don't look right.
[1582.26 --> 1582.60]  Hmm.
[1583.56 --> 1584.90]  What is C index?
[1584.90 --> 1586.92]  That's a good guess,
[1587.00 --> 1588.06]  but not what we're looking for.
[1588.64 --> 1588.92]  Chris?
[1589.34 --> 1590.60]  My guess is that it's a pun,
[1590.74 --> 1591.84]  and it's clear.
[1592.14 --> 1592.90]  Clear fix.
[1593.56 --> 1594.06]  Clear both.
[1595.02 --> 1595.26]  Yeah.
[1595.60 --> 1596.16]  You got it.
[1596.22 --> 1596.92]  The clear fix.
[1597.14 --> 1597.66]  Mm-hmm.
[1598.26 --> 1599.30]  A lot of these are older
[1599.30 --> 1600.38]  because we don't have to do them
[1600.38 --> 1601.84]  quite as often as we used to.
[1602.58 --> 1604.76]  That was Miriam's turn,
[1604.82 --> 1605.54]  so now it's Chris's turn.
[1606.90 --> 1607.30]  Ooh.
[1607.30 --> 1607.40]  Oh.
[1608.94 --> 1610.12]  Frame words for 1,000.
[1610.44 --> 1611.08]  Oh, my goodness.
[1611.16 --> 1611.68]  He's going big.
[1611.68 --> 1614.68]  The less formal CSS framework.
[1614.96 --> 1616.56]  Its goal is to be as minimal
[1616.56 --> 1618.48]  as possible when adding classes.
[1619.06 --> 1620.06]  When adding classes?
[1621.04 --> 1621.90]  I don't know.
[1622.06 --> 1622.84]  It's not Tailwind,
[1622.92 --> 1623.92]  but I'm going to say Tailwind.
[1624.90 --> 1626.14]  That is incorrect.
[1626.90 --> 1627.64]  Their goal is to be
[1627.64 --> 1628.88]  as maximal as possible.
[1628.94 --> 1629.38]  All right.
[1629.66 --> 1630.90]  Here's where I'll remind people
[1630.90 --> 1632.54]  to be careful with the steals
[1632.54 --> 1633.64]  because you can lose 1,000
[1633.64 --> 1635.38]  by stealing haphazardly.
[1635.38 --> 1636.54]  Sarah, do you know what it is?
[1636.66 --> 1637.16]  What would you like to steal?
[1640.06 --> 1640.70]  Tachyons?
[1641.68 --> 1643.36]  Sorry, that's also incorrect.
[1645.04 --> 1646.42]  Jeff, would you like to steal?
[1646.96 --> 1648.82]  I'm going to go out on a limb, yes.
[1650.32 --> 1651.84]  Despite all advice,
[1652.22 --> 1653.22]  they're just going for it.
[1654.16 --> 1656.66]  What is paper CSS?
[1658.36 --> 1659.56]  You got it.
[1659.90 --> 1660.88]  No way.
[1662.14 --> 1662.98]  Very good.
[1663.34 --> 1664.06]  Nicely done.
[1664.40 --> 1665.30]  That was an obscure one.
[1665.32 --> 1665.64]  Thank you.
[1665.84 --> 1666.18]  Thank you.
[1666.54 --> 1667.32]  Sarah, I think.
[1667.92 --> 1668.90]  Yep, Sarah, your turn.
[1668.90 --> 1670.54]  I want to do
[1670.54 --> 1673.78]  actual CSS tricks for 800.
[1674.12 --> 1675.14]  Okay, for 800.
[1676.04 --> 1678.14]  It used to be a trickier aspect of CSS,
[1678.44 --> 1679.52]  but Flexbox and Grid
[1679.52 --> 1680.94]  have made it trivial to pull off.
[1681.64 --> 1682.20]  Floats.
[1683.36 --> 1685.02]  Not what we were after there.
[1685.86 --> 1686.48]  But that's true.
[1686.48 --> 1687.28]  I can see where you're going.
[1687.96 --> 1689.60]  Jeff, first steal?
[1690.36 --> 1691.92]  What is aspect ratio?
[1691.92 --> 1694.44]  Not quite, right?
[1695.28 --> 1695.68]  Miriam.
[1696.22 --> 1697.78]  I'm going to go with what is layout.
[1698.38 --> 1700.06]  Well, that's such a generic thing to say.
[1704.14 --> 1704.54]  Layout.
[1704.74 --> 1705.84]  It's a large aspect.
[1706.68 --> 1708.02]  It's the holy grail?
[1709.78 --> 1710.90]  Not what we're looking for.
[1710.98 --> 1711.24]  Sorry.
[1711.50 --> 1712.40]  Just not what we're looking for.
[1713.60 --> 1715.46]  We have to read our minds as well as get it right.
[1716.40 --> 1718.26]  Just because everybody's risking it all.
[1718.32 --> 1719.40]  I'm going to say columns.
[1720.22 --> 1721.74]  Also not what we're looking for.
[1721.88 --> 1722.74]  Oh, nice.
[1722.88 --> 1724.50]  Let's duke the question from hell.
[1724.50 --> 1724.86]  Welcome, everyone.
[1725.14 --> 1726.00]  Welcome to the net.
[1726.12 --> 1726.68]  Equal height.
[1726.90 --> 1727.72]  It's the old,
[1727.96 --> 1729.60]  it's the thing that everybody complains about all the time.
[1729.66 --> 1731.02]  Just like how to center things, right?
[1731.34 --> 1731.94]  Vertically center.
[1732.94 --> 1733.62]  That's fair.
[1733.76 --> 1734.32]  That's fair.
[1734.46 --> 1735.12]  Okay, it's true.
[1735.86 --> 1737.26]  That wasn't even too broad of a question,
[1737.42 --> 1739.10]  but at least we all got bit by it.
[1740.04 --> 1742.62]  Which means it was basically a no-op at that point, right?
[1742.62 --> 1745.26]  Okay, whose turn was that?
[1745.36 --> 1747.22]  It's hard to even see who's winning anymore.
[1748.04 --> 1749.06]  Just blood on the streets.
[1750.38 --> 1750.90]  Jeff.
[1751.14 --> 1754.90]  Oh, I'll do divitis for 400.
[1755.50 --> 1756.08]  All right.
[1756.54 --> 1756.90]  Div.
[1757.04 --> 1759.30]  This text is important, serious, or urgent.
[1759.50 --> 1759.88]  End div.
[1760.62 --> 1761.62]  What is...
[1762.58 --> 1763.86]  No, that's not going to be it.
[1764.56 --> 1765.08]  Shoot.
[1765.48 --> 1765.84]  Oh.
[1766.54 --> 1767.52]  What is alert?
[1769.00 --> 1769.48]  Nope.
[1769.92 --> 1770.64]  Miriam to steal.
[1771.34 --> 1772.46]  What is strong?
[1773.62 --> 1774.78]  You got it.
[1775.84 --> 1776.40]  Strong.
[1777.94 --> 1778.92]  All right.
[1780.02 --> 1781.20]  And it's your turn as well, Miriam.
[1781.32 --> 1782.06]  Back in the white.
[1783.18 --> 1783.76]  Yes.
[1784.74 --> 1786.42]  I'll do divitis again.
[1786.62 --> 1787.36]  Let's go 600.
[1787.66 --> 1788.04]  Okay.
[1788.20 --> 1789.10]  Divitis for 600.
[1789.88 --> 1790.24]  Div.
[1790.50 --> 1794.46]  JSON and div stands for JavaScript object notation.
[1796.20 --> 1798.36]  What is ABBR?
[1799.16 --> 1799.86]  Got it again.
[1799.86 --> 1800.48]  Very good.
[1800.48 --> 1803.26]  It's an abbreviation.
[1804.82 --> 1805.30]  Okay.
[1805.44 --> 1806.12]  Chris, to you.
[1807.08 --> 1808.16]  I'm so nervous.
[1808.50 --> 1809.00]  I'm going to die.
[1810.08 --> 1812.16]  I want divitis for 1,000, though.
[1812.32 --> 1813.82]  He's going 1,000 each time.
[1813.90 --> 1814.22]  All right.
[1814.68 --> 1815.50]  Go big or go home.
[1816.34 --> 1817.68]  Div value equals 70.
[1818.04 --> 1818.30]  Progress.
[1818.30 --> 1818.82]  Max equals 100.
[1819.02 --> 1819.78]  Oh, you got it.
[1819.90 --> 1820.22]  Progress.
[1820.60 --> 1821.10]  No good one.
[1821.10 --> 1824.48]  Well played, sir.
[1825.48 --> 1826.84]  And Sarah, your turn.
[1827.42 --> 1829.28]  I want frameworks for 800.
[1829.78 --> 1830.26]  Okay.
[1831.88 --> 1835.78]  This 8-bit-like CSS framework is brimming with 80s nostalgia.
[1837.04 --> 1839.34]  That feels like something I would know.
[1839.34 --> 1843.72]  I don't know the answer.
[1843.72 --> 1844.32]  Okay.
[1845.50 --> 1846.74]  Jeff, would you like to steal?
[1847.72 --> 1848.44]  No, thanks.
[1848.92 --> 1849.64]  Miriam to steal.
[1850.30 --> 1850.62]  Nope.
[1851.26 --> 1851.82]  Chris to steal.
[1852.70 --> 1853.26]  Too risky.
[1853.80 --> 1854.02]  Yep.
[1854.60 --> 1857.46]  But I'll say if there's some, is it the Windows 98 looking one?
[1857.46 --> 1858.94]  That's a good second guess.
[1859.02 --> 1864.10]  It's actually NES.css, which is a very cool framework.
[1864.10 --> 1865.96]  All right.
[1866.08 --> 1866.70]  Moving on.
[1866.86 --> 1867.84]  It is now Jeff's turn.
[1868.30 --> 1870.96]  Let's take RaymWord600.
[1871.48 --> 1871.76]  I know.
[1871.82 --> 1873.82]  You guys are ignoring the Node category.
[1875.56 --> 1876.16]  Absolutely.
[1876.16 --> 1876.94]  Not a surprise.
[1877.66 --> 1881.76]  A free open source framework that provides ready-to-use front-end components that you can
[1881.76 --> 1884.70]  easily combine to build responsive web interfaces.
[1885.42 --> 1887.48]  No CSS knowledge required.
[1888.10 --> 1892.10]  What is, oh, geez.
[1892.10 --> 1892.54]  Right?
[1893.20 --> 1894.78]  Ready-to-use front-end components.
[1895.60 --> 1897.74]  This is straight off their, they're like a homepage, huh?
[1897.74 --> 1898.66]  This is right off their homepage.
[1898.90 --> 1900.16]  They make a big deal out of the end.
[1900.28 --> 1901.64]  No CSS knowledge required.
[1902.34 --> 1904.06]  No CSS knowledge required.
[1904.42 --> 1904.80]  Okay.
[1905.66 --> 1909.14]  What is material?
[1910.20 --> 1910.86]  I'm sorry.
[1910.96 --> 1911.54]  That's incorrect.
[1912.42 --> 1912.84]  Miriam?
[1913.92 --> 1914.50]  Say a no.
[1914.56 --> 1915.44]  No, I don't.
[1915.60 --> 1916.26]  I don't know.
[1916.52 --> 1917.08]  Okay, Chris?
[1917.42 --> 1917.72]  Steal?
[1918.28 --> 1918.86]  Too risky.
[1919.30 --> 1919.86]  Sarah to steal?
[1919.86 --> 1923.88]  I'm already in the red, so I'm just going to keep going.
[1924.24 --> 1924.44]  Okay.
[1925.34 --> 1926.48]  Is it Prismic?
[1927.38 --> 1927.84]  No.
[1928.28 --> 1928.72]  I'm sorry.
[1928.92 --> 1930.94]  The framework is Bulma.
[1931.64 --> 1932.16]  Oh.
[1932.34 --> 1932.82]  Okay.
[1933.38 --> 1934.02]  There you go.
[1934.80 --> 1935.44]  All right.
[1936.20 --> 1936.90]  I like Bulma.
[1937.02 --> 1937.52]  It looks good.
[1937.64 --> 1938.62]  It's a nice looking one.
[1938.80 --> 1939.56]  It does look nice.
[1940.08 --> 1941.52]  Marketing copy could use some work, maybe.
[1942.98 --> 1943.46]  Yeah.
[1943.46 --> 1945.66]  It's like CSS knowledge helpful.
[1946.30 --> 1946.62]  Right.
[1947.12 --> 1947.64]  Whose turn?
[1948.00 --> 1948.64]  Let's see.
[1949.02 --> 1950.52]  That was Jeff's turn.
[1950.68 --> 1951.44]  So Miriam, your turn.
[1951.92 --> 1954.44]  Actual CSS tricks, 600.
[1954.84 --> 1955.24]  Okay.
[1955.98 --> 1959.56]  This is the best place for your style rule to ensure it gets applied.
[1960.18 --> 1961.14]  Place is all caps.
[1961.72 --> 1962.86]  Why is place all caps?
[1963.44 --> 1964.36]  I'll tell you afterwards.
[1965.30 --> 1966.04]  In line?
[1966.26 --> 1967.02]  What is in line?
[1967.02 --> 1969.44]  You got it.
[1970.16 --> 1974.26]  I put place in all caps because you might think bang important is what you would do, but that's
[1974.26 --> 1975.04]  not really a place.
[1975.06 --> 1975.20]  Okay.
[1975.68 --> 1976.04]  Yeah.
[1976.38 --> 1978.28]  It actually, it did help.
[1978.80 --> 1981.98]  I was just thinking of the way people used to write HTML all caps all the time.
[1982.80 --> 1983.20]  All right.
[1983.38 --> 1983.70]  Oh, yeah.
[1985.36 --> 1986.02]  Very good.
[1986.14 --> 1986.62]  Got it right.
[1986.74 --> 1987.36]  Chris, your turn.
[1988.56 --> 1992.50]  I feel like I'm contractually obliged to take actual CSS tricks.
[1992.50 --> 1995.14]  All right.
[1995.30 --> 2000.16]  This proprietary Microsoft extension to Internet Explorer provides a mechanism to target each
[2000.16 --> 2003.62]  of the versions of IE either specifically or as a group.
[2004.68 --> 2008.76]  I thought that was like, I'm going to say conditional comments.
[2009.08 --> 2010.34]  I'm going to say you are correct.
[2011.24 --> 2011.72]  Oh.
[2012.40 --> 2013.14]  Very good.
[2013.52 --> 2014.92]  Feels good to be number one.
[2014.92 --> 2020.76]  All right, Sarah, your turn.
[2021.44 --> 2023.18]  Oh, no, you didn't for 200.
[2023.50 --> 2023.94]  Okay.
[2024.84 --> 2026.04]  Waiting into the Node waters.
[2026.66 --> 2027.30]  Missed the browser?
[2027.56 --> 2028.96]  This function might console you.
[2029.40 --> 2031.06]  It works pretty much the same in Node.
[2031.58 --> 2033.98]  I mean, this feels too obvious.
[2035.58 --> 2037.22]  It is the easiest in the column.
[2037.94 --> 2038.52]  All right.
[2038.66 --> 2039.44]  Console.log.
[2041.16 --> 2042.08]  You got it.
[2042.54 --> 2043.90]  I'm like, is this a trick?
[2044.92 --> 2046.06]  It feels like.
[2047.26 --> 2048.72]  All right, Jeff, your turn.
[2048.80 --> 2049.28]  Pick a square.
[2050.30 --> 2051.32]  Framework's 400.
[2052.02 --> 2057.06]  A utility-first framework to rapidly build modern websites without ever leaving your HTML.
[2058.18 --> 2060.60]  What is atomic CSS?
[2062.50 --> 2062.86]  Oh.
[2063.36 --> 2064.00]  Incorrect.
[2064.42 --> 2065.12]  Miriam DeSteel?
[2065.84 --> 2067.10]  I think you're on the right track.
[2067.10 --> 2069.14]  What is Tailwind?
[2070.16 --> 2070.92]  That's it.
[2071.40 --> 2072.00]  Thanks, Jeff.
[2074.92 --> 2077.58]  Miriam is benefiting from her placement on the board here.
[2077.68 --> 2078.74]  So your turn as well.
[2079.94 --> 2083.50]  I'll take divitis for 800 because I am not touching Node.
[2084.42 --> 2090.52]  A common equation in physics is E equals MC div to end div.
[2091.10 --> 2091.88]  What is?
[2092.00 --> 2092.54]  S-U-P?
[2094.44 --> 2095.50]  You got it.
[2096.44 --> 2096.98]  I'm jealous.
[2097.34 --> 2099.06]  You avoided my opportunity to say not much.
[2099.18 --> 2099.68]  Sup with you.
[2099.68 --> 2101.14]  All right.
[2102.76 --> 2104.38]  I've been waiting for it the whole game.
[2106.10 --> 2106.94]  Chris, your turn.
[2107.02 --> 2108.86]  There's only Node questions left.
[2109.02 --> 2110.46]  I'll take the 600 one.
[2110.64 --> 2111.84]  I got some ground to cover.
[2111.92 --> 2112.16]  Okay.
[2112.24 --> 2114.12]  He's not going for 1,000 this time around.
[2114.62 --> 2114.90]  No.
[2115.48 --> 2120.02]  You have to use require instead of import in Node because it relies on this module system.
[2120.68 --> 2122.34]  Like CJS probably?
[2123.54 --> 2123.98]  Common.
[2123.98 --> 2124.34]  Common JS.
[2124.34 --> 2124.74]  Yes.
[2124.74 --> 2125.18]  Correct.
[2125.58 --> 2126.02]  You got it.
[2127.88 --> 2131.40]  Not technically 100% true anymore, but it was true at the time of the writing.
[2131.78 --> 2132.10]  Okay.
[2132.32 --> 2133.74]  Because sometimes you don't have to anymore.
[2134.00 --> 2134.16]  Okay.
[2135.12 --> 2135.52]  Sarah.
[2136.62 --> 2137.66]  I'm going to do Node.
[2137.74 --> 2138.76]  You didn't for 400.
[2139.42 --> 2143.64]  Node.js runs on this JavaScript engine, which is also at the core of Google Chrome.
[2145.04 --> 2147.52]  It's, oh, God.
[2148.10 --> 2148.84]  My brain is.
[2150.26 --> 2150.66]  V8.
[2151.40 --> 2152.04]  That's right.
[2153.00 --> 2153.72]  Very good.
[2153.76 --> 2155.08]  You guys are drilling the Node questions.
[2155.66 --> 2158.00]  Jeff, to you, you got 800 or 1,000.
[2158.90 --> 2159.34]  1,000.
[2159.76 --> 2160.18]  Let's do it.
[2162.30 --> 2162.70]  Thanks.
[2163.70 --> 2168.74]  This, in the browser's global scope, refers to window, but in Node, it refers to?
[2169.36 --> 2170.94]  What is the document?
[2177.88 --> 2178.66]  Mercy points.
[2178.78 --> 2179.32]  Mercy points.
[2179.32 --> 2179.84]  We'll give it to you.
[2182.04 --> 2186.20]  It's actually the, it's module that I support, it's the current module.
[2186.54 --> 2191.26]  And so the doc, if you're in a document, there is no document object, but the current
[2191.26 --> 2193.84]  module, which would be the top level thing in the current document.
[2193.96 --> 2194.94]  So close enough.
[2195.02 --> 2195.50]  We'll give it to you.
[2196.22 --> 2196.70]  All right.
[2196.72 --> 2199.68]  Which leaves Miriam with, oh, Node, you didn't for 800.
[2199.90 --> 2200.38]  Here we go.
[2201.14 --> 2201.58]  Okay.
[2201.58 --> 2206.88]  If you want to read an environment variable or exit from a Node program, you must use this
[2206.88 --> 2207.60]  core module.
[2207.96 --> 2209.54]  Read an environment variable.
[2209.54 --> 2211.30]  I think I've done that before.
[2212.76 --> 2213.16]  Maybe.
[2213.76 --> 2215.32]  Do you remember the module you used?
[2215.56 --> 2215.86]  Nope.
[2216.90 --> 2217.32]  Okay.
[2217.80 --> 2220.30]  Hazard a guess or we'll just subtract the points.
[2221.44 --> 2223.10]  I think you can just subtract the points.
[2223.60 --> 2224.04]  Okay.
[2225.34 --> 2226.06]  Minus 800.
[2226.18 --> 2227.20]  We go to Chris for the steal.
[2227.28 --> 2227.72]  No.
[2228.20 --> 2228.80]  I'm going to pass.
[2228.88 --> 2231.12]  I could guess, but I'm absolutely not going to.
[2231.28 --> 2231.50]  Okay.
[2231.64 --> 2232.28]  Sarah to steal.
[2234.06 --> 2234.52]  Dot end.
[2234.52 --> 2238.24]  That's close, but incorrect.
[2238.70 --> 2239.04]  Dot end.
[2239.54 --> 2239.98]  Yeah.
[2241.34 --> 2242.14]  Jeff to steal.
[2243.44 --> 2245.24]  Oh, well, that was what I was going to guess.
[2245.24 --> 2248.66]  So I'm just going to let it slide.
[2249.00 --> 2249.32]  All right.
[2249.66 --> 2251.74]  The module is called process.
[2252.74 --> 2254.12]  Oh, okay.
[2254.34 --> 2255.34]  Process dot exit.
[2255.46 --> 2256.96]  Process dot end.
[2257.32 --> 2257.74]  Yeah.
[2258.26 --> 2258.68]  Okay.
[2258.90 --> 2259.06]  Etc.
[2259.06 --> 2261.82]  Thus concludes round two.
[2262.08 --> 2263.20]  Double trouble.
[2264.88 --> 2265.32]  What?
[2266.64 --> 2268.58]  Did your miss make me win?
[2269.34 --> 2269.78]  Yes.
[2270.56 --> 2271.50]  Well, the game's not over yet.
[2271.60 --> 2272.68]  We still have final trouble.
[2272.78 --> 2273.88]  The game is not quite over yet.
[2274.04 --> 2275.28]  So I got to go actually.
[2275.56 --> 2276.24]  Oh, dang it.
[2276.68 --> 2277.42]  I'm just kidding.
[2277.74 --> 2279.22]  Well, then Chris loses by forfeit.
[2279.88 --> 2280.80]  Taking my chips.
[2281.96 --> 2284.24]  Chris with 2,200 points.
[2284.54 --> 2285.84]  Miriam in second with 1,900.
[2286.46 --> 2288.64]  Jeff in third now with negative 1,000.
[2288.84 --> 2291.24]  And Sarah in fourth with negative 2,400.
[2291.64 --> 2294.40]  Now, we're about to play final trouble.
[2295.04 --> 2298.70]  And for that, everybody must have some points to wager.
[2299.10 --> 2300.98]  So a few of us are in the red.
[2301.14 --> 2304.00]  So what we will do is we will add negative 24.
[2304.22 --> 2308.74]  Actually, we'll add 3,000 to everybody's score to get Sarah back in the red.
[2308.74 --> 2310.14]  And that way it's still even still.
[2310.34 --> 2312.84]  It's like poor Sarah.
[2312.84 --> 2315.00]  So let's go ahead and do that.
[2315.06 --> 2316.56]  And then we'll start round three right after this.
[2316.56 --> 2339.32]  This episode is brought to you by the Dev Discuss podcast, an original show by the team behind Dev.to.
[2339.32 --> 2342.90]  The show is hosted by Dev co-founders Ben Halpern and Jess Lee.
[2343.24 --> 2349.86]  Ben has been on the Change Law podcast before, talking about their decision to go open source with a Dev platform now called Forum.
[2350.20 --> 2358.40]  The Dev Discuss podcast brings on notable industry guests to discuss trends and timeless software topics to help developers succeed within their teams and grow.
[2358.78 --> 2359.86]  Here's a clip from season two.
[2359.86 --> 2367.46]  When you deploy Node.js code, it doesn't matter if it's ARM or X86 underneath of it when it's serverless.
[2367.78 --> 2373.80]  AWS could probably move their fleet of Lambda services to ARM and very few customers will be affected.
[2373.92 --> 2378.88]  And not to say nobody, but very, very few customers will be affected by that kind of migration on Lambda.
[2378.88 --> 2387.42]  Whereas if they were to try that migration on Fargate or EC2, it's a much bigger and more complex migration for those customers.
[2388.04 --> 2398.06]  And, you know, here is them, you know, building something in a way that, you know, they may see as more productive or more traditional, but it is actually, you know, more locked in in a way.
[2398.56 --> 2399.46]  All right. Search for Dev Discuss.
[2399.72 --> 2401.64]  All one word in your podcast player.
[2401.74 --> 2404.78]  Subscribe and skim the backlog for an episode that jumps out to you.
[2404.78 --> 2407.60]  Again, search Dev Discuss anywhere you listen to podcasts.
[2408.88 --> 2428.44]  All right. We are back for final trouble.
[2428.56 --> 2430.30]  This is our very last question.
[2430.44 --> 2431.66]  A little bit different than the other rounds.
[2432.02 --> 2438.20]  Instead of taking turns, everybody is going to wager some points based on the category given.
[2438.20 --> 2440.04]  Then we'll show the question.
[2440.70 --> 2446.34]  And whoever ends up with the most points at the end is our actual CSS trickster winner.
[2447.14 --> 2453.00]  And the category is CSS Emoji Handshake R&B.
[2453.88 --> 2455.10]  So there's your category.
[2455.28 --> 2458.20]  Contestants, please submit to me your wagers.
[2458.38 --> 2460.22]  You can wager up to all of your points.
[2460.90 --> 2462.16]  And that's it.
[2462.42 --> 2463.06]  Submit your wagers now.
[2463.06 --> 2478.42]  Like this should be an R&B right now.
[2480.34 --> 2481.74]  Here comes the stressy part.
[2485.34 --> 2487.66]  I have everybody but Sarah's.
[2487.66 --> 2495.96]  I don't like it.
[2498.06 --> 2498.78]  All right.
[2498.88 --> 2500.56]  All of the wagers are in.
[2500.64 --> 2503.00]  Let's reveal our final trouble question.
[2504.08 --> 2509.00]  A year before CSS's debut, this chart-topping trio sang this song.
[2509.00 --> 2512.36]  Dreams are hopeless aspirations and hopes are coming true.
[2512.56 --> 2513.46]  Believe in yourself.
[2513.60 --> 2514.62]  The rest is up to me.
[2514.74 --> 2518.48]  Go, go chasing waterfalls.
[2518.84 --> 2523.72]  Please stick to the rivers and the lakes that you used to.
[2523.78 --> 2524.40]  We have Jeff's.
[2524.44 --> 2524.98]  We have Chris's.
[2525.04 --> 2525.90]  We have Miriam's.
[2527.04 --> 2528.56]  Very appropriate choice, by the way.
[2528.90 --> 2529.24]  Thank you.
[2529.90 --> 2531.28]  And Sarah is also in.
[2531.42 --> 2531.68]  Okay.
[2532.48 --> 2534.50]  So final results time.
[2535.24 --> 2538.80]  Chris, you wagered 4,901.
[2540.98 --> 2541.38]  Jeez.
[2544.26 --> 2547.92]  I forgot to mention that our game board only works in 50-point values.
[2548.74 --> 2549.22]  Sorry.
[2549.56 --> 2553.68]  Good strategy, but illegitimate due to technological hurdles.
[2554.36 --> 2554.72]  And your answer.
[2554.72 --> 2556.08]  I think you knew what I was going for there.
[2556.08 --> 2556.40]  Yes.
[2556.48 --> 2559.72]  Your answer was TLC, and that is correct, sir.
[2559.72 --> 2560.62]  Oh, yes.
[2560.76 --> 2561.26]  You got it.
[2561.26 --> 2564.26]  I was going to write tender love and care, but I'm glad I abbreviated.
[2564.50 --> 2564.90]  I abbreviated it.
[2565.58 --> 2569.54]  Miriam, you wagered 500, and you also answered TLC.
[2570.08 --> 2570.56]  Congratulations.
[2570.90 --> 2571.46]  You got it right.
[2572.84 --> 2578.64]  Jeff wagered 2,000, all of his points, and he answered TLC as well.
[2578.70 --> 2580.18]  So you're correct as well.
[2580.26 --> 2584.22]  And Sarah wagered all of her points, and she also said TLC.
[2584.34 --> 2586.28]  So everybody got the final triple answer, right?
[2586.32 --> 2586.74]  Congratulations.
[2586.74 --> 2586.94]  Yay.
[2589.02 --> 2589.34]  Yay.
[2589.34 --> 2589.54]  Yay.
[2590.54 --> 2592.34]  However, there can be only one.
[2593.38 --> 2598.70]  And Chris did have the most points and the highest points at the end.
[2598.80 --> 2603.32]  So our winner of this game of JS Danger is the one more, Chris Coyer.
[2603.32 --> 2613.84]  I'm going to Disney World.
[2619.20 --> 2621.86]  I don't know if Miriam wasn't too far behind.
[2621.86 --> 2624.98]  Well, that was a blast.
[2625.26 --> 2630.36]  Thank you to all four of you for being such good sports, for playing along, and for all
[2630.36 --> 2635.76]  of the web dev knowledge that you guys have shared over the years at CSS Tricks and continue
[2635.76 --> 2637.70]  to share on a daily basis.
[2637.88 --> 2640.92]  We really appreciate the work that you all do over there, and we appreciate you coming
[2640.92 --> 2642.56]  on the show and playing JS Danger with us.
[2642.90 --> 2643.88]  Thank you for having us.
[2643.88 --> 2644.68]  Thank you so much.
[2644.68 --> 2645.08]  Thank you.
[2645.40 --> 2646.44]  That was my huge pleasure.
[2648.14 --> 2648.50]  Yeah.
[2648.76 --> 2650.02]  Show my face bigger.
[2655.90 --> 2656.72]  What did he get?
[2656.80 --> 2658.32]  Did he get like a hot dog or something?
[2659.88 --> 2660.84]  Oh, he's hot dogging.
[2660.92 --> 2661.14]  All right.
[2661.54 --> 2663.64]  I get $50 off Linode hosting.
[2664.04 --> 2664.80]  Just kidding.
[2668.24 --> 2669.12]  All right.
[2669.16 --> 2669.46]  All right.
[2669.54 --> 2670.52]  That's JS Party for this week.
[2670.60 --> 2672.82]  Thanks for everybody for playing along, and we'll talk to you next time.
[2674.68 --> 2677.86]  Thank you for listening to JS Party.
[2678.16 --> 2679.78]  Please do tell a friend about the show.
[2679.96 --> 2683.08]  It's the number one way people find new podcasts they love.
[2683.42 --> 2688.08]  This episode was streamed live on YouTube, and it's fun to watch with the video game board
[2688.08 --> 2688.86]  and everything else.
[2689.10 --> 2691.84]  I'll put a link to that in the show notes in case you're interested.
[2692.52 --> 2696.44]  Music for JS Party is produced by Breakmaster Cylinder, and we're brought to you by awesome
[2696.44 --> 2696.88]  sponsors.
[2697.34 --> 2699.96]  Thanks again to Fastly, LaunchDarkly, and Linode.
[2699.96 --> 2706.32]  Next week on the pod, Emma Bastian, Nick Neesey, and a special guest discuss 10 accessibility
[2706.32 --> 2707.82]  mistakes you want to avoid.
[2708.54 --> 2709.66]  Stay tuned for that one.
[2709.98 --> 2712.56]  It'll be hitting your podcast feed next week.
[2712.56 --> 2713.06]  Music.
[2721.92 --> 2723.52]  He's on the break.
[2723.76 --> 2725.88]  Break it up, break it up, break it up.
[2726.08 --> 2728.86]  Gotta go back and strike that JPEG XL one from the record.
[2728.86 --> 2732.90]  Is that a thing?
[2732.98 --> 2733.32]  I don't know.
[2734.14 --> 2738.74]  It is, but I don't know if it's new, and AVIF is new and has all the press lately.
[2739.12 --> 2739.48]  Right.
[2740.46 --> 2746.38]  So those I was getting off of, I was just using Can I Use's blog, because I figured as
[2746.38 --> 2749.26]  they added new things to Can I Use, they were like relatively new features.
[2750.52 --> 2751.72]  I don't know if that's true.
[2751.84 --> 2756.56]  Yeah, I do that same thing, and I saw one the other day that was called Overflow Overlay,
[2756.84 --> 2758.56]  and I was like, what the hell is that?
[2758.56 --> 2762.16]  Yeah, I saw that too, and I went and looked at it, and I was like, this doesn't seem,
[2762.42 --> 2764.42]  and then they're like, this is deprecated.
[2764.62 --> 2765.46]  I'm like, well, then how's it new?
[2765.48 --> 2767.92]  Yeah, they were just adding an old deprecated thing.
[2768.10 --> 2769.14]  I'm like, oh, good job.
[2769.26 --> 2769.94]  Thanks for that.
[2770.02 --> 2770.64]  Super useful.
[2770.64 --> 2779.20]  So JPEG XL image format has zero support, like global zero percent, but does that mean
[2779.20 --> 2781.80]  it's like, maybe it's brand stinking new?
[2782.94 --> 2786.74]  Or maybe it's so old that no one, maybe it just like didn't ever become a thing.
[2787.54 --> 2789.44]  XL makes it sound like it's huge.
[2789.76 --> 2790.12]  Doesn't it?
[2790.24 --> 2790.48]  Yeah.
[2790.84 --> 2791.78]  Well, it's a terrible name.
[2791.78 --> 2796.24]  It does say JPEG XL competes with Avif, which has similar compression quality, but fewer
[2796.24 --> 2796.72]  features.
[2796.88 --> 2800.36]  So this might be like a brand new thing that someone's trying to do.
[2801.26 --> 2801.72]  I don't know.
[2802.16 --> 2804.28]  When you ask Leah Baru to be on the call.
[2805.78 --> 2806.80]  Yeah, I know.
[2806.80 --> 2808.76]  All right.
[2808.80 --> 2809.34]  Should we do it?
[2809.34 --> 2811.34]  Game on.
