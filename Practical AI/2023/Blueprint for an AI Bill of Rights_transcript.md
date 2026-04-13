[0.00 --> 8.64]  Welcome to Practical AI.
[9.20 --> 15.96]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 --> 18.78]  are changing the world, this is the show for you.
[19.20 --> 24.36]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.36 --> 24.66]  listen.
[24.92 --> 26.76]  Check them out at Fastly.com.
[26.76 --> 32.02]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 --> 33.70]  No ops required.
[34.02 --> 36.08]  Learn more at fly.io.
[43.00 --> 46.46]  Welcome to another Fully Connected episode.
[46.88 --> 51.80]  In these episodes, Chris and I keep you fully connected with everything that's happening
[51.80 --> 53.36]  in the AI community.
[53.36 --> 59.90]  We'll take some time to discuss the latest AI news, and we'll dig into learning resources
[59.90 --> 62.36]  to help you level up your machine learning game.
[62.88 --> 63.78]  I'm Daniel Whitenack.
[63.90 --> 68.66]  I'm the founder of Prediction Guard, and I'm joined as always by my co-host, Chris Benson,
[68.94 --> 71.36]  who is a tech strategist at Lockheed Martin.
[71.80 --> 72.70]  How are you doing today, Chris?
[72.96 --> 73.86]  Doing pretty good.
[73.94 --> 74.60]  How are you today?
[75.02 --> 75.86]  Doing really well.
[75.86 --> 82.28]  I told someone earlier today it was a beautiful day outside, and I've got a lot of interesting
[82.28 --> 83.38]  things to work on.
[83.58 --> 86.84]  So yeah, I don't know that I can complain.
[87.70 --> 89.16]  That's a good way of looking at the world.
[89.28 --> 94.16]  I got to say it's a beautiful day outside here in the metro Atlanta area, and I also have
[94.16 --> 95.50]  some pretty fun stuff to work on.
[95.58 --> 96.08]  So you know what?
[96.12 --> 97.70]  We don't have anything to complain about, do we?
[97.76 --> 98.44]  Yeah, yeah.
[98.46 --> 99.28]  I don't think so.
[99.36 --> 102.92]  And it seems like there's just fun things to talk about these days.
[102.92 --> 109.08]  I don't know if you and your immediate circles have been talking about this superconductor
[109.08 --> 110.46]  stuff that's happening.
[110.60 --> 116.46]  Have you been watching the sort of room temperature superconductor buzz, I guess?
[116.78 --> 117.96]  I have not.
[118.10 --> 118.82]  Tell me about it.
[118.92 --> 119.30]  Let's hear.
[119.66 --> 124.84]  Despite having some background in physics, I have not looked at any of this, so I can't
[124.84 --> 128.00]  really comment too much other than just following it from the sidelines.
[128.00 --> 134.12]  But apparently there was a research group that claims to have created a superconductor
[134.12 --> 137.72]  that superconducts at room temperature.
[138.44 --> 144.44]  So people might have seen these videos in the past of like little things levitating on
[144.44 --> 145.80]  something that's really cold.
[146.02 --> 151.12]  That's kind of the typical image of a superconductor.
[151.40 --> 155.00]  Like usually isn't it absolute zero kind of temperatures and stuff?
[155.00 --> 161.04]  Yeah, it's like measured in Kelvin, really low temperature sort of thing.
[161.60 --> 164.38]  So of course, this is very intriguing.
[164.38 --> 167.36]  And I've seen a number of things.
[167.36 --> 170.22]  There's like one group that's claimed they've reproduced it.
[170.32 --> 176.62]  There's others that are skeptical, but, you know, trying to reproduce some of the results.
[176.62 --> 179.80]  So it's like, I forget the name of it.
[179.88 --> 180.98]  I'm going to butcher this.
[181.04 --> 183.68]  I think it's like LK99 or something.
[183.68 --> 185.90]  Yeah, LK99 superconductor.
[186.30 --> 192.82]  So if you want to look at some cool stuff that doesn't involve transformers and neural networks,
[192.94 --> 194.30]  that's cool.
[194.66 --> 195.50]  That sounds interesting.
[195.78 --> 202.46]  So as a non-physicist who likes physics, but a non-physicist, and since we are the Practical
[202.46 --> 204.32]  Superconducting Podcast, of course.
[204.66 --> 205.16]  Practical.
[205.34 --> 211.02]  If you're going to ask me to explain all this, I'm afraid I'm too rusty to do a good job.
[211.02 --> 212.22]  Okay, fair enough.
[212.34 --> 216.10]  I was just going to say, like, what are some of the practical uses of a room temperature?
[216.26 --> 217.28]  I imagine there's tons.
[217.68 --> 223.48]  Well, yeah, I think in general, it's like a superconductor, as the name might suggest,
[223.80 --> 229.94]  conducts, which if you think about that is basically everything used in electronics is
[229.94 --> 231.84]  some type of conductor.
[232.10 --> 232.64]  Good stuff.
[232.82 --> 233.72]  Yeah, good stuff.
[233.72 --> 240.22]  And a superconductor, typically, if it's operating near absolute zero, it's not really that practical
[240.22 --> 244.22]  to put in your everyday electronic items.
[244.56 --> 251.30]  So something that is room temperature, I think, could open up possibilities, I guess.
[251.54 --> 252.06]  I understand.
[252.06 --> 258.72]  So I'm not, again, the superconductor expert, but people might be familiar with semiconductors
[258.72 --> 263.96]  as well, which, of course, are very important to electronics.
[264.46 --> 271.68]  And the supply of those in recent years has caused a lot of news because, you know, chips
[271.68 --> 277.54]  for cars and such have had issues in the supply chain and all of this stuff.
[277.54 --> 284.12]  So you could think about these materials fitting into a similar zone of research.
[284.36 --> 285.56]  It's really interesting.
[286.02 --> 291.66]  And though I don't talk about it much in my day job, there are places where I intersect
[291.66 --> 295.10]  with microelectronics and that is not my area of expertise.
[295.10 --> 299.52]  But I do know that there's quite the revolution going on in that space.
[299.68 --> 305.30]  And so this may be yet another, you know, aspect of what may propel the hardware side of things,
[305.30 --> 308.48]  which I am generally not very knowledgeable about.
[308.80 --> 313.72]  Yeah, there's a ton of stuff going on right now in that space, even in the small town where
[313.72 --> 315.82]  I'm at, where Purdue University is located.
[315.94 --> 321.12]  They're killing it on a lot of fronts, but they just established a huge partnership to
[321.12 --> 327.34]  build a bunch of semiconductor research facilities around Purdue because there is a lot of emphasis
[327.34 --> 335.40]  to kind of decouple chip production from a single location and bring some of that expertise or
[335.40 --> 337.26]  distribute some of that expertise around.
[337.62 --> 343.78]  And so it's quite interesting to follow some of that, which definitely influences the things
[343.78 --> 345.58]  that we talk about on this podcast.
[345.58 --> 346.08]  Yes.
[346.08 --> 351.94]  And in a more far reaching or twice removed sort of way.
[352.06 --> 354.26]  But it's interesting to keep a pulse on for sure.
[354.26 --> 360.88]  I have noticed more and more of the kind of convergence of microelectronics, really modern
[360.88 --> 368.52]  software approaches and artificial intelligence all converging into things and intertwining.
[368.98 --> 373.80]  And and so maybe at some point we need to have some dedicated episodes about some of those
[373.80 --> 375.10]  connection points between them.
[375.50 --> 375.86]  For sure.
[376.08 --> 376.26]  Yeah.
[376.78 --> 380.22]  And that's not the only news that happened this week.
[380.22 --> 389.34]  So as I do most days, you know, pulling up, hugging face and clicking on models and sorting
[389.34 --> 394.64]  by trending, which is the default, seeing what new models are out there.
[394.78 --> 396.52]  A couple of things to announce.
[396.68 --> 403.54]  Probably the most interesting would be stable diffusion XL 1.0.
[403.54 --> 408.34]  People might remember on one of our fully connected, it's not that long ago, we talked about stable
[408.34 --> 415.00]  diffusion XL 0.9, I believe it was, although I get confused with all the acronyms and numbers.
[415.22 --> 421.60]  But that was essentially a research only kind of beta version of what is now released as
[421.60 --> 428.80]  the general release of the new stable diffusion, which is stable diffusion XL 1.0.
[428.80 --> 435.28]  And yeah, I mean, I've played around a little bit with it through ClipDrop and some other
[435.28 --> 438.76]  places and pretty stunning output.
[439.00 --> 439.90]  I've really enjoyed it.
[439.98 --> 444.40]  I've created some posts on LinkedIn with generated imagery.
[444.98 --> 451.78]  They release it under an open rail license, which we've also talked about on this show.
[451.78 --> 457.58]  It's more open, although I think as we talked about in that episode about open rail licenses,
[457.58 --> 463.32]  it wouldn't be considered, you know, open source, quote unquote, but open access in some way.
[463.74 --> 463.82]  Right.
[464.00 --> 466.08]  And yeah, it's pretty cool.
[466.22 --> 470.42]  So I don't know if you're looking at any of the cool images, Chris, but.
[470.86 --> 471.64]  I am indeed.
[471.84 --> 472.66]  As we talk.
[473.74 --> 477.66]  They say that, of course, best ever.
[477.66 --> 481.62]  Obviously, you know, that's the thing to say when you're releasing something.
[481.98 --> 484.98]  They say world's best open image generation model.
[485.06 --> 490.04]  But to your point a moment ago, the word open is gets parsed in all sorts of different ways.
[490.48 --> 490.94]  So correct.
[491.14 --> 491.40]  Yeah.
[491.70 --> 493.96]  There's all sorts of nuances to that.
[494.32 --> 499.92]  So the things that they highlight in the post are better artwork for challenging concepts
[499.92 --> 507.34]  and styles, kind of creating a certain feel imparted, you know, by the prompt.
[508.12 --> 510.94]  More intelligent with simpler language.
[511.66 --> 518.50]  So I guess the thought with this is that the model is able to produce more complicated imagery.
[518.76 --> 526.26]  Like I'm looking at a panda astronaut in looks to be a coffee shop with a iced coffee.
[526.66 --> 527.88]  I see that one on their page.
[527.88 --> 528.12]  Yes.
[528.52 --> 531.92]  Apparently that's comes from a simple prompt.
[532.18 --> 534.50]  Although I don't see the prompt in their post.
[534.58 --> 536.12]  It just says simple prompt, but.
[536.28 --> 537.66]  They need to have more raccoons on it.
[537.74 --> 539.92]  You know, I'm a raccoon aficionado.
[540.38 --> 540.40]  So.
[540.54 --> 540.98]  Yeah, exactly.
[541.34 --> 541.84]  Pandas are fine.
[541.92 --> 545.00]  I like pandas, but they really need a raccoon or two.
[545.34 --> 545.72]  Yes.
[546.66 --> 549.10]  Similar to you said, I think they say the best.
[549.18 --> 551.86]  They also say the largest open image model.
[552.52 --> 556.36]  Though we talked about this on the previous show, how it's a two stage model.
[556.36 --> 560.04]  There's a base model and a refiner model.
[560.20 --> 561.62]  The base model is actually smaller.
[561.78 --> 563.74]  It's 3.5 billion parameters.
[564.04 --> 570.26]  The larger model is the refiner model, which is 6.6 billion.
[571.06 --> 572.80]  So that's a final.
[572.80 --> 579.68]  I think they say denoising, but sort of refining, make the image better step.
[580.06 --> 581.04]  Are those model sizes?
[581.04 --> 585.30]  I noticed they are both under your magical seven number that you educated us on a while
[585.30 --> 585.66]  back.
[585.82 --> 590.20]  Would that be to make this accessible to people so they can get in there and download the
[590.20 --> 592.02]  model and start or not?
[592.10 --> 592.92]  Is it just happen, Jim?
[592.92 --> 603.14]  They say that SDXL 1.0 should work effectively on consumer GPUs with eight gigabytes of GPU
[603.14 --> 607.34]  memory, VRAM, or readily available cloud instances.
[607.34 --> 611.28]  So this is definitely a one GPU model.
[611.52 --> 616.84]  Now, might not be work on all GPUs, depending on how you implement it and how you call it,
[616.90 --> 620.24]  but definitely accessible to people, which I think is really cool.
[620.24 --> 626.12]  And also that, I think, puts it in another realm, which is interesting, another thing
[626.12 --> 627.66]  they highlight around fine tuning.
[628.06 --> 634.10]  So if you have a bigger model, it's also generally harder to fine tune that model for
[634.10 --> 634.98]  your own purposes.
[635.32 --> 642.12]  But along with this, they talk about kind of out of the box support with LoRa or the
[642.12 --> 648.54]  low rank adapters type of technique where you can fine tune the model in a very parameter
[648.54 --> 649.42]  efficient way.
[649.42 --> 653.04]  And so the thought is, hey, people, this is open now.
[653.58 --> 656.02]  Create your own fine tunes off of it as well.
[656.26 --> 664.44]  And I imagine, you know, this was just released while it's been a few days, but the 26th of
[664.44 --> 671.46]  July, as we're recording this 2023, I'm guessing we'll see a whole bunch of fine tunes off of
[671.46 --> 677.62]  this appear on the model hub and elsewhere in days ahead, similar to what we're seeing actually
[677.62 --> 678.36]  with Llama 2.
[678.36 --> 684.40]  So that's the other thing I was going to note on the model hub is just proliferation of
[684.40 --> 685.36]  Llama 2s.
[685.36 --> 689.24]  So we've got if I'm just looking at it right now.
[689.24 --> 692.42]  So I see stable diffusion XL base.
[692.58 --> 694.82]  That's what's trending at the top.
[694.90 --> 697.34]  Then we have the base Llama 2 from meta.
[697.56 --> 704.18]  Then we have stable beluga, which is from also from stable AI and is a Llama 2 fine tune.
[704.18 --> 708.56]  We've got Llama 2, 7 billion, 32K.
[709.06 --> 714.14]  It looks like 32K context link from together computer, the chat Llama.
[714.64 --> 719.94]  And then I see one, two, a whole bunch of other llamas.
[720.18 --> 723.34]  So we'll continue to see those proliferate.
[723.48 --> 723.72]  I think.
[723.98 --> 724.62]  That sounds good.
[724.62 --> 729.78]  While you were telling me that I was busy playing with stable diffusion here with, of course,
[730.28 --> 731.40]  raccoons in space.
[731.58 --> 732.26]  Oh, nice.
[732.46 --> 733.94]  And trying different versions of that.
[734.16 --> 734.42]  Nice.
[734.50 --> 738.18]  Well, let me know how they turn out and definitely post them on all the places.
[738.34 --> 738.84]  There we go.
[738.98 --> 739.94]  We need more raccoons.
[740.06 --> 741.42]  We need more raccoons in the world.
[741.62 --> 742.26]  I know.
[742.42 --> 743.38]  Or out of this world, maybe.
[743.38 --> 750.46]  Yeah, one follow up to on the Llama 2 front, which is connected to the legal topic that
[750.46 --> 756.24]  we talked about before with Damien Reel, which people really love that episode.
[756.44 --> 757.82]  I love that episode, too.
[758.12 --> 763.20]  We'll link it in the show notes about the legal consequences of generated content.
[763.50 --> 769.84]  But I was chatting back and forth and actually Damien got in the Twitter chat, which is there's
[769.84 --> 772.34]  this interesting thing which we didn't really talk about on the show.
[772.34 --> 773.90]  But a lot of people are doing.
[774.48 --> 779.56]  I think it's worth just mentioning it on the show because it's kind of a conundrum to me,
[779.66 --> 785.22]  to be honest, without actually talking it through with a lawyer, which is technically,
[785.22 --> 794.84]  I think you're not supposed to use GPT output to train or fine tune another non-GPT model.
[795.08 --> 801.00]  So what comes out of, let's say you have an open AI account and you generate a whole bunch
[801.00 --> 805.36]  of output from GPT 4, which is going to be really good.
[805.56 --> 812.94]  And then you fine tune an open smaller model on that GPT output and you make the open model
[812.94 --> 814.94]  good like GPT 4.
[815.52 --> 818.00]  So that's what a lot of people are doing.
[818.08 --> 819.66]  It's not really like a hidden thing.
[819.90 --> 822.32]  People are posting these models on Hugging Face.
[822.32 --> 828.20]  And a question on Twitter, which I thought was really interesting and maybe users or listeners
[828.20 --> 835.80]  can consider is, well, first off, it seems to break the license agreement with open AI,
[836.10 --> 840.44]  but also machine generated content isn't copyrightable.
[840.44 --> 846.40]  But also if they do that and then they post the model, can I use the model that they posted
[846.40 --> 852.20]  on Hugging Face if it's sort of from the, what is the thing, poison well or whatever?
[852.88 --> 856.10]  And yeah, what all of that would actually hold up in court.
[856.18 --> 857.60]  It's a whole mix of things.
[857.74 --> 862.52]  So I just, I've been thinking about it a lot and I think it's an interesting thing that we'll
[862.52 --> 863.30]  see play out.
[863.78 --> 863.88]  Yeah.
[863.90 --> 868.82]  I mean, I think the term for kind of that, the sourcing is kind of the provenance of it.
[868.82 --> 869.76]  Am I thinking correctly?
[870.14 --> 874.20]  There's a point where it becomes very, very difficult to follow that.
[874.28 --> 879.16]  And you know, if you have enough rabbit holes that you're going down by using the output,
[879.16 --> 883.24]  I have no idea how that becomes enforceable down the road.
[883.32 --> 885.26]  I think we're seeing a bunch of these licenses.
[885.78 --> 889.58]  I think we saw one from Meta, which basically said you can use it for anything as long as
[889.58 --> 890.46]  you don't compete with us.
[890.70 --> 891.76]  It's me paraphrasing.
[892.10 --> 897.46]  I just have no idea how we would possibly have an organization that could follow through
[897.46 --> 897.80]  on that.
[898.82 --> 905.28]  This is a changelog news break.
[905.28 --> 911.36]  Have you already asked ChatGPT how to design a good UI for your new AI app and gotten back
[911.36 --> 912.00]  bubkis?
[912.92 --> 920.32]  Well, check out LangUI, an open source tailwind library of 60 plus responsive and dark mode
[920.32 --> 924.70]  enabled components tailored for AI and GPT projects.
[924.70 --> 926.96]  What exactly does that mean?
[926.96 --> 933.02]  It means prompt containers, history panels, sidebars, message inputs, and all sorts of
[933.02 --> 934.46]  stuff that are ChatBot related.
[934.66 --> 939.76]  So you can stop asking ChatGPT and build your own ChatGPT with a sweet UI.
[939.76 --> 945.32]  You just heard one of our five top stories from Monday's changelog news.
[945.32 --> 958.06]  Subscribe to the podcast to get all of the week's top stories and pop your email address in at changelog.com slash news to also receive our free companion email with even more developer news worth your attention.
[958.06 --> 961.96]  Once again, that's changelog.com slash news.
[961.96 --> 990.48]  Well, Chris, in addition to seeing interesting things play out with models and licenses and open source or not, and all of these conundrums that we're facing, at the same time, we have policymakers in various places trying to figure out what they should be doing with this.
[990.48 --> 992.64]  I don't know if you've been seeing that.
[993.06 --> 993.76]  I have.
[993.94 --> 994.68]  And it's funny.
[995.02 --> 996.32]  I'm kind of conflicted.
[996.56 --> 999.72]  There's a part of me that looks at this and says, it's important.
[999.88 --> 1000.42]  It's a time.
[1000.54 --> 1001.92]  You know, I mean, we have so much change.
[1002.16 --> 1011.56]  But there's also a part of me, the policymakers are just so far behind this audience, you know, that's listening right now.
[1011.56 --> 1020.38]  And the people that are doing this, that there's definitely a part of me that's kind of ready to shoot spit wads at them, you know, while they're doing it and poke fun.
[1020.90 --> 1022.14]  And maybe that's OK.
[1022.30 --> 1025.28]  I mean, it's what politicians are there for us to poke fun at.
[1025.60 --> 1027.80]  So I'll give them a little credit.
[1027.94 --> 1028.50]  They're trying.
[1028.50 --> 1030.58]  Yes, yes, they're trying.
[1030.90 --> 1037.86]  And one of the things that just came across my path this week is we've heard of this EU AI Act.
[1038.26 --> 1046.06]  And we've talked about it here where they're trying to restrict certain risky uses of AI and other things.
[1046.06 --> 1049.66]  It seems fairly, I think, to some fairly restrictive.
[1050.72 --> 1059.74]  And one of the things that I saw was that there was an open letter from GitHub, Hugging Face, Creative Commons.
[1060.58 --> 1061.34]  I don't know.
[1061.48 --> 1063.20]  I don't even know how this works.
[1063.46 --> 1068.50]  Like, I guess if you're an organization of that size, you know how to get a letter to the right people.
[1068.50 --> 1070.46]  I don't even know if it's open.
[1070.60 --> 1077.52]  You just post it on a website and hope they read it and hope that articles get published about it, which I guess is what happened.
[1077.76 --> 1078.34]  So I don't know.
[1078.64 --> 1081.76]  I don't know if the EU AI Act people are actually reading this.
[1081.94 --> 1084.04]  I guess that is where I was going with that.
[1084.38 --> 1087.06]  But I assume that they are aware of it.
[1087.06 --> 1097.76]  An open letter from GitHub, Hugging Face, and Creative Commons and a number of others calling on the EU to ease some of the rules in the AI Act.
[1098.22 --> 1114.20]  Basically arguing that some of the things in the AI Act are kind of regulating the upstream open source projects as if they're more commercial products, which they're kind of this open source ecosystem.
[1114.20 --> 1128.26]  And I think the fear is that if the restrictions come like they're planned, then that somehow stifles what we're seeing in the blossoming world of open source AI.
[1128.74 --> 1140.08]  So there's probably a counterpoint to that, which would be maybe that sort of blossoming is what's creating, like rapidly creating issues that are hard for people to deal with.
[1140.20 --> 1142.28]  I'm not saying I'm taking either one of those stances.
[1142.28 --> 1143.90]  I'm just trying to play devil's advocate.
[1143.90 --> 1159.40]  If the open source world is really driving this blossoming of things, right, and the blossoming of things is what are causing people to really have a lot of these risky type of scenarios pop up.
[1159.94 --> 1167.90]  You know, how do you put some regulation around that process when you don't want to stifle the open source thing, which I think we all love.
[1167.90 --> 1175.32]  We support that on this show and see how it's benefited things, but also create some problems probably.
[1176.00 --> 1177.66]  And how do you deal with that tension?
[1178.28 --> 1184.56]  Yeah, it's a really hard nut to crack, you know, to figure out where the right balance point is on that.
[1184.56 --> 1198.92]  Because this open letter that we're talking about, you know, it's really getting it that there are all sorts of negative unintended consequences that can come about by taking an action and making it a regulation or a law in doing that.
[1198.92 --> 1206.42]  And yet that's being balanced against really broad fear that the public is expressing.
[1206.64 --> 1211.94]  You know, there's a lot in the general media, you know, not the technical media, not AI media, but the general media.
[1211.94 --> 1215.92]  There's a lot of stories being published about concern going forward.
[1215.92 --> 1223.48]  But then that gets also balanced against organizations with various motivations that are worried about being left behind.
[1223.66 --> 1227.20]  They're worried about their competitors or their adversaries getting ahead of them.
[1227.58 --> 1231.88]  Potentially any given human in any one of those organizations has that same fear.
[1232.48 --> 1236.48]  So if you're a policymaker, how do you approach that problem?
[1236.72 --> 1242.60]  You're kind of lagging behind probably already on the technical side, you know, which kind of going back to the earlier point.
[1242.60 --> 1252.30]  And you're trying to regulate something that's as cutting edge as one can be before it ever happens by looking at what you have today and trying to project into tomorrow.
[1252.60 --> 1254.58]  It's a tough position to be in.
[1254.96 --> 1255.28]  It is.
[1255.38 --> 1266.94]  And I think there's really a lot of fear on both sides that this is, you know, fear on the one side because policy is falling so far behind what is the state of the art.
[1266.94 --> 1279.54]  But fear on the other side, because there's real consequences, like you say, if something is made into a law, whether it's enforced or not, the reality is that it's there.
[1279.54 --> 1287.22]  I'm just looking at Jeremy Howard from Fast AI has commented on some of these things and written a blog post.
[1287.22 --> 1310.84]  But one of the sort of quotes that I pulled out of or that he looked at with the EU Act was the fact that sort of any model made available in the EU without passing certain extensive licensing and approvals could face massive fines.
[1310.84 --> 1324.20]  And if you think about where those models are coming from, if those are just some developer somewhere creating a model and posting it on Hugging Face, certainly that's available in the EU, that puts a liability there.
[1324.42 --> 1327.16]  So there's real consequences on both ends.
[1327.48 --> 1336.44]  Because also if I'm a policymaker, and we've seen this in the US just this week too, people gathering to figure out like, where do we, what do we do?
[1337.12 --> 1338.62]  Yeah, where do we go?
[1338.62 --> 1352.70]  There's a dissonance between the way technology develops and evolves, which is not strictly consistent with nationalities and legal barriers and legal lines to some degree.
[1353.14 --> 1361.60]  And you've seen that in many different things outside of the topic we're talking about, where people will move it to a different nationality, where the laws are different and stuff like that.
[1361.60 --> 1364.42]  But there's an added complication here.
[1364.48 --> 1384.26]  And that is, this is, and we keep talking about it, especially this year, this is moving so bloody fast that the ability to render a law or regulation essentially completely ineffective is quite easy right now by simply moving things around the globe and taking advantage of the different things.
[1384.26 --> 1390.44]  So it's going to be interesting to see how different legal entities cope with this.
[1390.54 --> 1401.52]  How do you make whatever they end up with, whether it be the EU or I was looking at a member of Congress commenting, the White House has stuff out on it.
[1401.52 --> 1412.04]  But how to make that enforceable in the large, if you're really firmly planted, if like if you're an American company who does most of your business in America, you're regulated by American entities.
[1412.42 --> 1413.36]  That's one thing.
[1413.62 --> 1416.42]  But a lot of small businesses don't operate that way.
[1416.56 --> 1418.94]  And they're not strictly limited to that.
[1418.94 --> 1426.42]  So I think going back to our legal episode recently where we talked about the ability to enforce is really going to play out in this.
[1427.10 --> 1429.50]  Yeah, there's the enforcement side.
[1429.68 --> 1445.38]  There's also the side of this, which is how are policymakers thinking about this and what conclusions are they coming to and what guidance are they providing, whether that's put into law or not.
[1445.42 --> 1447.10]  That's an interesting thing to follow.
[1447.10 --> 1449.76]  I think that's one of the interesting things in the U.S.
[1450.46 --> 1455.64]  This week, one of the things that you sent me, which I think has been happening for some time.
[1455.80 --> 1461.44]  Of course, the White House and others have been talking about AI for some time here in the U.S.
[1461.54 --> 1468.82]  But there's interesting things like this blueprint for an AI bill of rights, which is published.
[1468.96 --> 1470.08]  And it's quite interesting.
[1470.08 --> 1486.86]  So just from a practitioner's standpoint, I'm coming to this saying, OK, how are maybe non-practitioners, hopefully advised by practitioners, how are they viewing the way in which we should go about doing our jobs?
[1486.86 --> 1489.92]  Because probably that's going to affect us at some point.
[1490.10 --> 1495.66]  And maybe they have some good ideas to influence how we do things practically.
[1495.84 --> 1501.66]  So it could just be completely ludicrous and it could provide some really interesting talking points.
[1501.72 --> 1502.62]  So I was reading through that.
[1502.70 --> 1504.98]  I don't know if you saw the bill of rights.
[1504.98 --> 1506.50]  I just pulled it up.
[1506.82 --> 1508.94]  And, you know, it's funny.
[1509.16 --> 1511.38]  This is kind of late to the game, in my view.
[1511.76 --> 1524.72]  Several years ago, you know, without going into specifics that could get me into trouble, I was kind of deeply involved in the early details of AI ethics in several organizations doing some of the work.
[1524.82 --> 1526.54]  And here's how I ended up.
[1526.58 --> 1528.30]  It's hard to come up with good principles.
[1528.30 --> 1542.36]  But even as hard as that is, that's still the easy part of the job because the devil is in the details of how you implement and what they mean and how you have the nuance to accommodate all the day-to-day life.
[1542.36 --> 1548.92]  Going back to the discussion we were just having about, you know, open models and unintended consequences and such as that.
[1549.16 --> 1550.56]  It's really hard to do.
[1550.98 --> 1554.08]  They have good verbiage from the White House.
[1554.08 --> 1565.80]  But I still, at each one of the points that they have, I can't help but wonder which of the many ways might you go about interpreting this and implementing any of those interpretations that you have.
[1566.02 --> 1571.84]  It's very nice, lovely, fluffy language and not terribly practical AI yet.
[1572.46 --> 1576.12]  Yeah, I think just to give our listeners an example.
[1576.12 --> 1583.88]  So this is an example of what policymakers are, I guess, giving us as guidance in developing systems.
[1583.88 --> 1590.60]  So for the blueprint, for an AI Bill of Rights, they have various parts of this, like the actual Bill of Rights.
[1591.14 --> 1593.56]  They even say from principles to practice.
[1593.74 --> 1595.44]  So they're from principles to practice.
[1595.96 --> 1598.82]  So they break this down into several different points.
[1598.94 --> 1600.52]  One is safe and effective systems.
[1600.52 --> 1607.00]  So their bill is you should be protected from safe or ineffective systems.
[1607.76 --> 1613.32]  And then they kind of go into what should be expected of automated systems.
[1613.32 --> 1620.08]  Well, it should be expected to protect the public from harm in a proactive and ongoing manner.
[1620.42 --> 1633.44]  And then they give some kind of ways to do that, like consultation, testing, risk identification and mitigation, ongoing monitoring, clear organizational oversight.
[1633.44 --> 1647.82]  So part of me, when I read this, part of me thinks, well, if I go and I try to make my product SOC 2 compliant or something like that, I have to do a lot of those things anyway.
[1647.82 --> 1660.64]  So why is this different than some of the sort of compliance things that are already widely accepted as compliance things that matter?
[1661.30 --> 1665.76]  And maybe it's where AI comes into the automation.
[1665.76 --> 1670.58]  There's some large language model reasoning going on or something like that.
[1670.84 --> 1674.90]  But a lot of these things would be things that I'm already looking at.
[1674.96 --> 1677.72]  Another one, algorithmic discrimination protections.
[1677.94 --> 1680.38]  You should not face discrimination by algorithms.
[1680.64 --> 1684.46]  And systems should be used and designed in an equitable way.
[1685.14 --> 1686.38]  What should be expected?
[1686.86 --> 1688.06]  Proactive assessment.
[1688.06 --> 1690.38]  Representation and robust data.
[1690.52 --> 1692.06]  Guarding against proxies.
[1692.48 --> 1695.58]  Ensuring accessibility during design development and deployment.
[1695.90 --> 1696.90]  Disparity assessment.
[1697.64 --> 1698.68]  Disparity mitigation.
[1699.12 --> 1701.62]  Ongoing monitoring and mitigation.
[1702.30 --> 1705.70]  I think a lot of this is good language, right?
[1706.16 --> 1712.90]  Some of it blurs the line a little bit for me to current things that exist in terms of compliance.
[1713.24 --> 1717.20]  And then some of it is a nice principle, but what do I do with it?
[1718.06 --> 1735.30]  So there was another point on the White House blueprint.
[1736.30 --> 1739.78]  It's a point that I see people grappling with a lot.
[1739.92 --> 1742.02]  And I don't think we found the right answer yet.
[1742.08 --> 1745.04]  And I don't think what they say in it is necessarily the right answer.
[1745.04 --> 1747.70]  Because at the end of the day, I don't think it's practical.
[1748.06 --> 1750.26]  And that point is near the bottom.
[1750.46 --> 1753.64]  They have human alternatives, consideration, and fallback.
[1754.00 --> 1756.94]  And they start off with the first line in bold.
[1757.16 --> 1764.50]  And the first line says, you should be able to opt out where appropriate and have access to a person who can quickly consider and remedy problems you encounter.
[1764.50 --> 1772.00]  And the problem that I have with that particular point is I think that's great for right now.
[1772.00 --> 1778.32]  For us in the moment that we're in at this moment and the level of AI and the level of automation.
[1778.32 --> 1786.74]  But in the years ahead across all industries, we're going to see dramatically increased automation.
[1787.10 --> 1794.86]  We're going to see a number of tasks being automated that are beyond human ability to be able to do.
[1795.04 --> 1796.60]  And that will be a natural progression.
[1796.60 --> 1800.28]  And that may sound scary today as people listen to this now.
[1800.36 --> 1806.36]  But I think that that is the evolution ahead as it always has been long before AI came out.
[1806.46 --> 1811.40]  If you, you know, moving from horse to the buggy, you know, to automobile, that kind of thing.
[1811.40 --> 1817.28]  We move into new directions and there are new concerns and dangers and we have to mitigate them.
[1817.44 --> 1828.50]  But the distinguishing thing about this particular transition that we're just at the early stages of starting is that we will move into things that we can't do in an automated sense.
[1828.58 --> 1829.98]  There is too much happening.
[1830.08 --> 1831.30]  It is happening too fast.
[1831.40 --> 1838.14]  When there are millions of considerations in a tiny fraction of a second, there's no human that can handle that.
[1838.14 --> 1843.66]  And I think that we will certainly make bloopers, but I think that a statement like this is driven by fear.
[1844.14 --> 1847.16]  It's fear of what happens if we lose control.
[1847.42 --> 1849.44]  And I'm not saying that's not a legitimate fear.
[1849.54 --> 1853.54]  I think it's one of those things that we need to be working through in many different areas.
[1853.86 --> 1860.74]  But when the White House starts off by saying, oh, no, no, no, whatever we're going to do, there's going to be a human right there.
[1860.74 --> 1869.08]  It's not really considering what we're observing here, the steep increase in AI being applied across many industries.
[1869.38 --> 1872.14]  So I'm throwing a stone at that particular item.
[1872.52 --> 1872.64]  Yeah.
[1872.90 --> 1879.08]  I do see what they're saying in terms of it could be, there could be this vicious cycle that develops, right?
[1879.08 --> 1884.86]  Because AI is getting better at doing customer service and generating responses.
[1885.46 --> 1890.02]  And AI is getting better at automating systems, right?
[1890.44 --> 1904.24]  So to be hyperbolic, right, if I get on a train car that's automated and there's some problem and I'm stuck on a bridge above a river or something like that,
[1904.24 --> 1913.10]  and I call the support number and it's a generated voice helping me through my issue, right?
[1913.18 --> 1920.16]  This whole thing cycles through automated systems, you know, not working properly for me and then trying to help me.
[1920.16 --> 1925.80]  And maybe actually the, to your point, maybe the automated system can help me guide me through that.
[1925.94 --> 1927.50]  It might be better than the human could have been.
[1927.50 --> 1934.38]  Yeah, I definitely get the concern around this sort of cyclical thing and where does a human actually pop in.
[1934.98 --> 1947.14]  Yeah, I think there's a lot of systems that will operate at speeds as well and with complexities that it's going to be hard for a human to debug these things anyway, right?
[1947.74 --> 1949.22]  So it's an interesting point.
[1949.22 --> 1957.58]  One of the other things that they link in there is this, it's a NIST AI risk management framework, AIRC.
[1958.24 --> 1968.96]  Part of me wonders as a practitioner, like if I'm developing a new software product or I'm offering software in an enterprise setting,
[1968.96 --> 1981.52]  there's probably going to be an expectation on me that I go through some process to maintain GDPR, SOC 2, Type 2, whatever the specific compliance, HIPAA compliance, right?
[1981.96 --> 1986.62]  You know, monitoring you can put in place, there's third party audits, etc, etc.
[1986.62 --> 1997.56]  So part of me wonders is this sort of AI framework kind of morph into maybe not this one specifically,
[1997.56 --> 2003.86]  but will there be sort of risk management frameworks that filter into not necessarily policy?
[2004.08 --> 2007.20]  So I think we've been talking about like the White House and governments.
[2007.32 --> 2009.16]  There's certain things that could be put into law.
[2009.16 --> 2016.28]  But also I could very well see a scenario where one enterprise says to one of their vendors,
[2016.80 --> 2020.58]  oh, are you AIRC compliant?
[2021.10 --> 2023.62]  And how do you prove to me that you are?
[2024.00 --> 2026.34]  Well, maybe it's a third party audit.
[2026.52 --> 2031.24]  Maybe it's a monitoring system like it's done with, you know, HIPAA or other things.
[2031.38 --> 2037.64]  I wonder if we're going to get into some of that as well, where whether or not the policymakers make laws,
[2037.64 --> 2045.24]  I suspect we're going to get into some of these scenarios where we'll have some compliance frameworks put into place
[2045.24 --> 2050.08]  that certain enterprises start forcing on other providers, right?
[2050.20 --> 2058.06]  Because they're accepting some level of liability for the type of AI reasoning that they're integrating into their applications.
[2058.06 --> 2066.54]  So if I'm an insurance company and I'm hiring X vendor to provide some of my AI logic or something like that,
[2066.78 --> 2068.86]  I'm making calls into their system.
[2069.36 --> 2076.50]  Do they have to be compliant in some way beyond the compliance structures that are already in place like HIPAA and others?
[2076.90 --> 2077.42]  Yeah, you're right.
[2077.60 --> 2080.14]  I wasn't trying to cut you off there, but you're totally right.
[2080.24 --> 2083.74]  I mean, that's a huge business opportunity that is to be realized.
[2083.74 --> 2084.84]  You heard it here.
[2085.00 --> 2090.42]  Take it and make the AIRC compliance monitoring framework and you can make some money.
[2090.82 --> 2093.04]  Daniel Whitenack, father of industry right there.
[2093.84 --> 2094.12]  Father.
[2094.62 --> 2097.02]  I'm all the time giving away ideas on this show.
[2097.12 --> 2098.90]  I probably need to keep some every once in a while.
[2099.58 --> 2100.10]  You know what?
[2100.22 --> 2104.38]  To stick with the AI theme, we'll call you the godfather of AI compliance.
[2104.80 --> 2109.02]  Because godfather is a popular thing for at least three luminaries that we know.
[2109.14 --> 2110.16]  Three luminaries.
[2110.88 --> 2111.58]  That's funny.
[2111.58 --> 2118.10]  I don't know if I want me associated with the whole compliance field, but maybe.
[2118.78 --> 2120.58]  Depends how much you pay me, I guess.
[2120.90 --> 2123.16]  Yeah, I was going to say it may not be sexy, but it's lucrative.
[2123.60 --> 2124.54]  Yeah, exactly.
[2125.30 --> 2128.68]  You know, I'm looking at some of this stuff like in the AIRC.
[2129.00 --> 2135.82]  It's there are certain things that I could see just knowing myself having gone through some of the compliance things.
[2135.82 --> 2141.18]  Like when you go through a compliance monitoring thing or an audit, it's like, do you have this policy in place?
[2141.18 --> 2143.26]  Are you educating people about it?
[2143.50 --> 2144.60]  You know, that sort of stuff.
[2144.66 --> 2156.74]  And there's certain things in here, like in the governance section, they're like, the characteristics of trustworthy AI are integrated into organizational policies, processes, and procedures.
[2156.74 --> 2164.30]  So I could just see it now, like, how are you integrating the characteristics of trustworthy AI, blah, blah, blah.
[2164.30 --> 2169.72]  And you'll have to show in some policy, which may or may not be ever read by certain employees.
[2169.72 --> 2171.76]  But hopefully, if you're being truthful, it is.
[2172.32 --> 2174.50]  So, yeah, I think we could see that soon.
[2174.50 --> 2203.48]  Not only that, but the ironic thing about this is that you have this framework here, but with this explosion, this proliferation of models that we keep talking about and new techniques that are just happening all the time and being released, as that continues to accelerate for some period of time, being able to apply these to that quickly enough for market forces to work will almost certainly require compliance AI models.
[2203.48 --> 2207.98]  That can look at new models, how are they approaching and figure out whether or not they're doing it.
[2207.98 --> 2209.68]  That's the real meta thing.
[2210.70 --> 2212.42]  It's meta all the way down.
[2212.56 --> 2214.52]  It's meta turtles all the way down on this one.
[2215.90 --> 2219.76]  There's the podcast title, meta turtles all the way down.
[2220.06 --> 2221.50]  Zuckerberg's all the way down.
[2221.66 --> 2222.20]  That's right.
[2222.20 --> 2233.22]  Well, on these shows, I think it's always good as well to share some practical learning resources with people.
[2233.52 --> 2235.70]  And I did find one this week.
[2235.70 --> 2245.78]  Actually, I monitor Hacker News for my good dose of humor and vitriol and superconductors and all the things.
[2245.78 --> 2256.68]  But one that was really good to point people to would be this patterns for building LLM based systems and products from Eugene Yan.
[2257.12 --> 2258.52]  Hopefully I'm saying that correctly.
[2258.52 --> 2262.52]  And this was a pretty extensive article.
[2263.28 --> 2264.98]  So it's very long article.
[2265.88 --> 2268.62]  And there's various sections in it.
[2268.72 --> 2277.02]  But he walks through a lot of the things that people maybe practically are struggling with in terms of building LLM based applications.
[2277.02 --> 2279.56]  So he talks through evaluations.
[2279.56 --> 2287.76]  He talks through retrieval augmented generation, fine tuning, caching, guardrails, defensive UI, and collecting user feedback.
[2287.76 --> 2298.74]  All of these things, you know, he talks about being used to measure performance, get better task specific results, reduce latency and cost, et cetera, et cetera.
[2298.82 --> 2303.18]  These are all the practical things that people are doing day to day as they're building their applications.
[2303.18 --> 2311.32]  And a little while ago, Anderson Horowitz put out this like evolving ecosystem of the LLM app.
[2311.62 --> 2315.06]  And it had a lot of these pieces on there like caching and guardrails and stuff.
[2315.48 --> 2320.62]  And I think this dives into a lot of those pieces in a much greater amount of detail.
[2320.74 --> 2325.26]  So if you're wondering like, oh, there's this emerging ecosystem of the LLM app.
[2325.26 --> 2334.02]  If you want to know about various pieces of that, I think this is a good way to understand a little bit more about how those pieces fit together.
[2334.22 --> 2339.84]  Just for audience, you slacked me over the link and I clicked on it as you started talking about it.
[2339.92 --> 2342.14]  And as you've been talking, I was kind of glancing.
[2342.56 --> 2351.12]  The very first thing I noticed when it came up was how small the slider on the right side of Chrome was, which expressed how long the...
[2351.12 --> 2352.60]  It's a significant article.
[2352.60 --> 2354.16]  It's a significant...
[2354.16 --> 2360.12]  And then the next thing I noticed was it wasn't a three-minute read or a five-minute or even a seven-minute read.
[2360.22 --> 2362.18]  It's a 65-minute read.
[2362.62 --> 2362.98]  Yes.
[2363.22 --> 2364.08]  And so I started...
[2364.08 --> 2364.58]  You're right.
[2364.72 --> 2371.38]  I mean, just like having not had the 65 minutes to go through it, just looking at this, it is incredibly detailed.
[2371.38 --> 2372.18]  So I can't...
[2372.18 --> 2374.82]  I'm going to dive into this after the show today.
[2375.30 --> 2377.30]  And that's a fantastic learning resource.
[2377.50 --> 2380.54]  I can tell that just all these graphs and everything in it.
[2380.62 --> 2381.14]  It's fantastic.
[2381.56 --> 2382.44]  Yeah, yeah, definitely.
[2382.60 --> 2384.16]  A lot of graphs.
[2384.48 --> 2392.62]  The first one you'll see is LLM patterns on a scale from data to user and offensive to defensive.
[2392.90 --> 2400.48]  In other words, improving performance or reducing cost and risk and kind of plotting those various strategies.
[2401.02 --> 2403.44]  And there's formulas if you want formulas.
[2404.02 --> 2408.02]  There's plenty of stuff that you don't need to read formulas to understand.
[2408.02 --> 2409.78]  But yeah, great resource.
[2409.94 --> 2413.32]  I'm very happy to come across this and point people to it.
[2413.52 --> 2414.26]  Well, it was a good one.
[2414.68 --> 2414.86]  Yeah.
[2415.38 --> 2427.24]  Well, Chris, I don't know what AI adventures are ahead of us in the coming week, but I'm certainly looking forward to talking with you about them next time on a fully connected or with a guest.
[2427.24 --> 2429.30]  We never have a dull week.
[2429.30 --> 2434.96]  There is so much happening that we're always trying to find which thing are we actually going to talk about.
[2435.32 --> 2435.52]  Yes.
[2435.52 --> 2438.12]  So it's a fun time to be in this field.
[2438.12 --> 2438.92]  Yes.
[2439.10 --> 2439.54]  Awesome.
[2440.02 --> 2441.78]  Well, thanks for chatting, Chris.
[2441.86 --> 2442.76]  We'll talk to you soon.
[2443.08 --> 2443.70]  Sounds good.
[2443.80 --> 2444.18]  Take care.
[2444.18 --> 2455.20]  Thank you for listening to Practical AI.
[2455.72 --> 2459.54]  Your next step is to subscribe now, if you haven't already.
[2459.98 --> 2466.00]  And if you're a longtime listener of the show, help us reach more people by sharing Practical AI with your friends and colleagues.
[2466.46 --> 2471.38]  Thanks once again to Fastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2471.38 --> 2475.78]  Check out what they're up to at Fastly.com and Fly.io.
[2476.16 --> 2481.48]  And to our Beat Freakin' residents, Breakmaster Cylinder, for continuously cranking out the best beats in the biz.
[2481.76 --> 2482.66]  That's all for now.
[2482.98 --> 2484.08]  We'll talk to you again next time.
