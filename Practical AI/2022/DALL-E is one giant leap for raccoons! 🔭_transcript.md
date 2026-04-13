[0.00 --> 10.52]  You know, I think that I think it needs to be OK for us to enjoy the evolution of machine learning, deep learning, you know, AI, whatever label you want to call it on.
[10.52 --> 15.30]  I know for me, if anything, I feel almost farther away from the idea of sentience than ever.
[15.76 --> 23.66]  But I say that with a deep respect for all that has been achieved so far by, you know, the global communities that are driving these technologies forward.
[24.08 --> 25.96]  And, you know, will we get there someday?
[25.96 --> 42.18]  Probably because we are just biological systems, you know, and at the end of the day, that ability to understand what it is that makes sentient creatures sentient, I think will be accomplished eventually.
[42.58 --> 47.20]  But I think that there's a long, long, long runway before we get to that point.
[55.96 --> 65.38]  Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive and accessible to everyone.
[65.74 --> 70.04]  This is where conversations around AI, machine learning and data science happen.
[70.42 --> 75.78]  Join us at practicalai.fm slash community and follow the show on Twitter.
[76.00 --> 77.96]  We're at Practical AI FM.
[78.40 --> 83.02]  Thank you to our partners at Fastly for shipping our pods super fast all around the world.
[83.02 --> 85.10]  Check them out at Fastly.com.
[85.96 --> 95.86]  Welcome to another fully connected episode of Practical AI.
[96.24 --> 105.76]  In these fully connected episodes, Chris and I keep you up to date on everything that's happening in the world of machine learning and artificial intelligence.
[105.76 --> 116.12]  And we help you level up your machine learning and we help you level up your machine learning game with some learning resources and some articles and things to keep you up with the state of the art.
[116.12 --> 121.02]  Excited to talk with you about stuff going on in the AI world today, Chris.
[121.24 --> 128.92]  It seems like this season, there's just been a lot hitting the AI fan.
[129.24 --> 131.08]  I don't know how else to put it.
[131.40 --> 133.18]  It's been a curious time lately.
[133.56 --> 135.90]  We've seen some interesting things arise.
[136.42 --> 138.30]  And yeah, absolutely.
[138.72 --> 139.06]  Yeah.
[139.06 --> 141.36]  And people's take on it is a little curious, too.
[141.44 --> 143.34]  I know we can go down that road as we get there.
[143.74 --> 144.02]  Yeah.
[144.14 --> 144.34]  Yeah.
[144.38 --> 157.22]  I guess I don't know if we if we want to sort of call it that that elephant in the room is that people are now calling certain AI models sentient.
[157.22 --> 166.36]  So I'm sure this is something that probably a lot of listeners have seen on popular media and that sort of thing.
[166.44 --> 167.86]  There was a is an engineer.
[168.50 --> 182.36]  I don't know actually his full position at Google, but that was kind of referring to this language and dialogue system that Google uses works with as having some level of sentience.
[182.36 --> 196.48]  I think both you and I sort of cringe when it is like, yeah, I don't know about you, but it's it's almost like how did we get here?
[196.80 --> 204.44]  Like, you know, like what is this state that we're in that people are calling these AI models sentient?
[204.64 --> 206.92]  How did we get to this state?
[207.08 --> 208.24]  Was it unexpected?
[208.60 --> 210.04]  Was it expected?
[210.84 --> 212.62]  What was the path that led us here?
[212.74 --> 215.02]  All of those kind of questions come up in my mind.
[215.42 --> 216.04]  What's your thought?
[216.52 --> 217.94]  You know, a little bit of both, I guess.
[218.10 --> 228.46]  So I guess any any of our longtime listeners know that we at the end of the day, we are very practical and pragmatic in terms of how we look at these things.
[228.72 --> 233.96]  And we have been doing this long enough to where we've seen quite a lot of evolution in the field.
[233.96 --> 244.88]  And certainly acknowledging that the goalposts kind of keep moving on various levels of kind of performance evaluation, if you will, for different models.
[244.88 --> 254.32]  But we've kind of come to a point this year where we're seeing some models with new, more expansive capabilities than the narrow ones of the past.
[254.40 --> 261.70]  And so maybe this is a logical moment for people to kind of reevaluate and apply some labels to it.
[261.70 --> 267.36]  When people talk about models having sentience today, I'm really struggling with that.
[268.14 --> 274.84]  But maybe, you know, I think it's probably every time we're hitting kind of a major set of milestones, we'll probably have these conversations.
[275.22 --> 275.72]  Yeah, yeah.
[275.72 --> 288.94]  So if we just sort of look back, like you say, we've been doing this show quite a while and this thing kind of pops up every once in a while and it does come into conversation and it's worth addressing.
[289.32 --> 303.24]  But I think if you look back and we look at the wider story of how kind of we had start with language models, but I think we'd go in other areas later and talk about kind of where we're at and where things have gone with vision and other things.
[303.24 --> 316.24]  But I think with language models, it used to be the fact that kind of the best language models would produce language that was sort of like passable.
[316.58 --> 328.56]  But you're not like really it doesn't grab you in the sense of like being like incredibly coherent, even like artful type language.
[329.10 --> 329.20]  Yeah.
[329.20 --> 341.02]  So starting out, if people don't know, this sort of language models used to be these models that would just look at the statistical frequencies of frequently incurring like n-grams.
[341.30 --> 350.56]  Like if I have this combination of two words, how often is that combination of two words seen with this other combination of two other words?
[350.56 --> 355.26]  And how many is this combination of three words compared to other combinations?
[355.26 --> 367.06]  And like you would kind of calculate all the probabilities of these things and be able to create a language model that would give you an understanding of like how probable certain sequences of text were.
[367.42 --> 372.70]  Well, that's like a very, actually very useful and still used in a lot of places.
[372.70 --> 373.26]  Absolutely.
[373.26 --> 384.68]  But we kind of went from that into this zone of like recurrent neural networks where now we've kind of got this element of memory and bidirectional memory.
[384.68 --> 404.36]  And then we like scaled that up very much with transformers, which are kind of a very computationally scalable way to look at, you know, a sequence of things coming into it and in context and scale that up in a very computationally favorable way.
[404.36 --> 416.64]  And that, of course, has kind of blossomed into these incredibly large transformer based language models trained on very, very much data.
[416.84 --> 433.60]  What happens then is these models, which can model context very well, right, can also produce sequences of text that are incredibly coherent and compelling, to be honest, to a person viewing them.
[433.60 --> 439.98]  So I don't know if you remember when I think we had some original conversations when the GPT models were coming out from OpenAI.
[440.14 --> 440.74]  Do you remember that?
[440.94 --> 441.16]  I do.
[441.62 --> 445.22]  Yeah, I remember really being quite surprised.
[445.78 --> 452.70]  I don't know if you shared that with colleagues or maybe people that were not practitioners, maybe.
[453.12 --> 453.36]  I did.
[453.64 --> 461.58]  I mean, I shared it with my daughter, as a matter of fact, just kind of drawing her over and she wasn't terribly interested, but, you know, kind of pulling her over to the laptop and saying, look at this.
[461.58 --> 464.24]  And we were talking about it at work.
[464.42 --> 467.60]  And so, yeah, I mean, it was a big deal for what it was.
[468.12 --> 468.24]  Yeah.
[468.58 --> 468.94]  Yeah.
[468.98 --> 471.06]  And I mean, this is quite compelling.
[471.44 --> 472.84]  I do want to bring up this.
[473.58 --> 479.50]  So I have pulled up this article that I think is really relevant.
[479.50 --> 486.44]  And I don't usually quote from things on the podcast, but I don't know that I could really say this better.
[486.82 --> 489.68]  It's probably worth having on the record in the podcast.
[489.68 --> 503.92]  But the paper is on the dangers of stochastic parrots by Timnett Gebru and crew who have done a lot of this work kind of looking at limitations and dangers of these large language models.
[504.14 --> 514.90]  And they're talking about how the outputs of these models like GPT-3 or something is seemingly coherent, but they label it as coherence in the eye of the beholder.
[515.34 --> 515.46]  Yeah.
[515.46 --> 517.96]  Let me just read some of this.
[518.08 --> 519.56]  I think it's worthwhile.
[519.94 --> 529.22]  So they talk about, we say seemingly coherent, and they're talking about like the output of these models because coherence is, in fact, in the eye of the beholder.
[529.44 --> 538.94]  Our human understanding of coherence derives from our ability to recognize interlocutors' beliefs and intentions within context.
[538.94 --> 548.14]  So they're talking about, hey, when you communicate with someone, you basically assume that they have some intentionality with their conversation.
[549.10 --> 551.90]  They're saying something because they are communicating.
[552.00 --> 553.30]  It's a two-way thing, right?
[553.30 --> 554.52]  They're communicating with you.
[554.52 --> 560.44]  They say text generated by a language model is not grounded in communicative intent.
[561.06 --> 564.56]  Any model of the world or any model of the reader's state of mind.
[564.56 --> 572.92]  It can't have been because the training data never included any sharing thoughts with the listeners, nor does the machine have the ability to do that.
[572.92 --> 579.94]  This can seem counterintuitive given the increasing fluent qualities of automatically generated text.
[579.94 --> 597.80]  But we have to account for the fact that our perception of natural language text, regardless of how it was generated, is mediated by our own linguistic competence and our predisposition to interpret communicative acts as conveying coherent meaning and intent, whether or not they do.
[597.80 --> 600.84]  So that's sort of a bunch of words.
[600.84 --> 619.22]  It's a really important set of words that like the fact that you can create seemingly coherent text doesn't imply that there was an intent behind that or some understanding of your state of mind or that there was even a state of mind by like the sentience behind this.
[619.70 --> 627.30]  I think that states super, super well the intuitive reaction that I have to the output of those kinds of models.
[627.30 --> 638.78]  So, so, so yeah, that represents the way I'm thinking when I'm getting that and when people are applying these, these labels to it, like, oh, clearly sentient because of this.
[638.90 --> 641.58]  I'm just kind of going, not so much.
[641.84 --> 641.98]  Yeah.
[642.12 --> 656.88]  And, but it's probably also true that when you see certain things like come out of a language model, there's like, before you go into that mode and maybe me when I was first seeing the GPT things, it's like, wow.
[656.88 --> 659.94]  This is like, I didn't think this was possible.
[660.52 --> 663.88]  There's something sophisticated going on here.
[664.10 --> 671.72]  Or that's where sort of like maybe a person's mind would go naturally is like, hey, this is really compelling, coherent text.
[671.72 --> 688.16]  And maybe there's something more going on here than I'm thinking because our mind kind of like you're talking about, it goes to, or many people's mind would go to the fact that like, wow, it understood exactly what I was talking about and responded in a really coherent way.
[688.16 --> 693.90]  So it must have like understood me or, you know, there was intent there or something like that.
[693.90 --> 698.70]  So I find it dangerous to go here because you're a language expert, definitely on our team.
[698.80 --> 699.86]  And I am certainly not.
[700.02 --> 714.12]  But as someone in the field, though, who does not have this expertise, though, my expectation is that, you know, languages, and I'm going to say this in all using all the wrong lingo based on, you know, the kind of professional work that you do.
[714.12 --> 719.84]  But it's a framework and there's relationships between all the aspects of the language.
[720.34 --> 727.94]  And I don't think I am as surprised in the large that a sophisticated model can find that.
[728.02 --> 734.68]  But that's a that's a far cry from all of the attributes that I normally associate with sentience.
[735.46 --> 737.18]  So is it impressive?
[737.74 --> 739.20]  Yeah, really impressive.
[739.40 --> 740.76]  And I'm acknowledging that.
[740.76 --> 752.64]  But but that's that's not the same thing as saying, OK, if you're seeing A, B and C here, that also correlates to to X, Y, Z, you know, which is a different a different set of criteria.
[753.12 --> 753.20]  Yeah.
[753.20 --> 764.76]  And I think we've seen this a bunch of times over the years that we've been doing this is that something kind of wow will happen and people will will infer a bigger jump than it actually is.
[764.76 --> 769.08]  It's an impressive jump nonetheless, but they they extend it, I think.
[769.26 --> 770.92]  And there's an emotional aspect to it.
[771.12 --> 776.90]  And I think that's how that's how I find this this particular, you know, moment.
[776.90 --> 777.58]  Yeah.
[777.58 --> 777.68]  Yeah.
[778.18 --> 780.52]  Just another statement from this paper.
[780.66 --> 796.40]  I really I can I'll link it in the show notes kind of gets to that fact of like you're saying stitching together words and stuff to make language is not what it means to, you know, at least in my mind to to be sentient.
[796.40 --> 807.44]  They say, contrary to how it may seem, when we observe its output, a language model is a system for haphazardly stitching together sequences of linguistic forms.
[807.66 --> 817.80]  It is observed in vast amounts of training data, according to probabilistic information about how they combine without any reference to meaning a stochastic parrot.
[818.44 --> 822.98]  And that's what the reference is to the sort of metaphor that they're that they're using.
[822.98 --> 839.96]  Sure. So it's interesting, though, that this trend, this sort of like trend in language model size, the amount of data that these language models are trained on has increased this apparent coherence of the output from these models.
[839.96 --> 855.74]  And I think they sort of in a lot of ways predicted in this in this work and maybe others that people would start increasingly thinking that these things have some type of sentience or something just because they're so much more compelling in the output.
[855.88 --> 862.52]  What they're saying is, I think this is coming, but beware, this is not what you think it is.
[862.52 --> 863.94]  That sort of message.
[864.48 --> 872.04]  So that that points out a problem in that if people are going to conflate coherence with sentience.
[872.36 --> 873.72]  Oh, it'll come up again. Yeah.
[874.12 --> 882.42]  Yeah. Oh, it'll keep coming up with every new model at this point because it's already the the what is possible is already so sophisticated now.
[882.42 --> 893.12]  So so how do you address that? How do you parse the difference in in cohesiveness versus sentience and have a way of distinguishing between the two?
[893.12 --> 893.62]  So.
[916.30 --> 923.06]  Well, Chris, we're always talking about language on this podcast, probably because of my own very biased.
[923.12 --> 934.34]  opinion. But there's a lot of trends happening right now that we can't ignore in the vision space as well and actually in ways that are also connected to the language space.
[934.34 --> 946.62]  And I think those are also things that are taking AI beyond the realm of practitioners into sort of the wider public's view.
[946.62 --> 953.56]  So an example of this recently was I saw on my Twitter is like Cosmopolitan magazine.
[954.12 --> 957.16]  I don't know if it's their latest at the time of the recording.
[957.28 --> 963.92]  It's one of their latest cover photos was generated by the DALI to model.
[963.92 --> 971.28]  I believe it was from open AI, which is a model that takes text input and then outputs outputs an image.
[971.28 --> 981.12]  So you can say I want a picture of astronaut riding on a horse on the moon in the style of, you know, Van Gogh or whatever.
[981.12 --> 985.02]  And it will give you that, which is pretty extraordinary.
[985.52 --> 987.08]  And that's also like these images.
[987.36 --> 987.84]  There's another.
[988.48 --> 990.06]  So there's similar models.
[990.34 --> 994.44]  It seems like there's all of these models coming out like within weeks of one another.
[994.72 --> 998.14]  I don't know exactly how the authors would prefer to say it.
[998.34 --> 1001.62]  Imagine, imagine from Google.
[1001.62 --> 1003.62]  Google and it does a very similar thing.
[1003.76 --> 1005.00]  There's two or three other ones.
[1005.16 --> 1008.64]  Sorry, if one of our listeners created one of these models and I didn't mention yours.
[1008.82 --> 1009.50]  I apologize.
[1009.84 --> 1016.78]  But it seems like five to ten of these things came out like within a month or something.
[1017.46 --> 1023.12]  And this is also one of those moments, kind of like the Google engineer saying that a language model is sentient.
[1023.26 --> 1025.88]  It's like something happened here.
[1026.26 --> 1026.44]  Yeah.
[1026.44 --> 1029.40]  Like what what led us to this point?
[1029.40 --> 1033.76]  What are the key things to maybe take away from like, why did all this happen at once?
[1033.88 --> 1034.68]  That's what I'm thinking.
[1035.22 --> 1036.58]  Well, we're making these leaps.
[1036.98 --> 1039.34]  There's this determination to say we've gotten there.
[1039.54 --> 1040.24]  We've gotten there.
[1040.78 --> 1044.46]  And if you look at like what Dali can do, it's amazing.
[1044.92 --> 1049.02]  As you said, I mean, you can you can input the text and you can get these.
[1049.22 --> 1050.62]  They're not just simple images.
[1050.62 --> 1055.40]  If any if anyone in the audience hasn't seen the output, you you need to go look.
[1055.48 --> 1056.50]  I mean, they're remarkable.
[1056.62 --> 1057.00]  It's there.
[1057.12 --> 1057.64]  It's art.
[1057.64 --> 1060.00]  You know what what's possible.
[1060.20 --> 1062.96]  And and they're super detailed and super complex.
[1062.96 --> 1071.68]  And so it's another one of those moments where you're like, wow, we've hit a big milestone here and something has changed.
[1072.00 --> 1073.12]  Must be sentience.
[1073.12 --> 1085.60]  This is that I mean, what we're seeing here visually is the is the equivalent sort of of the with the language models of being able to say with a visual output, being able to say it's coherent.
[1085.60 --> 1093.38]  I mean, you put in a simple thing, which is the text, and you came out with this enormously complex thing, which is the graphical image.
[1094.12 --> 1095.64]  So, yes, we're at the inflection point.
[1095.96 --> 1097.54]  So this is another one of those.
[1097.60 --> 1101.02]  It begs where does that coherence distinguish itself?
[1101.02 --> 1111.76]  This is really interesting, I think, because there is a connection between all of this stuff that's going on and the physics world that I grew up in.
[1111.90 --> 1115.86]  Maybe not grew up in, but that's where I started my career, at least.
[1115.86 --> 1124.62]  And that's this connection to like statistical physics or thermodynamics with these models, which I can describe here in a second.
[1124.80 --> 1135.82]  But it strikes me as well that there's a whole bunch of kinds of systems that given a very simple input, create very complicated output.
[1135.92 --> 1138.32]  I guess this is like chaos theory and other things.
[1138.32 --> 1147.66]  It doesn't mean that those those systems are like that's not an indication of sentience in and of itself that like that property.
[1148.10 --> 1150.68]  So you can have like a double pendulum.
[1150.68 --> 1155.86]  So a pendulum with a ball in the end, which is connected to another pendulum with the ball in the end.
[1155.94 --> 1158.42]  And you started out in a very simple arrangement.
[1158.42 --> 1164.28]  And then all of a sudden, the dynamics of that are extremely complicated and pretty amazing.
[1164.28 --> 1180.16]  So, yeah, I think that that was a good point that you made about this sort of seemingly simple or limited input to really, really complicated or seemingly artful output, I guess, is a good way to put it.
[1180.40 --> 1184.90]  What are some of the best pictures you've seen from Dali?
[1185.04 --> 1187.90]  Do you remember any that caught your eye?
[1188.36 --> 1191.24]  I've seen a lot over the last month or so.
[1191.86 --> 1193.92]  I like the animal ones, as you know.
[1194.28 --> 1194.70]  Yes.
[1195.50 --> 1200.24]  It's like animal in a certain place doing a certain thing.
[1200.34 --> 1202.62]  It's unusual and you wouldn't typically see it.
[1202.70 --> 1202.92]  Yes.
[1203.04 --> 1206.70]  Those that's yeah, that's that's definitely my my drug of choice.
[1206.96 --> 1215.44]  Who I am, you know, is the creation of that kind of organized and beautiful complexity that it does?
[1215.44 --> 1224.92]  Is that do you think what's driving that the leaps on analysis of what the models, you know, you know, is this the model that's pushed us into that?
[1224.92 --> 1230.36]  Is it just that creation of complexity and that with organization and understanding?
[1230.36 --> 1232.54]  And as you said earlier, coherence?
[1232.54 --> 1241.64]  I think that there's like there's probably several components here that when they were not put together.
[1241.88 --> 1242.60]  Right.
[1242.60 --> 1250.82]  The output of those components was maybe limited to a specific domain or modality of data.
[1250.82 --> 1257.82]  But now we've sort of had this progression in the industry where we've had transformers.
[1258.78 --> 1265.82]  We've had things like clip, which allows you to have this sort of like text image embeddings.
[1266.82 --> 1267.06]  Yeah.
[1267.06 --> 1274.08]  And then we've had another thing, which is where the connection with physics come in, which is these diffusion models.
[1274.92 --> 1287.74]  And so if you look at these text to image things that are being produced, at least like DALI 2, that sort of like builds on the combination of those things.
[1287.74 --> 1295.98]  So it's almost like these major components were developed in isolation for a specific purpose or with a specific goal.
[1295.98 --> 1298.04]  And then people are like, well, what?
[1298.46 --> 1307.38]  There is a really interesting combination when I combine these together and think about the different modalities of data that I'm working with, text and images.
[1308.14 --> 1314.72]  I think that sort of like there's these really powerful components that have developed over time.
[1314.72 --> 1321.50]  And people are now kind of mixing different modalities, mixing different of these components.
[1321.50 --> 1326.32]  Because really, a clip model is going to output a series of numbers.
[1326.56 --> 1332.42]  There's nothing saying I can't put those series of numbers into a diffusion model or into a transformer model.
[1332.42 --> 1336.82]  Or like what happens if I switch the order and change all these things around?
[1336.92 --> 1338.36]  I think that's what people are really.
[1338.36 --> 1341.36]  They're not doing it just sort of wild trial and error.
[1341.36 --> 1353.24]  But in a very like intentional and well thought out way, they're like, well, now it like it would make sense if I combined this clip model and this diffusion model in this way.
[1353.84 --> 1358.90]  And that's turns out to produce something that's extremely profound.
[1358.90 --> 1371.34]  But that is also if you think about it for a moment and take it outside of just the AI world alone and talk about technology at large, that's the normal way that technology innovation happens.
[1371.94 --> 1378.18]  People will push down a particular modality or something and try something out because they're fulfilling a need.
[1378.60 --> 1382.76]  And there'll be a bunch of small incremental improvements along the way.
[1382.76 --> 1385.82]  And then somebody goes, wow, this is a really powerful building block.
[1385.92 --> 1388.52]  What if I switch modes now and do that?
[1388.92 --> 1391.38]  And then they get something that's quite remarkable.
[1391.38 --> 1394.72]  And we've seen that in all technology development over time.
[1394.82 --> 1402.14]  So I think I think that what you just described was a really typical evolutionary path for technology.
[1402.28 --> 1407.42]  And, you know, like in the case of Delhi, we we have these amazing visual images.
[1407.42 --> 1409.48]  So it's really, you know, it catches you.
[1409.48 --> 1411.84]  Yeah, that's another side of the wider.
[1411.84 --> 1414.16]  It's super marketable in terms of the output.
[1414.54 --> 1423.84]  But it's really I see it as an important evolutionary innovation that drives the field forward and gives us a bunch of new capabilities and stuff.
[1424.08 --> 1425.32]  But I don't see it as unexpected.
[1425.90 --> 1427.68]  Yeah, yeah, I would agree with that.
[1427.80 --> 1438.24]  I think just to kind of further break down what what we're talking about here, the most recent that we found was or that came out was DALI 2.
[1438.24 --> 1444.52]  Well, maybe not the most recent of these types of models, but one of the ones that gained a lot of attention, DALI 2.
[1445.26 --> 1447.88]  And it's an evolution there.
[1447.98 --> 1452.66]  So there was an original DALI model and it was actually transformer based.
[1452.66 --> 1455.32]  So if you could kind of track back the steps.
[1455.32 --> 1461.22]  But if you think about coming maybe from the other direction, we had like we already talked about these.
[1461.22 --> 1465.70]  We said, hey, well, it would be useful for us to model sequences of things.
[1465.70 --> 1470.50]  We could look at different pairs and triplets of those things.
[1470.58 --> 1471.54]  That's an Engram model.
[1471.72 --> 1485.34]  And we could then kind of look at recurrent ways or bidirectional ways to look at the sequence in recurrent or bidirectional type of layers in neural networks.
[1485.34 --> 1498.22]  And then we said, well, this is kind of a scaling problem there and maybe some things that we maybe don't want to look at neighbors, but we want to look at attention at a sort of wider level.
[1498.34 --> 1501.32]  And so then came along attention and transformers.
[1501.88 --> 1505.44]  And then that was all still kind of text based.
[1505.44 --> 1505.84]  Right.
[1506.40 --> 1515.44]  Well, DALI, in my understanding, the original one, so not the most recent one, but the original one was based on a transformer architecture.
[1515.44 --> 1533.08]  So they basically said, well, what would prevent us from saying I'm going to take sequences of tokens that are words and concatenate them with sequences of tokens that correspond to image pixels and or an image embedding.
[1533.58 --> 1533.76]  Right.
[1533.76 --> 1537.68]  And so I can still put that through my transformer model.
[1537.78 --> 1538.26]  What happens?
[1538.36 --> 1551.74]  And then I think there was this realization of the goodness of these diffusion models, which if people kind of don't know about diffusion models, what happens is it's a way to kind of denoise something.
[1551.74 --> 1560.08]  So if you introduce a bunch of noise into an image, you can train a model to denoise that and kind of reverse.
[1560.26 --> 1563.38]  So go from noisy to not noisy.
[1563.38 --> 1579.52]  And people are like, well, what if we take some of these text encodings that we have and either we condition the diffusion model on those or we use these clip models and other things to get these text image encoders.
[1579.52 --> 1585.16]  And then we can put that into a diffusion model and you can kind of see these things start to pile on top of one another.
[1585.74 --> 1587.58]  And now we have these beautiful images.
[1587.58 --> 1594.56]  But I think you're right that when you see these images, it's almost like you don't get that full sense of the history.
[1594.92 --> 1595.14]  Right.
[1595.18 --> 1602.68]  And you're like, oh, this is achieved like a new level when in reality, there's been a lot of building blocks that have come along the way.
[1602.68 --> 1604.86]  And it shocks sort of the wider audience.
[1605.06 --> 1609.10]  But if you look back, there is a path that led there.
[1609.32 --> 1616.90]  It's interesting is that that path, it's not, you know, it's spanned a couple of different times, the visual and the language model side.
[1617.02 --> 1626.70]  You know, we really like to, from a human perspective, classify, well, something is NLP and it's language and it's text or this one's visual.
[1627.34 --> 1631.72]  But it's all a lot of these underlying building blocks are moving across.
[1631.72 --> 1638.18]  And so I think we've really seen that migration back and forth across modalities over time.
[1638.78 --> 1649.08]  And it's interesting in that there was a point in time where I thought it kind of felt like there were different branches of machine learning kind of going off on their own direction to some degree.
[1649.50 --> 1655.04]  But I think what we've seen with these recent models is they're all tied together and they're all coming back.
[1655.04 --> 1664.60]  And it's a lot of times it's when you mix the chocolate and the peanut butter together that you get something a little bit new right there that has value unto itself.
[1664.60 --> 1693.64]  Well, I often, I mean, I do get sort of in my own little NLP world.
[1693.64 --> 1697.32]  So it is good to look at kind of trends more widely.
[1697.32 --> 1706.40]  And I think the trends with the visual model or the text to image models that we've been discussing, those are really instructive in terms of how all these things are connected.
[1707.02 --> 1715.44]  I think you could connect those things as well to speech models, which oftentimes speech models leverage kind of spectrograms or something.
[1715.44 --> 1723.32]  And so there's a connection to processing those like images with computer vision type of models.
[1723.62 --> 1728.82]  My prediction, which will be wrong because, you know, all predictions are wrong.
[1728.82 --> 1736.84]  But my prediction would be that like we've sort of seen a lot of text image stuff.
[1737.50 --> 1739.92]  I think it would be interesting.
[1740.26 --> 1746.66]  And I think you'll see a lot of people maybe exploring more of sort of audio in that mix too.
[1746.66 --> 1759.58]  Whether that be audio image or other things where there's no textual representation or maybe there's like music accompanying a video.
[1759.90 --> 1766.82]  And those sorts of things are I think all of that sort of fits in this direction that we're going.
[1766.82 --> 1778.30]  I totally subscribe to that expectation from a prediction standpoint because I think that what you're saying there is that there's some modality mixes here that haven't been explored yet.
[1778.44 --> 1780.54]  But it would make sense to go do those.
[1780.66 --> 1789.52]  I mean, as people have found some value here, I think that all of those different modalities and the transfer between them and such will be explored.
[1790.58 --> 1793.16]  So I think we'll see a lot more of that over the next few years.
[1793.16 --> 1798.90]  Yeah, I think that there's a lot of areas to explore, I think, that like fit in this area.
[1799.02 --> 1806.88]  I was just on a had a discussion with some of our our partners that work with deaf organizations.
[1806.88 --> 1810.88]  So organizations that work with various deaf communities around the world.
[1810.88 --> 1817.46]  And a lot of the hearing people in the tech world that have like thought about, oh, we could use AI for sign language.
[1817.46 --> 1817.82]  Right.
[1818.10 --> 1822.96]  The first thing that they think about is, well, I'm going to take sign language and I'm going to convert it into text.
[1823.16 --> 1825.78]  Which is I mean, it's not a bad thing to do.
[1825.84 --> 1827.02]  I'm not I'm not saying that at all.
[1827.02 --> 1828.66]  I think it's actually quite interesting.
[1828.66 --> 1835.00]  But it's not really like in my understanding, a lot of a lot of deaf community.
[1835.00 --> 1844.12]  It's not like the first thing that comes to their mind in terms of the technology that that they would want as part of their community because their language is sign language.
[1844.12 --> 1857.92]  So I was just on a call with them and we were sort of dreaming together and it was like, well, could we take sign language videos and generate sign language videos in a different sign language?
[1858.08 --> 1861.58]  Because if people don't know, there's 400 sign languages in the world.
[1862.06 --> 1862.30]  Wow.
[1862.46 --> 1864.28]  I did not realize that at that level.
[1864.40 --> 1864.56]  Yeah.
[1864.56 --> 1865.86]  I knew there was more than one.
[1866.18 --> 1866.62]  Yeah.
[1866.62 --> 1866.72]  Yeah.
[1866.72 --> 1866.98]  Yeah.
[1867.08 --> 1875.92]  And or just doing things like thinking about like, hey, there's sign language content is video.
[1876.10 --> 1876.42]  Right.
[1876.42 --> 1882.26]  And we sort of take for granted that we can search through our content like it's text and we have text search.
[1882.46 --> 1887.66]  But if you have like hours and hours of sign language video, how do you how do you find what you want?
[1888.16 --> 1888.40]  Right.
[1888.40 --> 1896.56]  Are you forced to like go back into the text modality and like search based on text tags, which are not your language?
[1896.84 --> 1897.00]  Right.
[1897.40 --> 1904.74]  So is it possible to to sign into a camera and have that be a sign based search?
[1904.74 --> 1919.74]  So I think all of this, like these sorts of things partially are unexplored because like there's communities that haven't yet been served or engaged from a community perspective with with this technology.
[1920.56 --> 1931.84]  And we were just talking with Joshua Meyer, you know, on our last episode about how beneficial it is when you can partner with a community that end user group.
[1931.84 --> 1937.40]  And they're the ones really, really driving like, hey, we really want this for our community.
[1937.84 --> 1940.00]  And we're already putting work in.
[1940.08 --> 1942.24]  Could you partner with us to help like that?
[1942.30 --> 1945.76]  That produces a lot of maybe unexpected opportunities.
[1945.76 --> 1955.16]  And so, yeah, there's definitely still a lot of multimodal, very interesting problems and areas to to explore, I would say.
[1955.40 --> 1957.68]  Do you think we've just barely scratched the surface so far?
[1958.34 --> 1958.58]  Yeah.
[1958.68 --> 1966.54]  I mean, that's kind of, to be honest, some of the laughability, I guess, to me of the of the sentient thing.
[1966.54 --> 1978.90]  And I don't mean that to demean the person that said that, because obviously they made a very I mean, they made a decision to be very opinionated about that and defend it.
[1978.90 --> 1982.58]  But the world is just so complex.
[1982.90 --> 1991.98]  And to think about like these models dealing with all of these things that we haven't even thought about yet in modalities that we've only begun to explore.
[1991.98 --> 2000.30]  I just view it as a really fun time to be part of this technology because we get to explore really interesting things.
[2000.90 --> 2002.38]  You know, it's funny that you say that.
[2002.54 --> 2014.88]  I think it needs to be OK for us to enjoy the evolution of machine learning, deep learning, you know, AI, whatever label you want to call it on, without having to try to always stretch.
[2015.50 --> 2020.00]  I know for me, if anything, I feel almost farther away from the idea of sentience than ever.
[2020.00 --> 2028.48]  But I say that with a deep respect for all that has been achieved so far by, you know, the global communities that are driving these technologies forward.
[2028.60 --> 2030.26]  And they're hugely valuable.
[2030.82 --> 2032.70]  And, you know, will we get there someday?
[2033.10 --> 2049.22]  Probably because we are just biological systems, you know, and at the end of the day, that ability to understand what it is that makes sentient creatures sentient, I think, will be accomplished eventually.
[2049.22 --> 2054.28]  But I think that there's a long, long, long runway before we get to that point.
[2054.66 --> 2056.90]  And we're learning as we go.
[2057.00 --> 2061.22]  And I think it needs to be OK for us to say where we're at today.
[2061.38 --> 2064.78]  And that doesn't have to be the ultimate goal yet.
[2064.86 --> 2066.66]  We may have many years to go before we get there.
[2067.08 --> 2070.24]  But sometimes I think people are just overreaching for where we're at.
[2070.38 --> 2071.14]  Appreciate the moment.
[2071.28 --> 2075.02]  Appreciate the fact that we're doing some really, really cool stuff today.
[2075.02 --> 2082.88]  In research and the things that are coming out and go do some really fascinating things with what we have now that we didn't have yesterday.
[2082.88 --> 2091.62]  Yeah, I think that obviously there'll be a whole range of views on whether we would ever reach sentience or not.
[2092.00 --> 2098.78]  And somewhat driven by like different religious and philosophical views on what it means to be human.
[2098.96 --> 2103.94]  And I would be opinionated about some of those things very much based on my faith.
[2103.94 --> 2112.78]  But the fact that we will create more coherence and amazing output of these models like we've already talked about is going to happen.
[2112.78 --> 2130.94]  What I think is interesting and that the Timnet and that paper kind of brings up and discussions similar to that bring up is we as practitioners might understand how these things are stochastic parrots or maybe like not.
[2130.94 --> 2141.82]  Like we have maybe a little bit more understanding about how the relation is between their output, the data we feed into it, the sort of variability and limitations.
[2141.82 --> 2167.02]  And I think it's partially on us as practitioners to make sure we also tell that story well and not just like post a contextless, like amazing picture on the internet and, you know, mislead people about like just promoting this idea that AI can do things you never thought it could be able to do.
[2167.02 --> 2177.34]  When in reality, there is a sort of like predictable path like you were talking about of technology and incremental advancements towards that picture that you posted on Twitter, right?
[2177.68 --> 2181.64]  But when you do that, you sort of like it doesn't have any of that context, right?
[2181.80 --> 2182.00]  No.
[2182.46 --> 2184.76]  You know, we're always going to have that hype machine going.
[2185.34 --> 2186.72]  There's a lot of reasons for that.
[2186.82 --> 2192.62]  But I guess there's a little bit of a Zen attitude of appreciate where we're at, you know, keep pushing forward and everything.
[2192.62 --> 2200.32]  But appreciate where we're at for what it is and that it doesn't have to be more than it is for it to be a pretty wonderful thing.
[2200.82 --> 2204.90]  So, yeah, I'm a little bit, like I said, a little bit Zen-like in that way.
[2205.32 --> 2207.36]  But we've seen so many of those.
[2207.68 --> 2210.34]  And it's one reason we're still doing the podcast after all these years.
[2210.82 --> 2211.06]  Yeah.
[2211.26 --> 2211.44]  Yeah.
[2211.48 --> 2216.24]  I mean, it's definitely been a ride and always learning along the way.
[2216.24 --> 2220.74]  So, I'm sure it will continue to be that way.
[2220.96 --> 2232.28]  And I very much did not expect to be talking about things like photos of raccoons wearing an astronaut helmet looking out a window at night.
[2233.18 --> 2237.00]  So, I just got to tell the audience before we stop recording today.
[2237.00 --> 2239.64]  So, Daniel sent me this raccoon picture.
[2240.08 --> 2246.36]  And I'm already, before he did that, I'm already looking at all of these raccoon pictures from Dolly that there are out there.
[2246.48 --> 2250.22]  And so, somehow we're on this behind-the-scenes raccoon kick going here.
[2251.86 --> 2252.76]  But, yeah.
[2252.92 --> 2253.20]  Sorry.
[2253.34 --> 2255.72]  It's just an odd coincidence there.
[2256.34 --> 2261.90]  This is a totally off-the-wall idea and train of thought that has nothing to do with anything.
[2261.90 --> 2264.86]  But, Chris, I know all that you do with animals.
[2265.94 --> 2269.76]  My wife is giving me a bit of a hard time because I'm kind of geeking out over this.
[2270.66 --> 2274.18]  In our patio, she moved some houseplants out there.
[2274.30 --> 2281.56]  And we have a bird that established a home in one of the pots out there and has laid a couple of eggs so far.
[2281.56 --> 2290.20]  And so, I'm trying to determine, like, what is the appropriate, like, live stream camera that I can set up to observe this?
[2290.20 --> 2303.10]  And then, like, what there has to be some type of, like, alert that I can do that's AI-driven that tells me when an egg has hatched or when there's a, like, feeding going on or something.
[2303.62 --> 2303.80]  Yeah.
[2303.92 --> 2306.50]  This has consumed my thoughts for the past few days.
[2307.04 --> 2308.44]  I'm not surprised at all.
[2308.50 --> 2309.92]  Although, I was too lazy.
[2310.10 --> 2313.60]  We just stuck a live feed camera in there and watched it.
[2313.90 --> 2318.48]  And if there was daylight, there was always stuff going on between mom and dad taking care of the eggs.
[2318.48 --> 2324.34]  But, yeah, when I was on my last business trip away from Atlanta, I was down in Orlando and we were all around the table.
[2324.78 --> 2330.60]  And I was sharing the live feed with a bunch of people around the table of the mom and dad coming and going.
[2331.10 --> 2335.90]  And so, I'm telling you, there are people who are really, really into this.
[2336.02 --> 2344.74]  And if you are the guy who puts out the model that, like, alerts them for all the things, you'll be a very popular man in the bird watching world.
[2344.74 --> 2351.96]  Maybe I'll create a GitHub repo and a few YouTube videos describing my setup.
[2352.28 --> 2352.98]  That would be ideal.
[2353.08 --> 2353.10]  Okay.
[2353.10 --> 2353.92]  Daniel Whitenack.
[2354.34 --> 2355.44]  He said it here.
[2356.22 --> 2356.70]  Yeah.
[2356.84 --> 2363.10]  I mean, the people, maybe when you listen to this episode and you search for my repo and don't find it,
[2363.22 --> 2366.92]  then you'll realize that maybe I didn't get as far as I had hoped.
[2366.92 --> 2367.32]  Okay.
[2369.24 --> 2370.52]  Well, on that note.
[2370.62 --> 2376.24]  On that note, we will link some of the links that we've talked about in the show notes for everyone.
[2376.38 --> 2383.24]  So, make sure and check those out, including the Stochastic Parrots paper and some information about the fusion models and everything.
[2383.50 --> 2386.98]  So, that's a great way to follow up on some of these topics.
[2387.44 --> 2392.16]  We hope everyone enjoys the raccoon pictures that Dolly produces as much as Daniel and I have.
[2392.26 --> 2393.24]  Yes, of course.
[2393.24 --> 2394.64]  All right.
[2394.72 --> 2395.58]  Talk to you soon, Chris.
[2395.86 --> 2396.18]  Take care.
[2396.30 --> 2396.62]  Bye-bye.
[2400.24 --> 2406.26]  All right.
[2406.38 --> 2408.38]  That is Practical AI for this week.
[2408.72 --> 2416.96]  If this is your first time listening, subscribe now at practicalai.fm or just search for Practical AI in your favorite podcast app.
[2417.08 --> 2417.68]  We're in there.
[2417.96 --> 2421.10]  And if you're a longtime listener, please do share the show with your friends.
[2421.10 --> 2424.14]  It is the best way you can help Practical AI succeed.
[2424.60 --> 2431.68]  Thanks again to Fastly for shipping our shows super fast all around the world, to Breakmaster Cylinder for the Beats, and to you for listening.
[2431.92 --> 2432.62]  We appreciate you.
[2432.96 --> 2434.08]  That's all for this week.
[2434.22 --> 2435.32]  We'll talk to you again next time.
[2435.32 --> 2449.32]  Bye-bye.
[2449.32 --> 2449.66]  Bye-bye.
