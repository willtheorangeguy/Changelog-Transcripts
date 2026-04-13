[0.00 --> 10.02]  Welcome to Practical AI.
[10.44 --> 17.50]  If you work with artificial intelligence, aspire to, or are curious how AI-related technologies
[17.50 --> 20.78]  are changing the world, this is the show for you.
[21.46 --> 26.34]  Thank you to our partners for helping us bring you practical AI each and every week.
[26.34 --> 31.32]  Fastly.com, fly.io, and typesense.org.
[56.34 --> 57.22]  Is everywhere.
[57.92 --> 62.90]  And it might be time for us to start questioning, is AI our friend or our worst enemy?
[63.30 --> 67.82]  And that's the focus of the three-part season opener of the award-winning podcast called
[67.82 --> 68.64]  Trace Route Podcast.
[69.28 --> 72.96]  You can listen and follow the new season of Trace Route starting November 2nd on Apple,
[73.14 --> 75.38]  Spotify, or wherever you get your podcasts.
[75.74 --> 79.08]  And this show is all about the humanity and the hardware that shapes our digital world.
[79.30 --> 83.98]  In every episode of Trace Route, a team of technologists seeks to untangle the complex
[83.98 --> 85.94]  question, who shapes the internet?
[86.38 --> 91.48]  Seasons one and two gave us a crucial understanding of the inner workings of technology while revealing
[91.48 --> 92.94]  the human element behind tech.
[93.30 --> 97.78]  And season three tackles not just AI questions, but also how can we use technology to preserve
[97.78 --> 98.24]  the earth?
[98.42 --> 100.54]  Who influences the technology that gets made?
[100.88 --> 103.46]  And what happened to the flying cars we were promised?
[103.88 --> 107.92]  I think it's safe to say that the future of AI is both exciting and terrifying.
[107.92 --> 112.22]  So it's interesting to hear the perspectives of experts in the field.
[112.60 --> 117.40]  Listen and follow this new season of Trace Route starting November 2nd on Apple, Spotify,
[117.70 --> 119.60]  or wherever you get your podcasts.
[119.60 --> 145.62]  Welcome to another episode of Practical AI.
[145.98 --> 147.84]  This is Daniel Whitenack.
[147.84 --> 152.42]  I am a data scientist and founder at Prediction Guard.
[152.64 --> 158.06]  And I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed
[158.06 --> 158.40]  Martin.
[158.82 --> 164.14]  Today's a fully connected episode with just the two of us where we're trying to keep you
[164.14 --> 169.44]  updated with everything that's happening in the AI community and maybe learn some things
[169.44 --> 175.16]  ourselves that help us level up our own understanding of these topics and yours as well.
[175.16 --> 177.18]  So, yeah.
[177.32 --> 178.34]  How are you doing, Chris?
[178.38 --> 179.58]  Are you keeping fully connected?
[180.06 --> 181.44]  I'm definitely fully connected.
[181.64 --> 183.76]  And there's been a lot to fully connect to this week.
[184.38 --> 189.46]  You know, there was a bit of homework going into this episode here.
[189.82 --> 191.12]  So it's been interesting.
[191.28 --> 192.34]  We got a lot to talk about today.
[192.34 --> 195.36]  Yeah, there's a lot happening in the world.
[195.70 --> 201.06]  Normally in these episodes, or at least it feels like in recent times in these episodes,
[201.06 --> 205.66]  there's been a lot of updates on new models and other things like that.
[205.92 --> 207.96]  And that's still happening.
[207.96 --> 212.78]  So, you know, things like Mistral and other models have come out.
[212.94 --> 219.08]  But I think the interesting thing maybe that I've seen people talking about this week in
[219.08 --> 225.40]  particular circles back to government interactions with the AI community.
[225.40 --> 232.54]  And in particular, the White House here in the US, the White House, the president's executive
[232.54 --> 239.64]  order on safe, secure and trustworthy artificial intelligence, which is kind of timed interestingly
[239.64 --> 241.28]  with other things as well.
[241.46 --> 246.00]  But yeah, I know that you're very in tune with the public sector.
[246.38 --> 251.64]  Chris, are you seeing a lot of discussion of this in your circles?
[252.22 --> 253.44]  Yeah, we are.
[253.88 --> 257.94]  I would say that we're actually, as we parse through it, and we'll talk about the different
[257.94 --> 262.62]  sections and stuff, I would say a lot of the stuff that would affect my day job in the defense
[262.62 --> 264.92]  and intelligence world, we're already kind of doing.
[265.44 --> 266.56]  It's not kind of doing.
[266.60 --> 267.96]  We're already doing a lot of that stuff.
[268.06 --> 272.88]  And so there's a lot of specifics in this executive order, but it's not starting a new
[272.88 --> 275.08]  process for us in that world.
[275.54 --> 277.92]  It's something we've been working on for quite a lot, for years.
[278.24 --> 279.50]  So it's interesting.
[279.50 --> 284.32]  I was pleasantly surprised with this executive order because we've talked many times on this
[284.32 --> 290.60]  podcast about the fact that how long it's taken for governments to start getting a bead
[290.60 --> 295.98]  on these AI issues and what does regulation mean and who's going to participate and how
[295.98 --> 297.64]  you're going to do it and all this kind of stuff.
[298.06 --> 299.18]  We've been saying that for years.
[299.64 --> 306.92]  And finally, on Monday of this week, as we're recording, Monday, October 30th, 2023, we got
[306.92 --> 308.08]  this executive order issued.
[308.62 --> 313.64]  And then I believe we got the Bletchley declaration issued as well later in the week.
[314.28 --> 315.48]  You want to talk about that a little bit?
[315.96 --> 316.72]  Yeah, sure.
[316.84 --> 317.94]  It might be useful.
[318.48 --> 321.04]  I know we have a wide range of listeners.
[321.48 --> 329.02]  And if I'm being honest, even myself, we had a friend that just became a U.S. citizen
[329.02 --> 330.16]  the other week.
[330.68 --> 331.30]  And congratulations.
[331.30 --> 331.98]  Yeah.
[332.18 --> 337.22]  Talking through things with him is like, of course, it's fresh in his mind, but all of
[337.22 --> 343.54]  these ways about how our government works and the various ways in which things can be
[343.54 --> 346.74]  legally enacted can be quite confusing.
[346.74 --> 353.02]  So maybe before we jump into things, let's maybe just touch on an executive order.
[353.02 --> 359.96]  What might that imply and how it may be different than certain things that have preceded it?
[360.02 --> 366.84]  Because there's been statements on AI and government thinking about AI in the past here in the U.S.
[366.84 --> 372.26]  But from your perspective, what makes an executive order maybe different than some of the things
[372.26 --> 373.36]  that we've seen in the past?
[373.62 --> 373.82]  Sure.
[373.98 --> 379.04]  So noting that I am most certainly not a constitutional attorney or any such thing,
[379.26 --> 381.46]  just a dude who likes AI.
[381.46 --> 383.28]  I would still vote for you, Chris.
[383.50 --> 385.08]  Oh, that's really nice of you.
[386.26 --> 392.64]  But an executive order, in short, and I'm sure if we have listeners that say I'm slightly
[392.64 --> 394.18]  off, they can correct us on this.
[394.58 --> 401.12]  But the president of the United States can issue an executive order, which is a legal device,
[401.56 --> 404.82]  which essentially has the effect of law.
[405.20 --> 407.80]  It can be overridden a couple of different ways.
[407.80 --> 412.00]  The U.S. Congress can override it by passing an actual law.
[412.14 --> 417.64]  So if an executive order is in conflict with a law that is passed in Congress, that law
[417.64 --> 419.00]  in Congress will trump that.
[419.50 --> 425.12]  And in addition, an executive order, I believe, can be the U.S. Supreme Court can also override
[425.12 --> 426.64]  it on constitutional basis.
[427.14 --> 432.78]  But unless one of those two things happen, my understanding is executive orders otherwise
[432.78 --> 436.92]  have the effect for all practical purposes of law in the United States of America.
[436.92 --> 437.60]  Yeah.
[437.74 --> 446.02]  And apparently these actions are, quote, the most sweeping actions ever taken to protect
[446.02 --> 449.20]  Americans from the potential risks of AI systems.
[449.80 --> 455.60]  It's funny how, you know, the use of adjectives in government has come quite interesting over
[455.60 --> 455.98]  the years.
[456.10 --> 462.16]  But this is the most sweeping actions ever taken to protect Americans from the potential
[462.16 --> 463.42]  risks of AI systems.
[463.42 --> 465.38]  There are some interesting ones.
[465.50 --> 472.20]  And I think what might be interesting about at least a couple of these is the way that
[472.20 --> 480.36]  they might influence the AI industry in the U.S. in particular, but also some ways that
[480.36 --> 488.24]  government agencies and other entities might become involved in the AI world.
[488.24 --> 494.30]  So I guess before we jump into the specifics, you also mentioned the Bletchley decision.
[494.74 --> 496.28]  What's that for our listeners?
[496.52 --> 499.14]  How might that relate to things going on?
[499.60 --> 499.72]  Sure.
[499.86 --> 501.56]  So there was a summit.
[501.72 --> 507.80]  It was called the AI Safety Summit that took place on November 1st and 2nd of 2023, which
[507.80 --> 510.32]  was just a couple of days ago this week.
[510.32 --> 516.22]  They issued what they call a policy paper, which was the Bletchley declarations by countries
[516.22 --> 518.70]  attending the AI Safety Summit on that date.
[519.12 --> 520.56]  And it's fairly short.
[520.68 --> 521.96]  It's a few paragraphs long.
[522.30 --> 528.84]  And my understanding, not being a legal mind, is that it would not be binding in any way legally.
[529.24 --> 531.66]  But there's a number of countries listed.
[531.78 --> 537.38]  There's a couple of dozen that attended, including the United States, United Kingdom, and a lot of
[537.38 --> 542.60]  other countries around the world that basically said, we're acknowledging, the short of it
[542.60 --> 545.04]  is we're acknowledging AI safety is important to us all.
[545.20 --> 547.62]  It's by definition an international concern.
[548.02 --> 553.46]  And that the way to deal with these concerns going forward is for us to all work together
[553.46 --> 558.00]  and share information and such as that without reading the whole thing to the audience on
[558.00 --> 559.40]  the show, which I don't think we have time for.
[559.86 --> 559.96]  Yeah.
[560.30 --> 562.26]  We will link these things in the show notes.
[562.56 --> 562.98]  Absolutely.
[563.24 --> 564.08]  It's a good thing.
[564.18 --> 565.82]  I agree with everything they said.
[565.82 --> 570.80]  Uh, and it's a good, uh, kind of a kumbaya of saying we need to work together, but it's
[570.80 --> 573.68]  otherwise, you know, it's just saying, Hey, let's go do these things.
[574.16 --> 577.54]  That's very important because it is indeed an international concern.
[577.96 --> 579.44]  I'm definitely applauding that.
[579.58 --> 583.06]  I've been more focused a little bit on the executive order simply because it's binding
[583.06 --> 588.24]  having the effect of law and it's, and we'll talk about the details, but it gets quite
[588.24 --> 590.06]  specific in the executive order itself.
[590.24 --> 593.88]  There's a fact sheet that kind of gives you a high level and it doesn't give a lot of the
[593.88 --> 597.86]  detail and I read the fact sheet first and I was a little bit, I was like, okay, that's
[597.86 --> 599.38]  all great fluffy stuff.
[599.66 --> 604.84]  But when I read the executive order afterwards, it gets down to who's responsible for what,
[604.84 --> 607.32]  how long they have to do it and what they have to do it.
[607.72 --> 614.08]  And there's a bunch of specific, uh, results expected or, or standards applied that clearly
[614.08 --> 617.88]  were people from the AI community that were very, very knowledgeable.
[617.88 --> 623.30]  So it wasn't a, uh, a political only group of people that, that did this.
[623.34 --> 626.14]  They, they obviously had expertise available to them.
[626.14 --> 632.24]  So I was, I ended up being more impressed than I expected with what they came up with.
[632.82 --> 639.30]  I haven't done all of the research and I don't know if it's even published anywhere about who
[639.30 --> 646.90]  was involved in the process of developing this, but we can go through some of the, the high
[646.90 --> 647.94]  level things.
[647.94 --> 650.18]  And there's a few really helpful.
[650.72 --> 652.78]  Uh, so there's the fact sheet that you mentioned.
[652.78 --> 659.48]  There's also some good articles that I've been looking at over the past days that give some
[659.48 --> 662.98]  summary information that might be relevant for people as well.
[663.14 --> 668.20]  Uh, like the MIT, um, tech review has an article and some other ones.
[668.40 --> 675.56]  If we don't dive into the, the specific wording quite yet, and I just look at kind of the high
[675.56 --> 680.28]  level, what people are, are saying about it, what's standing out to them about it.
[680.28 --> 688.08]  One thing that I see really driven home is the real focus on safety and in particular safety
[688.08 --> 694.70]  and security and the real focus on kind of like labeling and water marking the output of
[694.70 --> 702.74]  AI systems, which I think if I'm understanding right, is framed within the executive order as
[702.74 --> 714.10]  a safety thing in terms of protecting our citizens from potentially fraudulent or harmful material
[714.10 --> 721.16]  that might come out of AI models, as well as giving, whether it's entities related to defense
[721.16 --> 728.50]  or education or whatever, the ability to identify and discriminate between AI generated assets or
[728.50 --> 734.32]  content or text and non AI generated, or I guess human generated.
[734.66 --> 738.60]  You know, we're talking about a specific point here in it, but it takes both sides of that.
[738.72 --> 746.68]  It both issues, uh, the directive that you, in essence, you must identify AI generated content
[746.68 --> 753.36]  so that you can't have deceptive representation there, but it also issues the appropriate government
[753.36 --> 759.06]  agencies to come up with mechanisms by which they may detect people who are not subscribing to that
[759.06 --> 763.98]  directive or foreign. Obviously there are, uh, all the other countries in the world and they are not
[763.98 --> 770.76]  held by our executive order. So the means to detect all that, but I also would say that that's not a new
[770.76 --> 773.94]  idea to the DOD and intelligence community.
[773.94 --> 782.84]  And am I understanding this right, Chris, that the executive order would put the obligation on certain
[782.84 --> 793.96]  government entities to figure out how to enforce this mandate on the other organizations, companies,
[794.14 --> 799.46]  entities, teams that are within their jurisdiction? Is that, is that a good way to put it or am I
[799.46 --> 805.20]  misunderstanding? Yeah, it, it leaves a lot undone. So, um, and at some point we probably should jump
[805.20 --> 810.90]  in and kind of hit the highlights on what they were, but it basically puts the burden on various,
[810.90 --> 817.32]  uh, agency leaders to come to, it's a, it'll outline what they have to accomplish and when it
[817.32 --> 823.02]  must be accomplished by, in some cases, what the output of that is, but it doesn't tell them how to
[823.02 --> 829.12]  accomplish all that. And I have yet to see any place where it ascribed any budget to any of those
[829.12 --> 835.70]  items. So there are strengths. Uh, it was good thinking in many areas. Uh, but the dollars to,
[835.90 --> 842.24]  uh, that, that would go into making some of these things happen, I did not see assigned. So positives
[842.24 --> 847.84]  and negatives. When you read this, when you see this coming through and how things have trended over
[847.84 --> 856.40]  the recent years with respect to the government's thinking on AI, is this like taking us up from a level
[856.40 --> 865.90]  two of priority in government and action up to, you know, 10 or how do you see this as escalating
[865.90 --> 872.14]  the kind of involvement from the government in the AI industry in terms of practical things that we'll
[872.14 --> 878.52]  see in, let's say the coming year? Oh, I, I would say that they don't have a choice, uh, given that
[878.52 --> 884.74]  it's now in an executive order and it directs them with timelines and specifics on that. If I was
[884.74 --> 891.50]  leading a federal agency that was being called out to do this, I would probably be scrambling and
[891.50 --> 896.40]  trying to figure out who I had and who I could get and where I was going to pull the money from
[896.40 --> 901.24]  to accomplish those things. And I'm hoping maybe a listener knows that there's budgets described that
[901.24 --> 906.44]  we haven't heard about yet. And that would be a good news. They would have to, to juggle a little
[906.44 --> 910.04]  bit in terms of their priorities to make some of these things happen. But I think it's good.
[910.04 --> 916.32]  It forces it right up to the top of our list of things to, you know, the government could, uh,
[916.44 --> 920.58]  could happen. And it, I don't think it was going to happen from industry alone. We've watched for
[920.58 --> 926.80]  years as commentators on the industry every week, we've seen individual companies kind of do their
[926.80 --> 931.28]  own thing. Uh, they kind of compete with each other because there's a bit of a marketing tinge to AI
[931.28 --> 937.06]  safety as well, but nothing that has ascribed the entire industry, uh, universally. And so this will
[937.06 --> 949.94]  clearly do that with external standards. This is a changelog news break. Hugging face released a
[949.94 --> 956.92]  distilled variant of whisper for speech recognition. It's English only and optimized to the hilt,
[956.92 --> 965.08]  which resulted in running six times faster while being 49% smaller and performing within 1% word error
[965.08 --> 970.24]  rate from the original model. It's designed to be a drop-in replacement. And the hugging face team
[970.24 --> 976.14]  cites five reasons why you might use it faster inference, robustness to noise, robustness to
[976.14 --> 982.46]  hallucinations designed for speculative decoding and permissively MIT licensed. This looks great,
[982.56 --> 988.74]  but I'm still waiting on speaker diarization. You just heard one of our five top stories from
[988.74 --> 994.74]  Monday's changelog news. Subscribe to the podcast to get all of the week's top stories and pop your email
[994.74 --> 1000.68]  address in at changelog.com slash news to also receive our free companion email with even more
[1000.68 --> 1006.80]  developer news worth your attention. Once again, that's changelog.com slash news.
[1011.58 --> 1018.18]  Okay, Chris, let's dive into some of these specifics, which I think are really quite interesting.
[1018.18 --> 1026.60]  The one that I thought was probably most interesting to me, although I think the others have both good
[1026.60 --> 1032.98]  and interesting implications, as my wife and her business would say, there's wins and opportunities.
[1033.98 --> 1041.00]  But I think one of the ones that stood out to me was, I'll just read the wording here and we can talk
[1041.00 --> 1048.22]  about it and in some of the wider implications. But one of the things is a requirement that developers,
[1048.22 --> 1054.60]  which is interesting to me because it's, I'm an AI developer, I guess, a requirement that developers
[1054.60 --> 1064.12]  of the most powerful AI systems share their safety test results and other critical information with the
[1064.12 --> 1067.56]  US government. How does that strike you? What are your thoughts?
[1067.56 --> 1074.74]  Depending on the model and the specifics of that, it will often be the US Department of Commerce that's
[1074.74 --> 1081.20]  receiving those. In some cases, it will be military or intelligence, depending on the nature of what
[1081.20 --> 1086.82]  the concern is and what the model can do. But that will have to be created. It doesn't exist today,
[1086.84 --> 1091.46]  to the best of my knowledge. If I was leading commerce, I'd be going, okay, how are we going to receive
[1091.46 --> 1096.12]  this information and store it? Because they're probably going to be getting quite a lot of data
[1096.12 --> 1101.08]  coming at them with the amount of development in this area. That's one of the things that
[1101.08 --> 1106.68]  certainly here in the US, we're going to have to learn how to do. Because as of now, once the
[1106.68 --> 1112.48]  timeline, I don't have in front of me how long they have to put that into place. But after a certain
[1112.48 --> 1118.14]  number of days, it will be required by law. If we're specific on the thing that would be required
[1118.14 --> 1125.60]  by law, if I'm understanding this right, it would be someone that is developing a new,
[1126.60 --> 1131.68]  maybe one thing, I don't know if you've seen this, maybe I just missed it. I'm not sure if this would
[1131.68 --> 1137.84]  be new in the sense of training from scratch or new in the sense of a fine-tuned model. But those that
[1137.84 --> 1147.08]  would release large models, like in recent weeks, we've seen Mistral and Llama 2 and Zephyr and all these
[1147.08 --> 1153.34]  models coming out, the models that are significantly large, like that foundation models that are
[1153.34 --> 1158.32]  significantly large, as those are released, after they're released, before they're released,
[1158.54 --> 1164.76]  maybe we can talk about that, that the people that are producing those models, the teams,
[1164.92 --> 1171.54]  the developers that are producing those models perform some sort of red teaming to probe the models
[1171.54 --> 1179.42]  in terms of potentially harmful outputs and kind of behavioral tests and perform risk assessments
[1179.42 --> 1187.26]  that would be, you know, gathered in some sort of coherent way and shared with the US government.
[1187.52 --> 1193.96]  One of the interesting pieces of this part of the executive order in particular, if I'm understanding
[1193.96 --> 1199.22]  right, is that it falls under the authority of the Defense Production Act. Correct.
[1199.22 --> 1206.98]  Which I think in addition to the executive order status might bring this point maybe a little bit
[1206.98 --> 1214.06]  higher up in terms of firm legal footing. Again, not an expert in that thing, but that's my
[1214.06 --> 1219.52]  understanding from what I've read. Yeah. And as a non-expert, but the Defense Production Act,
[1220.38 --> 1225.02]  in case listeners may recognize that because they've been hearing about it a lot over the last year,
[1225.02 --> 1232.88]  because it's been a point of, in the Russian invasion of Ukraine, it has been repeatedly cited
[1232.88 --> 1240.34]  as a mechanism that the US government can use to increase production to support that effort,
[1240.42 --> 1247.24]  our allies, the Ukrainians. And so you may have heard that before. And from that, I know as a non-attorney,
[1247.36 --> 1255.00]  non-legal mind, that it gives the US government broad powers on requiring commercial companies,
[1255.02 --> 1259.84]  companies in the United States, or that we do business with, to meet a certain set of criterias.
[1259.98 --> 1265.50]  And there are things that they can be told, you must go do this on, because it's in the interest of
[1265.50 --> 1270.92]  our national security. And so it's a fairly sweeping thing, is my understanding. Since it has been
[1270.92 --> 1275.84]  referenced here, I agree with you, you not only have executive order, but you also have reference
[1275.84 --> 1279.10]  to a fairly strong point of law from Congress.
[1279.10 --> 1288.22]  One of the interesting takes that I saw on this is, this is just a blog post that I'll link in the show notes.
[1288.36 --> 1293.10]  But the comment in the blog post was that this might be one of the things that would kind of
[1293.10 --> 1302.48]  lead to a firming up of the players within the AI market as we see it. Because not only is now there a
[1302.48 --> 1310.18]  computational data infrastructure burden on those who want to produce these large models, but now
[1310.18 --> 1319.42]  there's more of a regulatory burden that would actually be an additional kind of step here in
[1319.42 --> 1326.06]  terms of being a player in the foundation model space. Now, there's irony to that, by the way,
[1326.06 --> 1331.90]  and that they explicitly note they're trying to address equity in the executive order. But by adding
[1331.90 --> 1335.58]  the regulatory burden, that will be exclusionary.
[1336.62 --> 1342.42]  Correct. Yeah, you don't get anything for free, that's for sure. So this will be interesting.
[1343.08 --> 1351.12]  It's hard for me to think that the progress will slow very quickly around releases of these models.
[1351.12 --> 1358.28]  What is very interesting to me is how they will end up deciding, like if I pull down
[1358.28 --> 1368.20]  llama two, and use a small data set that I have access to, to fine tune it, and then I release that
[1368.20 --> 1376.52]  as another foundation model that people can use, well, you know, at what point, so I am modifying the
[1376.52 --> 1383.04]  weights, right? At what point between there and training from scratch, which, you know, even large
[1383.04 --> 1389.54]  models, I don't think often are, they might start from a starting point with their weights in certain
[1389.54 --> 1395.88]  cases. But yeah, at what point in there are you really a developer of a significantly large model?
[1395.88 --> 1401.90]  Because both of these models are large. When is it adaptation? When is it fine tuning? When is it
[1401.90 --> 1410.16]  training or releasing building as the executive order says? So yeah, that that's all kind of mushy
[1410.16 --> 1417.28]  in my mind, I think. Yeah, they do attempt to kind of address that one of the there's a section 4.2
[1417.28 --> 1424.10]  ensuring safe and reliable AI. And they talk about a timeframe. And this is one of those that calls out
[1424.10 --> 1429.94]  the Defense Production Act specifically. And within 90 days, there's a set of things that are being
[1429.94 --> 1435.44]  required, which is a very short timeline, you know, when you think about it. Part of that is they have
[1435.44 --> 1440.88]  a set of criteria, which is certainly not comprehensive, as to your point, just a moment
[1440.88 --> 1446.24]  ago, it's better than I expected, but it's not entirely sufficient. There's a lot of nuanced
[1446.24 --> 1452.92]  questions, as you just raised. I noticed that one of those, they talk about the quantity of computing
[1452.92 --> 1461.28]  power used for training. And they have picked, interestingly, 10 to the 26 integer or floating
[1461.28 --> 1467.30]  point operations for kind of as a general point of computation, it's like a threshold. And if you're
[1467.30 --> 1473.42]  above that, you're kind of in that large range that they are particularly focusing on, they have reduced
[1473.42 --> 1479.48]  that down to 10 to the 23rd integer or floating point operations for models that are based primarily
[1479.48 --> 1485.32]  for biological sequencing and things like that. They have some other aspects in, but they have an
[1485.32 --> 1490.10]  interesting threshold that they call out in the in the executive order. So you know exactly what's
[1490.10 --> 1496.28]  going to happen here, Chris, is that whatever that number ends up being so it's just like in in
[1496.28 --> 1506.52]  so the town where my dad grew up in in Kentucky is a actually still is, I believe, a dry county,
[1506.52 --> 1515.86]  meaning in the US, this is where you can't actually purchase packaged liquor in in a liquor store.
[1516.16 --> 1523.52]  Of course, what happens then is just on the edges of the county, you have these at the sign where the
[1523.52 --> 1528.92]  county ends, there's like 14 liquor stores, right? Yeah, we'll see something similar here, right? What
[1528.92 --> 1536.06]  we've been choosing our numbers of parameters and such 7 billion 13 billion for various reasons for our
[1536.06 --> 1541.48]  models. What's going to happen is people are going to get really, really good at training models right
[1541.48 --> 1546.60]  under that threshold, which is 10 to the 25th will be the magic number going forward. Yeah, which,
[1546.78 --> 1553.20]  you know, I think it could actually have a, even though that's kind of gaming the system,
[1553.20 --> 1559.00]  it could actually have a really nice effect that instead of us trying to always think about
[1559.00 --> 1566.54]  more data, bigger model as the way to incrementally improve. This does put a burden on those that want
[1566.54 --> 1573.14]  to operate at the lower level under the threshold of regulation, the burden to say, hey, what if we're
[1573.14 --> 1579.42]  creative, either in our model architecture, or the way we train it, or the way that we fine tune or
[1579.42 --> 1585.80]  whatever that ends up being, to actually do more with less, which I think overall will be a good,
[1585.80 --> 1592.06]  would be a good thing. And, and, you know, academia is already thinking about these things with things
[1592.06 --> 1597.64]  like the baby LM workshop and other things like that. So I think that could actually have a follow
[1597.64 --> 1602.96]  on effect. That's quite positive for the model landscape. You'll have a set of players that
[1602.96 --> 1607.20]  remain out of necessity, you know, they, they must play up in that area, because we're, you know,
[1607.20 --> 1613.90]  the large, the true LLM range isn't going to go away. But that will also be dominated by large players
[1613.90 --> 1618.96]  who are already doing regulatory stuff. Anyway, maybe they weren't in this, but they're accustomed
[1618.96 --> 1624.38]  to that. It is exclusionary to those large, you know, things like cloud providers and such will be
[1624.38 --> 1630.78]  doing that. But you'll probably have a whole range of mid sized players that are below the Amazons,
[1630.94 --> 1636.68]  Googles and Microsofts of the world and the open AIs of the world that will play in that just below
[1636.68 --> 1642.68]  that and, and, and build foundational models. It may be that, yeah, as you said, they'll, it'll be
[1642.68 --> 1647.74]  interesting to see what kind of innovations come from there. And one other question that I have
[1647.74 --> 1656.08]  coming out of that is, how do I know that I hit the 10 to the 26? And how do you, along with this
[1656.08 --> 1664.50]  sort of restrictions or legal implications throughout the executive order, this kind of naturally brings
[1664.50 --> 1670.34]  up a lot of questions. Like they also talk about watermarking, which we'll, we can talk about here in a
[1670.34 --> 1675.12]  second, but the general thought is like, whether you're talking about this computational power,
[1675.30 --> 1684.46]  red teaming, behavioral tests, watermarks, labeling, you need standards and tools and tests to help you
[1684.46 --> 1690.14]  ensure that you can do these things. Like how do I know when I hit that threshold? How do I watermark
[1690.14 --> 1697.10]  things, et cetera, et cetera. And so one of the other things that's drawn out right away is the
[1697.10 --> 1702.94]  developing of standards, tools, and tests to ensure that AI systems are safe, secure, and trustworthy.
[1703.58 --> 1710.48]  And this specifically calls out the national Institute of standards and technology or NIST that
[1710.48 --> 1717.36]  you might've heard of before. Cause they have like one of the most precise clocks to, you know,
[1717.36 --> 1723.48]  help keep the standard of time and the most precise weights. Yeah. The most precise, like,
[1723.48 --> 1731.30]  this is exactly what a kilogram is. And yeah, I actually in my, uh, undergrad, when I was doing
[1731.30 --> 1737.68]  research, I did research at NIST with one of our collaborators. So we were theoretical, they were
[1737.68 --> 1745.06]  experimental. And I think mostly all I succeeded in doing was spilling a bunch of carbon nanotubes on
[1745.06 --> 1751.68]  the floor. Um, not very good at experiment, but that's what they're experts in minus the occasional
[1751.68 --> 1759.34]  intern that spills carbon nanotubes on the floor, but they're specifically called out to help or set
[1759.34 --> 1766.30]  the rigorous standards for what's phrased in the executive order, extensive red team testing to
[1766.30 --> 1771.50]  ensure safety before public release. What are your thoughts on this, Chris? This goes back to something
[1771.50 --> 1777.36]  I mentioned earlier. There's a lot of figuring out the how that's undetermined. So, you know, you have,
[1777.36 --> 1782.86]  uh, clearly some bright, uh, AI minds that help construct the executive order, but they've left
[1782.86 --> 1787.44]  wide open, you know, what that means and, you know, what is red teaming? What is red teaming
[1787.44 --> 1790.76]  trying? They hit some things that red teaming should be trying to do at a very high level,
[1790.76 --> 1797.66]  but it's up to NIST and the, the department of commerce to come up with, you know, what the specifics
[1797.66 --> 1802.26]  are on that. And I think we're all going to be learning. I think the key thing that I would take away
[1802.26 --> 1808.16]  from that is that this executive order is the first of many things to follow over the next year
[1808.16 --> 1813.62]  from various agencies, uh, as they are trying to fulfill the executive orders, uh, uh, intent.
[1814.30 --> 1820.78]  Well, Chris, the next thing I see in here is biological materials, which I don't necessarily
[1820.78 --> 1826.70]  think about that much, even though I'm made up of biological materials, I guess I don't consider
[1826.70 --> 1835.58]  my own, uh, biological self very much, but they talk about protecting against the risks of using AI
[1835.58 --> 1844.46]  to engineer dangerous biological materials. What is a dangerous biological material? I guess a
[1844.46 --> 1849.46]  bioweapon. Is that what we're talking about here? It would be bioweapons. And, and it could be something
[1849.46 --> 1855.04]  that we've all heard about when we were in the height of COVID, there was the, uh, all the theories
[1855.04 --> 1861.58]  about whether or not it had been created in a lab in China or elsewhere and such as that, you know,
[1861.62 --> 1867.18]  and so it could be a weapon by design. It could just be a virus. It could be lots of different things.
[1867.32 --> 1874.80]  There are a lot of, uh, international laws and domestic laws against these things, but we also have
[1874.80 --> 1880.60]  actors around the world who don't necessarily subscribe to the same values. And so it's still something
[1880.60 --> 1886.50]  that, uh, that, uh, the intelligence and defense communities of both the U S and our allies spend a
[1886.50 --> 1893.90]  lot of time thinking about how to address and defend against. Um, though we follow those laws that our
[1893.90 --> 1904.44]  adversaries may not. So, yeah. Yeah. People might be wondering, well, how might you practically think
[1904.44 --> 1910.26]  about protecting against the development of dangerous biological materials with AI and we've
[1910.26 --> 1916.52]  had previous shows. We can try to find them and link them in the show notes about using AI to find
[1916.52 --> 1923.06]  new drugs or something like that. Right. Yep. Well, a lot of those projects, whether it be those kind of
[1923.06 --> 1932.60]  pharma related projects or academic projects related to biology and AI or AI and life sciences sort of
[1932.60 --> 1940.20]  overlap, a lot of those do have some sort of federal funding behind them, whether that be NIH or NSF,
[1940.36 --> 1947.08]  these sorts of grants. And so one of the things that's called out here is, Hey, if you want a grant,
[1947.20 --> 1955.68]  if you want our money, then you have to agree to establish these standards X, Y, Z, which to my
[1955.68 --> 1961.18]  understanding are not specified in this executive order, but it's saying we will create these standards
[1961.18 --> 1970.08]  that will be standards and requirements to receive federal funding for biological research with AI.
[1970.28 --> 1974.80]  Or I don't know, that's probably also to be determined like how to categorize that, but.
[1975.18 --> 1979.00]  And we're talking a lot about biological, but they don't just address biological in it.
[1979.30 --> 1984.08]  There's kind of some special stuff on biological, but then they also address what they refer to
[1984.08 --> 1990.38]  repeatedly as CBRN, which is short for chemical, biological, radiological, or nuclear weapons.
[1990.98 --> 1996.70]  And so the kind of civilian research on the biological side, but there's also the military
[1996.70 --> 2003.20]  side under the CBRN acronym that they're addressing on those. And there's a lot of concern expressed
[2003.20 --> 2010.26]  throughout the executive order about all of those being enhanced by AI in terms of finding solutions
[2010.26 --> 2015.70]  that where you're using models. How do you handle those both domestically under this law? And how do
[2015.70 --> 2021.68]  we direct agencies to help keep us safe from adversaries that might not respect that?
[2022.34 --> 2029.40]  Yeah. There were two things that I was seeing in the kind of news and commentary on this that
[2029.40 --> 2036.70]  were standing out. One we've already talked about, which is related to the requirement for the quote,
[2036.70 --> 2044.44]  most powerful AI systems to share their, their safety test results. The other one that stood out,
[2044.50 --> 2052.24]  or it seemed to stand out to many people was the protections that are put in place for
[2052.24 --> 2061.52]  establishing ways to detect and label AI generated content. So this would be images that are generated
[2061.52 --> 2067.88]  from, you know, text to image or text to video systems or audio that's maybe synthesized,
[2067.88 --> 2075.78]  which is continually getting better or voice clones, that sort of thing. Or also text, text would fall
[2075.78 --> 2081.68]  into this category too, around misinformation and that sort of thing that you might want to filter out.
[2081.68 --> 2088.20]  Or maybe if you're one of those teachers that want to prevent your students from using chat GPT to
[2088.20 --> 2095.52]  generate their essay, then using or finding ways to detect AI generated content and enforcing those
[2095.52 --> 2104.74]  in certain context. That's kind of my general reading of this stuff. And I think what I was seeing was
[2104.74 --> 2110.56]  there, there's a good bit of positive response to this, even from many in the AI community that
[2110.56 --> 2117.80]  recognize, yeah, this is an important piece of what we will need to do moving into the future in terms of
[2117.80 --> 2125.48]  having to label things and needing to be able to discriminate between these things. But also the
[2125.48 --> 2132.56]  recognition from those in the AI community that this is still very much a topic of research, which is
[2132.56 --> 2138.18]  not figured out yet. Totally. And I think that's one of the, it's interesting, I think that will be a
[2138.18 --> 2145.50]  big impact because that will affect so many industries that are not necessarily ready for, you know,
[2145.50 --> 2149.82]  they've kind of said, ah, we can make some money, we can generate content. And we've all been seeing
[2149.82 --> 2155.68]  that online. But it's coming from industries where they have not had the burden of responsibility for
[2155.68 --> 2161.84]  it. I think certainly all of us that are in the AI world have used different models to generate texts
[2161.84 --> 2166.86]  and stuff. And, you know, it started the first time is kind of cool. But then you realize, wow, this is an
[2166.86 --> 2171.94]  amazing business capability. But now it's an amazing business capability with a fairly significant
[2171.94 --> 2177.18]  responsibility attached to it. It will be interesting thing, you know, things like the marketing and
[2177.18 --> 2182.70]  branding industries, which I once upon a time I was in, will have to figure out a way to do that,
[2182.70 --> 2187.72]  and still serve their clients in that particular industry. Because if you just have everything as AI
[2187.72 --> 2193.44]  generated content, that will affect how people perceive the content you just generated, trying to
[2193.44 --> 2198.96]  satisfy your client, you know, in that particular industry. So there's a lot of nuance that's very
[2198.96 --> 2202.20]  industry specific, that's going to have to happen for that.
[2202.20 --> 2209.78]  Yeah. And I hope that many out there recognize that we need to figure out ways to label this
[2209.78 --> 2216.62]  generated content and track it, even if it's only for practical purposes of like, hey, more and more
[2216.62 --> 2223.04]  of this content is going to get out there. And I don't want to necessarily always be training my next
[2223.04 --> 2231.72]  AI system on AI generated content. Maybe I want human content. But there's a recognition that it is an
[2231.72 --> 2240.12]  active area of research. And there's also a gray area here, right? So if I have chat GPT, write me a
[2240.12 --> 2246.62]  cool blog post, and then I take that out, and I modify a few things. And then I put the paragraph back
[2246.62 --> 2252.02]  in and have it rephrase, and then I take it out, and then I edit some more things. This is a very,
[2252.58 --> 2260.32]  often a very dynamic process. And I think for safety and security and trustworthy AI systems,
[2260.32 --> 2266.70]  we would want that kind of back and forth with a human. But it's not always the scenario where
[2266.70 --> 2274.46]  it's simply human generated content, or it's simply AI generated content. This does get very mushy,
[2274.46 --> 2281.30]  even in automated systems where there's humans post editing machine translations, or there's
[2281.30 --> 2288.92]  humans reviewing analysis that's been generated out of a SQL table, or I don't know, there's all
[2288.92 --> 2296.56]  sorts of scenarios here where there's a lot of gray area. And maybe that's not the focus of this
[2296.56 --> 2302.98]  statement. It might be more these scenarios where you'd want to essentially create a factory of
[2302.98 --> 2309.62]  misinformation that's just pumping out things to Twitter or X. And that's maybe more within what
[2309.62 --> 2310.52]  they're talking about.
[2310.82 --> 2317.02]  I think that working through all those nuances in all these different industries, and I do the same
[2317.02 --> 2323.60]  thing. I write a lot of stuff, and I'll write, and I'll put what I've written into one or more models,
[2323.60 --> 2327.54]  and I'll see what it comes back with, and I'll choose, and I'll take part of this and part of that.
[2327.54 --> 2333.58]  I think a lot of people are doing that. I think that a lot of this will be settled through litigation.
[2334.20 --> 2340.24]  So I think the executive order has given a tremendous boost to the AI litigation industry
[2340.24 --> 2346.92]  that has been flowering over the last few years. I think we'll see far more of these nuanced cases,
[2347.20 --> 2354.56]  these gray areas, decided in court in the next few years. I have mixed feelings about the fact that
[2354.56 --> 2360.28]  it is beyond ability to handle all these cases given the short timelines. I'm glad to see short
[2360.28 --> 2365.54]  timelines instead of many years to get there, especially if they're unfunded. It will be
[2365.54 --> 2370.14]  interesting to see kind of what they come up with. If you're a department head and you have 90 days
[2370.14 --> 2375.96]  to come up with a solution that the executive order requires of you, you probably will not have
[2375.96 --> 2379.76]  solutions for all of these things. So we have some interesting times ahead of us, certainly.
[2379.76 --> 2387.92]  Yeah. And I hope that there's involvement from leaders in the space, large and small. So smaller
[2387.92 --> 2394.42]  companies that are really innovating in some of these things and larger kind of staples of the
[2394.42 --> 2400.28]  industry like Hugging Face and others that would pour into those things. But all of that will require
[2400.28 --> 2407.22]  some sort of, I mean, minimal exchange of money, even if it's just to buy people's time to spend on this,
[2407.22 --> 2410.04]  because there's so many things to work on.
[2410.58 --> 2417.42]  It'll be really interesting. Now that the burden has been placed on American agencies and by extension,
[2417.52 --> 2422.76]  the American people in their industries to comply with all these things, it'll be interesting to see,
[2423.16 --> 2429.74]  you know, we talked at the beginning about the Bletchley Declaration and that intent. And all of these
[2429.74 --> 2435.38]  other countries will presumably come out with their own versions of this. And some will be very similar.
[2435.38 --> 2439.52]  Some may branch out in different ways based on the values and laws of their own countries.
[2440.08 --> 2444.92]  But it will be to see how this works out. And there will also be some countries that refuse to
[2444.92 --> 2451.38]  subscribe to this whatsoever. Not only will they not contribute to this, they may be working very
[2451.38 --> 2457.14]  specifically against it. And we'll have to, in turn, we'll have to have very good capabilities for
[2457.14 --> 2464.12]  detecting when any of these cases that are within this purview of AI safety and security are being
[2464.12 --> 2471.28]  violated by others to an effect that is not good for us. It's late 2023, I suspect, through the end of
[2471.28 --> 2476.48]  the decade will just be absolutely fascinating on how we start sorting through these issues.
[2477.12 --> 2486.86]  Yeah. And to maybe end on a slightly positive note, for those of us that are working in day to day in
[2486.86 --> 2492.72]  this industry, we are the developers of some of these AI systems. You know, we could look at this
[2492.72 --> 2497.66]  and say, oh, there's all these like various intricacies and such that need to be worked out.
[2497.66 --> 2505.32]  But I do think that there's encouragement here in the sense that, hey, some kind of general guidance,
[2505.56 --> 2512.48]  firming up of standards, help in kind of understanding how we might behaviorally test or red team
[2512.48 --> 2519.36]  or assess the risk associated with our models. I think that's a really encouraging thing in many
[2519.36 --> 2525.92]  respects, especially for, I think, the vast number of AI developers out there that do actually want
[2525.92 --> 2534.88]  their systems to be safe, secure and trustworthy. Yes, there's a likely minority of developers out
[2534.88 --> 2542.10]  there that are trying to be nefarious and malicious even in what they're doing with AI, as there always be
[2542.10 --> 2548.66]  with any sort of technology. But I think most of us want to build safe and secure and trustworthy
[2548.66 --> 2554.84]  AI systems. And even if you're doing really good in one of those categories, like you've got your
[2554.84 --> 2561.62]  red teaming down, right, there may be other things that come out through these processes with Nest or
[2561.62 --> 2568.32]  the watermarking tooling or other things that it's hard to be an expert in all those things. So hopefully as
[2568.32 --> 2576.92]  more of this rolls into action, there is money put behind some of it to not only put guardrails around
[2576.92 --> 2581.84]  what we can and can't do, which might be how some people might take this, but actually to give us tools
[2581.84 --> 2588.72]  that will enable us to do more because we know that we're following good practices and best practices and
[2588.72 --> 2594.52]  we're being safe and secure. And of course, yeah, there'll always be a need for research beyond that. But
[2594.52 --> 2600.20]  yeah, I think it's encouraging in that sense. I totally second everything that you just said. This is an
[2600.20 --> 2606.24]  opportunity. There are huge business opportunities in helping people get through regulatory and we see that in
[2606.24 --> 2612.52]  other industries. So this has come about we're hitting regulation and AI for real. Every other time regulation
[2612.52 --> 2618.94]  has come out, there's been whole industries born that helped get through that and services that make it much
[2618.94 --> 2625.74]  easier than it seems today as we are first reading what is to come. So I also would encourage everyone
[2625.74 --> 2633.18]  to try to embrace it. We do need it for safety. The dangers are real. And let's do it for ourselves,
[2633.18 --> 2639.74]  our children, and our larger community. So absolutely, let's go make this thing a good thing.
[2640.54 --> 2647.12]  Yeah. All right, Chris, that's a great way to end and look forward to talking to you more in the future
[2647.12 --> 2651.92]  weeks about increasingly safe, secure and trustworthy AI. Absolutely.
[2651.92 --> 2663.02]  If you enjoy the music you hear on Practical AI, you'll be happy to know we've released two full-length
[2663.02 --> 2669.08]  albums for purchase or streaming. Just search for changelog beats in your music app of choice and
[2669.08 --> 2675.12]  check them out. Volume zero is called Theme Songs, and it includes special remixes in addition to the
[2675.12 --> 2680.80]  classics. And our first volume is called Next Level, featuring many of the video game inspired tracks
[2680.80 --> 2686.10]  you've heard on changelog podcasts over the years. Check us out, changelog beats. Thanks once again to
[2686.10 --> 2693.78]  our partners, Fastly.com, Fly.io, and Typesense.org. That's all for now, but we'll be back with more
[2693.78 --> 2696.02]  practical AI goodness next week.
