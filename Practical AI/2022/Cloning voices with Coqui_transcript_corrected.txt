[0.00 → 5.44] I think a lot of the discussions about machine learning and also voice tech and the kind of the
[5.44 → 10.40] place in humanity and where it's going to be in the next few years, there's a lot of this kind of
[10.40 → 15.14] dichotomy of machines is going to do everything here, and they're going to completely replace
[15.14 → 19.30] humans there. I don't think that that makes a lot of sense, especially when it comes to even
[19.30 → 24.84] voice technology. I think that there's a lot of call centre technology, speech to text,
[24.84 → 31.12] speech recognition. I don't see any time in the near future as replacing people who work at call
[31.12 → 36.58] centres. I see it as being very useful to people who work at call centres. They are the customer.
[37.02 → 42.50] And I think that this kind of using machines to augment what humans normally do and replace
[42.50 → 49.32] some parts that are maybe tedious or annoying or whatever, like parallel parking. I think that
[49.32 → 49.90] makes sense.
[54.84 → 65.56] Welcome to Practical AI, a weekly podcast making artificial intelligence practical,
[65.90 → 71.42] productive, and accessible to everyone. This is where conversations around AI, machine learning,
[71.42 → 78.44] and data science happen. Join us at practicalai.fm slash community and follow the show on Twitter.
[78.66 → 84.72] We're at practicalai.fm. Thank you to our partners at Vastly for shipping our pods superfast.
[84.84 → 87.76] All around the world. Check them out at fastly.com.
[94.12 → 99.62] Welcome to another episode of Practical AI. This is Daniel White neck. I'm a data scientist with
[99.62 → 104.04] SIL International, and I'm joined as always by my co-host Chris Benson, who is a tech strategist
[104.04 → 105.84] at Lockheed Martin. How are you doing, Chris?
[106.58 → 111.24] I'm doing well, Daniel. You sound a little funny today. Actually, so do I. What's going on today,
[111.24 → 111.60] Daniel?
[112.96 → 116.20] Nice, Chris. We have clones.
[116.76 → 119.38] And we might have frogs in our throat. Would that be?
[120.46 → 126.94] That's a good one. You know, for listeners who might have been with us a while and know our voice
[126.94 → 133.52] well, those are our voice, but not quite our voice. So today we're going to be talking a lot
[133.52 → 140.70] about synthesized voices. And we've got Josh Meyer with us, who is co-founder of Kochi. Welcome, Josh.
[141.20 → 143.60] Yeah. Thanks for having me, Daniel. Good to be back.
[143.88 → 151.34] Yeah. So just because we have to we have to say what that was first, and then we can then we can
[151.34 → 157.46] launch into other things. So your co-founder of Kochi. A few I don't know, it was a few weeks ago or
[157.46 → 163.74] whenever it was you came out with sort of live, I guess, demo prototype of some of the
[163.74 → 169.76] functionality that your company supports, which is text to speech. But it's a sort of voice cloning
[169.76 → 176.54] thing where what Chris and I did to create those was just uploaded. I think mine ended up being like
[176.54 → 183.30] 11 seconds. It was like 11 seconds of my voice. And then I was able to synthesize that that intro bit.
[183.30 → 190.46] And Chris did the same. So that was pretty cool. Maybe before we launch into like all the AI stuff
[190.46 → 195.16] and what you're doing and the company and the projects, like what's the general reception
[195.16 → 200.44] been to this kind of voice cloning thing that you're doing?
[201.38 → 207.58] Yeah, it's been honestly a very, I say, very positive, very interesting reception. Most people
[207.58 → 215.12] that end up showing it to, they're like, wow, that was fast. And that sounds like me. And it's,
[215.32 → 225.32] we've been working on this tech for a while, right? We published in ICML, the kind of the core
[225.32 → 229.46] technique that we're using for this. And it's been there for a while, the tech's been there for a while,
[229.46 → 236.38] but you really needed to be a coder. You needed to know your way around the command line. You needed
[236.38 → 240.94] to know, you know, how to navigate through GitHub and download the models and all this stuff. And
[240.94 → 248.12] what's different now, the reason that we're getting this kind of like, wow reaction is you don't need
[248.12 → 254.44] any of that. You can, you know, send the link to, for the website, you know, Koki.ai, you can send it
[254.44 → 261.94] to anybody you want. They just use the inner, you know, the web, web app, the whatever browser they're
[261.94 → 267.60] used to. And you, you don't even need to actually upload audio technically in terms of, you know,
[267.64 → 272.52] you don't need to go find a file on your computer and, or you don't need to pre-record. You just hit
[272.52 → 280.50] the microphone button and say a few sentences, seconds. I think right now we have it capped at 30
[280.50 → 287.82] seconds just to kind of be reasonable with server fees because more audio takes a little more
[287.82 → 294.36] server fees. But in general, we found that five seconds is good enough. You know, five seconds
[294.36 → 301.94] is, is enough to get a nice voiceprint or however you want to call it. So it's, it's been fun. And I
[301.94 → 309.60] think the reception, especially from non-technical people has been the most, the most fun. I don't know.
[309.60 → 314.22] I really like working on this because I get to interact with people who don't know AI, who don't
[314.22 → 318.66] know machine learning or deep learning. They think it's cool. They maybe read some articles in the
[318.66 → 324.62] New York Times about it, but they're not, they're not in the weeds like all of us are. And so getting
[324.62 → 330.14] it in a place that we can show it to them, and they're like, wow, this is cool. It's fun. It's, it's,
[330.14 → 335.30] it's refreshing if that makes sense. Yeah. I could, I could definitely see that. Like this is something
[335.30 → 339.82] like, I would not hesitate to kind of bring my wife in who definitely does not,
[340.20 → 345.98] her perception of my work is like, I always have a screen up, and it's a really dark screen with a lot
[345.98 → 353.20] of text on it. And that's like my life. But when I pull this up, it's very like welcoming and like
[353.20 → 357.62] easy, just like record your voice button. Yeah, it's cool. I think it's a similar, we,
[357.62 → 365.90] we recently interviewed Abu Bakr from a radio at Hugging Faces. It's similar. Like as soon as you
[365.90 → 372.58] put a demo in front of people, it's like a light bulb moment. Like, like this is, this is how this
[372.58 → 378.44] thing like works or this is what I could expect as output. Right. You know, it kind of feels a little
[378.44 → 383.18] bit like we've been waiting for this moment for a while because we've been talking through the show,
[383.18 → 389.46] you know, up until now, mostly to kind of technical tooling and technical use cases where
[389.46 → 394.78] people are putting together amazing things. But now it's, you know, as you point out, you can bring
[394.78 → 400.42] people in who have no technical capability and get something really, fascinating out of it.
[400.48 → 405.70] And we've been kind of waiting for AI to take this turn. So it kind of feels like maybe this
[405.70 → 411.02] conversation is kind of the beginning of starting to turn toward really broad usage by people that would
[411.02 → 415.80] not otherwise have access. And I think that there's kind of generally speaking outside of speech,
[415.80 → 422.48] outside of language technology, even there's this, uh, in the last few months in particular,
[422.58 → 427.30] maybe just last month. I mean, with the all the image generation stuff coming out with Dolly and
[427.30 → 437.52] party and crayon and all this stuff. Imagine. Yeah. Yeah. Yeah. You're seeing what creative people can do,
[437.52 → 444.28] like creators or creative types. I don't know how to, but people outside the coding community,
[444.28 → 450.30] uh, you give them the tools, you give them more tools in their toolbox to do creative things. And
[450.30 → 456.14] they're coming up with awesome stuff. I mean, there was, I remember there was that one week when it
[456.14 → 463.92] was just like Twitter was full of, you know, koalas riding unicycles. Uh, it was a bit overwhelming.
[463.92 → 471.16] Yeah. It was awesome. Yeah. What I'm really optimistic for is, is, is that kind of, uh,
[471.16 → 478.52] creative use for these, these voice tools, because there are tons of applications I have in my mind of
[478.52 → 485.92] where I see these tools being useful and, and helping the creative process. But also I know that,
[485.92 → 490.92] you know, the people who came up with all these image generation stuff, didn't think people were going
[490.92 → 496.06] to be doing everything that they're doing now with. And it's even more, more interesting than what
[496.06 → 501.66] they, the creators could have come up with. Right. And so that's, that's something that I'm
[501.66 → 507.20] really excited to see in the coming weeks, months is to see what cool stuff people are doing with the
[507.20 → 513.32] voice tech. Maybe that brings me to something that's kind of been on my mind in this discussion,
[513.32 → 520.58] which is so a while back, we, we had you on the show as part of a discussion about Mozilla common
[520.58 → 526.54] voice. And we were talking about speech tech and also like open data and that sort of thing,
[526.54 → 531.38] open speech data. I think it's episode one Oh four. If you're, if you're looking for that,
[531.44 → 537.80] so take a look there, but I've always kind of, even at that point, I think had in my mind,
[537.80 → 543.94] this perception of like speech tech and Alexa or Siri or whatever it is almost like a kind of novelty
[543.94 → 549.96] type of thing from, from my perspective, like coming to a computer where my first computer,
[549.96 → 555.66] like I interacted with it with keyboard and mouse. That's like my standard interface. And like,
[555.94 → 561.04] that's what I've grown used to, but there are tons of people all around the world where like maybe the
[561.04 → 567.40] first interface that they're interacting with a computing device with is, is their voice using,
[567.40 → 573.26] using Siri or different things. So I'm wondering like, how do you perceive as someone that's like
[573.26 → 580.80] very close in a sort of speech technology space? How do you, how do you see the trends shifting in
[580.80 → 587.48] terms of like how serious people are taking things like voice interfaces or creative uses, like you're
[587.48 → 596.06] talking about of speech technology in terms of like practical usage and like real world kind of scale,
[596.06 → 604.16] I guess. Yeah. So I think quick backstory in terms of kind of how long I've been in speech, I started
[604.16 → 613.54] really getting into it and probably 2012 and did academia research. And that was very fun. And,
[613.68 → 619.42] but I got into industry because I like building things that people use. I still like writing papers,
[619.42 → 625.28] which is why, you know, Daniel and I recently wrote this paper with, with the great folks at Malakand,
[625.76 → 633.06] an African text to speech, but working with Mozilla in particular, the last few years are collaborating
[633.06 → 639.60] with Mozilla because I don't work there anymore, but I still keep up ties and collaborate with them.
[639.60 → 647.28] And they're all great folks working on great things. Really? I think some of the best democratization
[647.28 → 653.50] of speech technology is honestly coming out of Mozilla, but in terms of kind of speech tech
[653.50 → 659.70] being a novelty and, or at least the perception of speech tech as a novelty, but actually finding
[659.70 → 664.90] real world applications for it. I think there, there used to be this talk about, you know,
[665.06 → 669.34] keyboards are going to be gone in 15 years, you know, like there's, there's this talk that
[669.34 → 675.38] we're never going to type again. We're only going to use our voice. And I never really
[675.38 → 682.06] subscribe to that kind of viewpoint because I think that mixed modality is always making sense.
[682.16 → 687.56] Sometimes you want to type just because, you know, maybe baby's sleeping in the next room, and I'm not
[687.56 → 695.30] going to shout at my computer to like wake it up. I think in general, the most interesting applications
[695.30 → 705.34] of voice tech and machine learning at large are where they augment and support humans doing
[705.34 → 711.66] human things. I don't think machines taking over completely kind of the functionality of a human
[711.66 → 717.86] makes a lot of sense, which is why, for example, let's say self-driving cars. I think that the
[717.86 → 725.06] technology underlying self-driving cars is super useful. If I had a self-driving car, I wouldn't let it
[725.06 → 732.80] drive for me around town, but would I let it parallel park for me? Of course. Like that's something
[732.80 → 739.30] that I don't like doing. And so there's functionality where if you take kind of parts
[739.30 → 746.80] of what the human pipeline is for whatever task, like going to the grocery store, there's multiple
[746.80 → 751.34] parts of that, that the machine can do better than me, but there's also parts of it that I can do better
[751.34 → 757.92] than the machine. So I think a lot of the discussions about machine learning and also voice tech and the
[757.92 → 763.48] kind of the place in humanity and where it's going to be in the next few years, there's a lot of this
[763.48 → 769.52] kind of dichotomy of machines is going to do everything here or humans are, and they're going
[769.52 → 774.20] to completely replace humans there. I don't think that that makes a lot of sense, especially when it
[774.20 → 780.12] comes to even, you know, voice technology. I think that there's a lot of voice technology that's being
[780.12 → 785.60] used to let's say, you know, call centre technology, speech to text, speech recognition.
[785.60 → 791.16] I don't see any time in the near future as replacing people who work at call centres.
[791.38 → 796.46] I see it as being very useful to people who work at call centres. They are the customer
[796.46 → 801.34] in that case, right? They're seeing, you know, you're on a call with somebody who's,
[801.34 → 806.82] whose TV is broken, and you got this transcript in real time of what they're saying, but also you're
[806.82 → 813.50] able to run NLP on that and come to answers faster. Like you're getting kind of recommendations on,
[813.50 → 815.34] on how to talk to the client.
[815.60 → 820.90] And I think that this kind of using machines to augment what humans normally do and replace
[820.90 → 828.16] some parts that are maybe particularly tedious or annoying or whatever, like parallel parking.
[828.16 → 836.98] I think that makes sense. And I think with voice tech, we don't exactly know yet which parts are
[836.98 → 843.22] going to be, how it's going to shape out because it's pretty new technology. I mean, speech recognition
[843.22 → 849.04] and speech synthesis have been around for a while. You know, I think the eighties maybe is when they
[849.04 → 856.56] first got some kind of more mass adoption or adoption. That's the word, mass adoption,
[857.12 → 860.54] dragon naturally speaking. I don't know if you guys remember that.
[860.88 → 861.24] I do.
[862.04 → 865.08] I probably still have it somewhere stuffed in an old bookshelf.
[865.08 → 870.90] Yeah. It's still around. And I mean, I remember having, my parents had that when I was in school
[870.90 → 877.18] and I tried it writing a few papers with it, and I was like, eh, not yet, you know, but since then
[877.18 → 883.24] it's advanced a ton just in general, the technology. And especially with the speech synthesis in the last,
[884.04 → 890.58] honestly, in the last like five years or less, it's just gotten crazy better. It's, uh, you know,
[890.58 → 897.54] five years ago, you would never listen to synthetic speech and be like, is that a human or is that a
[897.54 → 904.80] machine? I can't tell, but now it's like every paper that comes out in every research paper that
[904.80 → 911.26] comes out from the big labs. It's like, wow, this is, that sounds like a human. I can't tell. Is that
[911.26 → 915.84] the training data or is that the synthetic speech? You know? And now I think that the big challenge with
[915.84 → 921.28] speech synthesis is getting it to sound more expressive, more emotional, because I think
[921.28 → 927.82] machines and humans can basically do flat speech identical, but, um, yeah, it's, uh, it's going to
[927.82 → 933.48] be interesting to see how it all shapes out. But I, I, I think that there's going to be a lot more
[933.48 → 939.68] creative usage that we're not, that's not predicted by kind of the diehard technologists.
[945.84 → 969.00] So before we dive fully into the technology, I, I want to follow up on something. Um, and because I,
[969.00 → 974.16] as you were talking, you know, through that a moment ago, I'm thinking of my own experience and my
[974.16 → 980.74] families and stuff. And, and it's been pretty fascinating for me to see my wife, my daughter,
[980.94 → 986.94] my mother, people that are not, you know, technical currently that are, that are diving into this.
[986.94 → 993.78] And yet I, as a, as a technical person in the AI space, I'm still tending to default to the keyboard,
[993.78 → 999.46] going back to that. And it's a different user experience that they, I've seen my daughter
[999.46 → 1004.98] gravitate to it naturally. What is it before we, we dive fully into the technology? What is it about
[1004.98 → 1009.62] the that difference in user experience that seems to make it more accessible? Do you think
[1009.62 → 1014.84] that the idea of speech recognition, natural language processing to, to parse it all and come
[1014.84 → 1021.26] up with, with a good response? And then the speech synthesis coming back is something that is so natural
[1021.26 → 1026.26] for my 10-year-old daughter that it's just, you know, it might as well be one of her friends that
[1026.26 → 1032.66] she's talking to. And so could you speak a little bit about what, what that experience is and how
[1032.66 → 1039.52] the rest of us that maybe are doing it some, but maybe not in such a completely natural setting,
[1039.52 → 1042.00] how does that evolve over time? What does that look like?
[1042.00 → 1049.16] Yeah, I think, so I think that one reason that we are using new voice technologies that are, they're
[1049.16 → 1055.12] built on lots of other technologies, like, right. I think Alexa and Siri and Google home and just any kind
[1055.12 → 1065.36] of Mycroft. I think that any kind of voice enabled home assistant is useful. And so far as at, as it's
[1065.36 → 1072.96] immediate, like you can't sit there and wait, you know, two minutes, not even two minutes. I'm not
[1072.96 → 1079.94] even going to wait 15 seconds for Siri to talk back to me. Right. You know, I will be walking the dog.
[1080.02 → 1083.92] So, okay. I will say I'm somebody who's been working in this space for a long time, as I mentioned,
[1083.92 → 1091.26] but I've never been one who's had home assistance one, because of all my kind of privacy concerns.
[1091.26 → 1095.62] Like I just don't want to have them sitting around. I'm very realistic. Like I know people
[1095.62 → 1101.68] who work on all the teams, you know, nobody's consciously snooping and recording audio because
[1101.68 → 1107.16] one, it would just kill their servers. Cause there's way too much, way, way too expensive to
[1107.16 → 1112.28] even stream all that back and recognize it all. And you know, blah, blah, blah. So I haven't had them
[1112.28 → 1120.06] for a long time in any case, but I recently got an Apple Watch and I find that I use it every day when
[1120.06 → 1126.10] I'm walking the dog because it's just so convenient because I can't, my dog pulls on a leash, and I've,
[1126.14 → 1134.28] you know, only got one hand that's a functional. And so, but if my service is bad and Siri's not
[1134.28 → 1138.90] replying for like maybe even just 10 seconds, I'm like, forget it. I'll take care of it later.
[1138.90 → 1146.82] You know, the attention span I think of people is in general, not super long. And so the technology
[1146.82 → 1154.14] has gotten faster in general over the years. And that is a, is a big part of making it adoptable.
[1154.86 → 1161.86] And besides that, there's the kind of the pleasantness of, of talking to a voice that
[1161.86 → 1170.00] sounds really human. Like, I don't know when exactly Apple introduced it, but if I say, Hey Siri,
[1170.38 → 1177.62] at least the voice that I have sometimes will apply like a normal, you know, American English speaker
[1177.62 → 1183.08] would reply. Exactly. Like a yes, I'm listening. It's not going to say, yes, I'm listening. It's
[1183.08 → 1189.62] going to talk like a human, something closer to the movie her. And so I think that the voices being high
[1189.62 → 1194.48] enough quality that it almost sounds like you're talking to a human, not just the quality itself,
[1194.56 → 1200.56] but what they're saying. It's like that kind of turn of phrases, but also what it's connected to.
[1200.80 → 1208.34] So the, the home assistants now it's basically your access to a search engine for the internet,
[1208.48 → 1215.04] right? You can ask it kind of fact-based questions and get answers that are usually accurate pretty fast.
[1215.04 → 1223.98] At least they're more accurate than, than a GPT-3s question. But yeah, I think it's how fast it is,
[1224.30 → 1231.72] how human it sounds and the kind of breadth of functionality it has. You can ask it so many
[1231.72 → 1236.60] different things and ask it to do things for you, right? Like schedule appointments and blah, blah,
[1236.66 → 1242.42] blah. Not as a question, but just as a, as a final thing on that topic. It's interesting coming
[1242.42 → 1247.36] through COVID coming through the pandemic era, it's changed the way kids interact. And I've watched
[1247.36 → 1253.06] my daughter, they'll get on and play Roblox, you know, on online gaming, and they're, and they do a
[1253.06 → 1259.22] cellular conference call on the side is there. So all the kids are talking, and they're playing in Roblox
[1259.22 → 1266.02] and they include these home devices in the conversation and bring things up. And so it's kind of eerie
[1266.02 → 1271.74] to watch this whole thing happening because you're, you're seeing children leaping forward
[1271.74 → 1276.88] with this technology naturally, very, very rapidly. Multiple times I'll just stop and go,
[1277.08 → 1281.00] wow, I find that a little bit hot, but, and I'm in the space. So anyway.
[1281.00 → 1289.82] I really appreciated how, how you brought up this like concept of like how, how people actually use
[1289.82 → 1295.78] their languages. So like how, how do humans actually speech or speak, which I think is like a really
[1295.78 → 1301.34] interesting, like we've sort of done this to ourselves in certain ways because the speech
[1301.34 → 1307.92] corpora for the most part that we have created aren't actually representative of how people use
[1307.92 → 1313.72] their languages. So things like I recently at ACL, I saw this like amazing paper. I'll link it in the
[1313.72 → 1321.34] show notes from text to talk from a group at Rad baud university in the Netherlands. I'm, I'm not sure if
[1321.34 → 1327.58] I'm saying that right, but they were talking about like meta communicative devices, meaning like filler
[1327.58 → 1333.36] things like, um, uh, yeah, you know, like these sorts of things like you brought up, like these are very
[1333.36 → 1340.66] powerful communicative devices that people use very strategically in their conversation, but are for
[1340.66 → 1347.28] the most part considered like noise in our AI data. Right. And we like clean them out or don't want to
[1347.28 → 1353.36] have them. And I think the other one that you brought up Josh was like emotion and like how you
[1353.36 → 1359.56] like tune sort of like the emotional aspect of a synthesized voice. And I know that's something you
[1359.56 → 1366.66] emphasize on the Kochi website. Could you describe maybe like, maybe it's in the context of synthesized
[1366.66 → 1372.50] speech or speech technology more generally, but like, what are some of your kind of goals as you
[1372.50 → 1379.18] founded Kochi and like, how would you like to do some of these things like synthesized voice
[1379.18 → 1384.16] in like slightly different ways, or how is your perspective and being in the industry so long
[1384.16 → 1389.40] informed you about like, Oh, there are things like this emotional piece that we really need to think
[1389.40 → 1396.60] about more deeply? I think about emotion and speech way too much, especially the last, last month.
[1396.68 → 1404.28] It's been really kind of top priority for us because I mean, we've been working for, for a while on
[1404.28 → 1412.18] getting the voice cloning side of things working. So optimizing models on speaker similarity. So it sounds
[1412.18 → 1421.86] like you like your vocal tract, you know, physically, but getting emotion right is just so hard and not
[1421.86 → 1427.06] only getting it right, but there's this kind of, I'm also thinking about, so there's getting the model,
[1427.06 → 1432.90] you know, the neural network to, to produce speech that sounds appropriately emotional.
[1433.46 → 1440.30] That's one side of it. But another side that I've been thinking more lately about is how to, from a user's
[1440.30 → 1449.18] point of view, somebody who is creating new synthetic speech with some neural network, how do they want
[1449.18 → 1455.50] to interact with that? How do they think about emotions? Is it something like a colour wheel from
[1455.50 → 1463.06] Microsoft Word where you can say, I want my colour to be, you wouldn't even describe it in words. You just,
[1463.18 → 1467.24] there's, there's a pixel that you point to on the colour wheel. And you're like, I want that.
[1467.24 → 1475.44] That's a much better interface, even if you can't describe it in real human words, right? I mean,
[1475.44 → 1482.16] you can do whatever RGB coordinates, but, and some designers maybe understand those intuitively,
[1482.16 → 1488.00] but most people in the world do not. So think about colour and kind of design as thinking about
[1488.00 → 1495.88] putting emotion into speech. Do we want an emotional colour wheel of sorts? Do we want to have a
[1495.88 → 1502.20] drop down menu that, that says, make this sound more angry, make this sound more sad, make this sound
[1502.20 → 1510.10] more sarcastic? Or do you want something that's more free form, like type in a description of somebody,
[1510.38 → 1520.20] you know, responds in an angry, but sassy, but sarcastic, but also a little bit sad at the end
[1520.20 → 1527.66] kind of way, you know, it's hard. Yeah. It's almost like there's an arc to how you want it to happen.
[1527.66 → 1536.68] Right. Like even defining like one emotional flavour for a clip is sort of not, not enough in certain ways.
[1537.04 → 1542.80] It makes the communication authentic essentially, which creates trust, which affects that user experience.
[1542.80 → 1549.00] So you mean, if you're able to put the appropriate emotion, emotion into it. Yeah. Because at the end,
[1549.04 → 1552.18] there's a human that they're, that, that, that model is dealing with.
[1552.40 → 1555.44] It's something that you can think about it in this way that I was describing, like,
[1555.56 → 1561.52] like a designer that's using Photoshop, right. In terms of using a colour palette, you can also think
[1561.52 → 1567.94] about voice in terms of stage directions or actor directions. Right. I mean, I've spent,
[1567.94 → 1575.94] I spent a whole day sifting through scripts from movies and TV shows to just understand how do
[1575.94 → 1583.54] writers express what they're trying to get across in the lines. Because if you look at a movie script,
[1583.70 → 1590.10] there's, it's not just whatever Batman says, this Joker says that it's looking away from the camera
[1590.10 → 1597.92] distantly thinking about the future solemnly. Then they say this and putting that behind,
[1598.82 → 1607.38] a web-based user interface is, is a challenge. Even more so, it's a challenge to make a neural network
[1607.38 → 1614.50] that is that controllable. It's what we were working on. Like it's exciting to hear. One of my favourite
[1614.50 → 1619.78] parts of honestly working at Kochi is when we've, we've got so many people who are so much smarter than,
[1619.78 → 1625.30] than I am when it comes to speech synthesis. And, and, you know, we're, we're working away hacking on
[1625.30 → 1630.42] something for a week. And then on Friday, we, you know, share some, some new voice clips from the
[1630.42 → 1637.70] new models, and it's like, wow, that person sounds furious, you know? And it's just a synthesized,
[1637.70 → 1642.90] it's a synthesized voice talking about, uh, whatever, getting the wrong coffee. I don't know. It's,
[1642.90 → 1645.38] it's, it's one of my favourite things about, about working with this.
[1645.38 → 1651.94] Yeah. So would, would you say that the kind of the mindset that you have at, at Kochi and kind of,
[1651.94 → 1658.10] one of the things that you're wanting to enable is this sort of easy to access, like from a creator
[1658.10 → 1663.70] standpoint, this sort of configurable and controllable way to synthesize voices. Would
[1663.70 → 1669.22] that be a kind of like synopsis of like, at least part of what you're, what you're trying to do?
[1669.22 → 1673.06] No, I'd say definitely. I mean, that's, that's one side of it, which is very much the kind of
[1673.70 → 1681.86] business side customer facing, making synthetic speech for people who are creating content,
[1681.86 → 1686.34] right? That's one side of it. And another side, which is kind of historically where we came from
[1686.34 → 1693.38] is the open source research. I mean, I think that we're pretty special in terms of the kind of the
[1693.38 → 1697.54] voice cloning companies out there. I mean, I wouldn't say we're saying that we're a voice cloning
[1697.54 → 1702.82] companies not doing it justice or so we're synthetic, you know, speech company, but the
[1702.82 → 1708.58] amount of work that we do open source. And I think that because we're open source, we've been able to
[1709.46 → 1716.26] really attract some, some really smart people. We've learned from them. We, you know, share and
[1716.26 → 1723.38] collaborate. And, and that is honestly one of the most also refreshing parts of the job is getting
[1723.38 → 1728.90] people, especially people working on low resource languages, which is something that I did my whole
[1728.90 → 1735.86] kind of PhD on. And, and that's working on this paper with Daniel from the Bible TTS, which is
[1735.86 → 1743.94] coming out of interspeech, making some of the best synthetic voices for, for a handful of African
[1743.94 → 1748.82] languages is, I mean, the P working with everybody on that team was so much fun because it was like,
[1748.82 → 1753.62] everybody's so motivated, and also we're all in such different time zones. It felt like there was this,
[1753.62 → 1758.74] you know, passing off the torch. Yeah. Yeah. I mean, I think you have that, that clip if you want to
[1758.74 → 1764.66] play it of kind of what it, what it sounds like. Yeah. This was how's the clip. One of the interesting
[1764.66 → 1770.42] things about this clip, I think is its one of the out of domain clips. So we tried like synthesizing
[1770.42 → 1777.30] some voices because the voices are out of audio Bibles that we tried some Bible related synthesis,
[1777.30 → 1782.10] but this is actually out of domain. So this is like a news article, but using the same voice.
[1782.10 → 1786.90] Kumar WA Samozajiki, Tania Pachirisu waneshehu, gusawdega Shaw PETA.
[1807.30 → 1816.90] So Josh, I really, it was, as you mentioned, a lot of fun working on the project related to the
[1816.90 → 1823.38] to the synthesized African voices. That was so cool. And also seeing the, you know, the actual members
[1823.38 → 1830.26] of these language communities working on technology for, for their languages. And I think a lot of that
[1830.26 → 1836.82] was enabled because of like a variety of open source tools, but certainly kind of centred
[1836.82 → 1843.78] around some of these that Kochi has, has produced. Did those open source things, were those things that
[1843.78 → 1850.98] you were working on personally before, like the company was like founded, or was this like a sort
[1850.98 → 1856.74] of team thing that you, you started and was always kind of part of a strategy that you were building with,
[1856.74 → 1860.02] with, with Kochi.
[1860.02 → 1866.58] Okay. So in terms of the kind of core open source technology that we've been working on at Kochi,
[1866.58 → 1873.22] there's, there are two main sides of it. There's the speech to text, and there's the text to speech.
[1873.22 → 1881.62] Those two projects were projects that we were working on a founding team. We were all working on for the past,
[1881.62 → 1888.90] almost five years at this point, when we were, we were all working or collaborating with Mozilla.
[1888.90 → 1895.54] And so it's been going on for a while. And I think, so for this project in particular,
[1895.54 → 1900.26] there were a couple other parts that were really helpful that were actually outside, of outside
[1900.26 → 1905.22] of Kochi. So one of them, in case people are interested was the Montreal forced aligner,
[1905.22 → 1911.46] which is maintained by a very hardworking group of, of academic folks, which made,
[1911.46 → 1912.50] it is really nice.
[1912.50 → 1919.06] It's so nice, right? It's nice because it's built on top of Cali, which is Cali for anybody who's
[1919.06 → 1924.50] used, it can be a little painful, but the Montreal forced aligner wraps it so nicely that you don't
[1924.50 → 1930.34] have to worry about all the kind of, how do you put it? All the stuff inside the black box. But yeah,
[1930.34 → 1938.34] so we, the projects, they were started at Mozilla and the community, the open community grew around
[1938.34 → 1944.90] them and, and there's, you know, long time collaborators from all over the place in all
[1944.90 → 1948.98] different kinds of languages. And with project common voice, which we were talking a little bit
[1948.98 → 1957.30] about, we mentioned before was really, common voice was a project that was created to be the data
[1957.30 → 1964.50] feeder for the speech recognition side of, of the open source project. And that's why there's this
[1964.50 → 1971.30] really rich, I think, multilingual kind of heritage to the projects, if you want to call it that,
[1971.30 → 1979.06] because we've been working with kind of traditionally marginalized languages and those people from those
[1979.06 → 1985.94] communities, they are so motivated to work with the languages. They care so much and they get it.
[1985.94 → 1992.10] Like they get that this is important because some of the bigger companies are starting to put out
[1992.74 → 1999.78] more multilingual, multilingual work because of the existence of common voice really. Because before
[1999.78 → 2007.06] that there was just no data for, I think common voice has all the Celtic languages now, you know, it's got
[2007.06 → 2015.30] Welsh and, and Gaelic and Gaelic, and maybe there's Manx in there too. I mean, there's, there are tons of languages,
[2015.86 → 2021.94] that are just community driven efforts, at least their, their participation in common voice
[2021.94 → 2027.94] and in speech recognition is a completely community driven effort. So yeah, I mean, if it weren't for
[2027.94 → 2031.38] the open source side of things and then none of this would, would have been possible.
[2031.38 → 2039.46] So like one side of it is like the models, the architectures, the implementations that are
[2039.46 → 2045.86] driving like the speech to text, text to speech, and like the voice cloning things that you're doing.
[2045.86 → 2052.74] But then you also have kind of prebuilt models as well. Like if I'm, if I'm going to your site,
[2052.74 → 2058.34] like there's a there's a lot listed there, which like seemingly you could get started with
[2058.34 → 2064.02] kind of out of the gate. And maybe you could describe that kind of ecosystem a little bit,
[2064.02 → 2068.58] like what's currently there, how you've seen people use it, maybe even in surprising ways.
[2068.58 → 2074.74] Oh yeah. There's been some funny ways people have, uh, views. So the, so the largest diversity
[2074.74 → 2080.50] of languages we have is for speech to text, the speech recognition side of things. We set up the
[2080.50 → 2085.74] code base so that fine-tuning to a new language is super easy, even when you have a tiny bit of data.
[2085.74 → 2093.90] And if you constrain the vocabulary, you can do a really cool things, even if you don't have enough
[2093.90 → 2100.06] data to make a kind of full-blown speech transcription system. So for example, uh, we had a
[2100.06 → 2107.90] hackathon. Wow. Was it this year? I feel like it was earlier this year when a team put together a
[2107.90 → 2116.22] voice activated 3d chess board that you could, well, you can, it's, it's, it's, it's open source.
[2116.22 → 2123.18] It's out there, and they got it working for, for English, for Turkish, think maybe Hindi. And the
[2123.18 → 2130.06] right now there's some people who are adapting it for Korean. And that's like, like move on whatever
[2130.06 → 2137.82] to like, I'm not a like chess player, but I, I know the sort of like things I hear,
[2137.90 → 2143.02] on Harry Potter or whatever. Yes. Yeah. It's, it's exactly that, which is, uh,
[2143.02 → 2149.26] there's a huge discussion on how to do that. Well, so now after that, I know how to, how to
[2149.26 → 2154.46] move pieces in chess, but before I did not know how to say it out loud. You also have to capture
[2154.46 → 2158.86] Harry Potter's emotion though, as you're moving the pieces, you know, and all that, you know,
[2158.86 → 2162.94] that was a very emotional game that they were playing there. So yeah, we're right on topic.
[2162.94 → 2169.10] Yeah. The cool thing about that is the, uh, because the models for speech recognition are so small,
[2169.82 → 2177.02] I think they're like 46 mega megabytes for the acoustic model. And then the language model is like,
[2177.74 → 2184.22] like tiny because the vocabulary is so small. So these things you can run just like on your
[2184.22 → 2189.50] laptop, you know, you don't, you can turn off the turn off the Wi-Fi and just have it running locally.
[2189.50 → 2196.38] And actually right now, the last few weeks, there's been a group of folks, um, a lot who are, uh,
[2196.38 → 2203.34] working with the Catalan language who are adapting our speech recognition tools to make it work with
[2203.34 → 2210.70] Wasm so that it just runs in the browser, like superfast, like everywhere. I mean, it's, and you know,
[2210.70 → 2215.98] it's just, that's just like a, a group of the, you know, a set, a subset of the of our open source
[2215.98 → 2220.94] community who just picked up the tools and are running with it. You know, it's so, and then for
[2220.94 → 2227.66] the speech synthesis side of things, honestly, uh, one of the easiest places to interact with those
[2227.66 → 2235.42] models is on hugging face. We have a hugging face space. I think it's Kochi dash AI, and you can just
[2235.42 → 2240.78] with Radio, the Radio app is really nice. I have to admit, you just, you know, type in what you want
[2240.78 → 2245.66] to say, you click the language in the model you want, and then you, you get it. I don't remember
[2245.66 → 2251.10] exactly how many languages we have for speech synthesis, but it's growing. And after the
[2251.10 → 2257.58] the Malakand collaboration, it's six more languages from sub-Saharan Africa. So it's pretty cool.
[2257.58 → 2262.22] So I'm, I'm just wondering as you're, as you're doing some of these, how I'm going,
[2262.22 → 2265.42] I'm kind of going back to when you were talking about how you're just thinking about this all the
[2265.42 → 2267.98] time, you know, as, and you can't really turn that off.
[2267.98 → 2270.14] Voices in, in your head. No.
[2270.14 → 2277.02] Yeah, exactly. Like, like so many topics, what are the types of things that practitioners,
[2277.02 → 2283.10] as opposed to the users need to be thinking about as the field at large is moving forward? Because,
[2283.10 → 2288.22] you know, we've asked these kinds of questions of ourselves and, you know, 99% of everyone has
[2288.22 → 2296.30] the best of intentions as, as do you, but how do we make sure that as we really move the state of
[2296.30 → 2302.94] the art forward in terms of having things like very, very genuine sounding emotion, you know,
[2302.94 → 2308.70] in, in different emotions rippling through this, how does the how do we need to think about that in
[2308.70 → 2314.22] terms of the effect on, on the users? Because there's some amazingly positive things and
[2314.22 → 2318.94] potentially if we screw up or, or for the very few bad actors out there, there, there could be
[2318.94 → 2324.38] negative things as well. So it directly affects kind of mental health in a both positive and
[2324.38 → 2328.62] potentially negative of the end user. So how, like as someone who's thinking about this all the time,
[2328.62 → 2333.50] how do you frame that? How do you frame moving the field forward in a positive and productive way?
[2333.50 → 2339.10] So I think that I'm glad you brought this up because it is a huge part of working in this
[2339.10 → 2343.98] technology. If you ignore it, you say, I'm working in voice technology, and I'm just going to work in
[2343.98 → 2349.74] my bubble. And I'm not even going to care about the fact that somebody might be using our speech
[2349.74 → 2356.94] recognition for illegal surveillance, right? Like if you ignore that, that is a possibility you are doing
[2356.94 → 2364.46] yourself and also the community a disservice. So, oh, there's a lot with this. I would say that.
[2364.46 → 2369.02] So for, for one, I'd like to point, hopefully we can get up maybe a link to this. There's a
[2369.02 → 2378.14] an issue on our GitHub for, for text to speech, which is an open discussion on ways of mitigating
[2378.14 → 2384.58] misuse of synthetic speech systems. And that started as kind of actually not an issue as a GitHub
[2384.58 → 2388.90] discussion, I think. And it started as this kind of, you know, Hey, let's throw some ideas together.
[2388.90 → 2394.90] And it just evolved. And now it's just kind of growing discussion. And I think being open,
[2394.90 → 2399.62] having these conversations openly is really important because we got some feedback. There
[2399.62 → 2403.86] were ideas that came from, you know, people in the community that I'd never even thought of,
[2403.86 → 2407.70] you know, there's, there's watermarking audio, which is kind of obvious, but there's,
[2407.70 → 2410.98] there's whole layers of that. And then there was somebody who did, who's doing their
[2410.98 → 2416.42] master's thesis on, on this in particular, and they, you know, weighed in. So I think that,
[2416.42 → 2422.90] I think one kind of first step is to think about, to not brush it off, to think about what kinds of
[2422.90 → 2429.30] misuse is possible because there are so many different kinds. And if you lump them all together,
[2429.30 → 2434.42] then it becomes too kind of hard of a problem, and it can just kind of lock up. You get, you know,
[2434.42 → 2439.54] brain freeze or however you want to call it. But I like to think about kinds of misuse as
[2439.54 → 2446.10] basically two, two major groups. I think there's, there's people who will misuse technology
[2446.10 → 2452.66] kind of accidentally, or they don't think they're doing something bad, but it just blows up,
[2452.66 → 2460.02] which could happen very easily on social media. So the onion, right, is a satirical newspaper from
[2460.02 → 2466.34] the United States. Famously, I don't know, like every other month, there's an article from the onion
[2466.34 → 2472.02] that gets taken seriously by people who don't know the onion and that can cause real harm, right?
[2472.02 → 2479.06] It can get people very upset because they have a satirical headline, and it looks like a real news
[2479.06 → 2485.06] site, but it's not. And so that is an example of, you know, somebody who's not, they're not trying to
[2485.06 → 2491.46] spread fake news, but because people don't know the context, because people, it's just shared as a
[2491.46 → 2497.38] screenshot on social media, it loses all context, and it just snowballs into something that it was
[2497.38 → 2502.82] never intended to be. So there's, there are examples like that. Like, you know, you can think of somebody
[2502.82 → 2509.06] who uses our voice cloning to make a clone of, you know, President Trump saying something and they
[2509.06 → 2518.26] share it on social media. And earlier we had a voice demo, we had a voice cloning demo, which was,
[2518.26 → 2524.10] you didn't need to sign up to have an account to do it. So anybody could do it. And what we did then,
[2524.10 → 2530.42] because anybody could do it without having us know who they were, we put basically a watermark,
[2530.42 → 2534.66] a very audible watermark in the background, which is background music. I mean, it's like a very low
[2534.66 → 2541.90] hanging fruit, but anybody listening to it would not think, oh, this is an actual recording, you know,
[2541.90 → 2548.74] a secret recording of Trump in the Oval Office. You delegitimize it deliberately, you know,
[2548.80 → 2553.16] to where any user will pick up on that. And so if you're, if you're making something that's like,
[2553.48 → 2562.34] really, really accessible, easy to like the, the barrier to making a mistake, and making something
[2562.34 → 2566.50] that you think is funny and sharing it with your friends, and then it blowing up is very low, then I
[2566.50 → 2571.22] think putting those kinds of roadblocks in is important. And roadblocks is yeah, that's another,
[2571.48 → 2575.58] if you think about mitigating risk as putting up different kinds of roadblocks, because at some
[2575.58 → 2581.58] point, it's impossible to mitigate all risks, or at least it's impossible to guarantee that somebody
[2581.58 → 2587.78] or an organization that's motivated enough, will not do nefarious things with your
[2587.78 → 2592.78] code, right. But there are lots of responsible ways to put roadblocks in there. So right now we have
[2592.78 → 2598.18] this voice calling technology, but you have to sign in, you have to have a real email. And that
[2598.18 → 2603.18] is a way to have some kind of accountability. And on the speech recognition side of things,
[2603.68 → 2608.64] we have model cards that are out there that explicitly say, like, you know, you do not do
[2608.64 → 2614.36] bad things with this, but it's more specific than do not do bad things. And in terms of research
[2614.36 → 2618.62] collaborations, I think that especially when you're working with language communities,
[2618.62 → 2626.14] in which you are not a member, it's important to have members of the community working with you,
[2626.14 → 2633.92] so that you know, like, what are the risks, because the risks for, you know, me living in California,
[2633.92 → 2639.38] the ones that I can perceive are not the same kinds of risks for, you know, I have long-standing
[2639.38 → 2647.44] collaborators from Maker University in Uganda. And we've been working on radio, how do you say,
[2647.44 → 2654.58] keyword spotting and radio data for ideally to be used by the Ministry of Health kind of help inform
[2654.58 → 2662.68] health policies? And there's a bunch of risks that we spent a long time talking about,
[2662.68 → 2669.66] and figuring out how to mitigate for that context, because it's just different. And I think somebody
[2669.66 → 2674.50] brought us up on Twitter, why it's kind of forefront of my mind, how do you know if you're working with
[2674.50 → 2680.76] a language technology for a low resource or marginalized language that you're not doing
[2680.76 → 2685.44] harm to the community? And I think the simple answer is, if you're not a part of the community,
[2685.44 → 2689.98] you have no idea. That's why you really need to be working with people from the community,
[2689.98 → 2692.32] if you want to be working on that technology.
[2692.70 → 2696.30] I'm glad you addressed it. It's a relief to hear you have so much thinking around,
[2696.36 → 2701.56] I know way more than we can cover. But it's also, it's a relief to know that you kind of put that
[2701.56 → 2706.30] thought ahead of doing the stuff. And so it's, yeah, thank you for that. I appreciate it.
[2706.42 → 2712.30] But yeah, I think it's also like, there's really amazing positive things that come out of involving
[2712.30 → 2719.84] the community, like this Malakand work that you and I did, Josh, with that community. Like, I don't,
[2719.88 → 2725.20] I don't speak those languages. But there's like very simple things that like, I would have missed
[2725.20 → 2731.90] in the audio or in the processing that were just completely obvious to them. And like, it made
[2731.90 → 2739.32] the result so much, so much better, also in terms of the quality of the work. So like, just involving
[2739.32 → 2746.06] the community, like you learn so much, you learn about this, like, use and ethics side of things,
[2746.06 → 2753.38] but you also generally produce better, better output and better work. There's a lot, a lot to be said
[2753.38 → 2756.44] for that. And I'm glad you brought it up. And actually, I want to say just like,
[2756.62 → 2760.76] the way I think about it is, I don't want to be working on a project where I'm, you know,
[2760.84 → 2766.94] involving the community, I want, ideally to be involved, I want them involving me, like I don't,
[2767.08 → 2773.46] you know, the motivation. And I think that with this project in particular, I mean, I know, I did a lot
[2773.46 → 2778.36] of the kind of the technical, some of the technical, not even technical side of things, but it was very
[2778.36 → 2785.62] much a Malakand driven project. And I think that that is, if there's language communities out there
[2785.62 → 2791.80] that want to collaborate, I'm like, yes, let's do it. But I definitely want to be the one who's
[2791.80 → 2797.30] getting involved, as opposed to trying to pull other people into a project that might have false
[2797.30 → 2801.94] pretenses, you know, in the first place, like I, I could think this is a great project, and I might
[2801.94 → 2805.54] be able to convince people that it's a great project, and it's their language, but it's not.
[2805.54 → 2810.96] At the end of the day, I think that if you get the motivation, the impetus going the other direction,
[2811.34 → 2813.06] that's where real good work is done.
[2813.48 → 2818.62] Maybe that's a good sort of way to segue to a close as we're coming up on the end here is like,
[2818.70 → 2822.96] what would you tell kind of people out there? Maybe it's language community members, because now
[2822.96 → 2827.40] we do have listeners all over the world, like language community members that want to get involved
[2827.40 → 2834.12] and sort of like build things with the open source technology that Kochi is a part of,
[2834.12 → 2839.48] or maybe it's people that are creators are curious about this technology and want to get
[2839.48 → 2845.56] involved. Like what would you tell them in terms of like, joining into this work and helping move
[2845.56 → 2847.90] it forward positively?
[2848.14 → 2852.58] Yeah, I think there's like a million ways to get involved in a machine learning project,
[2852.58 → 2858.00] and you do not have to be technical. I think there's people who use the tech. And that's like,
[2858.06 → 2861.92] that's the obvious one to point to like, oh, you know, I'm involved in the project,
[2861.92 → 2868.66] because I'm using it to, you know, I'm using the voice cloning software to clone my voice sounding
[2868.66 → 2874.78] like five different characters in my video game. And I'm using that, that's one way. But there's,
[2875.04 → 2879.50] from the open source side of things, there are so many ways to get involved. Like documentation is just
[2879.50 → 2885.58] like the like a super low-hanging fruit, you know, documentation is something that really can make
[2885.58 → 2892.18] or break an open source project. And you can be super technical and write super technical
[2892.18 → 2898.08] documentation, which is useful, like API documentation. Or you can be somebody who's,
[2898.08 → 2904.16] you know, writing a kind of best practices playbook on how to use the tech. And honestly,
[2904.16 → 2909.68] the people who are less technical, maybe they're just starting, they know a little Python,
[2909.68 → 2917.56] Python, those people are able to write tutorials and beginner-friendly documentation way better than
[2917.56 → 2922.18] people who have been in it too long. Because if you've been in it too long, you're, you have all
[2922.18 → 2928.16] of these, you've just like absorbed all of these assumptions that are not intuitive for working with
[2928.16 → 2933.90] the code. And so I think getting involved with an open source project, an easy way to do it is to,
[2933.90 → 2941.42] you know, join wherever people are talking, whether it's on GitHub, whether it's like we use
[2941.42 → 2948.50] Gitter, G-I-T-T-E-R for our chat rooms. And you can pop into the chat rooms and say, Hey,
[2948.66 → 2954.42] this is me. I want to get involved. Here's my skills. That's a that's also a very low-hanging fruit.
[2954.42 → 2960.56] And also I think, so the Katakana community is, I think like, honestly, I think the best example of
[2960.56 → 2967.50] this, they've got such an active chat room on Slack. You've got people from all across the spectrum
[2967.50 → 2973.94] of super technical to not technical. But the thing that unites everybody is just, they love languages,
[2974.20 → 2979.16] right? When I think about where I want us to be like at Kochi for a kind of healthy open source
[2979.16 → 2983.10] community, I often think about Malakand and how they've, they've done a great job. It's just like,
[2983.20 → 2988.14] that's the whole reason the project started, like the, the, the speech synthesis project started is
[2988.14 → 2992.98] because I enjoyed hanging out in those Slack rooms because they were fun. And then we just,
[2993.06 → 2999.04] you know, started brainstorming, and then it just evolved. So yeah, I think that getting involved is,
[2999.14 → 3003.68] is very easy. Definitely don't have to be technical. And a lot of times the non-technical
[3003.68 → 3008.32] people have more to bring because they've got a fresh view on things.
[3008.96 → 3009.50] Beginner's mind.
[3010.18 → 3016.78] Yeah, definitely appreciate that. And I think it's a great way to end. I mean, definitely even
[3016.78 → 3022.96] with this podcast, it's great to be part of a wider community that's doing amazing things. And
[3022.96 → 3029.34] you sort of get sucked into these, these amazing stories and with Malakand or, or, or other,
[3029.50 → 3034.36] other things. So yeah, really glad that you brought out that, that side of things and appreciate you
[3034.36 → 3040.64] taking time to speak with us, Josh. Really excited to see what, what's happening with Kochi and hope to
[3040.64 → 3047.12] have you on again, uh, in another 80 episodes to share all the share all the great things that
[3047.12 → 3049.24] are, that are happening then. Thanks.
[3049.78 → 3050.98] Yeah. Thanks for having me.
[3050.98 → 3064.74] All right. That is practical AI for this week. If this is your first time listening,
[3065.18 → 3071.26] subscribe now at practical AI.fm or just search for practical AI in your favourite podcast app.
[3071.46 → 3075.52] We're in there. And if you're a long time listener, please do share the show with your friends.
[3075.52 → 3080.68] It is the best way you can help practical AI succeed. Thanks again to Vastly for shipping our
[3080.68 → 3085.98] shows superfast all around the world to Break master Cylinder for the Beats and to you for listening.
[3086.22 → 3089.64] We appreciate you. That's all for this week. We'll talk to you again next time.
