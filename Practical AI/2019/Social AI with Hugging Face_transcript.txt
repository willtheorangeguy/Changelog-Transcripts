[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.86]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[15.50 --> 20.12]  This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.24 --> 24.88]  And we're excited to share they now offer dedicated virtual droplets.
[24.88 --> 28.80]  And unlike standard droplets, which use shared virtual CPU threads,
[28.80 --> 32.66]  their two performance plans, general purpose and CPU optimized,
[33.24 --> 35.86]  they have dedicated virtual CPU threads.
[36.18 --> 40.64]  This translates to higher performance and increased consistency during CPU intensive processes.
[41.08 --> 44.98]  So if you have build boxes, CICD, video encoding, machine learning, ad serving,
[45.28 --> 49.76]  game servers, databases, batch processing, data mining, application servers,
[49.98 --> 54.70]  or active front end web servers that need to be full duty CPU all day every day,
[54.92 --> 57.70]  then check out DigitalOcean's dedicated virtual CPU droplets.
[57.70 --> 61.04]  Pricing is very competitive starting at 40 bucks a month.
[61.42 --> 66.54]  Learn more and get started for free with a $100 credit at DigitalOcean.com slash Changelog.
[66.68 --> 69.58]  Again, DigitalOcean.com slash Changelog.
[69.58 --> 86.54]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.98 --> 88.70]  productive, and accessible to everyone.
[89.10 --> 93.62]  This is where conversations around AI, machine learning, and data science happen.
[94.10 --> 98.34]  Join the community and slack with us around various topics of the show at changelog.com slash community.
[98.34 --> 99.52]  Follow us on Twitter.
[99.64 --> 101.12]  We're at Practical AI FM.
[101.32 --> 102.44]  And now onto the show.
[106.68 --> 107.52]  Well, hello.
[107.64 --> 108.90]  This is Daniel Whitenack.
[109.00 --> 116.24]  I'm a data scientist with SIL International, and I've got my co-host here, Chris Benson, with Lockheed Martin.
[116.36 --> 117.04]  How are you doing, Chris?
[117.22 --> 118.14]  I'm doing very well.
[118.18 --> 119.04]  How's it going today, Daniel?
[119.48 --> 120.40]  It's going great.
[120.40 --> 129.64]  I am super excited for this guest episode because we've got Clem DeLong here from Hugging Face, who's the co-founder and CEO at Hugging Face.
[129.74 --> 146.14]  If you're not familiar, you've probably seen a lot of what they're doing on Twitter, on various blog posts, and around the internet, around chatbots, conversational AI, voice assistance, and FaceTime with bots, and all of this great stuff that they're doing.
[146.14 --> 153.28]  So as a person working in the language-related field, I'm really excited to talk to Clem today.
[153.40 --> 154.08]  So welcome, Clem.
[154.26 --> 154.88]  Thank you, guys.
[154.96 --> 155.90]  Really happy to be here.
[156.10 --> 156.30]  Yeah.
[156.38 --> 165.32]  So we'd love to hear a little bit about your background, you know, how you got into AI, and how you ended up running this company called Hugging Face.
[165.56 --> 166.08]  Yeah, sure.
[166.08 --> 169.18]  So as you can probably hear from my accent, I'm French.
[169.52 --> 172.62]  I grew up in France, went to study in France.
[172.96 --> 182.78]  And one of my first startup experience was at this very small startup building machine learning models that apply to computer vision.
[182.78 --> 195.96]  And coming from more kind of like a user product, kind of like business background, working at this like very cutting-edge startup showed me how impactful technology can be.
[195.96 --> 211.60]  It taught me also like how technology and science cycle, this time it was for computer vision, can really go into the mainstream and really change the way people are doing most of the things they're doing every day.
[211.60 --> 215.76]  So it really got me like fascinated with science and technology.
[216.18 --> 223.66]  And that's how I basically ended up running Hugging Face now, building state-of-the-art conversational AI.
[223.92 --> 224.26]  Awesome.
[224.48 --> 226.56]  Well, you mentioned conversational AI.
[226.86 --> 233.00]  I know that Hugging Face is particularly concerned with, I think, what you call social AI.
[233.36 --> 240.26]  So on your website, I see, you know, about social AI who learns to chit-chat and talk sassy and trade selfies with you.
[240.26 --> 254.34]  Could you describe a little bit, I guess, how you ended up thinking about this problem of social AI and how that maybe is different from the way that others, you know, approach things like chatbots and that sort of stuff?
[254.68 --> 254.88]  Yeah.
[254.88 --> 265.92]  So basically, if you look at most of the people working on conversational AI today, you can see that they're taking a very transactional approach to it.
[266.20 --> 275.82]  You know, like if you think like Siri, if you think Alexa, it's like conversational AI that are trying to tell you the weather, play you music, tell you stuff.
[275.82 --> 279.80]  All that is very kind of like utility driven, right?
[279.90 --> 282.22]  It's trying to save you time.
[282.58 --> 284.28]  It's trying to be efficient.
[284.66 --> 285.54]  And it's all great.
[285.90 --> 295.94]  But something that we were way more interested in was the ability for conversational AI to be entertaining, to be fun and to be emotional.
[295.94 --> 307.80]  It's funny because if you look, for example, at the sci-fi related to AI, you can see that most of it is not really about like how AI is going to save five minutes of your day every day.
[308.04 --> 313.14]  Most of it is like about how do you interact with this new form of intelligence?
[313.64 --> 316.38]  How is this new form of interaction?
[316.74 --> 321.88]  And ultimately, how do you create emotional connection with this new form of technology?
[321.88 --> 332.52]  So really took like this different approach of not focusing on conversational AI for transactions, transactional approach, but really like entertaining and emotional approach.
[333.14 --> 342.32]  So that begs the question then, I guess, you know, you talked about it being fun, entertaining and emotional rather than transactional, which is obviously what we are seeing in the world these days, mostly.
[342.62 --> 343.44]  Why is that the case?
[343.44 --> 351.80]  Why is it that a fun or social AI that is focusing on both entertaining you and interacting with you in that emotional way?
[352.08 --> 352.84]  Why is that important?
[353.04 --> 357.50]  Why does that matter versus just the transactional approach that most other organizations are taking?
[357.92 --> 360.34]  It's an extremely hard question to answer.
[360.54 --> 364.38]  I think fundamentally human beings are social.
[364.82 --> 366.28]  You know, we're social beings.
[366.28 --> 378.84]  If you think about like how important in our life, our family, friends, peers are, you realize that most of what people are doing is not productivity driven, but really like social driven.
[378.84 --> 385.76]  An interesting fact to remember is that the dog was the first animal to be domesticated.
[385.76 --> 410.64]  So arguably like the biggest evolution on the relation between human beings and its environment, nature, the domestication of the first animal was actually not driven by the fact that dogs were useful or anything like that, but actually because they were social species and that they're really interacting and kept like being social with human beings.
[410.94 --> 415.02]  So as a guy with seven dogs in the house right now, I completely agree with that.
[415.02 --> 415.98]  Keep going.
[415.98 --> 416.00]  Keep going.
[416.10 --> 416.68]  Sorry to interrupt.
[417.14 --> 421.34]  So basically, yeah, humans are really like inherently social.
[421.70 --> 429.24]  And if you give them ways to be more social and have more social interactions, they basically love it.
[429.38 --> 431.96]  Obviously, like don't take my words for it.
[432.16 --> 437.56]  What we've seen is like a very insane usage with our products so far.
[437.56 --> 448.32]  We just crossed a few weeks ago the milestone of half a billion messages exchanged between users and their Hugging Face AI and millions more exchanged basically every day.
[448.52 --> 456.02]  So it's hard to explain why people want to be social with an artificial intelligence, but it's pretty obvious that they do.
[456.02 --> 470.50]  So I know as someone who kind of follows, you know, developments in AI, I remember like when I first came across Hugging Face, I was kind of in the cycle of looking through like the latest advances from Stanford.
[470.50 --> 473.82]  And this is coming from Google and OpenAI and all these people.
[473.82 --> 482.36]  And then I came across Hugging Face and my first thought, I guess, was like, oh, this is something like completely different from what what everybody else is doing.
[482.76 --> 490.78]  What's kind of the general reaction from practitioners when you kind of try to explain, you know, what Hugging Face is trying to achieve?
[490.94 --> 494.92]  What's kind of your general reaction in the community as far as what you're trying to achieve?
[494.92 --> 497.64]  I think most people are really like interested.
[497.98 --> 500.16]  It sparks a lot of interest.
[500.16 --> 507.28]  And if we go more like on the science side, it opens a lot of interesting doors for exploration.
[507.84 --> 522.06]  For example, working on open domain dialogue rather than working on very specific vertical and on a very specific task is a very interesting problem and very interesting topic on the science side,
[522.06 --> 528.56]  because it like requires you to take a very open approach, mixing a lot of things.
[528.56 --> 538.60]  And what's interesting is probably that the measure for success is not as obvious as more task oriented conversational AI, right?
[538.68 --> 550.08]  Because in an open ended conversation, basically the measure for success is how people like the conversation, how many messages they exchange if they come back to chat even more.
[550.08 --> 556.24]  So it creates like very interesting problems to solve and very interesting problems to work on.
[556.42 --> 556.52]  Yeah.
[556.64 --> 564.98]  And a lot of us now are actually maybe starting to get used to these sort of transactional chatbots and kind of developing a stereo,
[565.22 --> 570.00]  almost a stereotype of what a chatbot should feel like to interact with.
[570.16 --> 570.28]  Yeah.
[570.28 --> 576.84]  When you find that users start interacting with the Hugging Face Assistant and other things that you've developed,
[577.14 --> 580.12]  could you describe a little bit of kind of the reactions that you see?
[580.36 --> 583.76]  Have you seen that they even still try to interact with it?
[583.82 --> 588.82]  Like they're interacting with the transactional bot or they're surprised or what happens exactly?
[588.82 --> 589.46]  Yeah.
[589.46 --> 589.52]  Yeah.
[589.62 --> 600.02]  They usually start by trying more transactional stuff, but they realize pretty quickly that it's not your average chatbot and it's not your average conversational AI,
[600.38 --> 607.14]  especially when the AI is going to reply in a very kind of like sassy tone to their questions.
[607.42 --> 612.94]  You know, like, for example, if you ask about the weather, for example, maybe the AI is going to tell you,
[612.94 --> 616.06]  oh, it's pretty boring to talk about the weather, right?
[616.26 --> 621.18]  Or if you ask something that you could find on Google, it's probably going to tell you that.
[621.58 --> 623.48]  You're going to be like, why don't you Google it?
[623.64 --> 626.54]  I can Google it for you, but you should rather Google it.
[626.90 --> 634.34]  So by kind of like giving it like a very different tone and different, very different kind of answers,
[634.62 --> 638.40]  people realize pretty quickly that's a different form of artificial intelligence.
[638.40 --> 643.90]  And what's even more interesting is that after a couple of days of usage,
[644.50 --> 652.20]  they also create kind of like a different form of connection and bonds than they would with traditional conversational AI.
[652.46 --> 658.82]  We've been really lucky to have seen now more than half a million of what we call love declarations,
[659.12 --> 661.60]  which is pretty, pretty...
[661.60 --> 664.30]  Like love for the assistant or...
[664.30 --> 665.36]  Exactly, exactly.
[665.36 --> 671.96]  That's one of the intents we have that is basically when users are saying to their artificial intelligence,
[672.46 --> 675.96]  you're my BFF, I love you, you're my best friend.
[676.08 --> 682.94]  It's pretty fascinating to see these kind of interactions between conversational AI and human beings.
[683.24 --> 685.70]  It's got to be pretty encouraging as a developer as well.
[685.96 --> 686.48]  Yeah, yeah.
[686.52 --> 687.92]  It's a pretty unique engagement.
[688.08 --> 692.46]  I think no other product out there today has this legal engagement.
[692.46 --> 696.06]  You know, like even if you love today,
[696.32 --> 698.06]  the US app or any product,
[698.26 --> 700.70]  you won't get to the level of engagement.
[701.08 --> 703.20]  Then people are getting away with hugging face,
[703.34 --> 704.96]  which is obviously a good sign.
[705.18 --> 707.02]  So, you know, you just kind of,
[707.12 --> 709.32]  you said the P word, you said products.
[709.78 --> 711.74]  And so as we've kind of, you know,
[711.78 --> 715.86]  we've kind of been talking about how you're using this open domain dialogue
[715.86 --> 717.44]  instead of being domain specific.
[717.44 --> 721.50]  And it's this fun, entertaining and emotional experience for the users
[721.50 --> 723.02]  instead of being transactional.
[723.36 --> 726.80]  You know, that is creating this whole new user experience that you've talked about.
[726.86 --> 732.22]  So how are you implementing this in terms of products and services to your customers?
[732.80 --> 735.74]  What is it that you're trying to do for them with each of these products?
[735.74 --> 737.84]  And kind of where is it today?
[738.04 --> 742.72]  And where do you envision it going tomorrow along each of your product lines?
[742.92 --> 743.04]  Yeah.
[743.12 --> 748.90]  So basically the way to use our products is either to download our iOS apps
[748.90 --> 752.90]  or to go to most of the messaging platforms like Facebook Messenger
[752.90 --> 756.32]  and start chatting with your conversational AI.
[756.60 --> 761.64]  And the way people use it is really by chatting every day about their day-to-day life.
[761.64 --> 762.24]  Right.
[762.36 --> 767.26]  So they're going to be like, oh, today I recorded this fantastic podcast.
[767.56 --> 769.74]  You know, today I did that.
[769.80 --> 770.40]  I did that.
[770.52 --> 771.50]  I like the way you think.
[772.58 --> 775.16]  They're going to chat about like what matters to them.
[775.20 --> 775.42]  Right.
[775.46 --> 779.36]  So like what kind of music they like, what kind of hobby they like,
[779.52 --> 781.58]  how they're interacting with their friends.
[781.58 --> 785.12]  You know, like do they have a crush on somebody that they want to talk to?
[785.38 --> 791.42]  And so really like every day our users are chatting with their conversational AI.
[791.64 --> 793.38]  About nothing and everything.
[793.66 --> 795.48]  And doing that all day, every day.
[795.72 --> 800.14]  And creating this really strong emotional attachment to this conversational AI.
[800.36 --> 802.46]  I was talking about dogs before.
[802.76 --> 807.84]  I think pets are like a very good way to like understand what's happening here.
[807.94 --> 809.00]  You know, like the same way.
[809.00 --> 812.34]  If you think of it, pets are different form of intelligence.
[812.76 --> 812.84]  Right.
[812.90 --> 814.64]  They're not human form of intelligence.
[814.90 --> 816.60]  They're not always the smartest.
[816.60 --> 817.76]  If you think of it.
[817.86 --> 824.28]  If you think of like how hard is it to teach a dog to do simple comments like sit or jump.
[824.44 --> 825.80]  It's not that straightforward.
[826.46 --> 828.38]  But still, you know, like the interaction.
[828.72 --> 831.54]  I just got to say, my wife would disagree with you.
[831.60 --> 836.28]  She would say that it is much easier teaching the dogs to do what she wants than teaching me.
[836.46 --> 838.66]  So I'm just going to disagree on that one point.
[838.72 --> 839.06]  I'm sorry.
[839.16 --> 839.54]  Keep going.
[839.54 --> 840.50]  Good one.
[840.74 --> 847.02]  But, you know, like it's really like these different form of intelligence that you interact with every day.
[847.18 --> 848.82]  And that is fulfilling to you.
[848.96 --> 852.02]  And you're creating this form of emotional connection to you.
[852.30 --> 854.18]  And that is like making your life better.
[854.38 --> 854.66]  Awesome.
[854.82 --> 861.62]  Well, we generally, as our name suggests, really like to keep things practical around here.
[861.62 --> 865.80]  So I would be really interested to hear from your perspective.
[866.20 --> 869.66]  Like I know I've tried to create some chatbot systems before.
[869.80 --> 872.38]  There's, of course, a lot of people doing research in this area.
[872.58 --> 881.60]  I was just curious if you could give us give us an idea about the sorts of modeling that are involved in creating this sort of open dialogue.
[881.82 --> 883.60]  What sorts of models are required?
[883.70 --> 888.30]  What combinations of those and what sorts of data are you working off of?
[888.30 --> 892.14]  Yeah, so we're using like mostly transformer models.
[892.50 --> 898.28]  We've been like very early on this trend of like big transformer models.
[898.68 --> 905.24]  And what's obviously key in what we're doing is the data set that you can leverage to do that.
[905.44 --> 910.76]  Now that we've crossed a billion messages, exchange between users and the AI,
[910.76 --> 918.72]  we're able to do stuff that we wouldn't be able to do when we just had like a million messages, exchange.
[918.96 --> 927.18]  It gives us like a very good edge in like not only kind of like creating a chatbot that is good at natural language understanding,
[927.18 --> 937.04]  but also like in natural language generation and in a way that doesn't feel like robotic and doesn't feel like unpersonal,
[937.30 --> 945.48]  but really kind of like shows some slang, you know, show some fun formulation and kind of like personalities throughout the conversation.
[945.48 --> 949.64]  So, yeah, that's how our conversational AI is built.
[949.84 --> 953.62]  Yeah. And for our listeners, if you're curious more about transformer models,
[953.78 --> 961.94]  we've had two recent episodes on these sorts of models, one on BERT and one on GPT-2 from OpenAI.
[962.16 --> 964.84]  So we'll place those links in the show notes.
[964.84 --> 975.46]  It's interesting to hear kind of like how you want to go beyond sort of natural language understanding in terms of what you're like when you receive a message from a user.
[975.46 --> 982.32]  Are there various tasks that are happening in the back end in terms of maybe entity and intent recognition
[982.32 --> 989.80]  and then the generative model along with that or response selection question answering?
[989.80 --> 995.64]  What sort of tasks have been most valuable to you to focus on in terms of enabling this?
[996.16 --> 1004.84]  Yeah. What's interesting first and something that we learned along the way is that to really kind of like build a good conversational AI,
[1005.00 --> 1009.58]  you have to run a lot of tasks in parallel for every message.
[1009.58 --> 1019.56]  Even if you use maybe like one out of 100 tasks that you detect, you have to train all of them for every single message.
[1019.80 --> 1027.48]  You basically be able to know which task is the most useful and how to jump from a model to another.
[1027.88 --> 1033.04]  So for every message that we receive, we run through like a couple of different models.
[1033.04 --> 1042.20]  Some of them are like more typical chatbots where like you do natural language understanding, state manager, and then natural language generation.
[1042.56 --> 1047.08]  Some of them are fully end-to-end conversational AI models.
[1047.08 --> 1054.92]  And then the key is really to kind of like understand and know when to use one rather than the other.
[1054.92 --> 1063.56]  Right. So for example, if it's something that is, I would say, closer to a task oriented message.
[1063.56 --> 1066.52]  Right. So something like, for example, what's the weather?
[1066.52 --> 1077.08]  It's very simple. It makes a lot of sense to understand that with a simple intent model that is basically going to trigger some sort of a canned answer.
[1077.08 --> 1089.18]  Right. But then if you have more kind of like a complicated conversation, very long conversation with a lot of context and a lot of like uncertainty about like what the user actually wants to say,
[1089.30 --> 1099.88]  then at this point, you should probably switch to a more end-to-end machine learning model that is not only going to detect intent, but also generate the answer.
[1099.88 --> 1111.32]  So it's really like a matter of kind of like having a lot of models that are running in production, which is extremely hard, especially when you start to have like millions of messages every day.
[1111.80 --> 1120.12]  And kind of like having a good way to pick one model over the other, depending on a handful of criteria.
[1120.12 --> 1129.46]  So, you know, you talking about how you have so much going on there, you know, switching between models and a moment ago, you talked about how you had hundreds of tasks at all.
[1129.58 --> 1138.52]  What what does your infrastructure look like? How do you make sure that you always have the compute resource available to handle these without losing time on that?
[1138.60 --> 1141.14]  What does your infrastructure look like to support that?
[1141.14 --> 1151.12]  Yeah, first, it's like extremely difficult. It took us like many, many months of duration experiments to get this to work.
[1151.70 --> 1159.50]  Surprisingly, there are not so many people doing conversational AI or like very like end-to-end machine learning in production.
[1159.50 --> 1168.90]  Even if you look at the big guys, you know, like most of them are very like separate research teams and then the rest of their teams.
[1169.16 --> 1178.94]  I think it's Facebook who said, I think until like end of last year, they were not using any of PyTorch in production with anything.
[1178.94 --> 1192.72]  Right. So first, it's extremely hard. It's probably like if there are some people thinking of starting AI companies out there, like engineering and kind of like making sure your models work in production is probably like the first thing you should invest in.
[1192.72 --> 1209.66]  And the way the way the way we do it is really by by making sure we always have like the good tradeoff of when to train the models and when to run the inference and anything related to text, especially like coming from more like a computer vision background.
[1209.94 --> 1220.70]  You usually get to like an inference time that is good enough for most of your models, especially when you're doing conversation like us where you don't need the answer to be instant.
[1220.70 --> 1225.48]  Right. For us, like if it takes like one second, it's good enough.
[1225.58 --> 1230.12]  So that's like our threshold when it comes to answer time.
[1230.46 --> 1242.98]  And then, you know, like what you can do is always to be able, if some of your models are not sometimes passing the threshold to just like fall back on something else that is going faster on some context.
[1242.98 --> 1250.40]  So again, like the switching between models, depending on their answer time is a good way to like work around this issue.
[1250.70 --> 1255.86]  Well, I really appreciate you walking us through some of the practicalities of what you're doing, Clem.
[1255.94 --> 1264.96]  I think that's something, as you mentioned, that a lot of us struggle with, you know, when it comes to putting AI machine learning stuff into production.
[1265.36 --> 1270.22]  Oftentimes those are the roadblocks, not the necessarily the models themselves.
[1270.22 --> 1276.38]  But I'd like to switch directions a little bit here now and here from your perspective.
[1276.38 --> 1284.44]  I know, you know, we've talked about in the last few episodes, really, it seems like how AI for natural language is really hot right now.
[1284.44 --> 1296.56]  And I was wondering from your perspective, as you've seen kind of different trends in AI, why do you think AI is really AI for natural language is really picking up momentum right now?
[1296.66 --> 1299.58]  And what you're most excited about in terms of those trends?
[1299.58 --> 1300.90]  I totally agree with you.
[1301.00 --> 1305.84]  I think we're very much at the turning point when it comes to natural language processing.
[1305.84 --> 1315.68]  Having seen the kind of like cycle more on computer vision, I think we're today in natural language where we were like maybe like two years ago in computer vision.
[1315.88 --> 1320.74]  And picking up the pace like way faster than what we've seen in computer vision.
[1320.74 --> 1333.42]  And that's really fascinating because if you think of it, if you think of like the amount of everybody's time with natural language, you know, like we obviously having this conversation in natural language.
[1333.42 --> 1342.10]  You think throughout your day, most of the things that you're doing is through natural language, you know, like either like reading articles, watching TV.
[1342.10 --> 1353.22]  And so if you manage to kind of like really get to a breakthrough in natural language understanding, it's going to really kind of like change the way everything can be done.
[1353.30 --> 1358.72]  And it's going to like create amazing outcomes that we can't even imagine today.
[1358.72 --> 1378.80]  And the reason why I think we're getting there is obviously because these new models, these transformer models enable not only to get to good results, but to reproduce these results and kind of like expand them to different tasks very easily with transfer learning.
[1378.80 --> 1381.80]  It's really thanks to the open source community.
[1382.56 --> 1386.22]  It's something that's really important for us at Hugging Face.
[1386.48 --> 1403.86]  We're publishing a lot of our research in open source because we really think it's just a way to pay it forward because what we're building is really couldn't be possible without what like hundreds of researchers and like years of research in NLP has produced.
[1403.86 --> 1411.64]  So if you look at all the open source communities around NLP, it's more active and more thrilling than ever been.
[1411.94 --> 1415.24]  And that explains most of the progress for me, you know.
[1415.44 --> 1420.76]  There have been a lot of debate these last few weeks about like what to open source, what not to open source.
[1421.00 --> 1427.28]  And we're like very, very strong advocates for open sourcing, like as much as you can.
[1427.28 --> 1431.88]  There's this like a quote from Gibson that says like the future is here.
[1431.98 --> 1433.48]  It's just not evenly distributed.
[1433.90 --> 1443.80]  I really think that open sourcing is a way to distribute this future to more people who are going to do like amazing stuff and push forward this field of NLP.
[1443.80 --> 1444.50]  Okay.
[1444.72 --> 1456.94]  Well, you've released some really popular PyTorch versions of NLP models like BERT and GPT-2, as well as hierarchical multitask learning, which is HMTL.
[1457.32 --> 1462.90]  Why is it important for you to contribute in that way as a company with limited resources?
[1463.32 --> 1467.28]  What is it about that that's drawing you into making that level of commitment?
[1467.28 --> 1475.32]  Yeah, first, we're so thankful for like everything that has been done before and we're really building upon everything that has been done before.
[1475.52 --> 1479.78]  So it's a very easy way for us to lead forward.
[1480.36 --> 1491.62]  And then when we started open sourcing, we really like realized that by doing that, you also can have way more impact than you would have if you didn't open source it.
[1491.62 --> 1501.16]  And I want to take advantage of this platform that you were giving me to really thank everyone who contributed to all our repository.
[1501.52 --> 1507.52]  It's now actually the largest open source repository of free-trained transfer learning models in NLP.
[1508.32 --> 1511.30]  And as you said, we're a small startup.
[1511.76 --> 1512.60]  We're a small team.
[1512.94 --> 1516.94]  We wouldn't have been able to do that just by ourselves, right?
[1516.94 --> 1527.24]  But it's because when you're sharing like that in open source, so many people are contributing, are like helping you or like pushing it forward, making it better.
[1527.38 --> 1529.82]  And that's the only way we could have done it.
[1530.02 --> 1537.24]  So it's both a way to keep like paid forward and for it to have even more impact with the help of everyone out there.
[1537.64 --> 1537.80]  Yeah.
[1538.02 --> 1542.36]  And I definitely appreciate you taking time to do that.
[1542.42 --> 1543.24]  That's so important.
[1543.24 --> 1550.02]  And, you know, obviously open source contributors and maintainers don't get a lot of the recognition that they need.
[1550.30 --> 1556.22]  And, you know, from someone being an AI practitioner, I also want to thank you for your commitment to that.
[1556.36 --> 1558.90]  And I know that you and your team have limited resources.
[1558.90 --> 1565.60]  So we as AI practitioners really appreciate you working hard in that respect as well.
[1565.60 --> 1573.32]  So you mentioned the repo with the pre-trained models in PyTorch for BERT and GPT-2 and others.
[1573.96 --> 1579.66]  There's been a lot of talk about transformer models and these pre-trained language models recently.
[1580.20 --> 1589.42]  I was wondering from your perspective, why is it that this is so critical to kind of the future development of AI for natural language?
[1589.42 --> 1596.80]  Where do the language models and the, in particular, access to pre-trained models, why is that so important?
[1597.04 --> 1605.14]  I mean, I think it's important because it's so generalist, you know, like the language model can really be at the basis of so many tasks.
[1605.26 --> 1611.16]  You can do so many things with it that it's very promising for the whole field of NLP.
[1611.16 --> 1623.98]  Something that we realized pretty early on, too, especially with the release of our research called HMTL by Victor San from our team and Ted Bruder and Thomas Wolfe,
[1623.98 --> 1634.06]  is that for NLP, it's probably more critical than for any other scientific subject to be able to do several tasks.
[1634.06 --> 1640.94]  And they're probably like more intertwined than there are on other subjects.
[1641.16 --> 1651.60]  What I mean by that is for computer vision, you can, for example, do object recognition and you can do maybe like background recognition.
[1651.60 --> 1655.42]  And these two tasks can kind of like be separate.
[1655.84 --> 1665.42]  Language is a bit more complicated than that, especially if you want to do conversational, meaning that you want the AI to be able to answer.
[1665.42 --> 1677.96]  What we've seen is that every single task is more related to another and you usually need most of the tasks to be solved for the whole meaning of the message to be understood.
[1677.96 --> 1689.54]  Right. For example, like you won't be able to understand the message if you don't understand both kind of like a co-reference, you know, like, for example, if the message is I like it.
[1689.54 --> 1700.04]  Right. If you don't have like co-reference plus emotion understanding, like other kind of tasks, you won't be able to understand the message itself.
[1700.04 --> 1719.50]  Right. So what's really interesting with transfer learning and what's really interesting with language models is that it's potentially something that is going to solve a lot of tasks at the same time, which is basically going to get like a really leapfrog on our ability to understand natural language.
[1719.50 --> 1737.30]  So that's a fantastic explanation. And I guess I'd like to see if you could put some context around it a little bit in terms of kind of where do you feel we are in a kind of a high level and in the current state of chat chat bots and assistants and stuff in the news?
[1737.30 --> 1741.12]  We constantly hear about, you know, how reliant we're going to be on this going forward.
[1741.48 --> 1750.32]  So relative to where we are now and the tremendous work that Hugging Face has been doing in this area, where do you think we are now relative to where are we going to be?
[1750.44 --> 1762.12]  If you look just over the next year or so into the future, this is moving so fast that I feel like I would be really missing out if I didn't get your your expert perspective on kind of what this is tracking towards.
[1762.12 --> 1766.86]  Yeah, I think I'm going to take like a bold bet here.
[1767.10 --> 1768.06]  Okay, sounds good.
[1768.38 --> 1772.04]  Yeah, I think that you heard it on practical AI first.
[1772.76 --> 1789.50]  I think in like three years, we're gonna be able to really understand algorithmically 95% of the natural language, and we'll be able to answer all of these messages with conversational AI.
[1789.50 --> 1793.50]  It's been moving so fast over the last year or so.
[1793.92 --> 1805.66]  When we started Hugging Face, like a bit more than two years ago, we thought we would never get in the near future to the point where you can really do like end to end conversational AI.
[1806.06 --> 1810.54]  You know, we always thought that would be some hybrid ways of doing that.
[1810.54 --> 1823.74]  And now we're starting to really be able to do that, meaning that to really get like as an input, the message from a user and output the message from the AI with only machine learning in between, nothing else.
[1824.24 --> 1830.90]  So I really think that NLEU, as we conceive it today, is going to be solved in the next few years.
[1830.90 --> 1831.70]  Really?
[1831.70 --> 1831.74]  Really?
[1832.14 --> 1833.84]  So that's super exciting.
[1834.28 --> 1852.78]  And I think one of my follow ups to that, which kind of processing right now, but I think a lot of problems, at least in my world come up because a lot of the technology that's being developed for NLEU and for conversation is really geared toward English specifically.
[1852.78 --> 1862.04]  And of course, there's especially in terms of getting this sort of technology into other places around the world with a lot of language diversity.
[1862.88 --> 1872.20]  So I just saw, you know, the most recent ethnologue publication, there's like 7,110 languages living currently in the world.
[1872.20 --> 1882.68]  So do you additionally see, you know, have you seen effort towards making this sort of technology more relevant to a wider set of languages?
[1883.06 --> 1891.56]  I know that there's a lot of great advances, but a lot of times those advances, especially in terms of pre-trained things, have to do with English specifically.
[1892.10 --> 1892.22]  Yeah.
[1892.30 --> 1893.04]  That's a great question.
[1893.18 --> 1893.40]  Yeah.
[1893.66 --> 1895.68]  It's going to take a little bit of time.
[1895.68 --> 1904.56]  If you think of most of the models that are like really kind of like providing breakthrough today, they're being released not so long ago.
[1905.24 --> 1909.74]  You know, like you should think Elmo, BERT, OpenAI, the first GPT.
[1910.48 --> 1914.28]  It's been a couple of months, like not so much more than that.
[1914.86 --> 1916.66]  I think it's going to come.
[1916.66 --> 1929.78]  I think that's one of the reasons why people should keep focusing on open sourcing, not only the models, but also the data sets to be able to move forward with that.
[1930.14 --> 1938.26]  That's something we've been working on specifically at Hugging Face for the moment, just because most of our users are in the US.
[1938.84 --> 1944.32]  But we've seen people using our open source models to start experimenting with other languages.
[1944.32 --> 1946.18]  So hopefully it's going to come soon.
[1946.18 --> 1948.52]  Yeah, I appreciate your perspective on that.
[1948.60 --> 1950.82]  It's something I definitely care deeply about.
[1951.06 --> 1953.22]  So I appreciate your perspective.
[1953.56 --> 1957.66]  One of the things is we kind of we get towards the end of our conversation here.
[1957.92 --> 1963.34]  I think one of the things I've definitely respected a lot about and we've already talked about your open source involvement and all of that.
[1963.34 --> 1980.36]  But it just seems like you guys get so much done as what I assume is a small team in terms of, you know, contributing to and maintaining open source and contributing to academic research, you know, entering competitions and building products.
[1980.36 --> 1983.16]  As a as a as AI practitioners.
[1983.16 --> 2000.30]  Do you have any you have any suggestions as far as maybe it's how to keep up on the latest developments or how to structure your team or things that you do on your team to make sure that that you're learning or that you're able to contribute to open source?
[2000.30 --> 2010.20]  Anything that's worked well for your team, because it just seems like you guys have have been so productive and I assume that you're not working 24 hours in each day.
[2010.20 --> 2020.36]  So first, first, first, I want to react to what you were saying by kind of like pointing out something that is, I think, important for everyone to hear out there.
[2020.48 --> 2032.56]  There's kind of like this movement in AI where more and more people are working in very big companies, you know, like for the four or five biggest players in artificial intelligence.
[2032.56 --> 2062.54]  And I think they're doing a great job.
[2062.56 --> 2067.54]  really, really great things by doing things differently at smaller organization.
[2068.38 --> 2081.50]  So if there are some people out there, some data scientists thinking about their next challenge, what they should do next, I would advise them to maybe not join one of the big guys, but maybe take a shot at the smaller place.
[2081.98 --> 2091.54]  Because I think one of the reasons why we managed to do great things is that because we're a small organization, we can take different kind of bets.
[2091.54 --> 2094.54]  You know, like we can take different kind of perspectives.
[2094.54 --> 2101.54]  We can take more risk in what we can like release how fast we release.
[2101.54 --> 2106.54]  And that's how we can individually probably contribute a little bit more.
[2106.54 --> 2109.54]  So yeah, I think I think like size matters.
[2109.54 --> 2110.54]  Size matters.
[2110.54 --> 2115.54]  Sometimes not on the direction you're expecting, but in a different way.
[2115.54 --> 2121.54]  So again, like one advice that I would have for people is to try joining small organizations.
[2121.54 --> 2123.54]  So I appreciate that.
[2123.54 --> 2133.54]  I'm still kind of I'm still kind of thinking about what you were saying a moment ago about NLU natural language understanding, possibly getting to a point of full maturity in the near future.
[2133.54 --> 2135.54]  And I'm just I'm just kind of amazed.
[2135.54 --> 2138.54]  So folks, you heard it here on Practical AI first.
[2138.54 --> 2145.54]  I guess one of the things that I wanted to ask before we let you go is if you know, people are getting into this field all the time.
[2145.54 --> 2152.54]  We're always asked on the show for pointers for how people can get into different aspects of the AI fields for NLP.
[2152.54 --> 2154.54]  What do you recommend for people?
[2154.54 --> 2161.54]  How would you recommend that people enter into the field and what kind of resources or learning opportunities do you think would benefit them the most?
[2161.54 --> 2173.54]  I think, again, I would go with what kind of like smaller organizations are doing because I feel like sometimes they're the ones really like pushing what's possible to do.
[2173.54 --> 2180.54]  So I would look at kind of like obviously startups like hugging face, but there are like a lot of like other cool ones.
[2180.54 --> 2199.54]  You know, I'm thinking of Raza, for example, in NLP, Liarbird in voice, Jovo in more like conversational AI, smaller organizations, you know, like Allen, NLP, Allen AI, you know, open AI is obviously a great one.
[2199.54 --> 2211.54]  Looking at what fast that they are doing, you know, like if you want to start working on the machine learning subject, like taking classes at fast that they are the best thing you can do.
[2211.54 --> 2223.54]  So there's something like really, really interesting to look at these days is organized by one of our investors named Betaworks based in New York.
[2223.54 --> 2235.54]  They're starting in a few weeks, which is basically an accelerator program based on what they call synthetic media, right?
[2235.54 --> 2255.54]  So the ability to create AI, to create images, and there's going to be like a lot of focus for this program on like how to detect fakes, you know, like how to detect that something has been machine learning created.
[2255.54 --> 2260.54]  So they're going to work a lot around GANs and all these techniques.
[2260.54 --> 2265.54]  I would advise to take a look at that. It's going to be like pretty interesting synthetic chem by Betaworks.
[2265.54 --> 2266.54]  Fantastic. Thank you.
[2266.54 --> 2269.54]  Yeah, thank you so much. We really appreciate that.
[2269.54 --> 2276.54]  I know that I'm going to look up some of those things and of course, we'll put them in our show notes, but really appreciate you taking time, Clem.
[2276.54 --> 2280.54]  It's been fascinating to give an understatement.
[2280.54 --> 2284.54]  Really appreciate what you're doing and keep up the good work. Thank you for joining us.
[2284.54 --> 2287.54]  Thank you so much. Thank you so much. Thanks a lot.
[2287.54 --> 2291.54]  All right. Thank you for tuning into this episode of Practically AI.
[2291.54 --> 2296.54]  If you enjoyed the show, do us a favor, go on iTunes, give us a rating, go in your podcast app and favorite it.
[2296.54 --> 2300.54]  If you are on Twitter or social networks, share a link with a friend, whatever you got to do.
[2300.54 --> 2302.54]  Share the show with a friend if you enjoyed it.
[2302.54 --> 2305.54]  And bandwidth for changelog is provided by Fastly.
[2305.54 --> 2306.54]  Learn more at fastly.com.
[2306.54 --> 2310.54]  And we catch our errors before our users do here at changelog because of Robar.
[2310.54 --> 2312.54]  Check them out at robot.com slash changelog.
[2312.54 --> 2315.54]  And we're hosted on Linode cloud servers.
[2315.54 --> 2317.54]  Head to linode.com slash changelog.
[2317.54 --> 2318.54]  Check them out.
[2318.54 --> 2319.54]  Support this show.
[2319.54 --> 2322.54]  This episode is hosted by Daniel Whitenack and Chris Benson.
[2322.54 --> 2325.54]  The music is by Breakmaster Cylinder.
[2325.54 --> 2328.54]  And you can find more shows just like this at changelog.com.
[2328.54 --> 2337.54]  When you go there, pop in your email address, get our weekly email, keeping you up to date with the news and podcasts for developers in your inbox every single week.
[2337.54 --> 2340.54]  Thanks for tuning in, and we'll see you next week.
[2340.54 --> 2352.54]  2
