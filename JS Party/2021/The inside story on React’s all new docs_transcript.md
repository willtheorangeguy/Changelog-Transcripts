[0.00 --> 5.70]  I really hope to see more people embedding interactive examples into their teaching materials.
[5.98 --> 7.10]  I think it's just fabulous.
[7.46 --> 8.82]  It should change the way people learn.
[9.24 --> 11.12]  These tool chains are getting more and more complex.
[11.50 --> 14.60]  The start of any bootcamp is usually just installing dependencies.
[15.12 --> 16.86]  Run this line on your terminal.
[17.16 --> 18.20]  You know, run this, run that.
[18.26 --> 19.22]  Oh no, that didn't work.
[19.32 --> 20.18]  Brew install this.
[20.28 --> 21.24]  Did you update that?
[21.32 --> 22.06]  Delete that file.
[22.16 --> 22.54]  Rerun.
[22.72 --> 25.24]  It's a huge barrier to play.
[25.70 --> 29.56]  And let's be honest, a lot of folks are not learning React to build something from scratch.
[29.56 --> 33.06]  They're learning React so that they can work on something that was built in React already.
[33.24 --> 34.92]  So that's a waste of their time.
[35.14 --> 39.66]  They just want to figure out why set state isn't doing the thing they expected.
[39.92 --> 44.44]  They don't want to have to like go figure out how to start a blog site.
[47.26 --> 50.58]  Big thanks to our partners, Linode, Fastly, and LaunchDarkly.
[51.00 --> 51.62]  We love Linode.
[51.68 --> 53.44]  They keep it fast and simple.
[53.74 --> 56.60]  Get $100 in credit at linode.com slash changelog.
[56.94 --> 59.12]  Our bandwidth is provided by Fastly.
[59.12 --> 61.04]  Learn more at Fastly.com.
[61.36 --> 62.54]  And get your feature flags.
[62.68 --> 63.54]  Powered by LaunchDarkly.
[63.68 --> 65.78]  Get a demo at LaunchDarkly.com.
[69.62 --> 72.46]  This episode is brought to you by Retool.
[72.74 --> 79.86]  Retool is a loco platform built specifically for developers that makes it fast and easy to build internal tools.
[80.12 --> 82.00]  Instead of building internal tools from scratch,
[82.00 --> 87.72]  the world's best teams from startups to Fortune 500s are using Retool to build their internal apps.
[88.12 --> 93.86]  Assemble your app in 30 seconds by dragging and dropping from the complete set of powerful pre-built components.
[94.30 --> 101.82]  From there, you write custom code, connect any data source, API, and build custom logic and queries to create exactly the right tools for your business.
[101.82 --> 106.88]  Spend your time getting UI in front of your stakeholders, not hunting down the best React table library.
[107.20 --> 112.24]  Retool is also highly hackable, so you're never limited by what's available out of the box.
[112.46 --> 115.82]  If you can write it in JavaScript and in API, you can build it in Retool.
[116.14 --> 119.30]  Try Retool off for yourself at retool.com slash changelog.
[119.30 --> 122.72]  Again, retool.com slash changelog.
[132.20 --> 137.66]  This is JS Party, your weekly celebration of JavaScript and the web.
[138.20 --> 142.20]  Join us live on Thursdays at 1 p.m. U.S. Eastern.
[142.54 --> 147.18]  Catch all the screw-ups, the outtakes, the jokes nobody laughs at, and more.
[147.18 --> 149.26]  Oh, and don't forget to follow the show on Twitter.
[149.46 --> 151.12]  We are at JSPartyFM.
[151.76 --> 152.78]  Okay, let's get into it.
[152.82 --> 154.32]  Hey, it's party time, y'all.
[168.42 --> 169.86]  Hello, party people.
[170.24 --> 173.84]  Well, I mean, you're JS Party people, so you're like fun nerds, right?
[173.94 --> 175.20]  So hello, fun nerds.
[175.20 --> 177.64]  I am so excited about today's show.
[177.90 --> 184.38]  We are here with the wonderful, the one and only, my very good friend, Rachel Neighbors.
[184.56 --> 184.80]  Welcome.
[185.40 --> 186.06]  Hello, Mel.
[186.20 --> 186.76]  Hello, Amelia.
[186.90 --> 187.94]  Good to be with you today.
[188.50 --> 188.96]  Yay.
[189.16 --> 191.48]  And we have Amelia Wattenberg.
[191.64 --> 191.86]  Hello.
[192.04 --> 192.54]  Welcome, Amelia.
[192.82 --> 193.34]  Hey, hey.
[193.66 --> 194.32]  Happy to be here.
[194.82 --> 195.10]  All right.
[195.14 --> 195.48]  Excellent.
[195.76 --> 199.26]  So today's show, I mean, you know, unless you've been living under a rock, you can guess
[199.26 --> 199.92]  what it's about.
[199.92 --> 205.14]  So the React team a few weeks ago, maybe two weeks ago, one week ago, I don't know.
[205.34 --> 206.46]  Time is a flat circle.
[207.00 --> 208.08]  But two weeks, I think.
[208.24 --> 208.66]  Two weeks, yeah.
[208.78 --> 213.68]  Two weeks ago had dropped the new React documentation site.
[213.86 --> 219.46]  So it's the same link, but just put a .beta in front of, you know, so it's beta.reactjs.org.
[219.46 --> 225.48]  So essentially, there's a whole new redesign and, you know, it's beyond just kind of a
[225.48 --> 226.68]  fresh website.
[226.68 --> 232.90]  It's really a fresh take, I think, on education and documentation for, like, popular web libraries.
[233.24 --> 234.62]  So, like, kudos to y'all.
[235.14 --> 236.80]  So anyways, I'm going to stop yapping.
[237.04 --> 241.76]  Let's first get into, like, introducing who Rachel is, and then we'll get into some of
[241.76 --> 242.88]  those specifics next.
[243.06 --> 244.28]  So hello, Rachel.
[244.28 --> 249.10]  Rachel, you can tell I'm excited because I've been talking nonstop for about two minutes.
[250.28 --> 252.20]  Can you tell us who you are?
[252.30 --> 253.52]  Tell us a little bit about yourself.
[254.24 --> 255.44]  I'm Rachel Neighbors.
[255.62 --> 261.68]  I am the documentation engineer working with the React core team, as well as React Native
[261.68 --> 266.52]  and Relay, which is a React data solution you may or may not have heard about in the open
[266.52 --> 267.24]  source ecosystem.
[267.90 --> 271.58]  But basically, the React fam of technologies, as I like to think of them.
[271.58 --> 276.52]  So I started out, actually, came in working on React Native's documentation.
[277.12 --> 281.36]  And lately, I've been working with the React core team on the React documentation as well.
[281.74 --> 282.38]  That's awesome.
[282.88 --> 287.42]  And what's it been like to, you know, I know you used React before you had joined the company,
[287.52 --> 291.46]  but I mean, what's it been like to work closely with the React team and, like, be able to kind
[291.46 --> 294.96]  of see that part of the sausage, you know, come together?
[295.70 --> 299.90]  Well, the interesting thing about the React core team is that they are engineers.
[299.90 --> 303.86]  If you've worked with engineers before, you can kind of imagine what it might be like to
[303.86 --> 304.96]  work with the React core team.
[305.68 --> 307.48]  It's definitely different, though.
[307.60 --> 312.14]  I really like working on a team that's building things that other people are using to build
[312.14 --> 313.78]  their own solutions to problems.
[314.56 --> 318.70]  And I think that was the real attraction for me about working with the React team.
[319.24 --> 323.32]  I used to work with the W3C on APIs and standards.
[323.92 --> 328.16]  And for a little while, I worked on Edge, the browser over at Microsoft.
[328.16 --> 332.60]  I've always liked working on the things that enable other people.
[333.34 --> 338.72]  And that team here working on React at Facebook, well, I think it's meta now.
[338.92 --> 345.98]  But anyway, this team really focuses on the impact that React has across so many people's
[345.98 --> 350.08]  developer experiences across the open source ecosystem.
[350.08 --> 354.86]  I think it's interesting because you can kind of, when you're going back through the blog posts
[354.86 --> 361.02]  on the React site, you can see how React started as this kind of cool skunkworks.
[361.58 --> 365.68]  You know, what if we thought about building interfaces as components?
[366.06 --> 366.52]  Yes.
[366.54 --> 370.64]  And you could, like, compose components into greater interfaces.
[370.92 --> 375.00]  And, you know, design systems in parallel, we're thinking about componentizing design.
[375.00 --> 380.16]  So it's interesting to see, like, the JavaScript community and the design community both thinking
[380.16 --> 383.76]  more and more about, like, yeah, we just need to get a slider in there.
[383.88 --> 386.48]  We do not need to reinvent the slider.
[386.58 --> 387.24]  We need that slider.
[387.32 --> 388.46]  Yes, that slider there.
[388.76 --> 391.32]  It's interesting to see that evolving over time.
[391.50 --> 396.64]  And you can tell that originally React was, like, you know, kind of this niche, small,
[397.12 --> 399.26]  ooh, maybe this is a new way of thinking about it.
[399.28 --> 400.46]  Everyone was using Angular.
[400.72 --> 401.92]  Angular 2 was coming out.
[401.92 --> 404.82]  And then it just took off.
[405.62 --> 410.34]  And suddenly you go from, you know, like, oh, React is this cool alternative to, like,
[411.08 --> 416.64]  React's website gets 2 million developers visiting it from all over the world every month.
[416.86 --> 419.90]  And React's dev tools are used by 3 million developers.
[420.44 --> 425.48]  It's just like, oh, ah, hello there.
[425.92 --> 430.30]  Yes, you are using this very important JavaScript library.
[430.30 --> 441.48]  And I think that's been the most interesting thing about working on the team is that it still very much has the vibe of that original sentiment of let's try building interfaces in a different way.
[441.68 --> 445.76]  Only it has a huge, huge consuming audience.
[445.76 --> 452.38]  Now, it's gone from being a niche project to a stadium project in a very quick amount of time if you look at the numbers.
[452.94 --> 457.34]  Yeah, no, I mean, the adoption of React is just kind of really massive.
[457.78 --> 467.28]  And to kind of just give everybody a mental model for what the scale of the web is, React is still used by only 2% of websites on the internet.
[467.28 --> 473.36]  So, like, think about how widely React is adopted and then think that's only 2%.
[473.36 --> 476.44]  So, like, just that's how massive the web is.
[476.52 --> 479.48]  But that 2% is a ridiculous amount of traffic.
[479.62 --> 481.78]  It's, like, in the millions, billions, right, Rachel?
[481.96 --> 483.72]  I mean, well, Facebook alone, it's in the billions.
[484.28 --> 487.06]  So, yeah, Facebook plus plus all the other websites.
[487.28 --> 488.40]  So, I mean, it's huge.
[489.06 --> 490.00]  It's really incredible.
[490.00 --> 492.30]  And so, like, what's your relationship with React?
[492.42 --> 493.76]  Like, how is your relationship?
[493.86 --> 499.18]  So, it was really nice to hear you describe, like, what it's been like for you to witness it all come together and that experience.
[499.26 --> 505.28]  But how is your relationship with React, the library, changed now that you're kind of on the quote-unquote inside?
[505.82 --> 511.16]  Well, to be honest, I kept trying to learn React and kept not making it stick.
[511.30 --> 513.46]  It would just go in one ear and out the other.
[514.02 --> 517.20]  And I was like, well, maybe I need a job where I'm working with React.
[517.20 --> 520.80]  But at the time, I was thinking about what I wanted to do next.
[521.06 --> 525.82]  And I was like, you know, I could just learn React from the people who build it.
[525.94 --> 526.90]  Oh, look over there.
[527.00 --> 528.48]  There's a team.
[528.82 --> 530.16]  They work with React a lot.
[530.58 --> 532.40]  Hello, do you need any assistance?
[532.62 --> 533.68]  Can I do anything for you?
[534.26 --> 536.08]  Oh, yeah, okay, yeah.
[536.44 --> 538.50]  Yeah, let's write some educational materials.
[538.58 --> 539.46]  I'm pretty good at that.
[539.46 --> 551.06]  So, partly, I ended up taking on these projects and this mission to teach people React and React Native was partly because I wanted to learn it myself.
[551.44 --> 567.46]  I came in with a bunch of really weird notions about React that I picked up, like many of us do, in the community, reading Medium posts, watching YouTube videos, taking the odd course that probably is a couple years out of date, and getting into really grokking React.
[567.46 --> 576.54]  I realized it was a lot different from what I'd been led to believe and wanted to share some of those learnings with other people.
[576.92 --> 588.10]  When you work on a team building something for so long, it can be easy to lose track of the beginner's mindset, that fresh, I have no idea how props and state work.
[588.56 --> 589.50]  The je ne sais quoi.
[589.90 --> 590.10]  Yeah.
[590.10 --> 592.32]  The literally je ne sais quoi.
[593.56 --> 596.42]  It's like the literal je ne sais quoi, you know?
[596.64 --> 598.38]  Yeah, you don't know what the hell you're doing.
[598.70 --> 598.94]  Right.
[599.18 --> 600.80]  So, yeah, I get it.
[600.96 --> 609.96]  And that can be surprisingly valuable, especially if, you know, you're writing materials for other folks who are coming in for the first time as well.
[610.24 --> 610.50]  Yeah.
[610.50 --> 622.94]  What do you think is the, like, the biggest thing either people have trouble with when they're first starting to learn React, or the biggest thing that you can lose track of, like, after you've been using React for three, five plus years?
[622.94 --> 631.00]  I'd like to think that the beta docs actually changed this, because I know for me, it was really grokking how rendering works.
[631.50 --> 640.52]  In the older docs, you could really only find out what rendering was by, there was, like, one paragraph on the site that briefly describes render and commit processes.
[641.30 --> 647.14]  Now, these were perhaps less important to know about back when we had classes and lifecycle methods.
[647.40 --> 650.46]  You just had to memorize the lifecycle methods, and there you go.
[650.46 --> 657.48]  But Hooks really leans on understanding the render and commit process behind React.
[657.66 --> 667.10]  Rendering is when React calculates the component based on how a state has changed, and commit is when that component goes and is inserted into your platform's tree.
[667.42 --> 669.98]  When I say platform tree here, you're probably thinking, what is it?
[670.46 --> 675.54]  I'm talking about if you're working on the web, that would be your DOM, you know, your document object model.
[675.54 --> 681.38]  But React can actually output to different platforms, including iOS and Android via React Native.
[681.66 --> 682.54]  They have different trees.
[682.68 --> 684.20]  They have UI view trees.
[684.86 --> 690.88]  So platform tree is in turn a lingo saying whatever it is that React is spitting out to, that.
[691.04 --> 694.84]  It's usually a tree full of nodes representing content and data.
[694.84 --> 699.48]  But when I first came in, I wasn't really sure how the state was working.
[699.68 --> 706.42]  I mean, when you look at Vue and you look at other kinds of UI platforms, they tend to have more mutable state models.
[706.64 --> 707.98]  But React is different.
[708.06 --> 709.14]  It has one-way data flow.
[709.32 --> 711.58]  You have to deliberately set the state.
[711.86 --> 717.00]  And that act of setting the state tells React, yo, things have changed.
[717.56 --> 718.50]  Look at that component.
[718.68 --> 720.84]  Did that component change because the state has changed?
[720.84 --> 729.76]  If it has changed, go to that platform tree and make any necessary adjustments, the render and the commit process.
[730.40 --> 734.48]  And that was something, like, once you get that, everything else really falls into place.
[734.84 --> 740.08]  Hooks, the API that you use with React, it lets you hook into different parts of this process.
[740.60 --> 742.06]  Like, you use effects.
[743.02 --> 745.50]  They happen after the render process.
[745.50 --> 751.36]  And state itself kicks off set state, that hook, it kicks off the render process.
[751.90 --> 759.52]  Anyway, that, I think, grokking that when you come in, just like, oh, oh, I'm telling React what to do with these APIs.
[759.62 --> 760.24]  That's pretty cool.
[760.70 --> 767.10]  I think that is the difference between really succeeding and running with React and being like, what is going on here?
[767.10 --> 776.44]  And now it's like the new docs are completely written from the ground up with hooks first so that you really understand these internal processes.
[776.84 --> 790.62]  I think as you go on with your React journey, the challenge has become more about edge cases and interacting with external libraries, things that want to manipulate the DOM that maybe React has some control over.
[791.04 --> 794.72]  And how do you tell React, hey, I'm touching your things, React.
[795.16 --> 796.34]  React, I'm touching your things.
[796.34 --> 798.40]  And I hope this is consensual touch, Rachel.
[798.94 --> 800.98]  I was thinking more like, you know, little kids.
[801.04 --> 802.00]  I'm touching your CD.
[803.28 --> 803.92]  Yes, yes.
[803.96 --> 804.54]  I'm just joking.
[804.62 --> 805.36]  I'm in the basement.
[805.50 --> 806.86]  I'm messing with your stuff.
[807.20 --> 808.36]  Are you going to come down here?
[808.38 --> 808.90]  Oh, I see.
[809.04 --> 809.50]  Yeah, yeah.
[809.70 --> 809.92]  Yeah.
[809.98 --> 810.92]  That type of yes.
[811.04 --> 811.30]  Right.
[811.54 --> 811.80]  Okay.
[813.30 --> 818.88]  The challenge is more around figuring out the escape hatches from the React system.
[819.22 --> 819.44]  Yeah.
[820.00 --> 820.68]  No, for sure.
[821.28 --> 826.20]  Amelia's kind of like this interesting brain to, I think, have on this conversation because, like, she's got the, like,
[826.20 --> 830.54]  unicorn thing going where she's, like, designer, excellent, developer, excellent.
[830.76 --> 832.46]  Like, she's, like, a designer developer.
[833.00 --> 835.70]  So, you know, I think, like, yeah, I don't know.
[835.92 --> 836.98]  What do you think, Amelia?
[837.22 --> 841.96]  Like, it feels like your world is bridging a little bit in some ways, like, with these improvements.
[842.76 --> 851.66]  Yeah, I haven't had a chance to dig in really deep with the new docs, but I love how there's, like, the interactive sandboxes.
[851.72 --> 855.26]  You have challenges you can do in the docs themselves.
[855.72 --> 857.14]  There's, like, gotchas.
[857.66 --> 858.08]  Oh, yeah.
[858.08 --> 861.80]  Callouts of, like, oh, you might think this, but actually it's this other thing.
[862.28 --> 868.92]  Like, those are all really great ways to teach as well because you're, like, trying to think of, like, common problems people might have
[868.92 --> 873.24]  and also letting them invalidate their wrong mental models with the challenges.
[873.48 --> 879.46]  So, like, if you think it's one way and then you try it and it doesn't work out, then, like, it's a really quick feedback cycle,
[879.74 --> 882.14]  which I think those are really awesome.
[882.14 --> 889.64]  Were those, like, always in the plan when you were at the beginning, like, were going to have interactive components, like, littered throughout the docs,
[889.64 --> 892.20]  or is that kind of, like, a stretch goal?
[892.88 --> 893.44]  No, man.
[893.64 --> 897.84]  These were the, first off, Amelia, by the way, big fan.
[898.16 --> 902.10]  I absolutely love what you do in the doubt of his face.
[902.42 --> 906.98]  And I haven't said this to you in person, I don't think, but congratulations on your book.
[907.44 --> 910.56]  It's beautiful, and I have immense respect for your work.
[911.12 --> 911.58]  Thanks, Rachel.
[911.58 --> 913.60]  Now, back to the React world.
[914.14 --> 914.84]  You're pretty awesome.
[915.46 --> 917.36]  Maybe, let's be honest, it's a room full of awesome today.
[917.48 --> 917.86]  It's true.
[918.08 --> 920.06]  So, let's see.
[920.66 --> 921.06]  Hang on.
[921.20 --> 921.66]  You know what?
[921.98 --> 923.46]  It's a little late here in London time.
[923.94 --> 925.68]  I completely forgot what I'm responding to.
[925.74 --> 933.56]  Now, the question, like, was it intentional for you to do, like, all that, like, interactive, like, the sandboxes and the visuals and the gotchas?
[933.72 --> 936.54]  And, like, was all of that, like, a stretch goal or was that, like...
[936.54 --> 936.82]  Yes.
[936.92 --> 939.66]  See, I'm listening to Amelia, Rachel, for God's sake.
[939.66 --> 940.92]  No, that was baked in.
[941.48 --> 942.22]  You know, but that's okay.
[942.28 --> 943.18]  Anyways, we're good.
[943.24 --> 943.72]  You're forgiven.
[944.04 --> 944.96]  You're Rachel, neighbors.
[945.10 --> 946.04]  You can do no wrong.
[946.44 --> 948.14]  Rachel, you can do no wrong.
[948.26 --> 948.54]  Okay?
[948.66 --> 949.14]  It's fine.
[949.26 --> 949.90]  This is a...
[949.90 --> 950.24]  Oh, trust me.
[950.32 --> 952.14]  I can do plenty of wrong.
[952.14 --> 959.14]  This is a fart cloud that smells like strawberries and, like, fresh, like, chocolate chip cookies, okay?
[959.30 --> 960.50]  Like, you can do no wrong.
[961.84 --> 965.62]  You know, if I could come up with a pill that would do that, I would be a millionaire.
[966.20 --> 970.56]  I feel like there are entire crack teams of scientists working towards solving that problem.
[970.70 --> 970.92]  Yeah.
[971.12 --> 971.96]  Right, right, right.
[972.02 --> 973.86]  It's like, my farts smell like cookies.
[974.32 --> 974.84]  You know?
[975.06 --> 976.14]  That is Rachel neighbors.
[976.38 --> 977.16]  Genetic engineering.
[977.16 --> 978.46]  Actually, Rachel...
[978.46 --> 979.12]  It's going to be an add-on.
[979.32 --> 980.38]  That could be your tagline.
[980.48 --> 981.46]  My farts smell like cookies.
[981.56 --> 984.78]  Like, that could be your entire, like, your branding as an engineer.
[985.14 --> 987.72]  Like, it's like, I'm going to, like, you know...
[987.72 --> 991.98]  That will attract the wrong crowd of people.
[992.60 --> 993.64]  Okay, no, that's true.
[993.74 --> 994.64]  All right, back on track.
[994.78 --> 995.32]  Back on track.
[995.62 --> 995.80]  So.
[996.16 --> 996.40]  So.
[996.62 --> 997.98]  That is a great question.
[999.12 --> 1003.88]  So, working on the React Native documentation, like, I used to be a UX designer.
[1004.00 --> 1006.16]  I have been way too many roles in my career.
[1006.16 --> 1009.14]  Now I get to add documentation engineer onto the list.
[1009.62 --> 1010.06]  Wow.
[1010.26 --> 1012.28]  I just, I'm interested in things.
[1012.38 --> 1014.08]  And I wander over, like, hello, Fran.
[1014.66 --> 1015.38]  What are you doing?
[1015.38 --> 1019.82]  You are a misshapen puzzle in a world of squares and circles.
[1020.16 --> 1022.40]  And so, like, you can fit anywhere.
[1022.76 --> 1026.22]  And so, like, I think you're just a really adaptable person.
[1026.68 --> 1031.06]  And I think that's why your career is so awesome and different all the time.
[1031.16 --> 1032.76]  Like, I think that's a skill.
[1032.94 --> 1036.26]  And I think it's something, you know, it's like, I'm making a...
[1036.26 --> 1039.88]  This is a safe space for you to acknowledge, Rachel Ray neighbors,
[1040.38 --> 1042.60]  that you are a highly adaptable human being.
[1042.68 --> 1043.98]  And, like, that's badass.
[1044.26 --> 1045.00]  This is on YouTube.
[1045.00 --> 1046.86]  This is hardly a safe space.
[1048.18 --> 1048.84]  Well, no.
[1049.08 --> 1051.06]  Yeah, YouTube is not the primary outlet.
[1051.24 --> 1054.50]  But, yes, we are currently striving, streaming live on YouTube.
[1054.72 --> 1055.70]  Like and subscribe, everyone.
[1056.14 --> 1056.28]  So.
[1056.86 --> 1057.50]  Hello, YouTube.
[1058.04 --> 1060.44]  So, you may have recalled that I originally...
[1061.00 --> 1063.80]  The first task that was set for me when I came and was like,
[1064.30 --> 1067.18]  all right, I gotta go work with the people who build this stuff.
[1067.30 --> 1068.30]  All right, what am I gonna do?
[1068.34 --> 1070.72]  And they're like, all right, Rachel, spin this straw into gold.
[1071.14 --> 1073.60]  This is how everything I do in my life starts.
[1073.60 --> 1076.56]  It's like, yes, I can totally spin this straw into gold.
[1077.14 --> 1082.02]  The React Native documentation needed a bit of love when I arrived.
[1082.36 --> 1083.56]  And that was my first task.
[1083.66 --> 1085.60]  Turn the React Native documentation around.
[1086.54 --> 1088.26]  It was sorely out of date.
[1088.60 --> 1092.66]  Ran some community API documentation update drives around that.
[1092.66 --> 1093.54]  Love you guys.
[1094.12 --> 1097.20]  And adding more on-ramps, et cetera.
[1097.54 --> 1099.56]  The point was, I didn't just arrive and start writing.
[1099.90 --> 1102.58]  No, because I used to be a UX person back in the day.
[1102.68 --> 1106.08]  I was like, yeah, but you say the docs need work.
[1106.16 --> 1107.62]  But what exactly needs done?
[1108.04 --> 1109.22]  What do we need to do?
[1109.60 --> 1112.80]  Well, we should just ask the people who are using them what they'd like.
[1112.80 --> 1120.82]  So, you know, conducted user interviews, formulated a couple of ideas, really got to know the React Native community over here in the EU, which is really cool.
[1121.28 --> 1122.52]  It's a pretty hop in place.
[1123.02 --> 1130.76]  And started running surveys for the React Native and React communities to really start feeling out what it was that we were lacking, what they wanted more of.
[1130.76 --> 1136.90]  And one thing that came through for both communities time and time again was, needs more examples, interactive examples.
[1137.16 --> 1140.08]  I see the code, but I'm not going to spin up an environment.
[1140.62 --> 1141.40]  Like, come on.
[1141.54 --> 1143.22]  Yeah, especially a React environment.
[1143.40 --> 1149.14]  I mean, there was an entire freaking side baby project company born out of that called Create React App.
[1149.46 --> 1153.86]  Like, it was complex to do React on your own, and especially as a new engineer.
[1154.06 --> 1155.46]  So, like, the pain is real.
[1155.62 --> 1157.24]  Like, that's not even exaggerated, right?
[1157.44 --> 1159.40]  Like, React is not a platform.
[1159.40 --> 1160.32]  It's a UI library.
[1160.32 --> 1160.90]  Let's be honest.
[1160.98 --> 1162.82]  It's like, it's not even a hammer.
[1162.98 --> 1163.58]  It's a nail.
[1163.98 --> 1165.00]  Yeah, 100%.
[1165.00 --> 1170.14]  This would be like if you invited someone to a craft workshop and said, here are all these nails.
[1170.80 --> 1171.78]  Okay, great.
[1172.20 --> 1173.14]  I love the nails.
[1173.32 --> 1174.62]  What do I do with them?
[1174.86 --> 1180.04]  So, to show you the nails, it's great if you can give people, like, here's a piece of wood and a hammer.
[1180.50 --> 1183.14]  Now, hammer all the nails you want here.
[1183.28 --> 1185.34]  And that's sort of what the interactive examples do.
[1185.38 --> 1187.06]  You don't have to worry about spinning up an environment.
[1187.06 --> 1190.36]  You don't have to make big decisions like, next or guts fee.
[1190.68 --> 1191.90]  Or should I spend my own?
[1192.06 --> 1192.52]  I don't know.
[1192.70 --> 1194.12]  No, just go poke the code.
[1194.44 --> 1196.34]  Poke the code until you're in love with the code.
[1196.72 --> 1198.68]  Then you can make all those life-changing decisions.
[1198.94 --> 1200.70]  I mean, stack-changing decisions.
[1201.16 --> 1204.16]  But no pressure, no commitment, no renewal fees.
[1204.76 --> 1205.32]  Get in there.
[1205.32 --> 1210.54]  So, implemented these with these interactive examples for React Native, which were an even bigger challenge.
[1211.16 --> 1212.18]  And they took off.
[1212.28 --> 1212.92]  Everyone loved them.
[1213.00 --> 1215.28]  They loved the API docs having interactive examples.
[1215.78 --> 1219.28]  They loved that every single example on the site was suddenly interactive.
[1219.46 --> 1224.80]  There were a bunch of other little things that were tested out in the React Native docs effort that tested so well.
[1225.10 --> 1228.30]  Got such great feedback before and after, having made good on these.
[1228.30 --> 1234.62]  When we saw the same things going on with React docs, it was like, well, we know exactly what to do here.
[1235.36 --> 1237.48]  Anyway, the new interactive examples.
[1237.58 --> 1242.68]  I want to give a shout-out to our partners at CodeSandbox because they were working on this cool Sandpack API.
[1243.24 --> 1250.58]  You can actually go use this API to embed interactive examples from CodeSandbox on any project of your own.
[1250.58 --> 1252.84]  It works really well with MDX.
[1253.46 --> 1260.52]  So, when future people are wanting to update examples or add examples to the React documentation, you can just do it right there in Markdown.
[1260.88 --> 1261.80]  Even edit the CSS.
[1262.08 --> 1262.86]  It's super cool.
[1263.24 --> 1265.88]  Just a great workflow for the contributor.
[1266.44 --> 1268.06]  And I just wanted to give them a shout-out.
[1268.18 --> 1268.96]  They did a great job.
[1269.46 --> 1270.48]  It was a pleasure to work with them.
[1270.70 --> 1274.28]  Actually, I set that up, like, yesterday or two days ago.
[1274.46 --> 1275.56]  And it was so nice.
[1275.74 --> 1280.34]  You just, this is the one where you just hit the, like, you just get an endpoint.
[1280.58 --> 1282.18]  And you send it some code.
[1282.38 --> 1284.10]  And it's like, here's your Sandbox ID.
[1284.48 --> 1285.60]  And you can just include it.
[1285.60 --> 1292.32]  I really hope to see more people embedding interactive examples into their teaching materials.
[1292.60 --> 1293.88]  I think it's just fabulous.
[1294.52 --> 1295.88]  It should change the way people learn.
[1296.30 --> 1298.18]  These tool chains are getting more and more complex.
[1298.44 --> 1309.54]  It's harder and harder to ask somebody, you know, like, one of the things when doing research on how people learn is that the start of any boot camp is usually just installing dependencies.
[1309.54 --> 1312.48]  And, you know, run this line on your terminal.
[1312.78 --> 1313.82]  You know, run this, run that.
[1313.90 --> 1314.84]  Oh, no, that didn't work.
[1314.94 --> 1315.82]  Brew install this.
[1316.12 --> 1317.24]  Did you update that?
[1317.56 --> 1318.32]  Delete that file.
[1318.44 --> 1318.80]  Rerun.
[1319.00 --> 1321.98]  And it's a huge barrier to play.
[1322.44 --> 1323.16]  And let's be honest.
[1323.54 --> 1326.74]  A lot of folks are not learning React to build something from scratch.
[1326.92 --> 1330.22]  They're learning React so that they can work on something that was built in React already.
[1330.66 --> 1332.52]  So that's a waste of their time.
[1332.52 --> 1337.28]  They just want to figure out why set state isn't doing the thing they expected.
[1337.84 --> 1342.92]  They don't want to have to, like, go figure out how to start a blog site.
[1343.36 --> 1347.82]  Yeah, how to start a blog site or what Babel transform are you missing?
[1348.44 --> 1353.70]  You know, ma'am who does yet to know what even, like, JavaScript is or something, right?
[1353.72 --> 1354.46]  Like, it's crazy.
[1355.04 --> 1356.98]  So, you know, the barrier to entry is very real.
[1356.98 --> 1359.90]  So I think we've kind of squirted around a bunch of things in this site.
[1360.02 --> 1365.08]  So can I just, just for the sake of it, let's, from your own words, like, what is this project about?
[1365.86 --> 1367.94]  And, like, what were the goals?
[1368.10 --> 1373.84]  And then we are going to take a break after that because there's so much to dig into, I think, off of that discussion.
[1374.06 --> 1375.82]  So close us out, Rachel, neighbors.
[1376.52 --> 1376.84]  All right.
[1377.14 --> 1381.48]  The goal, our mission in this project, your mission, should you choose to accept it,
[1381.48 --> 1387.02]  was to provide the best React education in the industry for anyone who wants to get started or dive deep,
[1387.18 --> 1389.16]  no matter their background, income, or location.
[1389.88 --> 1397.60]  The goal was to create this resource that would teach people not just, you know, what is React,
[1397.96 --> 1401.22]  but how to think and react, how to go from good to great and react.
[1401.84 --> 1407.50]  And if they were having some problems somewhere, you know, wanting to know what that third argument in an API is,
[1407.82 --> 1410.36]  that they would have a reliable resource they could go back on.
[1410.36 --> 1415.08]  Additionally, we wanted to give this to people who are training folks to learn React 2,
[1415.18 --> 1417.98]  people who are writing articles, who are running meetups and workshops.
[1418.48 --> 1422.68]  We want them to be able to be like, yeah, if you're struggling with that, just check out the React docs.
[1423.02 --> 1425.52]  Or we're introducing you to this API today.
[1425.88 --> 1430.72]  Link goes to one page in the React docs that has anything to answer any question,
[1430.86 --> 1432.76]  any hiccup that people might have.
[1432.76 --> 1439.82]  We wanted to create a resource that would empower the community to become authority in their own right.
[1440.36 --> 1452.60]  What's up, party people?
[1452.68 --> 1455.10]  This episode is brought to you by Sentry.
[1455.32 --> 1457.96]  Sentry just shipped their SDK for Next.js.
[1457.96 --> 1464.64]  Now, in your Next.js apps, you can capture errors, measure performance, manage releases, configure suspect commits,
[1464.96 --> 1471.14]  and automatically upload source maps to view unminified JavaScript and TypeScript with zero-ish configuration.
[1471.60 --> 1476.06]  You can get your events enriched with device data, breadcrumbs created for outgoing HTTP requests,
[1476.48 --> 1479.08]  release health for tracking crash for users and sessions,
[1479.58 --> 1482.14]  and automatic performance monitoring for both the client and the server.
[1482.14 --> 1484.66]  Check for a link in the show notes for details to this release.
[1485.04 --> 1488.16]  JS Party listeners new to Sentry get the team plan for free for three months
[1488.16 --> 1492.90]  when you sign up and use the code PARTYTIME at the Sentry.io and use the code PARTYTIME,
[1492.98 --> 1494.52]  because, hey, it's PARTYTIME, y'all.
[1494.52 --> 1511.56]  Okay, Rachel, those are some really great goals.
[1511.72 --> 1517.10]  I'm really curious to hear if you think you have achieved them or you are on track to achieve them.
[1517.10 --> 1522.54]  And also, can you share some insights onto, like, the big TBD section that's on the website right now,
[1522.58 --> 1529.28]  where it's like, we're this percent complete with the API docs, we're this percent complete with the learning docs, right?
[1530.04 --> 1532.12]  So can you speak more about that?
[1532.70 --> 1532.88]  Awesome.
[1533.22 --> 1537.00]  So, yeah, we're about 75% done with the learning documentation.
[1537.50 --> 1544.56]  That's because the remaining documentation is mostly, well, how to use things around edge cases.
[1544.56 --> 1551.94]  You know, like, effects are largely used for doing things with React, interacting with things outside React.
[1552.42 --> 1556.62]  There's additionally, you know, going to have to add some things for React's developer tooling,
[1556.86 --> 1557.96]  which is coming later this year.
[1558.26 --> 1563.32]  So there's some stuff that we didn't have finished, but we had enough done that we didn't want to hold back
[1563.32 --> 1564.74]  until things were, like, perfect.
[1565.10 --> 1568.72]  We wanted to make sure that we were actually getting the content to the community.
[1569.36 --> 1573.20]  The API documentation itself is still very nascent.
[1573.20 --> 1580.78]  We want to really make sure that we are, because hooks are very challenging to document compared to more traditional APIs.
[1581.26 --> 1583.38]  They are deeply nested.
[1583.64 --> 1587.94]  They do interesting things with, you know, like, there's this thing that returns a function,
[1588.08 --> 1591.68]  that returns a cleanup function, and it takes a dependencies array,
[1591.84 --> 1595.04]  but it does different things depending on the state of that array.
[1595.04 --> 1604.36]  And a lot of those APIs depend on how we document that last 25% of content, how we explain how to use them.
[1604.62 --> 1608.40]  So there's sort of roadblock by finishing the rest of the guides themselves.
[1608.78 --> 1610.08]  So there's still an in route.
[1611.12 --> 1615.68]  Now, the community, of course, is very eager to assist in any way possible.
[1616.10 --> 1618.46]  And that is awesome, and we appreciate it.
[1618.46 --> 1621.24]  But we're not quite ready to accept community assistance.
[1621.76 --> 1628.06]  These flagship pieces of documentation are really things that come right from the core's heart.
[1628.72 --> 1630.86]  And it's not just something you can churn out.
[1631.00 --> 1631.64]  I would know.
[1631.86 --> 1632.58]  I've tried.
[1633.04 --> 1637.02]  It really does get a lot of input from the core team.
[1637.38 --> 1639.66]  So there's a lot of nuance, right, is what you're saying.
[1639.86 --> 1641.46]  Like, not only nuance, but like...
[1642.32 --> 1644.92]  Well, I guess, do you ever get pull requests on your documentation?
[1645.48 --> 1646.28]  Question mark.
[1646.60 --> 1647.06]  We do.
[1647.06 --> 1647.66]  Okay.
[1648.08 --> 1651.90]  And we really appreciate pull requests for things like, you know, typos.
[1652.32 --> 1654.42]  This example could be done like that.
[1654.88 --> 1660.94]  I actually did partner with a couple of people from the community to work on the documentation so far.
[1661.04 --> 1662.04]  And we'll continue to do so.
[1662.14 --> 1664.74]  For instance, I want to give a shout out to Sylvia Vargas.
[1665.28 --> 1668.94]  Originally, all our docs had kittens in the examples.
[1669.24 --> 1671.52]  We were using place kitten for everything.
[1671.96 --> 1675.60]  And I loved putting the cats jokes in there.
[1675.60 --> 1678.48]  But cats are not very inclusive.
[1678.90 --> 1679.90]  Not everyone loves cats.
[1680.02 --> 1681.40]  Not every culture loves cats.
[1681.98 --> 1688.96]  So we were like, we should do something with these docs that really showcases all of humanity, right?
[1689.26 --> 1692.44]  Great scientists, cities, art, that sort of thing.
[1692.44 --> 1702.44]  And partnered with Sylvia, who went through and updated all of the examples to showcase these amazing topics and really bring an added spark.
[1702.44 --> 1707.74]  But there will be ways in the future for the community to have even more impact.
[1707.86 --> 1710.04]  There'll be a translation effort that will kick off.
[1710.60 --> 1712.82]  And that is a great time to get involved then.
[1713.22 --> 1719.06]  But for now, we're mostly writing and generating and editing the content on team and with the people we've been partnering so far.
[1719.06 --> 1721.78]  It's like getting mentored by a team member.
[1721.78 --> 1723.48]  So it's pretty awesome.
[1723.64 --> 1726.90]  I feel great about the quality that that has been produced so far.
[1727.42 --> 1727.54]  Yeah.
[1727.76 --> 1729.16]  No, that makes a lot of sense.
[1729.26 --> 1732.96]  I mean, I'm like a completely rational decision.
[1732.96 --> 1738.78]  And I think good move, you know, to make sure you can take full ownership of the message, right?
[1738.82 --> 1742.34]  Like you can own the mistakes and you can own the success.
[1742.34 --> 1743.70]  Like I get that.
[1743.82 --> 1744.46]  So that's awesome.
[1744.86 --> 1745.96]  I'm just kind of curious.
[1745.96 --> 1752.86]  Like I was going to ask about like I've noticed like that there's more diverse example, like just everything.
[1752.86 --> 1753.98]  It's not even just examples.
[1753.98 --> 1757.88]  It's like imagery, examples, iconography, like whatever.
[1758.04 --> 1761.82]  Like it's just it feels more diverse and inclusive.
[1761.82 --> 1768.96]  And I couldn't quite put my finger on it because I initially thought like, oh, it looks like maybe they're just highlighting women in tech.
[1768.98 --> 1770.88]  And then I looked around and it's like, no, no, no, no.
[1770.88 --> 1772.20]  This is broader than that.
[1772.20 --> 1780.56]  And so really kudos to I guess Sylvia and to you also for listening and putting that feedback, you know, into action.
[1780.76 --> 1781.66]  So that's awesome.
[1782.32 --> 1790.58]  Is there like a formal feedback kind of channel that you establish with the community like around like questions and or whatever?
[1790.80 --> 1791.72]  Like I'm just curious.
[1791.82 --> 1798.94]  There are three ways you can give feedback on the docs and they're all linked to from the front page of the site at beta.reactjs.org.
[1798.94 --> 1803.44]  You can fill out a survey, privately drop your feedback directly to the team.
[1803.96 --> 1805.80]  You can leave a comment on GitHub.
[1806.16 --> 1808.02]  There's a sporting conversation going there.
[1808.10 --> 1811.32]  We get all the feedbacks, you know, for all kinds of things.
[1811.46 --> 1812.16]  And this is great.
[1812.26 --> 1813.78]  We love having that feedback.
[1814.00 --> 1816.74]  It often gets turned into an issue which someone acts on.
[1817.38 --> 1821.40]  I think we've got someone who made dark mode persistent recently.
[1821.48 --> 1822.00]  That's awesome.
[1822.68 --> 1823.44]  Adore that.
[1823.44 --> 1829.70]  But, you know, if you're shy, you can also leave feedback using the feedback button on each page.
[1829.78 --> 1833.00]  If you want to give us your feedback directly on something you saw.
[1833.66 --> 1835.06]  Maybe something wasn't working.
[1835.38 --> 1836.58]  Maybe something was confusing.
[1837.10 --> 1842.68]  This particular tool will let you tell us all about what you want, where you want it.
[1842.68 --> 1848.04]  And that's actually really helpful to us at this stage, getting that kind of feedback about what's working, what isn't.
[1848.44 --> 1851.84]  We really want to make sure that these docs do right by everybody.
[1852.10 --> 1854.78]  So if you do have that feedback, we do want to hear it.
[1854.98 --> 1860.04]  We hope we have made enough places and enough channels for you to get that feedback to us.
[1860.34 --> 1865.18]  You mentioned that you did a bunch of user experience interviews for the React Native docs.
[1865.86 --> 1867.64]  Have you been doing that with these docs?
[1867.96 --> 1869.52]  And, like, do you just do them at the beginning?
[1869.52 --> 1871.76]  Or have you been kind of doing them all the way through?
[1871.76 --> 1872.64]  Absolutely.
[1873.06 --> 1874.04]  Did them at the beginning.
[1874.32 --> 1875.74]  Did them with the prototype site.
[1875.92 --> 1877.38]  And did them, well, right now.
[1877.48 --> 1878.94]  We're kind of always taking feedback.
[1879.36 --> 1884.62]  You know, the sort of thing where you hand people the site and you just sit back and you watch them and take notes and ask them probing questions.
[1885.26 --> 1889.26]  The development of the site started that way and has continued onward that way.
[1889.78 --> 1894.62]  One of the challenges with this was, like, we could have, you know, it is a new design.
[1894.62 --> 1899.52]  We could have just designed things and thrown them over the wall and seen how they did.
[1899.52 --> 1903.30]  Or, you know, showed people designs with mock content in it.
[1903.30 --> 1911.02]  But we really wanted to test the design with the content and see where people were getting stuck, where they were doing well.
[1911.10 --> 1912.36]  We caught a lot of stuff early.
[1912.58 --> 1919.98]  For instance, networking issues that were making the examples take very, very long to load in, like, different parts of the world.
[1920.12 --> 1921.34]  We caught those so early.
[1921.72 --> 1923.54]  We were really happy we were able to do that.
[1923.54 --> 1929.22]  Other things, like, at first, people didn't realize that the interactive examples were interactive.
[1929.48 --> 1932.76]  They thought they were, right, interactive examples are still fairly new.
[1932.86 --> 1935.78]  They're going to be, like, old hat in a few days, I'm sure.
[1936.38 --> 1940.68]  But right now, people are still like, I thought that was a picture of the code.
[1940.84 --> 1942.76]  Or I expected that to be a code block.
[1942.76 --> 1950.36]  So we had to do some things where we rejiggered the design to make it look more interactive and more like a coding editor with numbers down the side, etc.
[1951.02 --> 1956.16]  But there is no way we would have known this if we'd just been, like, waterfall, launch everything with horns.
[1956.70 --> 1959.36]  So this is why we did so much testing along the way.
[1959.68 --> 1968.60]  There's also been surveys, formal surveys of people coming in and out of the testing pools to get a better idea of, like, how does this stack up against the old docs?
[1968.70 --> 1969.96]  Would you recommend it to a friend?
[1969.96 --> 1972.26]  And the signal has been strong.
[1972.52 --> 1973.50]  And it remains strong.
[1973.64 --> 1974.94]  We're still getting really good feedback.
[1975.50 --> 1976.56]  But now there's a question.
[1976.82 --> 1980.14]  Because, you know, you can sit over a person's shoulder and watch them for an hour.
[1980.34 --> 1983.70]  You can ask them to fill out a survey after they've interacted with the docs for a week.
[1984.28 --> 1990.42]  But now the question is, what kind of feedback do we get after people have been using the docs in beta for a while?
[1990.58 --> 1991.42]  That's the feedback.
[1991.68 --> 1994.88]  This is the third stage of user testing.
[1995.34 --> 1998.70]  And that's why we are exceptionally keen to get that feedback.
[1998.70 --> 2001.88]  And this is the uncharted territory stage, too, right?
[2002.20 --> 2008.22]  The super embarrassing stage where, like, podcast hosts might say things like, yeah, I tried the docs.
[2008.54 --> 2013.36]  But I got to ask, you know, like, when are you finishing all the API docs?
[2013.36 --> 2014.38]  Where's the close button?
[2014.68 --> 2015.26]  Just kidding.
[2015.40 --> 2016.28]  Hey, oh, gosh.
[2016.52 --> 2017.08]  Hey, no.
[2017.16 --> 2019.62]  I didn't ask that to be, like, prudish.
[2019.62 --> 2020.60]  No, I'm just saying.
[2020.60 --> 2020.64]  Prudish.
[2020.84 --> 2024.82]  I asked it to, like, say, hey, everyone's still a work in progress.
[2025.32 --> 2028.16]  Or, like, and really, I was going to ask, well, how can people contribute?
[2028.26 --> 2029.86]  But you answered that on your own.
[2030.36 --> 2031.92]  Maybe because you knew I was going to ask that.
[2032.00 --> 2033.44]  But still, thank you for doing it.
[2033.52 --> 2036.22]  Like, you saved me the, I didn't know what the answer was going to be.
[2036.28 --> 2038.86]  So you saved me the hassle of asking.
[2038.86 --> 2045.10]  I am pretty sure you asked about contributions, at least in your opening statement there.
[2045.22 --> 2045.84]  Oh, okay.
[2046.18 --> 2046.68]  I did.
[2046.76 --> 2049.26]  I'm pretty sure that I heard you mention that.
[2049.44 --> 2049.60]  Okay.
[2049.72 --> 2050.86]  Don't worry about that one.
[2051.42 --> 2054.86]  But no, what I mean is, like, now the feedback is more public.
[2055.20 --> 2058.36]  It's going to be one of those things where, you know, somebody might wake up in the morning
[2058.36 --> 2061.56]  and go onto Twitter and be like, the emperor has no new clothes.
[2061.58 --> 2061.82]  Right.
[2062.14 --> 2063.08]  Who knows?
[2063.08 --> 2069.34]  But you do have to eventually take your baby, release it into the wild, and see how it gets
[2069.34 --> 2070.10]  on with others.
[2070.44 --> 2072.76]  And it's all part of the iterative process.
[2073.34 --> 2076.88]  I think one of the things that's really awesome about the new documentation is that we really
[2076.88 --> 2081.50]  approached it like a product, like something we would develop, like we would solve all of
[2081.50 --> 2084.36]  these challenging issues that have come up for the community.
[2084.52 --> 2085.72]  We've been collecting this feedback.
[2085.86 --> 2087.74]  We know what we think people want.
[2088.10 --> 2090.82]  Now we've got to see if we actually solve those problems.
[2090.82 --> 2095.90]  And there's no better, no better way to test something than production.
[2096.32 --> 2096.46]  Yeah.
[2096.88 --> 2097.60]  You know, it's so funny.
[2097.70 --> 2101.94]  There's that saying, and I swear I have to remind myself all the time because I'm an
[2101.94 --> 2102.98]  absolute perfectionist.
[2103.48 --> 2108.50]  But it's if you wait till you're not embarrassed about your code to show your code, you've waited
[2108.50 --> 2109.28]  too long, right?
[2109.36 --> 2111.10]  Like, that is so true.
[2111.22 --> 2111.34]  Yeah.
[2111.38 --> 2114.94]  If you're if you wait till you're not embarrassed, then yeah, you've missed so many opportunities
[2114.94 --> 2118.12]  for early feedback that could have maybe even made it better.
[2118.12 --> 2118.42]  Right.
[2118.42 --> 2123.52]  Because that's the beautiful thing about feedback is like, you always are in a better place
[2123.52 --> 2124.18]  because of it.
[2124.34 --> 2129.02]  The collaborative experience, even if it just shifts you by one degree, like you are one
[2129.02 --> 2132.18]  degree better than you were without this feedback, you know?
[2132.22 --> 2137.34]  And so like, I can only imagine like, what it's like to kind of really be receiving that
[2137.34 --> 2141.46]  kind of feedback from a percentage of 2 million developers, right?
[2141.68 --> 2143.22]  That's a pretty big percentage.
[2143.22 --> 2148.42]  So we wanted to make sure that people were giving us like some stuff like networking issues.
[2148.42 --> 2153.14]  We don't want people to have to tell us that we should be doing that ahead of time.
[2153.22 --> 2157.24]  When you say that, do you mean like CDNs that CDN coverage that you needed to add?
[2157.28 --> 2160.26]  Or like when you say networking, do you mean just that the site was chunky?
[2160.56 --> 2162.08]  Like, what do you mean by networking?
[2162.08 --> 2166.40]  Yeah, we just had some issues in the beginning with when we were still working out how the
[2166.40 --> 2170.04]  interactive examples worked that, you know, in some places they took a little longer to
[2170.04 --> 2170.80]  render than others.
[2171.08 --> 2171.32]  Oh, yeah.
[2171.40 --> 2177.42]  And we didn't want to launch with something that was not polished enough for everybody.
[2177.88 --> 2181.62]  So there was a reason for keeping it behind a gate for a bit to make sure that everybody
[2181.62 --> 2186.78]  was going to have a great experience, that user testing was all around positive.
[2187.42 --> 2190.76]  People realized that the interactive examples were interactive, for instance.
[2190.76 --> 2192.52]  That was all good stuff.
[2192.82 --> 2196.44]  But now, now the real question is, how's it going to do in production?
[2197.10 --> 2202.34]  And you can only test on a subset of users for so long.
[2202.48 --> 2205.68]  Eventually, you do have to see how it's going to go.
[2205.70 --> 2206.72]  And you're absolutely right.
[2207.22 --> 2210.84]  Like, you can run all the tests on your code, make sure it's working.
[2211.04 --> 2216.66]  But in the end, doing the code review is going to probably give you the most insights.
[2217.04 --> 2218.42]  Eventually, you have to share.
[2218.42 --> 2218.80]  Yeah.
[2218.80 --> 2219.00]  Wow.
[2219.00 --> 2225.60]  I'm so curious if you have any, like, quantifiable metrics to know how it's doing or any, like,
[2225.68 --> 2227.76]  goals that you can measure.
[2228.28 --> 2228.86]  I have a couple.
[2229.18 --> 2235.14]  One thing that we measure across all the documentation in the React family is aha moments.
[2235.32 --> 2237.98]  Well, in the testing phases of the documentation.
[2238.60 --> 2243.22]  Actually looking at still testing to see if there's a way to let people tell us if they've had
[2243.22 --> 2249.72]  an aha moment on a page, this is a really good signal that the content is landing and that people
[2249.72 --> 2254.64]  are feeling like they're grokking something, like something has been a revelation to them.
[2254.70 --> 2256.28]  You know when you're having an aha moment.
[2256.80 --> 2259.52]  So that's one metric that's been really good for early testing.
[2260.14 --> 2265.52]  There's also questions that you can ask in a more mature documentation that's been released
[2265.52 --> 2265.88]  for a while.
[2265.98 --> 2269.62]  You can ask things like MDN does, which is, you know, did you find what you were looking
[2269.62 --> 2270.32]  for today?
[2270.74 --> 2272.78]  What were you here to do?
[2272.88 --> 2274.08]  Were you referencing documentation?
[2274.48 --> 2276.06]  Were you learning something from scratch?
[2276.14 --> 2277.32]  Were you decoding an error?
[2277.94 --> 2279.02]  Were you making a decision?
[2279.56 --> 2283.88]  And you can kind of, from these different things, you can triangulate where your documentation
[2283.88 --> 2285.68]  might need to be filled out more.
[2285.68 --> 2291.44]  This is a survey that you can share with like 1% of people who are visiting, and it kind of
[2291.44 --> 2296.82]  really helps you keep the pulse of your documentation so you don't necessarily have to, you know,
[2297.18 --> 2299.04]  run gigantic surveys once a year.
[2299.54 --> 2304.10]  This way you're getting a sample from all your user base throughout the year, and it's
[2304.10 --> 2304.98]  much less intrusive.
[2305.58 --> 2313.58]  Additionally, I like to use, there is this thing called Net Promoter Score, which is a measure
[2313.58 --> 2316.74]  of how likely someone is to recommend a resource.
[2317.30 --> 2319.72]  It has been abused all over the place.
[2319.88 --> 2324.08]  There are people who use Net Promoter Score with call centers, like, why would you do that?
[2324.52 --> 2327.64]  Like, that's just, you're just being mean to the people at the call center for that.
[2328.10 --> 2332.68]  Net Promoter Score doesn't really work well with people outside the American culture, because
[2332.68 --> 2338.66]  like, Germans, you ask a German person, like, how likely are you to recommend this on a scale
[2338.66 --> 2341.06]  from 1 to 10, and they will give you exactly what they feel.
[2341.06 --> 2346.88]  Which, Net Promoter Score is calibrated for Americans, where if it's not like a 9 or a
[2346.88 --> 2348.36]  10, you failed.
[2348.76 --> 2350.16]  They're not really into it.
[2350.26 --> 2353.94]  But, you know, like, in Germany, a 6 is actually pretty good.
[2354.18 --> 2355.14]  They did not hate it.
[2355.60 --> 2356.90]  It's more than half.
[2358.20 --> 2359.74]  Yeah, that's pretty good.
[2360.12 --> 2364.58]  So this is an interesting measure, and you really do have to read up on it before you start
[2364.58 --> 2365.14]  using it.
[2365.14 --> 2371.06]  But for me, from doing so much metric tracking with all the documentation efforts since getting
[2371.06 --> 2374.46]  here, it tracks really well with a bunch of other satisfaction metrics.
[2375.10 --> 2379.76]  So if that metric is doing well, I kind of expect that a bunch of other questions I could
[2379.76 --> 2384.18]  ask are also doing well, which means I don't have to ask people as many questions.
[2384.60 --> 2389.40]  How likely are you to recommend this particular set of documentation to a friend or a colleague?
[2389.40 --> 2396.00]  And that is a pretty good baseline from which you can compare before and after photos or
[2396.00 --> 2402.66]  compare, you know, how well is my JavaScript documentation doing next to my Android documentation?
[2402.94 --> 2405.48]  Well, NPS is X, NPS is Y.
[2405.64 --> 2409.08]  We can see that people are less likely to recommend this one.
[2409.24 --> 2410.36]  So let's investigate that.
[2410.72 --> 2413.34]  It's really good for taking the pulse and before and after pictures.
[2413.34 --> 2417.64]  You can always do page metrics, thumbs up, thumbs down.
[2417.82 --> 2421.42]  Those are great for tracking how people are feeling about the documentation after you've
[2421.42 --> 2422.42]  moved on from the project.
[2422.98 --> 2427.12]  They're a little less useful when you're doing beta testing on new content because you don't
[2427.12 --> 2430.34]  have a lot of people there thumbs upping and thumbs downing.
[2430.68 --> 2434.08]  You know, four people give you a thumbs up doesn't necessarily mean that that particular
[2434.08 --> 2434.86]  page is stellar.
[2435.52 --> 2437.94]  So that's the interesting thing about metrics.
[2438.36 --> 2442.58]  The more people you have giving you the data, the more trustworthy it is.
[2442.58 --> 2447.82]  When you're doing little tiny beta tests, you end up leaning more on qualitative feedback.
[2448.18 --> 2449.96]  You know, like, what did you think of the docs?
[2450.04 --> 2451.52]  People say, ah, this is amazing.
[2451.68 --> 2452.84]  It's exactly what I need.
[2453.16 --> 2454.26]  That's a really good signal.
[2454.74 --> 2458.64]  So it's a mixture when you're developing a new learning resource.
[2458.76 --> 2461.04]  It's a mixture of qualitative and quantitative.
[2461.50 --> 2466.40]  But once you release it into the wild, it really is helpful to have the quantitative metrics
[2466.40 --> 2471.96]  set up and running to help you ensure, you know, like, look and be like, oh,
[2471.96 --> 2476.00]  these docs haven't been updated in a while and they're getting a lot of thumbs down.
[2476.56 --> 2477.60]  You should look into that.
[2478.00 --> 2481.94]  Ah, getting a lot of feedback that people are coming to the references section, but they're
[2481.94 --> 2483.28]  not finding what they need.
[2483.88 --> 2484.10]  Hmm.
[2484.20 --> 2485.60]  I wonder what it is that they need.
[2485.74 --> 2487.24]  Let's dive into the comments.
[2487.90 --> 2493.28]  So metrics and both quantitative and qualitative are your friend in changing ways throughout the
[2493.28 --> 2494.96]  educational material development lifecycle.
[2495.44 --> 2496.38]  Did I answer your question, Amelia?
[2496.40 --> 2497.06]  Yeah, that was.
[2497.14 --> 2498.12]  I kind of gave you a dissertation.
[2498.24 --> 2498.66]  Very thorough.
[2498.82 --> 2499.88]  I really appreciate it.
[2499.88 --> 2501.26]  That was extremely thorough.
[2501.72 --> 2503.86]  I'm like, I should be taking notes, you know.
[2504.20 --> 2505.16]  But no, that was awesome.
[2505.30 --> 2507.66]  So like, where do I even start?
[2507.86 --> 2510.52]  Like, you can edit that down for the podcast.
[2510.52 --> 2511.04]  That's great.
[2511.18 --> 2512.16]  You don't need to share all that.
[2512.20 --> 2514.16]  No, you don't need to edit any of that.
[2514.24 --> 2514.62]  It's fine.
[2514.76 --> 2515.82]  It was phenomenal.
[2516.22 --> 2519.04]  So like, it seems like there's a few things like I want to ask you one.
[2519.32 --> 2521.12]  Maybe I'll combine them into two questions.
[2521.22 --> 2524.06]  So one is like, what was it like to work in the open?
[2524.06 --> 2526.26]  Or what was it like to not work in the open?
[2526.34 --> 2527.72]  Because I don't actually know.
[2528.32 --> 2533.50]  How were you working on this project before you had this massive, like, drop the ball moment?
[2533.68 --> 2536.90]  And then like, or did people have like a smell that this was coming?
[2537.32 --> 2540.42]  Like, or it was like, I'm just curious, like how you did that.
[2540.54 --> 2544.12]  And then the second question is really like what it was like to like work with all these people,
[2544.48 --> 2546.50]  maybe external to the React core team.
[2546.50 --> 2548.52]  Because it seems like there was a whole group of people.
[2548.62 --> 2549.28]  So who were they?
[2549.28 --> 2550.48]  And what was it like to work with them?
[2550.90 --> 2552.18]  So sorry for two big questions.
[2552.54 --> 2554.98]  But you're going to have to pick one of them.
[2555.06 --> 2555.36]  Okay.
[2555.48 --> 2556.78]  You know, I give dissertations.
[2556.94 --> 2557.26]  I know.
[2557.66 --> 2560.08]  You're like an entire, I know, entire essay.
[2560.20 --> 2562.16]  Okay, I might the external people.
[2562.54 --> 2563.12]  Oh, actually, you know what?
[2563.16 --> 2565.28]  No, no, I think you can list that pretty quickly.
[2565.40 --> 2566.90]  I just was curious who was working with you.
[2566.94 --> 2571.34]  But I think I'm maybe more curious about like how you worked on this before the launch, you know.
[2571.78 --> 2573.60]  And like, what was that experience like?
[2573.98 --> 2575.62]  Well, it was a couple of different experiences.
[2575.62 --> 2583.24]  We had to build a new site that would contain the new documentation and had a really good contribution workflow.
[2583.50 --> 2589.48]  It was hard to write the documentation before the site was finished because so much of the documentation is interactive.
[2590.16 --> 2596.08]  You know, like you'd be writing a Google Doc and then you'd have to like put a link to a code sandbox to explain what you're talking about.
[2596.16 --> 2597.28]  Like this would be embedded.
[2597.64 --> 2599.60]  It was really, really slow and churny.
[2599.96 --> 2602.86]  But things picked up once we got a prototype site in place.
[2602.86 --> 2606.18]  That was a quick collaboration to set something like that up.
[2606.36 --> 2609.60]  Did I read it correctly that Jared Palmer helped build the site?
[2609.98 --> 2615.10]  Jared Palmer helped build the prototype site that we were using to write the documentation up behind the scenes.
[2615.20 --> 2615.40]  Yes.
[2615.94 --> 2616.38]  Wow.
[2616.38 --> 2617.86]  That was spun up super quickly.
[2618.16 --> 2623.30]  Code Sandbox had a dedicated team working on integrating the sandpack with the site.
[2623.84 --> 2626.66]  And that was really fun, too, because we were sort of their guinea pig.
[2627.10 --> 2628.26]  They were also our guinea pig.
[2628.58 --> 2630.98]  So we were kind of like co-guinea pigs.
[2630.98 --> 2631.70]  Guinea-pigging.
[2631.70 --> 2632.18]  Yeah.
[2632.40 --> 2632.80]  Yeah.
[2633.30 --> 2633.98]  That was fun.
[2634.32 --> 2638.90]  And then to actually build out the final site, there was a design effort.
[2639.64 --> 2646.34]  We had a UI designer in-house who worked on the code diagrams and like how the interactive examples would work.
[2646.96 --> 2654.30]  And another designer who came up with the design system, which actually folded into a bit of a design refresh for the React brand.
[2654.44 --> 2657.98]  You might notice that the logo is a little smoother around the edges.
[2657.98 --> 2658.24]  No.
[2658.68 --> 2659.78]  It's very, very subtle.
[2659.78 --> 2660.48]  Wait.
[2661.48 --> 2667.08]  Is this like the difference between like a squircle and a-
[2667.08 --> 2667.68]  A rounded rectangle?
[2667.82 --> 2669.02]  A rounded rectangle.
[2669.56 --> 2671.76]  Like, you know, that's like very subtle.
[2672.62 --> 2674.16]  How different is this logo?
[2674.50 --> 2676.22]  I would actually say that's an accurate depiction.
[2676.56 --> 2677.04]  Oh, okay.
[2677.12 --> 2677.68]  Oh, excellent.
[2678.02 --> 2678.38]  Yay.
[2678.56 --> 2681.20]  That's what I figured because it's not like very noticeable.
[2681.20 --> 2681.60]  Yeah.
[2681.60 --> 2682.00]  Yeah.
[2682.46 --> 2684.74]  And that was Rajvan and Dan.
[2684.78 --> 2689.06]  What is it with big tech companies and the desire to like constantly change logos or names?
[2689.24 --> 2691.20]  Like Google has done this a hundred times.
[2691.42 --> 2693.04]  Like Facebook did this.
[2693.30 --> 2693.46]  Oh, no.
[2693.52 --> 2696.46]  We don't need to talk about the actual, like I just talk just in general.
[2696.56 --> 2699.14]  It's just like this hilarious thing that we don't need to spend any time on.
[2699.32 --> 2699.92]  It's a rhetorical question.
[2699.92 --> 2700.86]  Let's move on.
[2701.20 --> 2702.08]  Rhetorical question.
[2702.40 --> 2702.60]  Yes.
[2702.70 --> 2703.98]  That's exactly what it was.
[2704.48 --> 2704.82]  So, yeah.
[2704.88 --> 2705.22]  I don't know.
[2705.28 --> 2706.42]  Amelia, you go.
[2706.60 --> 2709.20]  I mean, I have so many thoughts, but this is amazing.
[2709.52 --> 2709.72]  Wait.
[2709.78 --> 2711.86]  I haven't finished with my thank you card.
[2711.86 --> 2712.60]  Oh, you haven't finished.
[2712.70 --> 2713.30]  Oh, sorry.
[2713.88 --> 2714.32]  Okay.
[2714.56 --> 2714.76]  Yeah.
[2714.88 --> 2715.10]  Great.
[2715.24 --> 2716.70]  So then we had these cool designs.
[2716.94 --> 2717.10]  Okay.
[2717.22 --> 2722.12]  And we worked with Dustin and Dane over at this dot.
[2722.68 --> 2725.38]  They did the implementation for the designs.
[2726.16 --> 2730.44]  And so there are a couple of different teams at different places doing different integration work.
[2730.92 --> 2737.12]  You know, different people designing UI, different people implementing it, different people putting the new design system into place.
[2737.48 --> 2743.78]  And Maggie Appleton, like the original prototype site was all my sketches and doodles everywhere.
[2743.90 --> 2748.76]  Because I'd be like in a meeting and I'd be like, okay, and state, does state work like this?
[2749.20 --> 2749.60]  No.
[2750.86 --> 2751.68]  Like this?
[2751.76 --> 2752.52]  Is this a good metaphor?
[2752.70 --> 2752.90]  Okay.
[2752.92 --> 2753.38]  That's close.
[2753.38 --> 2757.50]  And I put all these illustrations and hand-drawn diagrams in.
[2757.62 --> 2759.96]  And you know what the alpha tester feedback was?
[2760.16 --> 2760.40]  What?
[2760.76 --> 2766.06]  These illustrations are interesting and nice, but I cannot read the text.
[2766.24 --> 2767.40]  My handwriting was so bad.
[2768.02 --> 2777.10]  So toward the end, we ended up bringing in Maggie Appleton, who does amazing React illustrations, to come up with a diagramming system that really helps.
[2777.36 --> 2778.26]  And you'll see those soon.
[2778.54 --> 2779.22]  We're still in beta.
[2779.54 --> 2780.22]  They're going to be implemented.
[2780.42 --> 2781.04]  You'll see them soon.
[2781.04 --> 2786.16]  And these take my chicken scratchings and make them actual diagrams.
[2786.16 --> 2787.80]  The ones in the site right now?
[2788.06 --> 2790.28]  I thought those are your illustrations, right?
[2790.66 --> 2791.36]  They are.
[2791.54 --> 2792.84]  The actual illustrations.
[2793.24 --> 2798.94]  Like, you'll notice there are illustrations that show, like, React Head, who's like this Ikea dude doing things.
[2799.02 --> 2799.34]  Yeah.
[2799.64 --> 2800.82]  Those are final illos.
[2800.92 --> 2802.28]  Gender neutral dude.
[2802.94 --> 2804.46]  Or maybe not so gender neutral.
[2804.62 --> 2805.00]  I don't know.
[2805.00 --> 2805.74]  It's React Head.
[2805.82 --> 2806.48]  It's React Head.
[2806.48 --> 2808.74]  Not the star of a horror movie.
[2809.02 --> 2809.26]  Okay.
[2809.26 --> 2813.48]  But your helpful Ikea person assisting you with assembling your component.
[2813.68 --> 2816.52]  I feel like helpful Ikea person is, like, very gender neutral, though.
[2816.56 --> 2820.14]  So I figured, like, React Head was, like, non-binary or something.
[2820.22 --> 2820.70]  But who knows?
[2821.06 --> 2822.46]  I'd like to think of it that way.
[2822.58 --> 2822.76]  Yeah.
[2822.84 --> 2825.96]  And there are diagrams, which are still very sketchy.
[2826.14 --> 2829.30]  We've got a proper diagramming system coming in for those.
[2829.32 --> 2830.12]  Super cool.
[2830.12 --> 2831.14]  That's pretty awesome.
[2831.32 --> 2833.20]  I think I've given thanks to everybody.
[2833.56 --> 2837.38]  Of course, the actual docs themselves, the learning path, everything.
[2837.92 --> 2845.74]  This was designed by Dan Abramov, who, you might remember, has been, like, blogging about React on overreacted.io forever.
[2846.26 --> 2850.06]  You read these docs, you might be like, Rachel, you must know everything about React.
[2850.28 --> 2850.88]  I do not.
[2851.78 --> 2852.82]  No, I do not.
[2852.82 --> 2860.44]  A lot of this is collaboration with Dan, with the core team, to bring this information to light.
[2861.02 --> 2864.54]  And, you know, yes, I have wordsmithed a lot of it.
[2865.08 --> 2870.58]  One or two of those pages are definitely exact products from Rachel, but most of them are team effort.
[2871.06 --> 2873.58]  They have been through lots of revisions, iterations.
[2874.14 --> 2877.92]  They are how to think and react directly from React core team members.
[2878.70 --> 2880.88]  And that's what's so special about this.
[2880.88 --> 2889.92]  I mean, it was kind of like getting to co-author a book on React for a year and also produce the interactive part of it, too.
[2890.12 --> 2891.22]  That was just so cool.
[2891.90 --> 2897.60]  And the docs are the way they are because of so many amazing people putting in their efforts.
[2897.98 --> 2900.76]  We wouldn't have been able to test on real people without that prototype.
[2901.06 --> 2904.70]  We wouldn't have been able to get the interactive examples without Code Sandbox.
[2905.10 --> 2909.64]  We wouldn't have had these amazing examples in the first place without Sylvia.
[2909.64 --> 2920.38]  So I really think when you look at these docs, you're looking at a synthesis of so many efforts and a feedback of so many amazing volunteers who joined us at the start of the journey.
[2920.38 --> 2933.02]  This episode is brought to you by our friends at Square.
[2933.24 --> 2935.36]  Square is the platform that sellers trust.
[2935.84 --> 2942.68]  There is a massive opportunity for developers to support Square sellers by building apps for today's business needs.
[2943.12 --> 2945.88]  And I'm here with Shannon Skipper, head of developer relations at Square.
[2945.88 --> 2950.16]  Shannon, can you share some details about the opportunity for developers on the Square platform?
[2950.56 --> 2951.02]  Yeah, absolutely.
[2951.24 --> 2953.90]  So we have millions of sellers who have unique needs.
[2954.20 --> 2957.26]  And Square has apps like our point of sale app, like our restaurants app.
[2957.44 --> 2963.66]  But there are so many different sellers, tuxedo shops, florists who need specific solutions for their domain.
[2963.92 --> 2974.98]  And so we have a Node SDK written in TypeScript that allows you to access all of the backend APIs and SDKs that we use to power the billions of transactions that we do annually.
[2974.98 --> 2979.56]  And so there's this massive market of sellers who need help from developers.
[2980.12 --> 2990.98]  They either need a bespoke solution built for themselves on their own Node stack where they are working with Square dashboard, working with Square hardware or with the e-com, you know, what you see is what you get builder.
[2991.24 --> 2992.26]  And they need one more thing.
[2992.34 --> 2993.62]  They need an additional build.
[2993.94 --> 3001.98]  And then finally, we have the app marketplace where you can make a Node app and then distribute it so it can get in front of millions of sellers and be an option for them to adopt.
[3001.98 --> 3002.78]  Very cool.
[3002.86 --> 3003.10]  All right.
[3003.14 --> 3010.90]  If you want to learn more, head to developer.squareup.com to dive into the docs, APIs, SDKs, and to create your Square developer account.
[3011.20 --> 3012.98]  Start developing on the platform seller's trust.
[3013.34 --> 3015.66]  Again, that's developer.squareup.com.
[3016.04 --> 3019.68]  And by our friends at FASC, they're running a massive promo on Compute at Edge.
[3019.84 --> 3030.04]  They're inviting our entire listener base to move latency-sensitive workloads to the edge with Compute at Edge free for three months, plus up to $100,000 a month in credit for an additional six months.
[3030.04 --> 3038.52]  This is a limited-time offer, so head to Fastly.com slash podcast as soon as you can to check it out and get all the details.
[3039.00 --> 3039.92]  Here's the TLDR.
[3040.42 --> 3050.80]  Fastly's Edge Cloud Network and Modern Approach to Serverless Computing allows you to deploy and run complex logic at the edge with unparalleled security and blazing fast computational speed.
[3051.14 --> 3058.32]  Scale instantly and globally, reduce origin load, get real-time observability, and get seamless integration with your existing tech stack.
[3058.32 --> 3066.22]  Head to Fastly.com slash podcast to get Compute at Edge free for three months, plus up to $100,000 a month in credit for an additional six months.
[3066.70 --> 3069.08]  Once again, Fastly.com slash podcast.
[3069.08 --> 3069.32]  Fastly.com slash podcast.
[3085.84 --> 3096.18]  Okay, Rachel, that was really incredible to hear about just how many, you know, people were involved and people, vendors, you know, like volunteers, you name it.
[3096.18 --> 3103.02]  You have a whole kind of smorgasbord of people helping kind of birth this into the world, which is like so exciting.
[3103.54 --> 3107.12]  I'm curious, like the goals are kind of these lofty goals, right?
[3107.12 --> 3115.26]  Like, hey, you should be able to more or less master React through these docs, and you should be able to kind of be comfortable.
[3115.26 --> 3120.72]  The API reference should cover everything you need to know to stay safe and be productive.
[3120.96 --> 3127.86]  And so I'm assuming as much as, like, I know what I'm learning, I'm usually learning from multiple sources on the same topic.
[3128.04 --> 3134.50]  And usually that's because there's, they don't all cover the same thing or in the same way, and I don't always learn from them in the same way.
[3134.50 --> 3138.10]  And so, like, what gaps do you think that you guys are never going to cover?
[3138.70 --> 3145.64]  And, like, what types of things would people want to kind of look to other places beyond the docs to kind of, like, gain mastery?
[3146.42 --> 3150.00]  Well, for one thing, the docs strictly teach React.
[3150.42 --> 3161.10]  They don't teach React and, you know, Next or React and Gatsby or React for building a blog or React for building your own app.
[3161.10 --> 3163.80]  It's strictly how to get great with React.
[3164.04 --> 3168.74]  If you want to learn those other things, there are amazing resources available.
[3169.28 --> 3173.80]  The documentation at Next and Gatsby is, you know, excellent.
[3174.22 --> 3179.50]  What we wanted to do, though, was to make sure that these people who build great courses, great platforms, et cetera,
[3179.88 --> 3188.12]  that they had reference material that they could link out to, lean on, or even, you know, re-explain React better than we could to their audiences,
[3188.12 --> 3194.96]  but feel certain that they were, in the case of trainers making courses, really be sure that they were explaining it right.
[3195.48 --> 3200.34]  We're not able to go out and offer editorialship to everyone's documentation and courses.
[3200.56 --> 3201.26]  We wish we could.
[3201.66 --> 3201.84]  I know.
[3201.90 --> 3202.80]  I know you wish you could.
[3202.90 --> 3205.74]  I know you all are so generous with your time and feedback already.
[3205.84 --> 3208.96]  Honestly, I really feel that truly about the React core team.
[3209.18 --> 3212.60]  Like, you're very, very, very good about giving feedback to educators.
[3212.60 --> 3218.06]  And I think, like, and also just in general, you have folks like Mark Erickson.
[3218.22 --> 3223.86]  How can I talk about React without talking about Mark, you know, who's like Ace Mark on Twitter and in Discord.
[3224.04 --> 3227.06]  He's a phenomenal educator, super patient.
[3227.34 --> 3229.42]  But I feel that very strongly about the React community.
[3229.62 --> 3231.94]  Like, y'all are just incommunicado.
[3232.20 --> 3234.96]  But I'm so glad to hear that, like, that was the goal, you know?
[3235.04 --> 3236.10]  Like, that's so cool.
[3236.64 --> 3238.02]  Like, it's, like, very platformy.
[3238.02 --> 3248.16]  It's like, I'm going to build a platform for platforms, which is, like, I'm going to make sure that we're supporting the educators when they're talking to their audiences in the language that their audiences prefer, you know?
[3248.34 --> 3249.36]  So that's really cool.
[3249.62 --> 3260.26]  So one thing I wanted to ask about is the layout and navigation is a little bit different from the official docs or the last docs, which I think they're both going to live in harmony now.
[3260.72 --> 3265.14]  Well, eventually the beta documentation will be the documentation.
[3265.48 --> 3265.72]  Gotcha.
[3265.72 --> 3269.60]  Beta.reactjs.org will get merged to reactjs.org.
[3270.08 --> 3270.62]  The end.
[3270.90 --> 3271.86]  That's the end goal.
[3272.16 --> 3272.38]  Gotcha.
[3272.54 --> 3272.76]  Okay.
[3272.92 --> 3274.06]  Thanks for clarifying that.
[3274.42 --> 3276.66]  I read once that there's four.
[3276.98 --> 3280.92]  It lists four, but there's at least four types of documentation that are all kind of different.
[3281.14 --> 3285.58]  There's, like, tutorials, how-to guides, explanations, and references.
[3285.58 --> 3294.92]  And it seems like you've kind of split out to treat at least two of those separately, which I'm curious what was the thinking behind that and kind of, like, what is going where?
[3294.92 --> 3296.28]  That is great.
[3296.36 --> 3297.52]  Thank you for bringing that up.
[3297.52 --> 3305.96]  So originally, I don't know if you've looked at reactjs.org recently, but it's sort of all of it is guides, is guides.
[3306.14 --> 3311.06]  There's some API documentation in there, but depending on what you're looking for, it could exist in multiple places.
[3311.06 --> 3313.96]  Like, you go find where the API docs are on the site.
[3314.14 --> 3316.02]  It takes a little bit of rummaging around.
[3316.14 --> 3318.90]  If you're looking for a hook, you're going to be rummaging in a couple of different places.
[3319.62 --> 3323.76]  But, you know, this is what happens when your information architecture kind of gets away from you here.
[3324.00 --> 3326.28]  So there was an information architecture overhaul.
[3326.28 --> 3340.90]  We have API references, and we have the actual React Learn content, which is step-by-step lessons and guides for how to install, how to get something quickly running, and how to dive deep with React.
[3341.42 --> 3349.18]  These guides are actually a little bit different from the conceptual overview and guide stocks you mentioned.
[3349.18 --> 3355.96]  They're kind of a merging of the two, because it's very hard to talk about React conceptually without actually showing things in progress.
[3356.50 --> 3366.78]  And if we did split out the conceptual overview, we'd run into a situation where we might end up with long essays here and then explanations that don't really help you understand what's going on over here.
[3367.18 --> 3370.28]  And you can guess how much time people are going to spend on which.
[3370.88 --> 3379.00]  So this goal-based approach to learning React actually kind of blends those two kinds of content into one.
[3379.18 --> 3388.48]  So as you're learning about, like, how state works, you're also learning about the concept of render and commit, which is necessary to understand how state works.
[3388.68 --> 3390.40]  Setting state triggers the render process.
[3390.72 --> 3392.82]  Oh, but what is that render process?
[3392.96 --> 3394.24]  Don't go to the other side of the site.
[3394.32 --> 3395.12]  Stay right there, kiddos.
[3395.16 --> 3396.54]  We're going to tell you about it right here.
[3397.00 --> 3398.98]  So that's the approach that we took with these.
[3398.98 --> 3405.62]  It's a little different, a little experimental, but it seems to be doing well with test audiences, and we think it's doing well in production so far.
[3405.70 --> 3406.58]  So fingers crossed.
[3407.22 --> 3409.06]  We did take that particular approach here.
[3409.18 --> 3411.60]  We do want to add some tutorials.
[3411.96 --> 3420.02]  Once we've switched over to gotten out of beta and gone fully loaded into the new site, that is on the roadmap for the future.
[3420.62 --> 3423.60]  So, so glad that you brought up those different content types.
[3424.10 --> 3424.64]  That's incredible.
[3424.64 --> 3428.34]  I mean, it really does feel like very intentional.
[3428.34 --> 3438.56]  And it's clearly laid out, like, when you're kind of learning and then when you're really just in execution mode trying to access API docs.
[3438.72 --> 3444.04]  And then when you're learning, I really like the new organization of top level contents, like buckets as well.
[3444.04 --> 3451.50]  I think that's like, you've really kind of shifted the mental model for like how people should understand React, right?
[3451.56 --> 3461.36]  Like, you know, like, remember you mentioned earlier, just kind of that more of a focus on the rendering, you know, life cycle, more of a focus on like how things work under the hood.
[3461.36 --> 3462.50]  And it's phenomenal.
[3462.76 --> 3468.50]  It just feels good, you know, you know, when it feels good to like navigate and read and learn in that order.
[3468.78 --> 3476.20]  Like I spent a couple of hours on the new doc site and I just was, I just didn't feel exhausted two hours later, you know?
[3476.50 --> 3477.28]  And that's a good thing.
[3477.28 --> 3478.44]  Well, that's wonderful feedback.
[3478.60 --> 3479.54]  I'm going to write that down.
[3479.54 --> 3480.24]  You should write that down.
[3480.30 --> 3482.52]  I did not feel exhausting after two hours.
[3483.86 --> 3485.14]  Don't ask about other symptoms.
[3485.28 --> 3485.86]  No, just kidding.
[3486.30 --> 3489.42]  So what's your favorite part of the site?
[3489.62 --> 3493.98]  Like, I want to hear, like you, Rachel, like, what did you love?
[3494.14 --> 3496.36]  Whether you, you know, helped contribute to it or not.
[3496.40 --> 3497.90]  Like, what are your favorite parts?
[3498.26 --> 3499.64]  That's a really good question.
[3499.88 --> 3505.00]  Because, you know, your answer is going to be the title of the book called React Docs, The Good Parts.
[3505.18 --> 3505.78]  Just kidding.
[3507.28 --> 3509.96]  Just kidding, kids.
[3510.08 --> 3510.34]  Anyways.
[3510.74 --> 3513.24]  I love so much of the documents here.
[3513.48 --> 3516.20]  I love, like, even some of the content.
[3516.54 --> 3522.88]  Like, there was the question of, like, did we, there's this one piece called Thinking in React, which was, like, one of the original.
[3523.34 --> 3525.80]  Here's how React helps you think about building UI.
[3525.80 --> 3532.14]  And at first it was like, yeah, I'm going to make a whole new page all about thinking in React.
[3532.26 --> 3533.70]  Yeah, like for the modern world.
[3533.70 --> 3539.62]  But people kept in beta testing being like, don't forget about keeping Thinking in React.
[3539.76 --> 3540.76]  I love that piece, man.
[3541.30 --> 3543.54]  And I was like, you know, it's such a classic.
[3543.62 --> 3545.76]  We can't, we can't burn it down.
[3545.76 --> 3549.90]  So, went through and gave it a bit of a facelift for the modern era.
[3549.90 --> 3554.92]  You know, the original Thinking in React piece was very, you know, like, here's a new way.
[3555.04 --> 3557.94]  You may not have thought about thinking about your interfaces, kids.
[3558.32 --> 3559.98]  Have you heard about atomicity?
[3560.10 --> 3561.58]  Yes, everyone has heard of that by now.
[3561.96 --> 3565.78]  Let's write this as though people probably have encountered some of these concepts already.
[3565.78 --> 3568.74]  They've permeated other branches of programming.
[3569.22 --> 3573.10]  They've, you know, they've inspired new approaches out there.
[3573.20 --> 3575.80]  So, let's talk more in the present, less in the past.
[3576.30 --> 3578.76]  But just updating that classic was a real honor.
[3579.20 --> 3586.28]  Very awesome to see it with actual interactive examples showing the thing that it was describing originally in the text.
[3586.28 --> 3593.00]  My personal favorite is the describing the UI section, which is really just introducing you to the concept of components and props.
[3593.16 --> 3594.28]  You know, what are these things?
[3594.48 --> 3596.92]  How do you structure them into extra files?
[3597.24 --> 3603.56]  There's a lot of stuff there that we saw people, like, coming out of boot camp, maybe not quite picked this up yet.
[3603.90 --> 3606.06]  We got to cover some of those basics again.
[3606.06 --> 3612.14]  And it was actually a lot of fun to work on some of those pieces and break things down.
[3612.30 --> 3616.76]  And even more fun to get, you know, read through the individual feedback on those pieces.
[3617.08 --> 3620.54]  And hear someone say, like, this was the best explanation of this that I've ever read.
[3620.62 --> 3622.40]  And I'm just like, hmm.
[3622.56 --> 3623.76]  Yeah, nailed it.
[3624.04 --> 3625.18]  Yes, yes, yes.
[3625.34 --> 3631.50]  So, I'm kind of proud of the whole thing, but exceptionally proud of the guides and the work done on those.
[3632.04 --> 3634.04]  It's just, people love it.
[3634.08 --> 3635.04]  It just came out so well.
[3635.04 --> 3635.50]  Yeah.
[3636.06 --> 3637.38]  That's the educator in you.
[3637.56 --> 3640.68]  You know, Rachel, I think at core, maybe you are just a teacher.
[3641.26 --> 3645.36]  Honestly, like, and I shouldn't say just, like, just, you know, but I think you are, like,
[3645.86 --> 3650.92]  I think education has definitely been the theme that's, like, been woven throughout everything that you've done, I think.
[3651.38 --> 3652.38]  And that's, you know.
[3652.40 --> 3653.28]  It's kind of the red thread.
[3653.40 --> 3654.46]  It's the red thread.
[3654.68 --> 3654.96]  Yeah.
[3655.16 --> 3661.04]  You know, so it's just, I think it's no surprise that those are the pieces that kind of, like, come home, you know, for you.
[3661.04 --> 3662.22]  But that's really exciting.
[3662.72 --> 3664.12]  Really, like, very, very cool.
[3664.12 --> 3666.64]  So, I'm glad that I had the chance to be a part of this.
[3666.88 --> 3667.58]  It's inspiring.
[3667.78 --> 3683.06]  I know that these resources are going to change who gets great with React, who gets what jobs, who teaches who, and the quality of how people feel about that and the confidence that they have going forward.
[3683.06 --> 3690.26]  I'm really honored that I got to be a part of something that's going to just be so useful for so many folks.
[3690.70 --> 3691.60]  Yeah, no, for sure.
[3691.70 --> 3702.48]  And I think what's interesting is also, like, kind of circling back to your earlier comment around, like, you're really excited to make better material for educators, right?
[3702.48 --> 3709.24]  Like, I think what's great about this is it's one of those things that's like a rising tide lifts all boats, you know?
[3709.48 --> 3718.12]  It really feels like with the core docks being better, everything else is going to have a new baseline as well in some ways.
[3718.30 --> 3726.42]  You know, of course, not everything, but those things that choose to participate, I think, and pull from these docks will certainly be elevated, right?
[3726.42 --> 3730.70]  And that makes me want to give a callback to something we talked about earlier about the metrics.
[3731.24 --> 3734.28]  Funny thing about net promoter score, it's always falling.
[3735.08 --> 3735.82]  You know why that is?
[3736.02 --> 3736.42]  No.
[3736.68 --> 3738.14]  Oh, because recency bias?
[3738.48 --> 3739.22]  I don't know.
[3739.58 --> 3740.06]  Why?
[3740.40 --> 3742.18]  I don't actually know that expression.
[3742.52 --> 3743.34]  Oh, recency bias?
[3743.50 --> 3745.62]  Oh, it's probably because it's something I made up.
[3745.70 --> 3749.34]  I don't know if it's official, but it's, like, just the thing that's most recent.
[3749.34 --> 3756.24]  You know, like, let's say you have a competition and there's five people pitching, and it's usually, like, the last one or two people pitching.
[3756.60 --> 3759.58]  Like, they have the recency bias advantage because they were most recent.
[3759.68 --> 3761.18]  Because we tend to forget things.
[3761.54 --> 3762.92]  We are, like, short-term members.
[3763.08 --> 3765.22]  We have, like, low RAM, you know?
[3765.36 --> 3766.18]  This is not that.
[3766.34 --> 3766.98]  This is not that.
[3767.06 --> 3767.54]  Okay, cool.
[3767.92 --> 3771.92]  So there is a word for this, and jump in and tell me if you've heard of it before.
[3772.62 --> 3777.10]  It's where today's amazing becomes tomorrow's expected.
[3777.10 --> 3780.66]  You know, like, remember when the iPhone came out and it was like, it's a touchscreen!
[3781.32 --> 3781.62]  Yeah.
[3781.94 --> 3782.88]  It doesn't have keys!
[3783.24 --> 3783.66]  Oh, yeah.
[3783.72 --> 3787.82]  And now it's like, would you be able to sell someone a phone that wasn't a touchscreen?
[3788.18 --> 3788.62]  No!
[3789.34 --> 3793.42]  Nobody would buy that, except for very strange people who have specific needs.
[3793.56 --> 3793.82]  Yeah.
[3793.96 --> 3797.52]  Like, those keys are so much easier to feel if they're actually, like, physical.
[3797.72 --> 3801.76]  But let's be honest, the mass market has changed its baseline.
[3801.96 --> 3805.20]  They now expect what was once unexpected.
[3805.48 --> 3806.16]  Oh, my God.
[3806.16 --> 3807.30]  I mean, think about it.
[3807.66 --> 3810.64]  People are going to expect interactive examples in their docs.
[3811.34 --> 3816.40]  People are going to come to the React documentation in a few years, so they're going to be like,
[3816.92 --> 3820.68]  yeah, but I can't just click a button and it builds my app for me.
[3821.12 --> 3826.46]  Or, yeah, you know, these are great, but I expect to be able to dial in and talk to a core team member
[3826.46 --> 3827.16]  when I have trouble.
[3827.82 --> 3831.40]  Who knows what's going to happen with the future of documentation?
[3831.40 --> 3837.08]  Yes, because React.js developers will all become Oracle Enterprise developers, too.
[3837.58 --> 3840.50]  Anyways, actually, no, Rachel, OMG.
[3840.78 --> 3841.68]  I can't believe I...
[3841.68 --> 3846.70]  Like, that's why I was, like, gasping while you were saying that, because, like, I just realized, like, yeah,
[3846.70 --> 3858.06]  this is, like, one of those tipping points that where React has enough of a market in the developer tooling community that we are going to now see this be the new standard.
[3858.06 --> 3862.52]  Like, similar to how, like, zero config became a new standard for developer tooling.
[3862.72 --> 3864.54]  Like, you know, install and run commands.
[3864.74 --> 3867.18]  Like, don't worry about config files if you don't need to, right?
[3867.32 --> 3872.68]  So this whole kind of, like, smart defaults movement, interactive API documentation, like Stripe,
[3872.72 --> 3875.84]  and this is a really good segue into, I think, some of the inspiration for the site,
[3875.94 --> 3879.32]  but, like, Stripe, like, set the bar.
[3879.58 --> 3886.84]  Like, literally just kind of everything became copy-paste after that, like, where you see services like Twilio and, right?
[3886.84 --> 3888.74]  Like, it just was, like, the first domino.
[3889.28 --> 3893.12]  And so this might be the first domino in that same way, like, which is interesting.
[3893.28 --> 3895.10]  And actually, yeah, I'll let you respond.
[3895.24 --> 3897.58]  But I do remember the question that I wanted to ask you from earlier,
[3897.70 --> 3899.90]  which I think is a very relevant question from our listeners.
[3900.24 --> 3907.78]  So my question, Rachel, is how long are the current docs going to live side-by-side with, like, this beta?
[3907.98 --> 3913.88]  And can we expect that, like, the current docs, like, the content is always going to be, like,
[3913.88 --> 3917.84]  the most accurate and latest and greatest on both the beta and the current?
[3917.98 --> 3921.88]  Like, I just wonder, like, what's the lifecycle and management of these two?
[3922.04 --> 3928.90]  Like, because you can't strictly cut over yet because of the API docs that are still in progress and whatever else, right?
[3929.26 --> 3930.94]  And we're achieving content parity.
[3930.94 --> 3937.10]  There's still some documentation and content on the main site that needs to be ported to the new site.
[3937.42 --> 3939.68]  We're writing the documentation live right now.
[3939.68 --> 3944.98]  I can't give you an exact date about when that will land, like, if anything.
[3945.30 --> 3949.22]  I think the last year has taught us that exact dates are kind of a tricky thing to promise.
[3949.68 --> 3949.98]  I know.
[3950.12 --> 3955.22]  But if you want the latest and greatest, beta.reactjs.org is a safe bet.
[3955.66 --> 3958.98]  We are actively developing the content there and contributing to it.
[3959.34 --> 3961.12]  And that is the place to go to.
[3961.60 --> 3962.12]  That's awesome.
[3962.24 --> 3963.30]  Thank you so much for that.
[3963.78 --> 3966.28]  And so I guess kind of we can close out on the inspiration.
[3966.28 --> 3972.32]  And it's clear that there's echoes from many different things, including even just in your collaborations, right?
[3972.38 --> 3981.50]  Like, this new beta site wouldn't have been possible without all of the hard work from folks like Sandbox, CodePen, all of the JS Fiddle.
[3981.80 --> 3988.16]  Whatever was the first thing made it easy for us to write JavaScript and, like, interact with it in a web browser, right?
[3988.16 --> 3991.64]  Like, there's so many kind of shoulders of giants that you're standing on.
[3991.70 --> 3999.88]  So can you just kind of, like, maybe talk us through, like, what were some of your inspirations and, like, how did they feed into, like, this final product?
[4000.40 --> 4005.62]  I think a lot of our inspiration for this came from, honestly, texts about how to teach people.
[4005.62 --> 4018.32]  Making it stick is a really good example of one of those books that really changed how we approached React, you know, instead of just telling people, like, this is how React works, you know, with a bunch of diagrams.
[4018.68 --> 4023.06]  We added actual interactive challenges so that people could get retrieval practice in.
[4023.62 --> 4029.20]  We were inspired by textbooks as well, the structure of textbooks with chapters, overviews.
[4029.20 --> 4036.26]  A lot of people in courseware design are doing really amazing things that could apply to the realm of documentation.
[4036.96 --> 4044.14]  Course design, courseware design, which takes a lot of inspiration from sketch textbooks and formal education.
[4044.14 --> 4061.42]  I know some people who work on whole, like, computer science, like, aligning how their documentation and educational materials teach to new computer science standards for curricula that are coming out for the United States and the United Kingdom.
[4062.06 --> 4067.36]  There's, like, an entire formal education component where I could not name all the different inspirations.
[4067.36 --> 4069.70]  We tried to bring a little bit of that here.
[4069.92 --> 4075.56]  We wanted it to be something that could be a good foundation or at least plug in nicely to other people's curricula.
[4076.30 --> 4079.92]  And, of course, the Stripe documentation, you already mentioned it.
[4080.12 --> 4087.42]  There are a lot of things that didn't make it out of prototyping stage that we wish we could have done, but we really wanted to focus on getting to beta.
[4088.08 --> 4090.22]  That Stripe has just been such an inspiration.
[4090.58 --> 4095.54]  I love how they use scrollytelling to get through the examples and line by line the code.
[4095.54 --> 4097.80]  I really found that informative.
[4098.38 --> 4102.86]  And lastly, I do want to give a shout-out to everyone's favorite, MDN.
[4103.34 --> 4107.58]  Way back in the day, I used to write documentation for the Web Animations API with MDN.
[4108.08 --> 4119.54]  And that spirit of collaboration of, you know, like, everyone who's written on MDN gets their name added to the, well, if you dig around on GitHub, you can find it.
[4119.54 --> 4125.96]  But that spirit of this is a team effort, it's like documentation as open source.
[4126.20 --> 4128.24]  And I loved how MDN did that.
[4128.48 --> 4133.34]  I loved how MDN partnered with the community to teach the community.
[4134.00 --> 4138.86]  And I think that a lot of that spirit has found its way into this project as well.
[4139.68 --> 4139.76]  Wow.
[4140.42 --> 4141.80]  Well, that was inspirational.
[4142.20 --> 4142.88]  Are you inspired?
[4143.00 --> 4143.84]  I'm inspired, Amelia.
[4144.28 --> 4144.70]  Oh, yeah.
[4145.24 --> 4145.46]  Yeah.
[4145.50 --> 4146.46]  Such a good list.
[4146.70 --> 4147.36]  Solid list.
[4147.36 --> 4153.06]  It's, like, near impossible to, like, talk about documentation and not mention Stripe.
[4153.66 --> 4155.72]  Like, it's just, like, I can't do it.
[4155.84 --> 4159.60]  If you find a person who can, really, is my challenge to you.
[4160.24 --> 4173.74]  But actually, kind of speaking of docs, so listening to you, I had this thought that I wanted to share, which is, I wonder if any other industry uses technical documentation in the same way that engineers do, software engineers particularly.
[4173.74 --> 4177.04]  Like, because, like, I studied biomedical engineering.
[4177.18 --> 4180.98]  So I do have a background that's in engineering that's not related to software.
[4181.44 --> 4187.86]  And I can tell you, like, we read textbooks and open things and whatever, you know, my thermodynamics book or whatever.
[4188.00 --> 4191.74]  But, like, you don't really go back to your reference material in that way.
[4191.74 --> 4198.86]  And, like, versus, like, me, like, I have, I'm opening API docs and I'm looking at reference material and I'm reading technical content.
[4199.04 --> 4203.10]  And there's something very educational about our documentation, right?
[4203.14 --> 4211.28]  Like, in a way that I feel like your comment about how so much of good courseware design could be applied to technical docs.
[4211.28 --> 4215.20]  Like, I think that that's, that's the first time I've ever heard of that.
[4215.76 --> 4217.12]  And I couldn't agree with you more.
[4217.54 --> 4226.42]  I just kind of wish that we really thought about technical docs really as more education versus just trying to get something done.
[4226.90 --> 4227.26]  I agree.
[4227.66 --> 4233.72]  And I've noticed this being in the, I came in as a developer advocate slash docs at Hybrid.
[4233.72 --> 4243.06]  And, obviously, I found after a little bit working here, I realized, like, wow, the documentation just has such a scaling impact.
[4243.32 --> 4245.16]  I can get up on stage and give a few talks.
[4245.34 --> 4251.72]  But once you write something, everyone can reference it, repeat it, catches like wildfire.
[4251.98 --> 4253.62]  And that's the big impact.
[4254.16 --> 4260.14]  But I feel like between developer advocacy, which is very much going out and really interacting with the community,
[4260.14 --> 4266.86]  and there's a community stewardship aspect to it, there's information teaching aspect to it.
[4267.24 --> 4273.64]  And with documentation, you get, like, you've got the teaching aspect, you've got the formalized baking of features concept.
[4273.96 --> 4280.70]  But there's a space that sometimes falls in between the two, this developer education space.
[4281.38 --> 4285.60]  And it's not always clear who's running with that ball.
[4285.60 --> 4293.94]  And I'm always interested to see who in the community is making that their job and really, like, investing efforts in that.
[4294.04 --> 4302.00]  And I think you see that in some places, like Stripe and Twilio, where they're really going all in on the developer education aspect.
[4302.60 --> 4304.86]  And I think that's something we'll be looking at more and more.
[4305.24 --> 4309.38]  And pardon me for saying it, but the pandemic, with everyone being inside, not being able to be on stages,
[4309.38 --> 4314.84]  we really only had one way of communicating, which was, you know, through the screen.
[4315.28 --> 4319.86]  I think it brought the focus back onto, well, how do we scale this knowledge?
[4320.08 --> 4326.82]  How do we convert the great content that the core engineers are making, that the advocates are sharing on stage and on workshops?
[4327.24 --> 4331.14]  How do we turn that into something that anybody can access at any time, anywhere?
[4331.76 --> 4334.64]  And I just can't wait to see what the next couple of years holds for this space.
[4334.82 --> 4336.96]  I couldn't think of a better way to end the show.
[4336.96 --> 4343.34]  I mean, I didn't even make that connection myself around technical docs and the pandemic.
[4343.84 --> 4346.42]  And, like, there being less ways to learn these days.
[4346.54 --> 4350.42]  You can't go to, like, an in-person workshop as easily as you could in the past.
[4350.56 --> 4353.58]  And so we're forced to get better at this, right?
[4353.62 --> 4358.84]  Similar to, like, how a lot of companies started investing in their testing infrastructure once the pandemic hit
[4358.84 --> 4360.80]  because they found all these bugs on their website.
[4360.80 --> 4368.12]  So, like, I just want to say thank you so much for everything that you bring to this community, Rachel.
[4368.46 --> 4370.00]  We're really lucky to have you.
[4370.56 --> 4373.54]  And truly, like, this is a game changer.
[4374.02 --> 4379.64]  And I'm really excited to at least be witnessing this bar get raised, like, right in front of my eyes, you know?
[4379.64 --> 4381.16]  So thank you so much.
[4381.68 --> 4384.50]  And that's all for today, kids.
[4384.78 --> 4385.80]  Have a good day, y'all.
[4385.80 --> 4391.30]  That's JS Party for this week.
[4391.54 --> 4392.74]  Thanks for hanging with us.
[4393.12 --> 4397.08]  And thanks again for all of the kind words in response to our 200th episode.
[4397.52 --> 4398.26]  Feels good, y'all.
[4398.80 --> 4402.34]  By the way, that's a great episode to share with your friends who may enjoy the pod.
[4402.46 --> 4404.62]  Kind of like a sampler platter, you know?
[4404.98 --> 4406.00]  Plus, it's easy to remember.
[4406.42 --> 4408.20]  JSParty.fm slash 200.
[4408.80 --> 4410.28]  Did you hear the big Svelte news?
[4410.66 --> 4414.56]  Rich Harris has been hired by Vercel to work on Svelte full time.
[4414.56 --> 4415.92]  How cool is that?
[4416.36 --> 4419.82]  And we have Rich coming on the pod in the first week in December, so stay tuned.
[4420.08 --> 4421.26]  We'll surely talk about it.
[4422.26 --> 4427.70]  JS Party is produced by me, Jared Santo, accompanied by the Zelda Trap Jazz of Breakmaster Cylinder.
[4428.16 --> 4430.00]  We are brought to you by some awesome sponsors.
[4430.58 --> 4433.20]  Thanks again to Fastly, Linode, and LaunchDarkly.
[4433.82 --> 4434.92]  All right, that's all for me.
[4435.18 --> 4436.26]  We'll talk to you again next time.
[4444.56 --> 4448.36]  Game on!
[4448.36 --> 4448.38]  Game on!
