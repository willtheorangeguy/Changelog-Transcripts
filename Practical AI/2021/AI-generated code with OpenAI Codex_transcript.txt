[0.00 --> 4.22]  These models, for them to be any good, for them to be productive, they've got to end up in software.
[4.50 --> 9.90]  And there's a reason that so much of the modern internet infrastructure has been written in Go.
[10.10 --> 11.84]  It's a fairly small language.
[12.08 --> 16.20]  There's kind of one way of doing everything, which is a struggle for people when they move into it.
[16.20 --> 18.54]  But after you accept that, it's just wonderful.
[18.74 --> 20.24]  So you can remember everything.
[20.50 --> 23.42]  And that means you're more productive and you're less likely to create errors.
[23.66 --> 29.12]  I know, as I've watched over the last few years, the modeling get out and be productive and all these different use cases,
[29.12 --> 35.04]  I think Go is a really good language for doing that in terms of being able to get to productivity quickly with your models.
[38.24 --> 40.90]  Big thanks to our partners, Linode, Fastly, and LaunchDarkly.
[41.26 --> 41.82]  We love Linode.
[41.90 --> 43.32]  They keep it fast and simple.
[43.32 --> 45.82]  Check them out at linode.com slash changelog.
[46.12 --> 48.12]  Our bandwidth is provided by Fastly.
[48.46 --> 52.00]  Learn more at Fastly.com and get your feature flags powered by LaunchDarkly.
[52.28 --> 54.00]  Get a demo at launchdarkly.com.
[54.50 --> 57.88]  This episode is brought to you by our friends at Rudderstack.
[57.88 --> 62.58]  And we're calling all data engineers to check out Rudderstack Cloud and start building smart customer data pipelines.
[63.08 --> 64.82]  Rudderstack is warehouse first.
[65.02 --> 66.00]  No more silos.
[66.46 --> 69.80]  Rudderstack builds your customer data lake on your data warehouse, not theirs,
[70.04 --> 75.50]  enabling all functionality of a CDP with more security and retaining full ownership of your data.
[75.78 --> 78.26]  It's open source and API first.
[78.58 --> 82.02]  Rudderstack can be easily integrated into your existing development processes.
[82.02 --> 85.34]  And because they're open source, you can see all their code.
[85.56 --> 87.98]  So you don't have to worry about vendor lock-in or black boxes.
[88.54 --> 90.10]  And best of all, they have transparent pricing.
[90.30 --> 92.54]  Stop paying your CDP a premium to store your data.
[93.02 --> 97.90]  Rudderstack is free up to 500,000 events and pricing scales transparently from there.
[98.36 --> 100.36]  Learn more and get started at rudderstack.com.
[100.36 --> 102.90]  Again, rudderstack.com.
[103.06 --> 106.60]  That's R-U-D-D-E-R-S-T-A-C-K dot com.
[116.28 --> 123.38]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[123.68 --> 127.76]  This is where conversations around AI, machine learning, and data science happen.
[127.76 --> 132.84]  Join the community and Slack with us around various topics of the show at changelog.com slash community.
[133.16 --> 134.14]  And follow us on Twitter.
[134.28 --> 135.58]  We are at Practical AI.
[140.04 --> 145.14]  Welcome to another episode of Practical AI.
[145.52 --> 147.12]  This is Daniel Whitenack.
[147.22 --> 150.28]  I am a data scientist at SIL International.
[150.66 --> 156.20]  And I'm joined, as always, by my co-host, Chris Benson, who is a tech strategist at Lockheed Martin.
[156.74 --> 157.42]  How are you doing, Chris?
[157.42 --> 158.38]  Doing very well.
[158.50 --> 161.22]  It is Thanksgiving week as we record this.
[161.54 --> 163.86]  And so I'm chilling out.
[164.00 --> 164.90]  No stress, man.
[165.22 --> 165.24]  Yes.
[165.64 --> 167.22]  Getting the Tofurky ready.
[167.46 --> 167.94]  Tofurky.
[168.08 --> 168.50]  Absolutely.
[168.94 --> 169.24]  Yes.
[169.68 --> 175.14]  I'm super pumped this week because Natalie Pastunovic is with us.
[175.26 --> 175.90]  Welcome, Natalie.
[176.32 --> 176.72]  Thank you.
[176.80 --> 177.02]  Hi.
[177.40 --> 177.76]  Hey.
[177.88 --> 179.44]  So I met Natalie.
[180.04 --> 181.94]  I don't remember what year it was, actually.
[182.28 --> 183.70]  But we were in Siberia.
[184.22 --> 185.02]  I do remember that.
[185.76 --> 186.26]  2016, I think.
[186.26 --> 186.66]  Yes.
[186.78 --> 194.08]  So at a conference, 2016, in Siberia, we discussed a lot of Go and AI-related things.
[194.28 --> 196.88]  And I'm glad this has kind of come full circle.
[197.26 --> 205.78]  But also, Natalie is a distinguished co-host of our sister podcast, GoTime, which is all about the Go programming language.
[206.16 --> 206.38]  There you go.
[206.38 --> 207.02]  Yeah.
[207.02 --> 208.12]  Check that out.
[208.24 --> 210.70]  It's great to have some cross-pollination.
[211.22 --> 213.40]  But yeah, Natalie, you're doing so much.
[213.72 --> 221.84]  You're a developer advocate at AeroSpike, OpenAI ambassador, Google developers expert, founder of various things.
[222.20 --> 227.30]  So very honored to have you on the show and excited to talk about all that.
[227.30 --> 231.78]  Maybe to start out, what's it like to be an OpenAI ambassador?
[232.08 --> 233.26]  What's involved in that?
[233.36 --> 234.44]  And what do you get to do?
[234.70 --> 235.88]  That's what I was wondering, too.
[236.16 --> 236.46]  I'm sorry.
[236.56 --> 237.40]  I signed an NDA.
[237.60 --> 238.24]  I cannot answer that.
[238.24 --> 238.42]  Oh, okay.
[238.48 --> 238.76]  Right, right, right.
[238.76 --> 239.46]  No, I'm kidding.
[239.46 --> 246.56]  I'm getting to have a weekly sync with the other six developer ambassadors.
[246.78 --> 247.82]  So there's seven of us.
[248.26 --> 255.90]  And what we get to do is offer office hours for people who get access to GPT-3 and to Codex and to all the other engines.
[256.26 --> 261.76]  And I get to hear all sorts of interesting ideas that people think and try to use the engines for.
[261.90 --> 263.88]  And I get to offer them some help.
[263.88 --> 272.64]  And then we have a weekly sync that we chat between us, kind of interesting ideas that we saw, maybe tips that we can give to each other as ambassadors.
[273.10 --> 276.82]  And we get to hear from the OpenAI team about what's fun and upcoming.
[277.24 --> 281.64]  And we get to sign NDAs and we get to try all sorts of engines before they come out.
[281.80 --> 284.82]  So we got to play with Codex a while before it came out.
[284.94 --> 286.02]  Yeah, that's awesome.
[286.24 --> 287.76]  I have a follow-up even to that.
[287.94 --> 290.16]  I'm diving into follow-ups early on here.
[290.16 --> 299.58]  So without giving away someone's special sauce or super secret idea, what's a really cool thing that you've heard through that or that you've seen or anything?
[299.76 --> 300.26]  I mean, just what?
[300.62 --> 301.74]  Interesting use case or something.
[302.02 --> 302.44]  Yeah.
[303.90 --> 305.52]  She's having to think NDAs.
[305.94 --> 312.60]  From the usage of GPT-3 or Codex, someone said, hey, can we do this?
[312.68 --> 314.92]  And maybe it was surprising to you or something.
[315.32 --> 316.72]  Anything like that that comes to mind?
[316.96 --> 317.64]  Yeah, definitely.
[317.64 --> 334.30]  So one of the things that is less familiar or GPT-3 is kind of less in the titles for is that it has some endpoints that you can create your small little world of knowledge base and then ask it all sorts of questions and kind of maybe it will label things for you and so on.
[334.80 --> 345.68]  So one team wanted to use that to help them understand and kind of analyze cities and kind of like give them properties with that database.
[345.68 --> 351.98]  So they kind of create their own, this is the information that I have about this city and now kind of give me back a description of it.
[352.16 --> 352.70]  Very interesting.
[353.06 --> 364.48]  So I have to reveal I am a total biased user of GPT-3, but also I recently got access to the Copilot Codex stuff and have been trying it out.
[364.48 --> 376.38]  But at SIL, we had this problem where so we translate a lot of content right into various languages and we're working on technology that will help us estimate the quality of those translations.
[376.64 --> 383.26]  The problem is like if we're trying to work on that, we don't have a ton of data with like really bad translations.
[383.26 --> 388.96]  Right. Because everything we've published have been quality checked, good translations of whatever material.
[389.48 --> 396.70]  And so we use GPT-3 to like help us generate like bad contradicting translations.
[396.70 --> 414.28]  So like we said, hey, here's like the source language and here's like what would be like a contradicting statement to this or what would like follow this pattern of like removing like clauses or certain types of information or something.
[414.56 --> 419.10]  So that was actually very useful for us in kind of creating that labeled data set.
[419.10 --> 428.58]  Yeah, I don't know. What's the sort of after you've seen a lot of use cases, what are the kinds of the things that people want to do most with GPT-3?
[428.96 --> 435.72]  Is it like creating like movie scripts or is it like what's the thing that people want to do most?
[436.10 --> 437.42]  Variations of marketing.
[437.72 --> 443.02]  So writing content or adjusting content to different audiences.
[443.02 --> 453.32]  Copy.ai, I think, was one of the very early companies to have raised money that are built very much on top of GPT-3 and many tried to reproduce what they did.
[453.70 --> 455.32]  Yeah. Not surprised by that.
[455.52 --> 455.68]  Yeah.
[456.88 --> 459.02]  You also mentioned Codex.
[459.64 --> 467.10]  So we talked a little bit about GPT-3 and we have mentioned that before on the show, but we haven't talked as much about Codex.
[467.10 --> 476.32]  Could you give us just like a brief sketch of what Codex is and what the intention is that someone might do with it?
[476.56 --> 481.18]  Definitely. Codex is the engine that drives GitHub's Copilot.
[481.18 --> 497.28]  This is one of OpenAI's engines and it is designed to not just perform general language tasks or natural language tasks, but it's specifically trained to translate language to code.
[497.50 --> 508.16]  And it's trained on some languages, so mostly 10 or 15 languages that it's really good at, but it performs great even in other languages that it was not meant to be trained for.
[508.16 --> 517.52]  So Python, it's a language that it performs best at, but as you mentioned, I'm a big fan of Go, and it's also one of the first languages on the list that it's supporting.
[517.86 --> 520.68]  Some unexpected languages that it supports, for example, is Shell.
[521.02 --> 522.30]  Yeah. So like Bash scripts.
[522.34 --> 523.26]  All the Bash magic.
[523.40 --> 523.56]  Yeah.
[523.68 --> 524.28]  Yeah, exactly.
[524.70 --> 525.82]  The data scientists jump.
[525.90 --> 526.40]  Yes, finally.
[527.70 --> 529.58]  All the commands, all the set commands.
[529.80 --> 531.14]  Somebody's going to do that for me.
[531.14 --> 542.06]  Yeah, I mean, it's probably better than my endless stream of copying commands from Stack Overflow, which sometimes do strange things on my local system.
[542.34 --> 545.74]  But yeah, so you mentioned Copilot.
[546.10 --> 549.18]  How do people use Codex in practice?
[549.18 --> 551.80]  So you kind of explained what it does a bit.
[551.94 --> 558.06]  How are people using it or how is it intended to like impact people's workflow or development?
[558.06 --> 565.06]  So probably the most used way of Codex is through Copilot, which is available as a VS Code plugin.
[565.42 --> 570.18]  So anytime you use Copilot, you use Codex, whether you're aware or not.
[570.56 --> 579.92]  And if you have applied to the Codex waitlist and you got your access, then you see the exact same interface that you see when you use any GPT-3 engine.
[579.92 --> 585.94]  And you get to choose kind of syntax highlighting, which is nice and then kind of makes everything familiar for you.
[586.02 --> 591.14]  But you basically kind of give the same type of commands, write this for me or complete that for me.
[591.46 --> 596.68]  And you know that this will perform like particularly good in code.
[596.68 --> 606.10]  And some fun things that I like showing when I'm saying what can it do is just mention casually kind of a name of a library.
[606.10 --> 608.48]  So no direct path or anything like that.
[608.48 --> 612.42]  And say, add a unit test or write a function.
[612.60 --> 614.12]  And here's the signature of it.
[614.12 --> 624.60]  And if we're talking to developers and I'm saying, hey, Daniel, can you take this client, Go client for Aerospike and kind of like do some example of crowd operations?
[624.60 --> 628.62]  You're like, OK, let me Google Aerospike Go client.
[628.96 --> 630.04]  Let me look at the documentation.
[630.04 --> 631.98]  Let me copy paste some examples.
[632.22 --> 633.18]  Let me change one thing.
[633.24 --> 633.78]  Oh, it broke.
[633.88 --> 634.96]  Wait, let me try again.
[635.58 --> 636.84]  Copilot like three seconds.
[636.94 --> 638.44]  OK, here's everything for you.
[638.58 --> 639.34]  Kind of mind blowing.
[639.34 --> 646.48]  It's so much faster than us and it does not make mistakes in the sense of using the library, but also in the syntax of the language.
[646.48 --> 656.58]  It's performing like it knows to do those two things in a few seconds with a little context that you're not even by the time you finish Googling, it already finished doing what you ask it to do.
[656.90 --> 657.04]  Wow.
[657.16 --> 665.98]  So aside from speeding that process up, does it change your workflow in any other ways or is it just the time compression of getting to something productive?
[666.22 --> 667.16]  It's changing.
[667.34 --> 667.76]  Absolutely.
[667.76 --> 672.06]  So some people like reading the documentation and then going and trying things.
[672.20 --> 680.10]  Some people like just kind of finding some quick guide or even just copy pasting from Stack Overflow and seeing how it goes or maybe taking an example and playing with that.
[680.62 --> 684.72]  So sometimes the examples are not covering everything you need.
[684.78 --> 688.14]  So you can say, generate this example for me and then you can start playing with that.
[688.50 --> 689.48]  That's one thing it does.
[689.80 --> 694.28]  Some of the nice things that you can say is add a unit test, right?
[694.32 --> 696.86]  And then maybe it will do something that you did not think of.
[696.86 --> 701.26]  It can propose a different solution for the problem that you have.
[701.26 --> 706.24]  And then, you know, usually you make a pull request and then you start discussing, ah, this is one way of doing that.
[706.30 --> 708.28]  But your colleague tells you, no, you can also do it this way.
[708.34 --> 709.36]  And then you have this conversation.
[709.60 --> 713.40]  So this is becoming a lot faster because you're having this conversation with the AI.
[713.54 --> 717.36]  You're like, give me some proposals, something else, another way to implement this.
[717.36 --> 719.70]  Or here's this function signature.
[720.08 --> 722.24]  And tell me, how would you implement that?
[722.36 --> 725.38]  And so it's sort of like pair programming for the computer.
[725.80 --> 726.06]  Okay.
[726.24 --> 732.08]  Write some unit tests, whether if it's the boring part of just automate, like for all the different types, do that.
[732.08 --> 738.32]  I'm sure there's a lot of data scientists out there who are like, oh, you mean I don't have to write all my unit tests?
[738.82 --> 746.40]  I've had a lot of interactions with data scientists who really want to write that code, but are pretty hesitant to write tests.
[746.68 --> 748.78]  Yeah, you can also say refactor this for me.
[748.98 --> 749.34]  Oh, yeah.
[749.34 --> 759.82]  And I was going to ask, I mean, and it really goes with what you're kind of saying there, Daniel, is there's a point here where no code, you know, it's already kind of coming to realization in various places.
[760.10 --> 761.82]  Where does this go down the road?
[761.90 --> 764.90]  Do you think that are we going to be writing our own go pretty soon?
[764.90 --> 772.06]  Or do you think we're just going to be giving kind of use cases and getting to that or Python or pick your language, whatever it is?
[772.06 --> 781.16]  I think that in the short term, we will be using this in the IDE and getting all the help and different proposals and so on.
[781.24 --> 784.64]  But I do think that no code will go even one step further.
[784.74 --> 790.64]  So not just to your IDE, because for having an IDE, you need to be, you need to have it set up.
[790.74 --> 794.04]  You need to, you know, whatever language binding set up and so on.
[794.04 --> 801.62]  I do see that the world of no code is developing even further to the place that with just an interface, you can already play that.
[801.62 --> 805.88]  So kind of somebody will put a GUI on top of that, and then it will be a few clicks.
[806.42 --> 811.84]  And then it translates to that call to the API of Codex that then generates that code for you.
[812.14 --> 812.24]  Gotcha.
[812.60 --> 813.24]  So I'm curious.
[813.52 --> 816.16]  I mean, you mentioned the different languages that are supported.
[816.42 --> 821.50]  I'm assuming, and it would be interesting to dive into all of these details, which would take a whole nother episode.
[821.50 --> 827.36]  But I'm assuming that like a lot of code from GitHub was used to train this model.
[827.36 --> 835.82]  I've always been curious, like you mentioned how it sort of doesn't make mistakes in terms of the syntax of the language and following those prompts.
[835.82 --> 846.12]  Is that because there's sort of like the prediction of like generated code plus an analysis of like, is this like valid syntax or not?
[846.12 --> 849.74]  Or is that like a rule based analysis of the syntax like behind that?
[849.80 --> 859.12]  Because I know, like with generating natural text, you can certainly generate things that are like not grammatically correct.
[859.88 --> 860.10]  Right.
[860.14 --> 866.64]  And I assume it's similar on the code side, generating things that are not syntactically valid or something like that.
[866.76 --> 869.32]  Any insights there in terms of how that happens?
[869.32 --> 875.56]  Yes, this is a hot topic, especially around the time that the copilot was released first.
[875.76 --> 881.08]  There were lots of questions on what type of license had the content that it was trained on.
[881.34 --> 884.32]  So obviously, it was only trained on the open code, right?
[884.38 --> 891.32]  Not anything that is private on GitHub and only on the like a specific set of licensed code.
[891.62 --> 893.00]  But some code is not licensed.
[893.00 --> 897.38]  And even for some of the licensed types, there was also a discussion whether it's okay or not.
[897.38 --> 904.04]  And the code is generated correct, like whatever grammatically equivalent is for code.
[904.30 --> 911.72]  But what's interesting is that if you tell it something like generate an SSH key for me, it will generate a key for you.
[911.86 --> 914.32]  It will have the right syntax.
[914.58 --> 915.90]  So it will be the right length.
[915.98 --> 920.26]  It will not use like forbidden characters, but it will not be a valid one.
[920.26 --> 930.06]  So this is also an interesting point how it automates development, but not just yet develops infrastructure in this world.
[930.18 --> 933.68]  Because all the world of configurations, it will not do correct for you.
[933.76 --> 935.30]  You still have to put all the keys.
[935.38 --> 940.34]  You still have to set up all those values, you know, because it can generate a value in the right range.
[940.60 --> 941.92]  But does that value make sense?
[942.14 --> 942.94]  That's still to come.
[942.94 --> 959.14]  This episode is brought to you by iMerit and their upcoming ML DataOps Summit in partnership with TechCrunch.
[959.30 --> 962.48]  It's a virtual event happening December 2nd, 2021.
[962.80 --> 966.72]  Check out the speakers and register at iMerit.net slash DataOps.
[966.72 --> 978.46]  The event is gathering more than 700 attendees from top AI and ML companies and feature major speakers, including Facebook AI, Cruise, Zoox, GE Healthcare and more.
[978.92 --> 983.38]  And I'm here with Ivan Lee, the founder and CEO of Datasaur, who's also speaking at the event.
[983.76 --> 989.46]  Ivan, I know you'll be speaking at the conference on this subject, but can you share a teaser of what's happening right now in the NLP space?
[989.68 --> 994.74]  If we look at the advances in NLP over the last few years, there have been some really exciting developments.
[994.74 --> 1003.24]  Perhaps most notably, OpenAI's GPT-3 and their ability to just really start mimicking humans in generating snippets of English language.
[1003.40 --> 1009.10]  What we've noticed is that perhaps of all the branches of AI, NLP is one of the most mature.
[1009.44 --> 1012.96]  And there were some obvious use cases when we were starting out.
[1013.12 --> 1017.74]  There's things like the ability to handle customer support, improve upon chatbots.
[1018.58 --> 1022.32]  These were very clear verticals that we wanted to go after.
[1022.32 --> 1029.94]  But as we learned more, it turns out there's applications in the legal industry, in healthcare, in financial.
[1030.42 --> 1040.00]  There were a number of nonprofit organizations using us to label COVID-19 research and be able to just make sense of all the abundance of research that was coming out.
[1040.32 --> 1044.90]  We were kind of astounded by the creativity and the ways in which NLP could be produced.
[1044.90 --> 1050.72]  All right, learn more and register to attend for this free virtual event at imerit.net slash data ops.
[1051.02 --> 1057.36]  Again, you'll hear from top AI and ML speakers who have successfully deployed machine learning data operations in their organizations.
[1057.86 --> 1060.64]  Again, this event is free and it's virtual.
[1061.20 --> 1064.68]  Learn more and register at imerit.net slash data ops.
[1064.68 --> 1094.06]  Okay, so I did get access to the GitHub copilot.
[1094.06 --> 1096.88]  The trial or whatever they're calling it.
[1097.06 --> 1098.44]  And I've tried out a few things.
[1098.60 --> 1104.48]  For a while, I didn't try it out because I'm one of those annoying people that use Vim.
[1105.00 --> 1108.84]  And so I was like, I don't really want to install VS Code.
[1109.16 --> 1111.68]  But I did because I wanted to try it.
[1111.84 --> 1114.08]  And I think actually I could be wrong about this.
[1114.12 --> 1119.88]  But when I looked at the documentation last on copilot, there was a little bullet that said NeoVim.
[1119.88 --> 1124.00]  So maybe I need to look a little bit deeper into that and play around with it.
[1124.26 --> 1125.90]  And I don't know if you have any info there.
[1125.98 --> 1129.22]  But I did try just like a whole bunch of things.
[1129.58 --> 1137.60]  And what I found interesting was there's sort of like tab complete kind of operations like you might find in Gmail.
[1137.60 --> 1140.68]  And then there's the like prompt type of thing.
[1140.84 --> 1142.66]  So it does seem like there's...
[1142.66 --> 1143.72]  Am I correct on that, Natalie?
[1143.84 --> 1149.68]  That there's sort of like you can start typing something that you're about to do, like a loop or a function or something.
[1149.68 --> 1153.00]  And it will kind of tab complete a lot of things for you.
[1153.06 --> 1158.40]  Or you could like in natural text or a comment tell it to do something for you.
[1158.50 --> 1159.14]  Do I have that right?
[1159.42 --> 1159.58]  Yeah.
[1159.70 --> 1161.82]  Those both are two ways of using it.
[1161.82 --> 1168.64]  I saw a tweet the other day, a funny one that says my next startup is going to be auto generated from scratch by Codex.
[1169.08 --> 1172.96]  I'm just going to press tab until I have a software and then let's see how it goes.
[1172.96 --> 1181.38]  I did think like three years ago, and I probably should have done it, that I should have just created a script that bought.
[1181.66 --> 1191.06]  So took like real words and converted them into something.ai and just like bought up a bunch of domains and then sold them.
[1191.64 --> 1193.20]  But alas, I didn't.
[1193.38 --> 1194.40]  You missed that opportunity.
[1194.74 --> 1195.64]  Oh, yeah, I know.
[1195.64 --> 1199.52]  But yeah, like some of the things I did just to like give people a sense.
[1199.78 --> 1204.40]  And this is like, I'm sure it's not as complicated as the things that you just mentioned.
[1204.40 --> 1212.68]  But as a simple example, I like started like a Python list, like data equals, you know, bracket one comma two.
[1212.94 --> 1217.10]  And then it just like filled in the rest of the numbers for me up to a certain point.
[1217.10 --> 1221.54]  Right. And then it was cool because then I was like, well, I want to create a data frame now.
[1221.68 --> 1223.76]  Right. And that's going to be one of the columns.
[1223.76 --> 1227.22]  And I said, like labels equal bracket A, B.
[1227.52 --> 1231.76]  And then it filled in the same number of things, but with the A, B pattern.
[1232.08 --> 1235.28]  And then, you know, data frame, create data frame.
[1235.36 --> 1236.14]  It did that for me.
[1236.20 --> 1239.92]  And then I just said, you know, comment, you know, save data frame to CSV.
[1239.92 --> 1241.06]  And it did the thing.
[1241.06 --> 1252.02]  So that's just a very simple example, but it was pretty cool to see, like for a non VS code user who was also learning how to use VS code at the time.
[1252.16 --> 1257.40]  I wrote things like very, very quickly, which maybe is blasphemous from from a VEM user.
[1257.74 --> 1259.66]  But it's very exciting.
[1260.12 --> 1269.86]  I want to get back maybe to one thing you mentioned, Natalie, around the the open source code and and, you know, how it was was trained and such.
[1269.86 --> 1271.14]  I wonder if you have any thoughts.
[1271.14 --> 1280.92]  One of the things that I've thought about this whole time with the open AI codex stuff is that like open source code is really like a lot of it's really bad.
[1281.42 --> 1284.70]  And there's a lot of closed source code that's like really good.
[1285.24 --> 1288.32]  Was there like and if you don't know, it's fine.
[1288.38 --> 1294.38]  But outside of like the licensing issue in terms of code quality, like what code might be there?
[1294.52 --> 1298.92]  And also there's all sorts of stylistic like opinions that people have.
[1298.92 --> 1303.56]  So is that part of that, like providing ways to have people have alternates or something like that?
[1303.56 --> 1308.18]  So the wonderful thing about Go is that there's no different styles.
[1308.46 --> 1310.64]  There's GoFund, which is the formatting function.
[1310.84 --> 1311.86]  And then we all use that.
[1312.22 --> 1313.70]  So not in my universe.
[1314.24 --> 1314.36]  Yeah.
[1315.96 --> 1319.22]  I think you probably can see different styles.
[1319.46 --> 1326.08]  I think if you use Copilot, it will stick to the style that you started if you use a different language.
[1326.08 --> 1336.04]  And I do think that if you use the prompt, so kind of a clean way of interacting with it, you will see sometimes one style and sometimes another style.
[1336.14 --> 1336.54]  Gotcha.
[1336.68 --> 1340.36]  And training on good versus bad code, that's a wonderful question.
[1340.52 --> 1343.60]  It's a model that's trained on hundreds of millions of parameters.
[1344.32 --> 1345.88]  Certainly there's good and bad code.
[1345.98 --> 1351.00]  I don't know if it represents the ratio of good, bad code in open and closed source.
[1351.14 --> 1353.36]  I don't know if such a number exists.
[1353.36 --> 1359.88]  Yeah, I'm just thinking that there's code out there that is in the open that I've written that I wouldn't want anything emulating.
[1363.12 --> 1365.06]  So maybe I should deal with that on my own.
[1366.50 --> 1367.74]  I'll take a stab at that.
[1367.94 --> 1369.36]  At my bad code or?
[1369.60 --> 1370.64]  No, no, no, no.
[1371.36 --> 1373.54]  Just the general, because I mean, this has come up before.
[1373.54 --> 1382.46]  I think open source tends to be better than closed source because open source people are going to see if it's out there on GitHub or any other place.
[1382.66 --> 1387.62]  People will see it and people are embarrassed to publish code that's just not very good.
[1387.80 --> 1389.68]  But in closed source, they do it all the time.
[1390.02 --> 1391.42]  I have no shame, I guess.
[1391.74 --> 1391.90]  Yeah.
[1393.98 --> 1396.82]  There's open source, there's closed source, and there's Daniel's code.
[1397.34 --> 1397.54]  Yeah.
[1397.72 --> 1398.12]  Yeah.
[1398.56 --> 1399.74]  It's a whole nother category.
[1399.94 --> 1401.14]  That adds up to OCD.
[1401.14 --> 1401.82]  Yeah.
[1402.88 --> 1403.40]  Right.
[1403.56 --> 1406.84]  Yeah, that works out, which is also a part of my life.
[1407.44 --> 1410.38]  So we've mentioned Go quite a bit.
[1410.54 --> 1417.20]  There's probably a good portion of our audience that might not even be aware of what Go is.
[1417.78 --> 1425.58]  Could you just like maybe give a couple of minutes of like, if I don't know what Go is, what is it?
[1425.64 --> 1430.18]  And how is it sort of like used in things that I might be familiar with?
[1430.18 --> 1435.02]  It's a statically typed language that just celebrated its 12th birthday.
[1435.24 --> 1438.60]  It came from Google, but it's used everywhere.
[1439.14 --> 1441.90]  So not private to Google in any way.
[1442.32 --> 1446.52]  And there's lots of community contributions, obviously more as time goes.
[1446.94 --> 1452.38]  So the closest language to it is Pascal or Pascal, as I heard the American pronunciation for it.
[1452.78 --> 1453.00]  Right.
[1453.00 --> 1454.40]  I like yours better.
[1454.40 --> 1462.40]  It's pretty close to C, but it has all sorts of benefits like built-in concurrency and parallelism.
[1463.20 --> 1469.34]  It has safety and it's used in all sorts of tools that you know.
[1469.50 --> 1473.50]  So obviously in the beginning, it was used mostly for web development.
[1473.50 --> 1480.48]  So lots of websites and it kind of bubbled into the world of DevOps and infrastructure.
[1480.80 --> 1483.08]  So Docker is written in Go.
[1483.22 --> 1484.62]  Kubernetes is written in Go.
[1485.12 --> 1488.74]  If you do monitoring, you might have heard of Prometheus or Jaeger.
[1489.14 --> 1490.44]  Both are also written in Go.
[1490.84 --> 1493.54]  SpaceX is unofficially shared.
[1493.78 --> 1494.48]  They're using Go.
[1494.48 --> 1496.02]  So it will be on Mars soon.
[1496.52 --> 1496.82]  Exciting.
[1497.18 --> 1497.34]  Yeah.
[1497.44 --> 1500.58]  I know also that Go is used at CERN.
[1500.90 --> 1504.60]  I have a friend there that's using Go for high energy physics.
[1504.80 --> 1506.34]  It's a whole range of things.
[1506.66 --> 1506.78]  Yeah.
[1507.08 --> 1507.32]  Yeah.
[1507.54 --> 1507.78]  Yeah.
[1507.88 --> 1509.00]  It's mostly backend.
[1509.16 --> 1513.22]  It's not exactly great for front end, but surely you can do something.
[1513.34 --> 1516.16]  Also, you probably can do something with mobile if you really want to.
[1516.16 --> 1524.44]  I personally see it not just a great fit for web and for tooling, but also for things like
[1524.44 --> 1525.10]  machine learning.
[1525.84 --> 1532.10]  And I think we've both been preaching the idea of using Go in the infrastructure of systems
[1532.10 --> 1533.30]  that do machine learning.
[1533.42 --> 1539.26]  So serve AI models, because it's wonderful with parallelism and concurrency, and it's super
[1539.26 --> 1539.66]  fast.
[1539.84 --> 1543.50]  And it has this really nice feature that it's very easily cross-compilable.
[1543.50 --> 1547.68]  So one CLI command, add the flag, and you're good.
[1547.92 --> 1554.68]  So that's also why teams that do tooling internally really love that, because you have five people
[1554.68 --> 1558.16]  or five types of operating systems and whatnot, and architectures.
[1558.26 --> 1559.28]  You just add all flags.
[1559.82 --> 1560.04]  Done.
[1560.24 --> 1561.50]  Your binaries run everywhere.
[1561.94 --> 1562.12]  Yeah.
[1562.32 --> 1567.90]  And I definitely am really excited that this messaging is getting out on this channel,
[1568.00 --> 1571.12]  because I definitely believe in what you're saying.
[1571.12 --> 1574.28]  On our team, and it's sort of a mix, right?
[1574.32 --> 1578.58]  I think it's still a mix because maybe you can comment on your workflow with this, Natalie,
[1578.78 --> 1588.42]  but there's so much tooling in the sort of experimentation phase of AI around training and testing models
[1588.42 --> 1590.60]  that's really great in Python.
[1590.60 --> 1595.36]  But our team has found that as you sort of transition that out, right?
[1595.42 --> 1596.62]  You've done your experimentation.
[1597.52 --> 1603.42]  You know this model architecture and this sort of data is what we want to do, and it's useful in these ways.
[1603.54 --> 1606.60]  This is the access pattern and how we want to run inference.
[1606.60 --> 1615.34]  Then transferring to running that behind an API that's written in Go or a streaming server that's written in Go
[1615.34 --> 1622.10]  or some type of batch processing infrastructure that's written in Go that sort of integrates with that model
[1622.10 --> 1626.50]  is what we've found to be a really useful pattern in my own work.
[1626.58 --> 1631.04]  I don't know if you have any comment about that, Natalie, if I'm off or if you have other thoughts.
[1631.04 --> 1637.10]  No, I definitely share this to you that this is a great choice, although it's not a trivial one.
[1637.74 --> 1645.32]  And I do think that as AI kind of bubbles into any field like legal tech or agri tech or whatnot,
[1645.70 --> 1649.76]  like this is all becoming things of how do you serve your AI model?
[1650.22 --> 1654.60]  One thing is kind of have it trained and running, but then comes everything else.
[1654.60 --> 1662.10]  And there is a wonderful paper by a group of Googlers from 2015 about the technical debt of AI systems.
[1662.10 --> 1667.96]  And it's kind of what happens when you patch up a system that does ML and quickly upload it to production.
[1668.20 --> 1674.40]  And it lists over 12 or so pages of everything that can go bad and all the considerations you should have.
[1674.98 --> 1680.40]  And, you know, it's things that in the past you may have not thought of them in the context of systems that serve AI,
[1680.52 --> 1683.90]  but you just thought of them as kind of general systems or any website.
[1683.90 --> 1692.58]  But monitoring, security, all the additional stuff that like making sure that things are working, all these systems.
[1693.08 --> 1698.88]  It's the wonderful ecosystem of infrastructure that already has the perfect ecosystem inside Go.
[1699.12 --> 1701.08]  Everything you need is kind of already there.
[1701.28 --> 1708.42]  So plugging those two together is even a better reason for using Go because Go is really fast for serving your model
[1708.42 --> 1710.92]  and also really useful for monitoring everything.
[1710.92 --> 1718.90]  There's a thing, and I know we've brought it up before, and that is that these models, for them to be any good, for them to be productive, they've got to end up in software.
[1719.60 --> 1725.30]  And there's a reason that so much of the modern Internet infrastructure has been written in Go.
[1725.64 --> 1727.60]  It gives you all those things that you just talked about.
[1727.68 --> 1731.50]  It gives you two other things that we alluded to earlier I just wanted to bring back up.
[1731.50 --> 1741.32]  It's a fairly small language, and part of that is, going back to what you were saying, is there's kind of one way of doing everything, which is a struggle for people when they move into it.
[1741.64 --> 1746.58]  But after you accept that, it's just wonderful, so you can remember everything fairly easily.
[1747.02 --> 1750.64]  And that means you're more productive and you're less likely to create errors.
[1750.64 --> 1763.48]  And so I know, as I've watched over the last few years, the modeling get out and be productive in all these different use cases, I think Go is a really good language for doing that in terms of being able to get to productivity quickly with your models.
[1764.04 --> 1776.42]  And one other benefit for this characteristic of Go is that if you have the AI generate a huge chunk of Go, it will look exactly like the code that you wrote, because there's only one way of doing that.
[1776.42 --> 1781.98]  So you know that uncanny valley of robots, you're not going to see the uncanny valley of code.
[1782.40 --> 1784.66]  If it looks too human, it's too creepy.
[1785.00 --> 1790.12]  But once you cannot tell whether it's a robot or a human, you're happy with it again.
[1790.58 --> 1795.92]  And because there's only one way of writing Go code visually, you will not be able to know who generated that.
[1796.20 --> 1801.92]  So you're not falling into that uncanny valley, unlike with many other languages that have multiple formats.
[1802.28 --> 1802.40]  True.
[1802.44 --> 1804.40]  So that's why it's a great language for AI.
[1804.40 --> 1808.62]  So like sort of bringing this back to the codex world.
[1808.86 --> 1824.44]  So if we're generating code, and there's like a lot of variability in like style or how you might do something, or even like things like, like there's a lot of Python 2 code out there and Python 3 code out there, right?
[1824.84 --> 1827.48]  You know, Go sort of is more consistent like that.
[1827.48 --> 1841.06]  So would you say that like, it's maybe a bit easier to get bigger chunks of code generated and Go than like, just kind of the small helps that I was alluding to earlier in Python, where like I was doing small-ish things.
[1841.58 --> 1841.74]  Yeah.
[1841.74 --> 1849.48]  And you will feel easier reading it and integrating that into your code base or creating that to be your code base and you integrate into that.
[1849.48 --> 1868.72]  We are going to ship.
[1868.88 --> 1871.42]  Three, two, one.
[1871.42 --> 1879.14]  I'm Karhal Azu, host of Ship It, a show with weekly episodes about getting your best ideas into the world and seeing what happens.
[1879.54 --> 1885.62]  We talk about code, ops, infrastructure, and the people that make it happen like charity majors from Honeycomb.
[1886.04 --> 1890.54]  We act like great engineers make great teams, but it's exactly the opposite.
[1890.54 --> 1894.34]  In fact, it is great teams that make great engineers.
[1894.70 --> 1898.14]  And they finally, when the founders of continuous delivery.
[1898.42 --> 1901.22]  Start off assuming that we're wrong rather than assuming that we're right.
[1901.42 --> 1904.14]  Test our ideas, try and falsify our ideas.
[1904.22 --> 1906.26]  Those are better ways of doing work.
[1906.26 --> 1908.54]  And it doesn't really matter what work it is that you're doing.
[1908.64 --> 1910.38]  That stuff just works better.
[1910.82 --> 1919.88]  We even experiment on our own open source podcasting platform so that you can see how we implement specific tools and services within changelog.com,
[1919.88 --> 1921.94]  what works and what fails.
[1922.30 --> 1926.18]  It's like there's a brand new hammer and we grab hold of it and everyone gathers around.
[1926.28 --> 1930.08]  We put our hand out and we strike it right on our thumb.
[1930.32 --> 1933.16]  And then everybody knows that hammer really hurts.
[1933.30 --> 1935.80]  When you strike it on your thumb, I'm glad those guys did it.
[1935.86 --> 1937.22]  I've learned something instead.
[1937.36 --> 1942.24]  Yeah, I think that's a very interesting perspective, but I don't see that way.
[1942.40 --> 1942.66]  Okay.
[1942.74 --> 1945.86]  It's an amazing analogy, but I'm not sure that applies here.
[1946.20 --> 1948.50]  Listen to an episode that seems interesting or helpful.
[1948.50 --> 1950.30]  And if you like it, subscribe today.
[1950.42 --> 1951.54]  We'd love to have you with us.
[1951.54 --> 1977.36]  So we were talking just before we started recording about this whole world of ML ops or AI ops and how that is like so,
[1977.36 --> 1981.64]  so much of the conversation in the AI world is centered around this.
[1981.64 --> 1986.16]  We've got sort of various takes on this over time on the podcast.
[1986.32 --> 1997.78]  And I'm curious, like when you're thinking of ML ops or like when you're thinking of a project that is coming up in your pipeline and it involves machine learning or AI in some way,
[1998.08 --> 2005.38]  like what is it that you have in mind in terms of like the ML ops things that you need to be thinking about?
[2005.38 --> 2009.30]  So kind of what is a checklist for your ML ops project?
[2009.30 --> 2018.44]  Like what are the first things that are like, yeah, the necessities of ML ops that are just crucial to making things work in production?
[2018.80 --> 2019.64]  It's a great question.
[2019.74 --> 2021.46]  And I think it's getting this bare minimum.
[2021.60 --> 2026.08]  It's getting more complex or like the longer every year this list gets a bit longer.
[2026.08 --> 2029.74]  So you definitely need to have some sort of data processing, right?
[2029.82 --> 2032.66]  Data governance variation, you'll call that.
[2032.82 --> 2035.00]  You need something for serving the model.
[2035.14 --> 2039.68]  You need something for the feedback loop of retraining it online or offline.
[2039.96 --> 2048.34]  So a growing trend that I noticed over the last year or two is about feature extraction, feature engineering, feature stores and so on.
[2048.40 --> 2053.18]  So you almost cannot ignore this anymore in the context of ML ops.
[2053.18 --> 2058.62]  I guess because it's an AI podcast, we don't need to talk what is a feature, which is fun.
[2058.88 --> 2060.64]  We get to talk instead about what is Go.
[2061.02 --> 2065.90]  But the reason that I think that Go is a good choice for that, for things about features is again,
[2066.02 --> 2071.66]  it's that it's really fast in all the different benchmarks, partly because they're good concurrency.
[2072.08 --> 2074.12]  And it's also easy to utilize this feature there.
[2074.62 --> 2074.76]  Yeah.
[2074.92 --> 2080.62]  We were also talking with for the show about how both of us have been trying to promote this within the Go community.
[2080.62 --> 2085.20]  And I'm really excited because you are giving a talk at the upcoming GopherCon.
[2085.50 --> 2089.96]  So this will be December of 2021 for those listening in.
[2090.08 --> 2092.54]  So if you can find it on the internet after that.
[2092.92 --> 2098.66]  What are you hoping that sort of your audience takes away from that talk at GopherCon,
[2098.80 --> 2102.32]  who may be an audience that isn't as familiar with AI,
[2102.68 --> 2106.12]  but is into all of these infrastructure and monitoring things?
[2106.30 --> 2109.56]  What are some of the takeaways that you hope they'll have?
[2109.56 --> 2116.70]  So for the good practices of MLOps, there's some short checklist of things that you should have in mind,
[2117.10 --> 2123.44]  like be aware of all the things that MLOps mean and why Go is a great choice for that.
[2123.56 --> 2127.08]  And the more general cause that I have,
[2127.14 --> 2131.50]  and I hope that everybody who comes to the talk eventually will have as kind of a heads up of,
[2131.62 --> 2135.78]  this is how AI is likely to integrate into your developer flow.
[2135.78 --> 2139.74]  Whatever it is you're doing with Go or even in another language, really.
[2140.36 --> 2142.08]  And, you know, you can be cynical about this.
[2142.16 --> 2144.70]  You can say, no, I'll keep, I'll stick to what I know.
[2144.76 --> 2148.56]  But you can also utilize all the different benefits that we said,
[2148.60 --> 2150.72]  like you can automate boring parts.
[2151.06 --> 2153.74]  So, you know, we all love Kubernetes for doing that for us.
[2153.84 --> 2157.28]  And not just because it's boring, but also it actually prevents us from making mistakes.
[2157.28 --> 2163.36]  You get inspired for all the autocompletions or the alternatives that it offers for you.
[2163.76 --> 2170.22]  And a huge thing that we didn't give enough focus that it can do is that documentation,
[2170.76 --> 2172.78]  but like both ways documentation, right?
[2172.84 --> 2177.98]  It can help you document your own code and it can help you read somebody else's code
[2177.98 --> 2182.36]  if the documentation is bad slash non-existent or just a language that you don't know.
[2182.36 --> 2187.58]  Can Codex add like comments, like I can just say add comments to this text
[2187.58 --> 2188.88]  or comments to this code?
[2188.96 --> 2190.04]  Will it do that yet?
[2190.20 --> 2191.34]  Yeah, explain this code.
[2191.82 --> 2192.12]  Awesome.
[2192.40 --> 2192.88]  That's awesome.
[2193.08 --> 2196.76]  It can be something like help me understand this code base that I wrote last year
[2196.76 --> 2198.06]  because I forgot what I did there.
[2198.14 --> 2198.84]  That hits home.
[2200.72 --> 2202.04]  I was just thinking that.
[2202.18 --> 2202.58]  Exactly.
[2203.00 --> 2205.04]  I always look back on my old code and go, oh.
[2205.38 --> 2205.98]  Who did that?
[2206.16 --> 2207.98]  Who hacked into my computer and changed everything
[2207.98 --> 2210.50]  and then also changed the history of commits and the timestamp?
[2210.64 --> 2211.10]  How dare they?
[2211.34 --> 2211.74]  Exactly.
[2212.36 --> 2215.78]  So sometimes you have to understand what somebody else did.
[2215.86 --> 2219.32]  Like, for example, I'm really not good in front-end technologies.
[2219.88 --> 2221.00]  I am generalizing.
[2221.26 --> 2224.10]  I've barely experienced working with any of these,
[2224.16 --> 2225.70]  but sometimes you have to understand what's happening.
[2225.80 --> 2227.64]  So I can go and try to understand it.
[2227.70 --> 2229.82]  I can go and find a developer to explain that to me,
[2229.84 --> 2233.38]  or I can just highlight this and say, hey, AI, please explain this for me.
[2233.72 --> 2235.28]  So I have a question for you.
[2235.32 --> 2237.68]  I actually want to take the same question Daniel asked you
[2237.68 --> 2241.86]  about kind of bringing the Go folks kind of into AI.
[2241.86 --> 2246.08]  And for some of the folks that are listening to this podcast right now,
[2246.22 --> 2248.38]  and they've been hearing us talking about Go,
[2248.50 --> 2251.76]  they may not have been exposed to it very much in the past, maybe not at all.
[2252.18 --> 2253.42]  But they're now kind of curious,
[2253.76 --> 2256.42]  having heard the three of us chit-chatting about it for a few minutes.
[2256.42 --> 2259.60]  How would they incorporate that or start to?
[2259.72 --> 2264.00]  What would be a reasonable way of them doing that to get that into their flow right now,
[2264.06 --> 2265.26]  maybe alongside their Python?
[2265.76 --> 2267.22]  What's a good first step for them?
[2267.68 --> 2271.42]  If you have access to Copilot or Codex,
[2271.72 --> 2275.06]  just take any code in Python, highlight it, and says,
[2275.18 --> 2276.28]  rewrite that into Go.
[2276.52 --> 2277.96]  Run that, see what happens.
[2278.14 --> 2278.80]  That's fantastic.
[2279.02 --> 2281.24]  That's one thing I would do right away,
[2281.44 --> 2283.30]  because I first like to play with that,
[2283.34 --> 2286.00]  and then I'm going to go and read the docs and kind of go through the tutorial.
[2286.00 --> 2288.22]  So once you've played with that a little bit and got excited,
[2288.56 --> 2289.94]  Google for the tour of Go.
[2290.14 --> 2292.58]  This is a fun little sandbox that you can,
[2292.82 --> 2296.50]  like it's a guided step-by-step of all the things that you need to know.
[2296.70 --> 2298.74]  It's not specific for AIOps.
[2298.80 --> 2300.42]  It's not specific for Ops in general,
[2300.42 --> 2302.72]  but it does cover most of the interesting features of Go
[2302.72 --> 2304.82]  and kind of helps you understand how it's built
[2304.82 --> 2306.68]  and what's happening under the surface
[2306.68 --> 2309.88]  and how can you utilize the fun features that it has.
[2310.00 --> 2310.78]  It's been around for a while.
[2311.06 --> 2313.98]  You can definitely find some code examples.
[2313.98 --> 2316.02]  If you want to see, Daniel,
[2316.18 --> 2319.36]  is there a workshop that you're giving about this topic,
[2319.42 --> 2322.88]  about infrastructure in Go for ML stuff?
[2323.00 --> 2324.74]  Is it available anywhere?
[2325.08 --> 2328.48]  Yeah, so I'm giving an updated workshop at the upcoming GopherCon.
[2328.90 --> 2330.32]  So thanks for bringing it up.
[2330.54 --> 2334.10]  There will be the GopherCon event in early December,
[2334.68 --> 2335.74]  and there are workshops.
[2335.96 --> 2339.10]  Also, the main event is free for everyone.
[2339.34 --> 2341.06]  That's my understanding this year.
[2341.06 --> 2344.16]  So the sort of main talks you'll be able to join.
[2344.60 --> 2349.60]  But then, yeah, I'm going to post an updated version of my workshop
[2349.60 --> 2352.40]  around the time of the workshop.
[2352.62 --> 2354.76]  So if you're listening to this and it's early December,
[2354.76 --> 2358.60]  you can check out my GitHub and see some updated things there.
[2359.02 --> 2361.18]  But yeah, I think it's a great idea, Natalie,
[2361.42 --> 2365.32]  to rewrite some Python stuff in Go to see how it might look.
[2365.32 --> 2371.06]  It's fun to see that Codex can be like a productivity thing,
[2371.18 --> 2373.22]  but maybe it can also be a learning thing.
[2373.52 --> 2377.32]  Chris, I don't know if you remember one of the early shows that we had was like,
[2377.62 --> 2382.92]  there was an app that helped African farmers identify disease spots on cassava plants.
[2383.12 --> 2383.88]  I do remember.
[2384.10 --> 2386.24]  The model was completely capable of saying like,
[2386.30 --> 2387.68]  this is diseased or not, right?
[2387.68 --> 2394.98]  But the intentionality behind the app was that it wanted to sort of help infuse that knowledge in the community, right?
[2395.08 --> 2401.60]  So it pointed out things and sort of explained why they might be indicative of what, you know.
[2401.72 --> 2406.62]  And by doing that, it sort of freed the community from dependence on the app.
[2406.66 --> 2408.08]  And that knowledge was sort of infused.
[2408.08 --> 2414.00]  So it's cool to see that like, you know, these tools can also, you know, automate things for us,
[2414.00 --> 2418.38]  but also help us kind of gain knowledge in new areas a lot quicker.
[2419.04 --> 2419.78]  So, yeah.
[2420.18 --> 2423.12]  Kind of cool when AI brings humanity into focus there.
[2423.38 --> 2424.44]  Yeah, yeah.
[2424.74 --> 2428.62]  Natalie, I know you do a lot of community related things,
[2428.62 --> 2433.38]  whether it's the open AI stuff or it's related to Google developers
[2433.38 --> 2436.70]  or with GopherCon Europe or GopherCon.
[2436.70 --> 2441.66]  When you're sort of talking about AI and machine learning,
[2442.22 --> 2447.22]  I'm just curious how you've seen those conversations shift over time.
[2447.38 --> 2454.36]  Because I think early on, like I heard people talking about like Terminator and sentient things.
[2454.54 --> 2459.86]  I've seen some of those conversations shift over time to other maybe more useful subjects.
[2459.86 --> 2462.40]  But as you're interacting with those communities,
[2462.40 --> 2468.22]  have you noticed any trends in terms of people's interest in AI or their fear around AI
[2468.22 --> 2472.46]  or their desire to do this or that or any thoughts on that?
[2472.86 --> 2481.14]  Yeah, I think in 2017, I talked and shared some code that I wrote on how to use Go with TensorFlow,
[2481.50 --> 2484.78]  which seemed as unrelated as using Go with mobile.
[2485.24 --> 2487.18]  And Go with mobile has never really picked up.
[2487.18 --> 2491.06]  It's still under the experimental path of the Go project.
[2491.54 --> 2495.44]  But the TensorFlow API actually is available in Go.
[2496.04 --> 2499.88]  And I guess it came not just from the side of the software of like,
[2499.94 --> 2502.72]  here's how you can use that and use that API and so on,
[2502.76 --> 2504.74]  but also from the side of the infrastructure.
[2504.74 --> 2511.58]  And here's how the entire monitoring and DevOps ecosystem that is already in Go mostly,
[2511.88 --> 2518.36]  just fitting itself nicely with ML as ML and AI bubble into the average tech stack.
[2518.70 --> 2521.54]  So now you have front end, you have back end and you have AI.
[2521.82 --> 2522.98]  Everything is getting automated.
[2523.30 --> 2526.58]  And we obviously have to support that as DevOps people,
[2526.76 --> 2529.60]  as infrastructure people, as back end people, as a tech team.
[2529.72 --> 2530.84]  That's a great point.
[2530.98 --> 2532.10]  I love that point.
[2532.10 --> 2537.46]  I'm going to steal your point going forward is that we find ourselves commonly talking about how AI,
[2537.70 --> 2539.22]  you know, is in software.
[2539.34 --> 2540.86]  It's a part of software now and stuff.
[2540.96 --> 2545.44]  But the way that you just put it in terms of a front end and back end, now there's AI.
[2545.62 --> 2548.54]  And there's a reason for it's not just for data scientists.
[2548.54 --> 2549.78]  It's for developers.
[2549.78 --> 2554.28]  And there's so many tools like what you're working on that are making it accessible to people.
[2554.50 --> 2558.44]  How do you think that will change the software development world going forward
[2558.44 --> 2565.16]  in terms of how non-specialists and AI are engaging now that these new tools like Copilot
[2565.16 --> 2567.96]  and Codex are becoming part of the workflow?
[2567.96 --> 2574.68]  I think it will make things faster and efficient in the sense of how, you know, in the past,
[2574.74 --> 2576.88]  you developed code by writing everything.
[2577.08 --> 2582.62]  And then IDEs came and got all those fun plugins and useful things like show me the signature,
[2582.80 --> 2586.38]  remind, help me find quickly where the function is defined and so on.
[2586.40 --> 2588.28]  And it became a part of your workflow.
[2588.56 --> 2592.12]  Although it depends how back you go for the developer's history.
[2592.24 --> 2593.56]  This would be considered a cheat.
[2593.60 --> 2594.56]  And like, oh, I don't need that.
[2594.56 --> 2597.34]  I'm just, I just need the clear notepad.
[2597.48 --> 2602.82]  So I see this as a next step of something that fits the world of developer productivity.
[2603.14 --> 2611.12]  It also helps boost the world of no code, which kind of introduces into the community of people
[2611.12 --> 2616.88]  who create tech, people who don't know code, just because they will have the tools that will
[2616.88 --> 2621.82]  translate their English commands into tech or into code, right?
[2621.82 --> 2626.80]  So we as developers, we kind of in our mind, we do this translation from our instructions
[2626.80 --> 2631.78]  in English in the GitHub issue from the product manager, whatever you translate that into code.
[2632.20 --> 2637.02]  And then the machine goes and translates that into compiled binaries for you.
[2637.30 --> 2641.52]  So in addition to this being, this flow being more efficient, it's going one level up of
[2641.52 --> 2644.46]  abstraction that I will just write in English what I need.
[2644.56 --> 2649.80]  I will play with the GUI and the AI will tell the computer to compile the code that it generated
[2649.80 --> 2656.22]  for us. So I see that as we go forward, there'll be like these two branches of developer productivity.
[2656.64 --> 2661.52]  But I also see that things like infrastructure and monitoring, not necessarily going to be as
[2661.52 --> 2667.20]  affected by that because you cannot have it, like you cannot say to the AI, create a config
[2667.20 --> 2673.12]  file for me. And you can just go ahead and use that because the numbers will be funny and the keys
[2673.12 --> 2674.80]  will be funny as we talked in the beginning.
[2674.80 --> 2679.42]  So this is something that people will still have to manually do for a while.
[2679.90 --> 2684.26]  Yeah, I hope that maybe that comes someday. But I think even those other things that you mentioned
[2684.26 --> 2690.76]  are just like an amazing new kind of development and how we write code and how we think about the
[2690.76 --> 2696.32]  things that we automate and the code that we generate. So I'm super happy that you joined us on
[2696.32 --> 2704.26]  the other podcast in changelog. And we will include a number of links that are relevant to this
[2704.26 --> 2710.72]  discussion, including the waitlist for the codec system, along with the sign up for co-pilot.
[2710.92 --> 2717.40]  We'll also include links to GopherCon and all the cool Go stuff that we mentioned. So if you're
[2717.40 --> 2723.60]  interested in either of those things, definitely check out those links and make sure and listen to
[2723.60 --> 2729.36]  Natalie's upcoming talk at GopherCon. I know I will be. So thanks so much, Natalie. Appreciate
[2729.36 --> 2730.72]  you taking time to join us.
[2730.92 --> 2732.06]  Thanks, Daniel. Thanks, Chris.
[2735.50 --> 2740.14]  That's our show. Thanks for listening. For more like this, check out our master feed.
[2740.14 --> 2746.82]  It is all changelog podcasts in one easy to consume place. Let your podcast app snag everything we
[2746.82 --> 2752.50]  produce and then pick and choose which ones to listen to. Subscribe today at changelog.com slash master,
[2752.50 --> 2757.62]  or just search for changelog master in your podcast app of choice. You'll find it. Special
[2757.62 --> 2762.64]  thanks to Breakmaster Cylinder for providing our music and to our longtime sponsors, Fastly,
[2762.88 --> 2767.44]  LaunchDarkly, and Linode. That's all for this week. We'll talk to you again next time.
[2767.44 --> 2785.20]  Bye.
[2790.34 --> 2790.56]  Bye.
[2792.72 --> 2793.76]  Bye.
[2793.76 --> 2794.12]  Bye.
[2794.12 --> 2796.22]  Bye.
[2796.22 --> 2798.22]  You
