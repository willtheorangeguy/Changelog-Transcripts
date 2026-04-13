[0.00 --> 8.64]  Welcome to Practical AI.
[9.20 --> 15.96]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 --> 18.78]  are changing the world, this is the show for you.
[19.20 --> 24.36]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.36 --> 24.66]  listen.
[24.92 --> 26.76]  Check them out at Fastly.com.
[26.76 --> 32.02]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 --> 33.70]  No ops required.
[34.02 --> 36.08]  Learn more at fly.io.
[43.08 --> 46.40]  Welcome to another episode of Practical AI.
[46.76 --> 48.30]  This is Daniel Whitenak.
[48.38 --> 54.10]  I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris
[54.10 --> 57.16]  Benson, who is a tech strategist at Lockheed Martin.
[57.70 --> 58.40]  How are you doing, Chris?
[58.82 --> 59.96]  Doing well, Daniel.
[60.14 --> 61.82]  What are we in search of today?
[61.96 --> 63.22]  What's the topic coming up?
[63.42 --> 64.22]  That's a good one.
[64.36 --> 72.56]  Well, I mean, we've been talking about ChatGPT and people using it for search and other things,
[72.68 --> 79.46]  but we've got the real powerhouse with us today, Brian McCann, who's co-founder and CTO at
[79.46 --> 83.18]  you.com, which is an AI search engine.
[83.30 --> 84.08]  How are you doing, Brian?
[84.62 --> 85.56]  I'm fantastic.
[85.96 --> 87.18]  I'm so excited to be here.
[87.42 --> 87.74]  Yeah.
[87.94 --> 93.16]  Just got finished watching an old episode last night with Demetrius and laughed about all
[93.16 --> 96.58]  the ML Ops stuff I've learned myself at you.com over the last couple of years.
[97.52 --> 97.96]  Yeah.
[97.98 --> 105.62]  There's no shortage of cringe moments in the ML Ops journey, but yeah, that was a good one
[105.62 --> 106.46]  for sure.
[106.46 --> 116.34]  Maybe just taking an initial step back at you.com, AI search engine, how did you come
[116.34 --> 124.56]  upon this idea that there needed to be a new type of search engine and in particular one
[124.56 --> 127.26]  that involves some type of AI within it?
[127.60 --> 130.90]  How did this idea come to shape and what is you.com?
[131.34 --> 132.24]  Maybe we can start there.
[132.72 --> 133.02]  Great.
[133.20 --> 133.50]  Yeah.
[133.56 --> 134.70]  I can tell you all about it.
[134.70 --> 139.74]  It depends on how far back you really want to go, but I'll start back when my co-founder
[139.74 --> 144.14]  and I were at Salesforce doing research in natural language processing.
[144.48 --> 148.46]  My co-founder and our CEO, Richard Socher, was the chief scientist there.
[148.46 --> 156.58]  And we worked for quite a few years on exactly the kind of technologies that are getting kind
[156.58 --> 160.06]  of more math adoption today, like these large language models.
[160.56 --> 165.78]  When I started out, it was a challenge to get them to do anything.
[166.18 --> 170.44]  And oftentimes people would question why anybody worked on language models.
[170.44 --> 175.02]  It was starting to almost become hard to get any publications about them because they were
[175.02 --> 178.40]  supposed to be just a theoretical exercise of some kind.
[178.40 --> 183.68]  But then over the course of several years in our research and first transfer learning,
[184.36 --> 190.48]  contextualized word vectors, and then pushing multitask learning and unified approaches to natural
[190.48 --> 193.80]  language processing, we saw what was happening.
[194.50 --> 201.60]  And eventually we ran some pretty fun experiments, even with authors and writers around collaborations
[201.60 --> 205.68]  with generative AI, like GPT tools today.
[206.40 --> 209.80]  And the first moment was that it was just kind of fun and inspiring.
[210.16 --> 211.28]  You know, it was starting to work.
[211.28 --> 217.24]  And seeing that, I think both of us started thinking about what was really going to happen
[217.24 --> 218.52]  in the next few years.
[218.98 --> 220.38]  And there's two ways you go.
[220.54 --> 223.84]  All this NLP stuff becomes as good as it is today.
[224.10 --> 230.68]  And it just goes into making Facebook ads better or something like that, or Instagram ads.
[230.86 --> 236.96]  And all that understanding that we work on doesn't really go into something that I was super
[236.96 --> 238.06]  stoked about at the time.
[238.06 --> 242.96]  You know, I came from a philosophy background, got into all the natural language stuff because
[242.96 --> 248.10]  I was interested in meaning and understanding what meaning was, which took me into the analytic
[248.10 --> 250.66]  philosophy direction and focusing on language.
[250.78 --> 256.62]  So for all of that to then just channel into like selling my little sisters something better
[256.62 --> 259.46]  on Instagram was not really what I was hoping for.
[259.88 --> 261.06]  And that was the first thing there.
[261.24 --> 267.18]  And then the second was, I think, after we had both seen much of the research community
[267.18 --> 271.94]  adopt this direction, which was really not popular when I was just starting out.
[272.24 --> 273.60]  You know, this was controversial.
[273.80 --> 276.36]  It was even against software engineering principles.
[277.72 --> 283.92]  Engineers at various research groups and companies would actually decry some of what we were advocating
[283.92 --> 288.96]  for because, well, how can you disentangle and understand where problems are in the model
[288.96 --> 290.28]  if you're training on all this data?
[290.28 --> 296.06]  It was not exactly neat and tidy from a software engineering principle perspective.
[296.32 --> 298.92]  But after four or five years, everybody was doing it.
[299.72 --> 307.72]  And so we felt like it was time to start looking at an area where maybe people felt similarly
[307.72 --> 311.16]  about the likelihood of it changing much.
[311.86 --> 316.92]  And search was one of those areas where it was very much like the original time in NLP.
[316.92 --> 319.34]  People were like, oh, you know, we should do it this way.
[319.72 --> 322.68]  And there was a lot of people saying, no, that sounds like a bad idea.
[323.46 --> 325.34]  And they come around to it eventually.
[325.88 --> 329.30]  Now with search, I can tell you over the last couple of years, yeah, lots of people asked
[329.30 --> 331.38]  me like, why the heck wouldn't you start a search engine?
[331.80 --> 336.08]  But we saw a lot of these technological advances coming, you know, and we saw that there was
[336.08 --> 337.28]  this inflection point coming.
[337.86 --> 343.92]  We wanted to be on the other side of research and kind of directing and channeling that into
[343.92 --> 344.96]  a better way to do it.
[344.96 --> 347.88]  And search was really the gateway of the internet for that.
[348.48 --> 354.20]  It's for so many people, the place they go that they then find the rest of the internet,
[354.46 --> 355.32]  they find information.
[355.86 --> 361.64]  And it becomes like a key point for people where this technology and understanding them
[361.64 --> 363.56]  can then help them in different ways.
[363.68 --> 368.46]  So with U.com, we wanted to really found the company on three values of like trust, facts,
[368.46 --> 374.44]  and kindness and leverage this technology to make search more about serving you and using
[374.44 --> 379.38]  understanding rather than, you know, just monetizing your attention.
[379.84 --> 388.44]  And from your perspective, I mean, people probably think that at least algorithms like have played
[388.44 --> 389.28]  a role.
[389.52 --> 394.74]  Like maybe generally people think like, oh, there's sophisticated algorithms behind search.
[394.74 --> 401.40]  Now people are talking about like AI driven search, neural search, semantic search.
[401.58 --> 407.08]  Could you help us kind of like parse out like what's fundamentally different about like the
[407.08 --> 412.22]  things people are talking about now when they're referring to that sort of like AI and neural
[412.22 --> 418.98]  search, as opposed to like what might have been going on like all along with what isn't like
[418.98 --> 424.92]  dumb algorithms, but like they're not in the same sort of class as this other type?
[425.32 --> 425.94]  Yeah, for sure.
[426.26 --> 431.98]  I mean, I think, you know, five years ago before generative AI was really on the radar and now
[431.98 --> 434.88]  we still thought there was AI involved in search.
[435.08 --> 436.82]  It just wasn't the kind that we're seeing today.
[437.06 --> 441.26]  So AI has been trying to understand this for a long time.
[441.50 --> 446.34]  What's happening now is the algorithms or the kind of AI we're using, the neural networks
[446.34 --> 453.04]  we're using are much better at understanding the context of what we're trying to say.
[453.04 --> 458.40]  But I think this is one of the key underlying features of what we're seeing.
[458.80 --> 464.14]  So when you type to it or you're talking to it, one of the dot threads has been understanding
[464.14 --> 464.82]  context.
[464.98 --> 468.24]  We started out with training word vectors in NLP.
[468.84 --> 474.28]  So if people are familiar with word vectors, every single word or token has a vector that's
[474.28 --> 475.28]  associated with it.
[475.84 --> 477.84]  And that was pretty much all the context we had.
[478.50 --> 483.24]  And we started looking at sentences as a whole to take into consideration context.
[483.82 --> 487.52]  And now these things are reading, you know, as much of the internet as they can get their
[487.52 --> 493.24]  hands on custom data sets, supervised training data on top of all the unsupervised training
[493.24 --> 493.54]  data.
[493.54 --> 497.82]  And with that comes this more nuanced understanding.
[497.92 --> 500.46]  Every parameter that we're adding in these models are getting bigger.
[500.84 --> 504.52]  They're recording some subtlety of how we use language, right?
[504.66 --> 508.78]  Just mimicking our behavior and picking up on those patterns.
[509.04 --> 510.70]  So the first is understanding context.
[510.82 --> 513.70]  And then the second is the generative aspect of it.
[513.70 --> 519.36]  So there's taking in a piece of text from you and understanding what that means, but
[519.36 --> 520.60]  then producing text.
[520.70 --> 524.34]  And I think that's been the part that's really, really exciting for people.
[524.70 --> 528.78]  Both have been really important for us at u.com and building a search engine differently.
[529.34 --> 537.10]  But now with uChat, for example, these generated responses are really opening up a different
[537.10 --> 544.18]  way of serving users that's totally in line with what we were planning for u.com as well.
[544.26 --> 550.44]  Because we really wanted to move search from being just about finding blue links to ideally
[550.44 --> 555.78]  replacing every blue link in as many cases as possible with the thing you'd actually want
[555.78 --> 558.40]  to do or the information you'd actually need.
[558.92 --> 562.00]  And these generative models have essentially memorized a lot of the information on the other
[562.00 --> 563.26]  side of those links.
[563.26 --> 567.54]  So it makes it a lot easier for you to access and they can spit it back out at you.
[568.18 --> 572.14]  No, I was just going to say as kind of a follow-up to that, I'm kind of talking about the world
[572.14 --> 573.46]  before and the world after.
[573.66 --> 578.48]  I mean, obviously, kind of the big news thing that's changed the public's perception lately
[578.48 --> 581.60]  was chat GPT and the public kind of becoming aware of that.
[581.66 --> 587.24]  And you guys have been out there leading the way all along, you know, for years at this
[587.24 --> 587.56]  point.
[588.04 --> 590.82]  How does that public perception change?
[590.82 --> 598.68]  How has that changed u.com and uchat and things like what, aside from just the technology
[598.68 --> 604.22]  considerations, how has that changed the way you guys are approaching, you know, your business
[604.22 --> 608.06]  in the marketplace with that public perception change at large?
[608.76 --> 610.66]  It's a different world from six months ago.
[610.66 --> 611.88]  Oh, it's fantastic.
[612.28 --> 612.86]  It is.
[612.98 --> 613.94]  It absolutely is.
[614.04 --> 619.04]  I think so many of the things that we had started to build into u.com, you know, we had
[619.04 --> 620.72]  some generator writing tools.
[620.84 --> 622.80]  We had image generation tools.
[623.04 --> 627.12]  We call them apps inside u.com because we have a platform for developers to build these
[627.12 --> 627.94]  apps into it.
[627.94 --> 636.40]  And what we saw happen was the door kind of opened to do some of these newer things with
[636.40 --> 641.50]  more acceptance from a much wider portion of the population.
[641.76 --> 647.72]  I think like a lot of people had expectations about what search was and what search should
[647.72 --> 648.32]  do for them.
[648.32 --> 653.14]  And even though we were at the forefront of that, releasing these things, that kind of
[653.14 --> 658.24]  moment last fall, really, when it started going viral is when everybody kind of dropped
[658.24 --> 663.30]  those expectations and said, Hey, what is this new technology that could be dooming something
[663.30 --> 665.96]  like search for us in a very different way?
[666.04 --> 672.58]  And so with that, you know, uchat has been super popular and it's becoming more and more
[672.58 --> 674.54]  popular as part of u.com.
[674.54 --> 679.06]  Right now we have more default normal search experience, but then you can also use the
[679.06 --> 680.06]  conversational approach.
[680.74 --> 682.74]  And that's really picking up a ton of traction.
[683.14 --> 687.28]  And it's clear there's a lot of use cases that it just serves users better for.
[687.98 --> 694.84]  So while you all were talking, I was asking uchat, how can AI be integrated into search?
[695.18 --> 697.82]  And at least you're consistent with uchat.
[698.10 --> 702.04]  The answer is AI can be integrated into search in a variety of ways.
[702.04 --> 707.02]  For example, AI can be used to provide more accurate search results by understanding user
[707.02 --> 709.58]  intent and the context of their search query.
[710.22 --> 711.04]  So there you go.
[711.66 --> 712.08]  There you go.
[712.24 --> 717.22]  But I mean, I just mentioned I have, you know, I have uchat on my phone.
[717.34 --> 718.32]  I've been playing with it.
[718.44 --> 721.76]  And really, I don't even know if I would consider playing it, but using it.
[721.76 --> 727.96]  And I think one of the things like people are realizing, yeah, it's fun to like generate
[727.96 --> 734.28]  like a new like Eminem rap song about like AI or something in chat GPT.
[734.44 --> 741.16]  But people are starting to think about these like interfaces as like tools that can, like
[741.16 --> 745.74]  you said, give them the content that they're really after without them having to follow
[745.74 --> 746.72]  a bunch of links.
[746.72 --> 753.68]  Now, like the search industry in general, I think has been like there's money to be made
[753.68 --> 755.92]  by pointing people to links, right?
[756.02 --> 760.28]  And ads like promoting links from your perspective.
[760.28 --> 766.38]  Like how does this shift in people thinking now about like a chat interface, which isn't
[766.38 --> 772.32]  driven by these links influence maybe like the industry at large and maybe some responses
[772.32 --> 777.50]  that we'll see across the industry, because like that's kind of the bread and butter of
[777.50 --> 779.86]  how everything works in search, right?
[780.62 --> 781.02]  Absolutely.
[781.58 --> 781.88]  Yeah.
[782.24 --> 784.06]  It's a big question right now.
[784.06 --> 789.50]  And I think it's one that's exciting to see evolve over the next however long.
[789.62 --> 795.36]  But from our perspective, what we've been trying to set up with u.com from pretty much
[795.36 --> 802.72]  the start, though we released it publicly last fall as well, is this more open platform approach
[802.72 --> 810.94]  to search where partners, content creators, developers, whoever it is that owns what's
[810.94 --> 819.18]  on the other side of the link has an active role and a clear way to monetize and benefit
[819.18 --> 821.68]  from anything that these languages are generating.
[821.68 --> 829.22]  So, for example, you know, a partner can come into u.com and create an app in a couple hours
[829.22 --> 834.20]  if they've got an API or they can just give us the data and we'll create a search API for them,
[834.32 --> 835.18]  support the infrastructure.
[835.76 --> 841.58]  And then we'll show an app that either allows people to interact with their product, kind
[841.58 --> 846.52]  of like a try before you buy way, or the information from their site, but they own
[846.52 --> 847.10]  that space.
[847.10 --> 854.18]  So it's not like more traditional search engines where, you know, any monetization that happens
[854.18 --> 859.86]  on their website is their monetization and traffic has to get to that other place for
[859.86 --> 861.06]  those of people to monetize.
[861.68 --> 865.02]  At u.com, the app itself is considered theirs.
[865.68 --> 868.88]  And any monetization that happens is theirs at that point.
[869.16 --> 871.34]  So it's kind of flipping the script in a way.
[871.54 --> 875.32]  Like you said, that's the biggest shift that we can see happen.
[875.32 --> 880.98]  And we can also see a lot more people moving towards paying for some of these tools as
[880.98 --> 886.80]  productivity tools and kind of tools that empower them more rather than just a tool that
[886.80 --> 890.18]  connects them to different things, which they're very used to having free.
[890.46 --> 895.74]  I imagine what's going to come out of it will be some combination of the two, but there will
[895.74 --> 902.30]  be more and more of a shift towards providers being closely linked to that content.
[902.30 --> 907.96]  Even if the content is less clearly attributable through a language model.
[907.96 --> 912.34]  But it's something that's, it's going to be interesting to see how all the different
[912.34 --> 918.24]  industries adapt or try not to adapt and, you know, try to keep things the way they are.
[919.14 --> 924.82]  So you were talking a little bit about the idea of using it for tooling and some of the
[924.82 --> 925.38]  things now.
[925.38 --> 930.08]  And that got me, as you were kind of describing that before the break, I got me wondering,
[930.38 --> 935.84]  can you talk about some examples of, of how you chat and the technologies underlying that
[935.84 --> 938.56]  and the algorithms might be used to enhance tooling?
[938.68 --> 942.38]  What are some of the things that you're thinking about, you know, when you're laying awake at
[942.38 --> 945.86]  night thinking about what's next, where, where do I want to go with this?
[946.22 --> 946.42]  Yeah.
[946.72 --> 947.68]  Great, great question.
[947.68 --> 953.64]  Back in the summer before that, we'd been working mostly on what we called uCode.
[954.10 --> 959.66]  And we were starting to bring in a lot more developer resources and generative AI specifically
[959.66 --> 962.06]  for generating code on behalf of developers.
[962.80 --> 968.60]  And now with these more conversational interfaces as well, you see people going to them a lot
[968.60 --> 975.94]  for writing code, even debugging code, debugging code that the AI asks or that the AI generates
[975.94 --> 980.92]  for them already, see a lot of people going and, you know, just saying, this is what I
[980.92 --> 981.54]  have in my fridge.
[981.80 --> 983.02]  Like, what can I make with this?
[983.52 --> 989.20]  And, and much broader sets of questions that then the conversational interface allows you
[989.20 --> 995.20]  to gather some context on over the course of the conversation in a much more seamless
[995.20 --> 999.04]  way until you can get a satisfying answer or response.
[999.58 --> 1002.28]  But yeah, lots of marketing, lots of students as well.
[1002.28 --> 1007.82]  We had an application called you write that's still inside you.com.
[1008.14 --> 1012.66]  And that's been really popular with students, for example, because it can come up in the
[1012.66 --> 1013.06]  chat.
[1013.82 --> 1018.98]  Sometimes like you can ask it to do some things, but getting the language model nudging in the
[1018.98 --> 1023.24]  right direction is still something that's challenging for people who don't quite understand
[1023.24 --> 1023.80]  how to do it.
[1023.80 --> 1030.82]  And so these productivity tools usually involve a little bit more of a touch from our side
[1030.82 --> 1034.76]  to make it like really useful for a particular niche.
[1035.18 --> 1039.18]  I just want to note that going to the refrigerator and saying, this is what I have, it's going
[1039.18 --> 1041.04]  to be really, really useful for me.
[1041.86 --> 1042.26]  Yeah.
[1042.92 --> 1045.30]  For me, it's like nothing in there.
[1045.44 --> 1045.88]  What do you do?
[1046.26 --> 1046.66]  Yeah.
[1046.66 --> 1049.84]  I was going to say like, it's pretty sparse in my fridge right now.
[1049.84 --> 1054.06]  So I don't know that there's a good answer to that regardless, like go to the grocery
[1054.06 --> 1054.52]  store.
[1054.84 --> 1056.00]  My wife makes fun of me.
[1056.06 --> 1057.46]  She's like, put something together.
[1057.46 --> 1058.18]  And I'm like, what?
[1058.36 --> 1060.50]  So this is going to be, that's a good use case, actually.
[1060.74 --> 1060.94]  Yeah.
[1061.56 --> 1067.42]  So you're talking about like this kind of like idea of like a thread of conversation, which
[1067.42 --> 1074.02]  people like learn about some topic or like the, the thread provides context for a response
[1074.02 --> 1074.74]  or answer.
[1074.74 --> 1081.66]  But I'm also intrigued, like some of the unique things about you chat in particular and you.com,
[1081.82 --> 1088.22]  like sort of more generally is like a little bit more holistic view of like multiple modes
[1088.22 --> 1094.08]  or multimodal like approaches to where, um, Hey, like I'm not always just getting a text
[1094.08 --> 1094.98]  blob, right?
[1095.44 --> 1101.74]  Sometimes I want a text blob and sometimes like I actually don't like if I'm asking about
[1101.74 --> 1106.40]  the weather, maybe I want like a little graph of like, you know, a little card telling me
[1106.40 --> 1107.20]  about the weather.
[1107.20 --> 1113.76]  So could you explain a little bit, maybe how you all are thinking about multimodality in
[1113.76 --> 1119.86]  terms of like these sorts of natural language interfaces, maybe both in terms of like the
[1119.86 --> 1126.88]  outputs, but potentially also in terms of the inputs, um, and like how you're thinking
[1126.88 --> 1130.30]  about merging those technologies and those inputs together.
[1130.72 --> 1130.82]  Yeah.
[1131.32 --> 1132.02]  Great question.
[1132.66 --> 1133.44]  It is the future.
[1133.84 --> 1137.30]  You know, it's so much, I think of what we're learning from language.
[1137.42 --> 1140.48]  Some of it starting to make its way into image generation, right?
[1140.60 --> 1143.58]  With many tools that have come out, but all these other modalities as well.
[1143.76 --> 1150.88]  In you.com in particular, you chat has access to the kind of more traditional search engine
[1150.88 --> 1151.68]  underneath it.
[1151.70 --> 1157.46]  So it actually uses that more or less a little metaphorical, but it knows how to understand
[1157.46 --> 1161.50]  your intent and it can go out and ask what kind of information it needs from different
[1161.50 --> 1161.86]  sources.
[1162.58 --> 1166.16]  Um, and it can also interact with all of these apps that we've created in the open platform.
[1166.16 --> 1171.00]  So if you are looking for weather, it can go and say, Oh, give me the chart for the
[1171.00 --> 1171.28]  weather.
[1171.40 --> 1176.34]  And over time, it's a little bit of a contrite example, but I would want it to look at that
[1176.34 --> 1179.08]  data and be able to answer any question you want about that data.
[1179.08 --> 1184.04]  You know, maybe run its own Python code, you know, doing statistics over that data.
[1184.12 --> 1187.82]  If you really wanted that, you know, it should be able to do all of these things.
[1188.24 --> 1189.50]  Uh, same goes for finance.
[1189.68 --> 1195.24]  You know, if you ask about a particular stock, UChat is not going to necessarily tell you in
[1195.24 --> 1200.42]  text about all the things that you would want to know, you know, the volume and high and
[1200.42 --> 1201.40]  all those things.
[1201.46 --> 1204.02]  It's going to show you a nice application there.
[1204.20 --> 1208.92]  And then over time, we're enabling UChat to use that data more and more.
[1209.08 --> 1214.84]  It's ground its responses in that data in the same way that it's currently grounding and
[1214.84 --> 1220.34]  citing search results right now to try to lessen the effect of hallucination, which has
[1220.34 --> 1225.30]  been like a really kind of widely known problem with some of these generative models, especially
[1225.30 --> 1226.22]  in the research days.
[1226.22 --> 1230.48]  That was one of the most frustrating aspects of these models, you know, and they're getting
[1230.48 --> 1230.94]  better.
[1230.94 --> 1236.00]  Um, and they're especially better when you ground them in other kinds of data, like our
[1236.00 --> 1239.04]  open platform apps or the search engine results themselves.
[1239.50 --> 1242.12]  So we're going to use that to make it better and better.
[1242.24 --> 1247.62]  And I mentioned, you know, writing Python code for itself, you know, we want it to be able
[1247.62 --> 1251.52]  to pretty much do anything that you'd want to do on the internet.
[1251.52 --> 1254.10]  Like that's where this kind of technology can go.
[1254.24 --> 1260.32]  Kind of realizing the promise of some of those early kind of persistent like things,
[1260.42 --> 1260.62]  right?
[1260.68 --> 1265.04]  Like Siri and Cortana, you don't want to just say, oh, tell me about this thing.
[1265.12 --> 1267.22]  We want to be able to do things for you.
[1267.46 --> 1272.92]  And we want to keep moving more and more towards that vision of kind of what we call like a do
[1272.92 --> 1274.74]  engine instead of just a search engine.
[1275.44 --> 1275.90]  Very inspiring.
[1276.04 --> 1280.40]  What you're saying as you're looking at the world going forward and you're trying to think
[1280.40 --> 1285.22]  about like getting those capabilities out into all the places.
[1285.70 --> 1289.42]  Um, and as you're looking at, you know, whether it be something as mundane as you're in the
[1289.42 --> 1294.56]  kitchen, as we talked about jokingly, or whether you're getting out, uh, into vehicles,
[1294.56 --> 1299.74]  uh, that are either cloud connected or on the edge or anything, or maybe even something,
[1299.84 --> 1303.70]  you know, another popular topic out there to throw buzzwords out as things like metaverse
[1303.70 --> 1304.12]  and stuff.
[1304.60 --> 1310.32]  How do you get this capability out into all those use cases, uh, in a, in a very
[1310.32 --> 1314.84]  practical and functional way for people to start taking advantage of it?
[1314.84 --> 1319.56]  Because you have almost unlimited potential in terms of, of this generative capability
[1319.56 --> 1322.26]  that we're, that we're on the forefront of.
[1322.58 --> 1327.24]  Um, and so like I have a 10 year old daughter, I'm imagining, but you know, another 10 years
[1327.24 --> 1333.16]  out, she's going to really have a tremendous college experience, very different from us because
[1333.16 --> 1334.54]  she's going to have all these new tools.
[1334.54 --> 1341.44]  How are you looking at trying to get this technology into all the places that really
[1341.44 --> 1342.94]  affect people's lives going forward?
[1343.40 --> 1347.84]  It's very likely that 10 years from now, you know, the way that people interact with
[1347.84 --> 1352.94]  the internet and the information that is out there, they're going to find it hard to imagine
[1352.94 --> 1357.76]  how we did it, you know, without such strong language understanding at that point.
[1358.00 --> 1360.80]  Because language is this like really natural interface for us, right?
[1360.80 --> 1363.46]  Like you can talk about doing pretty much anything.
[1363.62 --> 1368.58]  So if something could be on the other side and be that other you out there, right?
[1368.66 --> 1372.54]  Kind of doing those things a little bit for you on your behalf, just the way you would.
[1373.12 --> 1375.74]  I think it's probably something we can't really conceive of yet.
[1375.86 --> 1379.40]  We can't really wrap our minds around it, but getting there, you know, there's traditional
[1379.40 --> 1380.48]  ways to do it.
[1380.50 --> 1386.10]  Like we have mobile browser apps and I think people understand how those work.
[1386.10 --> 1390.88]  Like Chrome or Safari, we have like a U browser on iOS and on Android.
[1391.40 --> 1396.34]  I think desktop browsers are another natural one, but pretty much anywhere you might type
[1396.34 --> 1402.02]  in text could eventually become an interface for you to interact with these things.
[1402.80 --> 1408.04]  And if you can type text into it, you can also speak to it and have speech to text take
[1408.04 --> 1409.66]  care of that for you if you want to do that.
[1409.66 --> 1414.84]  But any interface where you're using language or could use language to communicate with something
[1414.84 --> 1423.76]  is an opportunity, I think, for the next generation of search and chat and do engines like e.com.
[1424.10 --> 1424.64]  That's the forefront.
[1424.84 --> 1430.18]  I, you know, I have some sci-fi thoughts, you know, like paths we could go down.
[1430.46 --> 1433.30]  I don't know about you guys, but I have like an inner voice.
[1433.48 --> 1437.58]  Like I can hear what I'm thinking as text more or less.
[1437.58 --> 1441.92]  You should definitely go there because we, this is what these conversations are all about.
[1442.26 --> 1442.98]  Yeah, yeah, yeah.
[1443.22 --> 1446.26]  It's so, you know, not everybody has this.
[1446.54 --> 1450.60]  Some people are surprised to learn that as well, but like some people can't see images
[1450.60 --> 1451.80]  in their head, for example.
[1452.38 --> 1454.18]  Some people don't have an inner monologue.
[1454.74 --> 1457.94]  I've for many years now, since I've been working on these things, refer to my inner monologue
[1457.94 --> 1460.80]  as my like own inner language model, right?
[1460.84 --> 1464.42]  It kind of even predicts a little bit what you're going to say next.
[1464.42 --> 1468.88]  That's how you complete people's sentences and anticipate things.
[1470.34 --> 1473.48]  You know, so I don't, I don't have any aspirations to work on this.
[1473.86 --> 1477.80]  I think there are a lot of things to think about, but in the long run, like that's kind
[1477.80 --> 1478.94]  of a language interface too.
[1479.18 --> 1482.22]  Like what if these things were hooked up to that?
[1482.56 --> 1485.76]  You know, if you're into the neural interface stuff, that's maybe a realm.
[1485.86 --> 1486.80]  We're very far from it.
[1486.94 --> 1490.96]  But you know, what if your inner monologue could also be supplemented by these things?
[1490.96 --> 1493.04]  And your own like thoughts, thought processes.
[1493.70 --> 1493.90]  Yeah.
[1493.98 --> 1495.50]  Not on our roadmap, but.
[1495.82 --> 1497.20]  I get, I get that.
[1497.32 --> 1501.92]  I like that thought though, because we've come to a point and I think everyone is coming
[1501.92 --> 1506.54]  to this point where things that would have been like, eh, well, you know, that's way
[1506.54 --> 1507.04]  out there.
[1507.46 --> 1510.58]  People are starting to kind of go, that's an interesting idea.
[1510.64 --> 1515.20]  You know, kind of seeing how fast things have ramped up in recent times.
[1515.20 --> 1520.34]  And I think it's pushing imagination out there at large, uh, in terms of what might
[1520.34 --> 1521.24]  be coming.
[1521.56 --> 1521.68]  Yeah.
[1521.76 --> 1522.60]  It's really inspiring.
[1522.90 --> 1527.24]  You know, at some point when we were making some of these early language models, we were
[1527.24 --> 1530.96]  working on our version of like a GPT-2 size model.
[1531.08 --> 1531.88]  We called it control.
[1532.70 --> 1537.84]  And someone I was working with read at some point a poem that this model had generated
[1537.84 --> 1540.06]  and was legitimately touched.
[1540.20 --> 1543.56]  You know, they were like, whoa, I actually really liked that poem.
[1543.56 --> 1545.30]  They didn't like poems before.
[1545.96 --> 1550.30]  And then we spent, you know, weeks, you know, in our off time, like talking about poetry and
[1550.30 --> 1552.72]  trying to find poets they liked and things like that.
[1552.82 --> 1559.58]  So even in the kind of simple moments, this opening, I think that you're talking about,
[1559.66 --> 1559.84]  right?
[1559.98 --> 1564.54]  This dropping of expectations about search or what technology can really do for us.
[1564.90 --> 1566.48]  It's changing the way people think about it.
[1566.56 --> 1568.60]  It's changing people's lives in some ways.
[1568.64 --> 1571.16]  It's like inspiring them, getting to be more creative.
[1571.16 --> 1576.76]  And going back to Daniel's really question, when you combine different modalities of images
[1576.76 --> 1581.22]  and vision and text and just thinking about what you could do with your own thoughts,
[1581.22 --> 1584.70]  if you could actualize them and realize them more easily.
[1585.38 --> 1585.72]  I don't know.
[1585.80 --> 1587.14]  That's a cool journey to be on.
[1587.14 --> 1594.56]  So, Brian, super interesting to think about like where this could be headed.
[1594.72 --> 1598.92]  And I've had similar experiences to what you talked about a second ago, where it's like,
[1599.50 --> 1603.30]  I'm kind of have like mental block in this scenario.
[1603.30 --> 1606.18]  And like I go to one of these chat interfaces.
[1606.18 --> 1612.36]  And even if it's just to like unblock myself, like I start chatting and like then it gets,
[1612.74 --> 1615.72]  it sort of jumpstarts my mind in a new direction or something.
[1615.94 --> 1619.24]  That's very, yeah, very intriguing to me.
[1619.50 --> 1627.80]  Now, you've been interacting with these models quite a bit over time and have probably dealt with,
[1627.80 --> 1633.70]  like you've already talked about things like grounding and hallucination and like the sort
[1633.70 --> 1637.66]  of power of the knowledge embedded in these models that they've memorized and things that
[1637.66 --> 1640.20]  people have like talked about more recently.
[1640.20 --> 1643.92]  You've been kind of at the forefront of thinking about these things.
[1644.10 --> 1649.70]  So I'm wondering, like now that like the whole world is talking about all of these things,
[1649.70 --> 1655.76]  if you have any sort of like wisdom you would like to impart in terms of like either like
[1655.76 --> 1660.76]  these topics that people are concerned about in terms of like grounding and hallucination
[1660.76 --> 1667.66]  or like harmful outputs or on the other side, like the ways that this is like,
[1667.70 --> 1672.46]  like I think people were concerned that this is like an automation of our life,
[1672.46 --> 1677.60]  but really like people are getting such a benefit from it as like an assistive technology.
[1677.94 --> 1683.38]  So like the fact that you've spent a longer time thinking about these things that many of us
[1683.38 --> 1687.78]  have just been like hit in the face with any wisdom or thoughts on that,
[1687.96 --> 1692.68]  like that you've kind of started to develop as your own kind of like mental model of these things.
[1693.38 --> 1694.82]  Oh, yeah. Yeah, for sure.
[1695.44 --> 1700.94]  Just remember that it wasn't very long ago that they would just repeat themselves over and over again,
[1700.94 --> 1702.04]  and they did nothing useful.
[1702.62 --> 1702.82]  Right.
[1703.02 --> 1704.42]  And there's two ways to remember that.
[1704.54 --> 1706.34]  One, they're probably going to get a lot better.
[1707.44 --> 1710.18]  As long as we keep going the way we've gone, they're going to get a lot better.
[1710.18 --> 1712.54]  And two, they're just tools.
[1712.94 --> 1713.90]  They're still just tools.
[1714.50 --> 1716.80]  And there's a lot of things we don't understand about them.
[1717.28 --> 1724.74]  But I think I would suggest trying our best as a community not to anthropomorphize them too much,
[1725.12 --> 1729.48]  you know, and think of them as like these other people.
[1729.64 --> 1735.72]  I think the chat interface in particular gets our mind ready to be talking to a person,
[1736.12 --> 1739.10]  even just the UI and the layout of it and things like that.
[1739.10 --> 1743.62]  Right. It looks like we're talking to a person more rather than a box where you type in keywords.
[1743.62 --> 1746.94]  And we've all been trained to do that for 20 years or something like that.
[1747.50 --> 1749.28]  And when we're texting with people, it's this way.
[1749.36 --> 1749.92]  And that's people.
[1750.42 --> 1751.92]  People, AI, people, AI.
[1752.08 --> 1754.56]  Now it's like, ooh, what is this thing?
[1754.84 --> 1758.14]  And try to just keep at the forefront of your mind that this is a tool.
[1758.54 --> 1759.30]  It's an algorithm.
[1759.30 --> 1762.68]  There's like a computer out there behind the scenes somewhere doing this stuff.
[1763.62 --> 1772.18]  And keep the awareness that sometimes it might be helpful for you to let yourself slip into conversational flow with it as if it's a person.
[1772.52 --> 1775.82]  And if that's helpful, that opens up, you know, inspiration and things like that.
[1776.08 --> 1777.88]  But then don't get too caught up in it.
[1778.00 --> 1779.26]  You know, remember that it's there for you.
[1779.26 --> 1787.72]  I got a question there that you're making me think of as you say that because what you just said really applies to my personal experience.
[1788.02 --> 1794.30]  And so having grown up with computers, I'm in my early 50s, so decades of computers.
[1794.58 --> 1799.04]  In the past year, my relationship with technology has changed.
[1799.04 --> 1806.26]  I have always used it for automation and kind of productivity and whether it be code or whether it be other tools that are out there.
[1806.62 --> 1811.64]  The thing that's changed dramatically is that I place a very high premium on creativity.
[1812.32 --> 1818.82]  And creativity is something that has historically, prior to the last few years, been the domain of humans.
[1819.12 --> 1824.48]  And we always expected creativity to continue to kind of be the more human thing and computers.
[1824.88 --> 1826.66]  But that's kind of been flipped around.
[1826.66 --> 1835.28]  And so we're seeing tremendous capability assistive, you know, techniques, to use the word assistive that Daniel did a moment ago.
[1835.46 --> 1840.74]  In other non-AI parts of my life, I'm using these AI tools for creative purposes.
[1841.02 --> 1843.52]  And so where do you see that going?
[1843.52 --> 1852.90]  Because that surprised me to be able to go to chat and get inspiration and bring my own creativity to it and then have it in turn,
[1852.90 --> 1857.64]  extra creativity that is algorithmic-based, enhancing that.
[1857.74 --> 1866.32]  So we end up with a product that is creativity that is both human and automation together that are generating this thing, which is really cool.
[1866.74 --> 1870.60]  And I'm using it, like, to teach children and stuff like that in other parts of my life.
[1870.60 --> 1875.54]  And so how do you see that kind of relationship going forward?
[1875.86 --> 1880.74]  You know, when you were kind of talking a little bit about, you know, the sci-fi influences and stuff like that.
[1880.78 --> 1887.92]  And as we're looking at these models, which are most definitely, as you said, not entities of themselves, you know, not people,
[1888.46 --> 1891.66]  but they're going to get much more powerful in the fairly near future.
[1892.22 --> 1893.00]  Where does that go?
[1893.12 --> 1893.90]  What does that mean?
[1893.90 --> 1898.06]  How does the relationship look going forward between us and those systems?
[1898.86 --> 1898.98]  Yeah.
[1899.12 --> 1904.24]  I mean, I fully intend to just get more creative myself, you know?
[1904.84 --> 1908.62]  I think I've not, over the years, been playing with it.
[1908.76 --> 1913.52]  And I think it might help to have been playing with it for so long and seeing them get better and better
[1913.52 --> 1917.12]  and still see all the places that they still fail me, I suppose.
[1917.12 --> 1924.08]  But for me, it's fully incorporated as just, like, you think of it as this different thing, right?
[1924.62 --> 1927.78]  That's, like, almost competitive with you on your creativity.
[1928.34 --> 1932.88]  But going 10 years in the future, like, the next generation, like we were talking about before,
[1933.68 --> 1935.34]  I doubt they're going to think about it that way.
[1935.36 --> 1939.08]  They're going to think about it like you think about a normal search engine.
[1939.90 --> 1942.78]  I know there are studies, right, on people who think they know things,
[1943.24 --> 1945.24]  but really they just know how to search for it.
[1945.24 --> 1947.60]  And then they feel like they knew the thing.
[1947.96 --> 1948.08]  Yeah.
[1948.34 --> 1953.64]  There's, like, this appendage experience that we, like, merge with it somehow subconsciously.
[1953.94 --> 1959.40]  Something like that will probably happen, where this will just feel like part of your creativity.
[1959.62 --> 1964.50]  And I would encourage us to also develop the technology that way, too, so that it continues.
[1964.70 --> 1969.70]  The narrative is such that it's built for us to enhance us so that we're more creative.
[1970.20 --> 1972.18]  I feel more creative using it.
[1972.18 --> 1975.38]  I don't feel like it's creative, and I'm not.
[1975.60 --> 1976.04]  Me, too.
[1976.04 --> 1981.50]  I feel like it's giving me access to data and the data distribution in, like, a really
[1981.50 --> 1983.84]  condensed way, more or less.
[1983.90 --> 1986.10]  And I can kind of test the waters, right?
[1986.12 --> 1990.76]  I see what all the other people are doing in some way, some portion of the population,
[1990.96 --> 1992.80]  whatever the data is representing.
[1992.80 --> 1998.26]  And then I can choose to either do that or do something else and change it.
[1998.26 --> 2001.48]  And that's actually really cool from a creative perspective.
[2001.48 --> 2006.78]  Because sometimes you might be in your own little vacuum or echo chamber or whatever it is.
[2007.06 --> 2009.28]  You think you're doing something really novel and cool.
[2009.56 --> 2011.90]  It turns out a million other people have done that kind of thing.
[2011.90 --> 2015.42]  Now, you see, it doesn't look like it.
[2015.50 --> 2018.22]  But what you're seeing with the language model is what everybody else said.
[2019.10 --> 2019.82]  Not everybody else.
[2020.04 --> 2022.60]  A lot of people, enough people for the language model say that.
[2022.92 --> 2027.72]  So you're getting a little bit of a measurement of what's going on out there that you couldn't
[2027.72 --> 2028.38]  get before.
[2029.12 --> 2036.48]  And if you use that as another input for yourself, I think the way that, you know, humans and chess
[2036.48 --> 2041.66]  algorithms are better together, we'll continue being better together with these creativity
[2041.66 --> 2043.36]  tools, these productivity tools.
[2043.92 --> 2047.60]  And we'll just learn to be better at whatever we want to do.
[2047.74 --> 2050.94]  And hopefully it'll just free us up to think about the things that we want to think about.
[2051.60 --> 2051.70]  Yeah.
[2051.86 --> 2055.72]  And I'm also kind of wondering selfishly.
[2055.72 --> 2061.38]  So we've been talking about kind of like you've had the benefit of like working with these
[2061.38 --> 2066.36]  models for a very long time and kind of getting an intuition of some of these things and how
[2066.36 --> 2071.34]  to think about them in the capacity that they play, how to think about like the UIs around
[2071.34 --> 2071.64]  them.
[2071.70 --> 2078.60]  But also you've been on the technology side and kind of like at the forefront of integrating
[2078.60 --> 2085.08]  these things into your systems and also like, hey, there's output from this model.
[2085.08 --> 2087.24]  Should we show this to a user?
[2087.48 --> 2089.02]  Hey, there's output from this model.
[2089.32 --> 2093.84]  Like, or there's like these references that we could inject as context into this model.
[2094.04 --> 2094.80]  Like, do we do that?
[2095.06 --> 2099.08]  A lot of people as practitioners are wrestling with those things too.
[2099.20 --> 2104.38]  Now that like, oh, I can go get Langchain and like pull it down and like integrate a bunch
[2104.38 --> 2107.16]  of things together and create this workflow.
[2107.16 --> 2114.24]  I can go like, so on the practitioner level, I guess more so than like the perception level
[2114.24 --> 2119.00]  on the practitioner level for all of those listeners out there that are like jumping into
[2119.00 --> 2123.98]  this and starting to deal with some of these issues around integrating language models into
[2123.98 --> 2125.04]  their own applications.
[2125.68 --> 2131.10]  Do you have any wisdom that you'd like to impart in terms of like that practical side of things
[2131.10 --> 2140.68]  and like how to go from this concept of integrating generative AI for this particular domain and
[2140.68 --> 2145.58]  this particular problem to actually realizing that in an application that's useful for people?
[2146.38 --> 2146.50]  Yeah.
[2146.86 --> 2149.98]  And this goes back to some of the other tips I'd provide for people interacting with them
[2149.98 --> 2150.24]  too.
[2150.24 --> 2156.54]  I think for developers of these things and practitioners, do try to ground their responses as much as
[2156.54 --> 2157.00]  you can.
[2157.42 --> 2163.10]  Unless your product that you're giving people is specifically, you know, say whatever you
[2163.10 --> 2165.28]  want, language model and do whatever.
[2165.42 --> 2171.14]  If people are actually looking for real information from you, just know that your users, there's
[2171.14 --> 2175.48]  your users are also seeing that conversation interface and everything I just described that is
[2175.48 --> 2179.30]  making them feel a little bit like it's more human than it is.
[2179.30 --> 2183.74]  And it might even be their first time seeing one of these things and how well it works.
[2183.90 --> 2190.44]  So keep that stuff in mind and try to anticipate the hallucinations, try to ground things, try to
[2190.44 --> 2193.44]  provide clear attribution as much as possible.
[2193.98 --> 2199.82]  And then I would say switch back and forth as much as you can between those moments of
[2199.82 --> 2206.32]  surprise and wonder in yourself and let your expectations drop a little bit so you can think
[2206.32 --> 2207.86]  about what you can do with these things.
[2207.86 --> 2213.16]  But then once you implement something, be very skeptical and critical of it, you know, as
[2213.16 --> 2218.50]  much as you possibly can, like you would any other engineering system, any other like research
[2218.50 --> 2223.44]  project or experiment you're running, like go get some numbers, like get close to the data
[2223.44 --> 2227.90]  because it's very foreign to a lot of people right now.
[2227.90 --> 2233.34]  And the only way to do that is to go use it a lot, not as a user, but as a practitioner.
[2233.34 --> 2237.72]  So you're going to see that prompts matter a lot.
[2237.72 --> 2243.88]  And in ways that you probably won't anticipate sometimes and you will anticipate sometimes.
[2243.98 --> 2248.08]  So just like start getting your hands dirty, embrace that whole process.
[2248.42 --> 2254.88]  It's quite fun because it feels like you get a lot farther a lot more quickly than you used
[2254.88 --> 2255.02]  to.
[2255.40 --> 2258.72]  You know, you can kind of dream up a use case and it just kind of works.
[2258.72 --> 2260.84]  And so celebrate that, right?
[2260.94 --> 2264.26]  Like, like I love in that moment, oh my gosh, this kind of works.
[2264.58 --> 2267.14]  But then immediately go back like, okay, wait a second.
[2267.46 --> 2269.22]  Like, what if we evaluated this properly?
[2269.36 --> 2271.50]  What if we put all these conditions around it?
[2271.54 --> 2274.96]  Like, let's find all the places where it doesn't work, where it's going to let people down.
[2275.44 --> 2279.34]  And, you know, with you.com as a search engine turning to do engine, like the goal is to make
[2279.34 --> 2283.76]  it impossible for you to fail in what you're trying to do more or less.
[2283.76 --> 2286.26]  So, you know, try to embrace that mindset here too.
[2286.56 --> 2287.44]  It's a new tool.
[2287.96 --> 2288.76]  You have to use it.
[2289.06 --> 2292.94]  Like, I don't know, if you've been a Kubernetes person or HomeTrad person, like you're not
[2292.94 --> 2294.22]  going to just know all the things.
[2294.82 --> 2300.70]  This is familiar looking because it's your language, but treat it almost as if it's foreign
[2300.70 --> 2303.58]  language, you know, and take a little bit of that perspective.
[2304.38 --> 2305.10]  Yeah, I love that.
[2305.20 --> 2307.64]  That's a really good perspective to bring into this.
[2307.64 --> 2312.84]  As we wrap up and get to the end here, I'm wondering, like, we've talked a lot about
[2312.84 --> 2313.72]  you.com.
[2313.84 --> 2315.22]  We've talked a lot about you chat.
[2315.38 --> 2320.16]  If you were to encourage listeners, like maybe they haven't interacted with you.com yet
[2320.16 --> 2325.94]  or you chat, like what are like a few things that they can do a few places that they can
[2325.94 --> 2333.16]  visit to like get and kind of understand the you.com experience and like maybe a few things
[2333.16 --> 2337.50]  to try that would kind of highlight some of the things that we've talked about.
[2337.64 --> 2338.08]  Yeah.
[2338.30 --> 2340.30]  So there's you.com.
[2340.76 --> 2341.78]  It's you.com.
[2341.96 --> 2342.84]  You can go there.
[2343.28 --> 2348.60]  If you're on mobile, we do have our app and I do recommend that because they provide a
[2348.60 --> 2350.72]  better experience on mobile, especially for the chat.
[2351.32 --> 2356.56]  Now, if you go to you.com, I'd also encourage you to look for the chat tab or go to you.com
[2356.56 --> 2361.30]  slash chat because that's where a lot of this new exciting stuff is showing up.
[2361.58 --> 2366.22]  I'd also love to just chat with people directly and we have a discord.
[2366.22 --> 2370.60]  And so if you go to you.com, it should be pretty easy to find and join the community.
[2370.76 --> 2371.56]  There's a link to it.
[2372.22 --> 2374.42]  And yeah, come talk to us about your use cases.
[2374.86 --> 2383.16]  So far, people love it for writing essays and emails to professors and code and recipes.
[2383.96 --> 2389.10]  Lots of people just like asking it about themselves, even though the model doesn't always know,
[2389.10 --> 2390.02]  you know, exactly.
[2390.22 --> 2393.12]  That's like a fun use case that blends hallucination with truth.
[2393.52 --> 2395.10]  But look for those citations.
[2395.66 --> 2400.22]  You know, like I said, like any other thing, look for the citations of grounding and follow
[2400.22 --> 2402.12]  up with us on on our discord.
[2402.36 --> 2405.34]  We're pretty much there all the time that you can talk to us directly about it.
[2405.82 --> 2406.62]  Yeah, that's awesome.
[2406.62 --> 2412.26]  Well, I'm I've have been enjoying interacting with you, Chad, and other things.
[2412.26 --> 2416.88]  And I'm just really happy that we had the chance to have you on the show, Brian, and learn
[2416.88 --> 2418.34]  a little bit more about what you're doing.
[2418.34 --> 2423.66]  And also, you're really insightful perspective from working with these large language models
[2423.66 --> 2424.40]  for so long.
[2424.56 --> 2429.86]  So thank you for taking time and and joining us and would love to have you back on the show
[2429.86 --> 2435.84]  in a year to think about like, I'm sure next year, AI search is going to look way different
[2435.84 --> 2436.74]  than we expect.
[2437.34 --> 2440.98]  Because, you know, six months down the road, it always looks different.
[2441.16 --> 2444.20]  But yeah, thank you for your innovation and your insights.
[2445.12 --> 2446.20]  Thank you so much for having me.
[2446.28 --> 2447.76]  It was a real pleasure to meet you.
[2447.88 --> 2450.62]  And yes, I intend to make it very different in a year.
[2450.84 --> 2455.28]  So I'll be stoked to come back and see how much of what we said holds true.
[2455.28 --> 2460.64]  And whether we all think of these things as ourselves at that point, I don't know, we'll
[2460.64 --> 2461.44]  see what happens.
[2462.22 --> 2463.02]  Sounds good.
[2463.20 --> 2463.70]  Yeah, thank you.
[2464.08 --> 2465.06]  Yeah, thanks, Brian.
[2465.18 --> 2465.36]  Bye.
[2474.58 --> 2477.02]  Thank you for listening to Practical AI.
[2477.58 --> 2481.34]  Your next step is to subscribe now, if you haven't already.
[2481.34 --> 2486.48]  And if you're a longtime listener of the show, help us reach more people by sharing Practical
[2486.48 --> 2487.84]  AI with your friends and colleagues.
[2488.46 --> 2493.20]  Thanks once again to Fastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2493.78 --> 2497.58]  Check out what they're up to at Fastly.com and Fly.io.
[2497.98 --> 2502.58]  And to our Beat Freakin' residents, Breakmaster Cylinder, for continuously cranking out the best
[2502.58 --> 2503.30]  beats in the biz.
[2503.58 --> 2504.48]  That's all for now.
[2504.78 --> 2505.90]  We'll talk to you again next time.
[2511.34 --> 2518.68]  All right.
[2518.68 --> 2519.02]  Bye.
[2519.02 --> 2519.42]  Bye.
[2533.40 --> 2535.80]  Bye.
[2536.00 --> 2537.06]  Bye.
[2537.18 --> 2539.16]  Bye.
[2539.16 --> 2540.24]  Bye.
[2540.24 --> 2540.70]  Bye.
