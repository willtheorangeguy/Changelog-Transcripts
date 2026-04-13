[0.00 --> 6.70]  Bandwidth for Changelog is provided by Fastly. Learn more at Fastly.com. We move fast and fix
[6.70 --> 11.42]  things here at Changelog because of Rollbar. Check them out at Rollbar.com. And we're hosted
[11.42 --> 23.68]  on Linode servers. Head to linode.com slash Changelog. Welcome to Practical AI, a weekly
[23.68 --> 28.58]  podcast about making artificial intelligence practical, productive, and accessible to everyone.
[28.58 --> 34.18]  This is where conversations around AI, machine learning, and data science happen. Join the
[34.18 --> 38.24]  community and snag with us around various topics of the show at changelog.com slash community.
[38.76 --> 42.32]  Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[47.06 --> 50.72]  Well, hey, Chris, how you doing? I'm doing fine. How's it going today, Daniel?
[51.02 --> 56.58]  It's going really well. I'm still in the midst of grading for my Purdue class, but I see the finish
[56.58 --> 62.72]  line. So how about with you? Just started the new job at Lockheed Martin a couple of weeks ago and
[62.72 --> 67.30]  have been heads down in that. And obviously, the holiday season's coming up with the family. So
[67.30 --> 74.40]  a great time of year. Yeah, definitely. So today we actually have two guests from IBM Healthcare. I'm
[74.40 --> 80.16]  really excited that Ajay Raiuro and Gishermo Cechi are joining us. Welcome, guys.
[80.16 --> 86.06]  Hey, hi. Hi, Chris. Hello, Daniel. So as I mentioned, they're both with IBM Healthcare. So
[86.06 --> 93.32]  Ajay is a VP of IBM Healthcare and Life Sciences Research. Gishermo is a principal researcher of
[93.32 --> 100.60]  computational psychiatry and neuroimaging. And so I'm really excited to hear about what they have to
[100.60 --> 106.96]  tell us here on Practical AI today and how AI is related to healthcare and psychiatry and mental
[106.96 --> 112.46]  health. It's going to be a really exciting show. But before we jump into those things, I'd love to
[112.46 --> 117.18]  give our guests a chance to introduce themselves and give us a little bit of background about
[117.18 --> 124.00]  how they eventually got to this place of integrating AI and healthcare and psychiatry. So Ajay,
[124.04 --> 129.98]  do you want to start us out? Sure. Thanks for the opportunity to chat. This is Ajay. I am leading
[129.98 --> 136.40]  our healthcare and life science research portfolio at IBM. I just completed 20 years working at IBM.
[136.40 --> 143.62]  Ah, congratulations. Thank you. My background is in molecular structural biology. Prior to coming to
[143.62 --> 149.72]  IBM, I was a postdoctoral scientist at Memorial Sloan Kettering Cancer Center, but that was a while
[149.72 --> 155.92]  ago. And, you know, moving to IBM, a lot of my research interest has become entirely computational.
[156.58 --> 161.72]  So the work that I do now is actually at the intersection of healthcare biology and all things
[161.72 --> 166.38]  information technology. It's really interesting how you've kind of gone through that path,
[166.38 --> 172.60]  eventually landed at all of these integrations of computation and IT. I'm excited to hear more.
[172.60 --> 178.48]  Guillermo, do you want to give us a brief intro? How did you get eventually into this world of
[178.48 --> 186.68]  computational psychiatry? Well, my background is in physics and neuroscience, but I was always
[186.68 --> 194.62]  interested in philosophy. And then after completing my PhD, I did a fellowship in psychiatry before coming
[196.38 --> 204.84]  and naturally, mental health became very clear, clearly for me, an intersection between all of my
[204.84 --> 212.16]  interests, right? So this is what I'm doing now, just trying to understand how we put together mental
[212.16 --> 221.16]  health with AI. And so how did you really decide that mental health was a good target to start using AI
[221.16 --> 230.88]  technologies on? Well, one clear reason is that mental health needs it, right? So if you look at the daily
[230.88 --> 238.96]  practice of mental health, it's very constrained by the fact that you have neurologists, psychiatrists,
[239.38 --> 247.10]  healthcare providers that need to make judgments about the mental state of a patient or a prospective
[247.10 --> 256.78]  possible patient. And the way it's done today relies to a large extent, among other things, on the
[256.78 --> 266.46]  interaction between the patient and the clinician who evaluates them. That interaction is to a very large
[266.46 --> 274.40]  extent determined by language patterns, right? So how the patient is speaking to the clinician.
[274.40 --> 284.28]  And outside of mental health, we have an incredible wealth of tools to study language that at the moment,
[284.50 --> 290.46]  unfortunately, are not being used for the purpose of helping clinicians doing the evaluation, actually,
[290.78 --> 300.16]  in the end, helping patients to have better healthcare. So it's a really dire need of help from
[300.16 --> 304.48]  mental health practitioners. And, you know, that's perhaps the main motivation.
[305.08 --> 310.36]  Yeah, it's interesting that you've brought up the idea of analyzing language, because actually,
[310.36 --> 316.64]  when this topic was first brought up to me, I guess it wasn't the first thing that came to my mind. I was
[316.64 --> 322.26]  thinking, oh, we're studying like mental health computationally, maybe we're studying like brainwaves or
[322.26 --> 327.64]  something like that. But from what you've said, is the motivation to combine, like you said,
[327.64 --> 335.34]  these NLP techniques and AI and with language as related to mental health, is that really spawning from the
[335.34 --> 343.46]  patterns that you've seen in clinics that they're using language as a primary means to measure and identify
[343.46 --> 349.98]  mental health issues? Is that the primary motivation? Or was it because maybe you also are able to get data
[349.98 --> 358.42]  more easily than some other ways or something? Well, yes, of course, it's, in principle, easier to get
[358.42 --> 366.70]  speech data and language data in general, because that's, we don't need any special machines to do
[366.70 --> 373.98]  that. But fundamentally, you know, you were talking about brainwaves. Well, you know, speech is a brainwave.
[373.98 --> 380.04]  And it's very important because it is important for our behavior, right? It's one of the most essential
[380.04 --> 389.08]  tools that we humans use to interact with the world and with each other. And it's a very clear way in
[389.08 --> 394.84]  which most psychiatric conditions, but even neurological conditions are expressed, right? So
[394.84 --> 403.90]  disrupted patterns of behavior go hand in hand with disrupted patterns of language.
[403.98 --> 410.48]  Right. So in some cases, it's obvious, like in psychosis, you know, it's directly mapped to
[410.48 --> 419.44]  language, but we see that even in conditions such as Parkinson's, there is a clear trace of the disease
[419.44 --> 426.68]  in the language patterns that are produced by the patients. And in other cases, even the language
[426.68 --> 433.70]  patterns that can be or cannot be processed by the patients. So it's more than just availability
[433.70 --> 440.20]  data. It's really at the core of what defines a mental dysfunction.
[440.20 --> 447.18]  So AJ, could you tell us kind of how you're tying together this process, these techniques of using
[447.18 --> 453.78]  NLP for speech into kind of a practical, I mean, what is your goal here? What are you actually trying
[453.78 --> 456.64]  to produce in terms of usability?
[457.44 --> 462.28]  Yeah. So we should really talk about how this becomes very practical, but, you know, just examine
[462.28 --> 469.78]  the context first. The clinical encounter that used to occur entirely in the clinic, where the
[469.78 --> 474.96]  individual, let's say a patient, is actually coming with a scheduled appointment, is meeting with an
[474.96 --> 482.32]  expert practitioner, and they're having a dialogue or a clinical exam, and a clinical evidence is gathered
[482.32 --> 488.02]  in the course of that discussion. It may be through a physical exam or a psychiatric evaluation,
[488.02 --> 493.90]  as Gishar Moore was explaining. So that's a typical clinical encounter. It used to be that that was the
[493.90 --> 499.24]  only way in which you, the practitioner, would know something about the patient. But what has occurred in
[499.24 --> 506.38]  the last decade or so is, with the availability of many, many different forms of technology, including
[506.38 --> 512.92]  audio recording of speech, we are actually able to take the evidence gathering from the clinic to
[512.92 --> 519.46]  something that is of similar quality, but outside the clinic. And it allows the observations to move
[519.46 --> 525.22]  from an episodic encounter in the clinic to possibly a more continuous measurement that is occurring,
[525.48 --> 529.16]  in addition, outside the clinic as well, in the life of the person.
[530.02 --> 534.84]  So this is not necessarily a clinician that is using this mobile app that you're talking about.
[534.98 --> 540.26]  So this is used outside the clinic by non-medical personnel, non-medical people,
[540.26 --> 542.84]  between clinic visits. Is that accurate?
[543.36 --> 549.98]  It is being used by a clinician, let's say, to do a research study involving human subjects. But
[549.98 --> 555.98]  instead of just observing and recording while in the clinic, the clinician is actually able to use
[555.98 --> 562.18]  technologies like a speech recording device on a phone to actually observe outside the clinic as well.
[562.18 --> 567.42]  So it's still under the direction of the clinician there, essentially. But is it fair to say that the
[567.42 --> 573.60]  person who is being measured is also using it outside the clinic's environment between sessions?
[574.40 --> 580.04]  Right. The sessions could be any time during the day, could be initiated by the subject,
[580.64 --> 585.96]  and a conversation is happening. It could be a monologue or a dialogue that is getting recorded
[585.96 --> 592.46]  and then being analyzed by the techniques that Gijermo will describe. But it extends the observation
[592.46 --> 599.60]  window from the 20 minutes or 30 minutes in the clinic to the entire day, from in the clinic premises
[599.60 --> 606.24]  to wherever the subject is. And as we all know, when you have a mental health condition, sometimes even
[606.24 --> 612.44]  showing up for an appointment in the clinic is not something that will achieve 100% compliance.
[612.44 --> 619.38]  So extending the observation, physical location as well as time window allows better participation.
[619.38 --> 625.32]  And of course, the mental health status of the individual is not constant, right? So let's say
[625.32 --> 631.30]  you have the opportunity to initiate a conversation with the mobile app and record it, you would do it
[631.30 --> 637.02]  in instances where you want that to be captured. And that when it is not in the clinic, doing it in
[637.02 --> 641.94]  this manner actually allows the subject to actually provide more information about their condition
[641.94 --> 644.68]  that may or may not always be reproduced in the clinic.
[644.68 --> 650.98]  Yeah, I think you brought up a few really good points here. I know that in previous shows and in
[650.98 --> 656.72]  my conversations outside of the show, when I'm talking about AI and healthcare, a number of things
[656.72 --> 662.06]  come up. The first being like, well, we don't want people, you know, just using a smartphone app to
[662.06 --> 667.52]  diagnose themselves and not going to a doctor. So we don't want to kind of get rid of doctors or
[667.52 --> 672.82]  automate them away. But there's also, you know, privacy concerns. So it sounds like that,
[672.82 --> 678.02]  you know, in your case, you're not just like having a recording of all conversations at all
[678.02 --> 684.82]  point to improve diagnosis, but they are kind of like clinical sessions, but you're recording them
[684.82 --> 690.66]  at the participants indication throughout, you know, between clinical visits, but then also it's
[690.66 --> 697.70]  being reviewed by a doctor, right? Do you view this as kind of like an augmentation to the doctor's
[697.70 --> 704.30]  current workflow or, you know, or something kind of that couldn't turn into a completely different
[704.30 --> 709.34]  workflow for helping diagnose and treat and measure mental health?
[710.06 --> 716.44]  You're right. It is actually very thought out or deployed really as an augmentation to how the
[716.44 --> 724.26]  clinician observes and makes decisions for the patient or subject. It is with informed consent,
[724.26 --> 732.58]  and it is with the ability of the participant to turn the observation on or off, right? So it is not
[732.58 --> 738.68]  always on and the participant is actually deciding when they want to actually allow the observation to
[738.68 --> 744.14]  take place. And after the observation is done, so let's say, you know, the conversation you and I are
[744.14 --> 751.16]  having, if I had subjected this conversation through that consent, after I'm done speaking, me as a subject,
[751.16 --> 758.18]  I'll get to review what it is that has actually been observed from this. And then I choose whether
[758.18 --> 766.62]  the clinician is now being provided this input or not. So every session is therefore has that rigor of
[766.62 --> 767.06]  consent.
[767.90 --> 774.20]  So that's fascinating to me, just kind of as I'm trying to imagine if I had this app on my device
[774.20 --> 780.96]  going around through daily life. I'm curious, how do people choose to turn it on and off, you know,
[780.98 --> 785.74]  in terms of the, if you're looking at lots of different use cases, do people tend to have it on
[785.74 --> 790.66]  most of the time, kind of knowing that that's recording? Does it make them nervous? Does it change
[790.66 --> 796.06]  their behavior? I'm trying to imagine if I was that patient, how I would react to having this tool.
[796.06 --> 802.72]  Right. So, you know, we have done some analysis with retrospective data. That means sessions that
[802.72 --> 808.74]  have previously been recorded already in a clinician's office, for example, and built the
[808.74 --> 814.58]  analysis methodology based on such retrospective data. And then we moved into the very carefully
[814.58 --> 819.82]  constructed prospective studies that you're asking about. In the prospective studies, not only is the
[819.82 --> 825.60]  individual first informed what it is that every session will be about and how they have to
[825.60 --> 831.90]  participate. But for each session, they are actually taking some steps. For example, in one study,
[832.36 --> 838.60]  the technology is actually deployed as an app on the phone, and they are actually starting the app.
[838.98 --> 844.16]  The app will actually prompt them with certain questions. Then Gizermo can walk you through actually
[844.16 --> 850.82]  what the example questions are and what an example session is like. So it's initiated by the individual,
[850.82 --> 856.78]  and, you know, they go through it, it may be a few minutes, five minutes, 10 minutes, and then they
[856.78 --> 861.06]  conclude the session. And that's, that's the information that then gets used to analyze.
[861.80 --> 867.88]  Yeah, I'd love to turn to Gizermo, actually, on that same point, I was already thinking of kind of a
[867.88 --> 873.14]  follow up to this in terms of on the technical side, the people that are actually, you know,
[873.14 --> 878.68]  implementing the technical, you know, the models and the interaction of the models with the app and
[878.68 --> 885.54]  all of that. It sounds like there's a real importance between those technical people and
[885.54 --> 892.26]  the doctor's expertise, like you just mentioned, kind of developing this question and answer session.
[892.48 --> 895.94]  Could you speak more to that interaction and the importance of that, Gizermo?
[895.94 --> 903.96]  Yeah, it's a great point. And it's something that we have developed very carefully in all the studies
[903.96 --> 911.20]  that we have published, and we are conducting, we are working very close to clinicians, psychiatrists,
[911.28 --> 918.18]  and neurologists. And that's very important, both because we want to eventually, what we develop,
[918.40 --> 925.92]  be adopted by the field of mental health, but also because we are interacting in a very productive
[925.92 --> 936.84]  way. So, and I mean, we can think of this in two parallel avenues. One is the typical AI,
[937.28 --> 945.18]  big data science approach, right? So we try to create features of all colors and shapes and
[945.18 --> 952.88]  throw them against the wall and see what sticks. But at the same time, of course, you know, the space of
[952.88 --> 960.28]  features is, for all practical purposes, infinite. So you always need knowledge, right? So at the same
[960.28 --> 967.06]  time, what we are doing is, is by interacting with the, with clinicians and biomedical researchers,
[967.68 --> 975.14]  we are trying to, you know, open up their minds and trying to understand how the features and the
[975.14 --> 982.86]  symptoms that they have found to be most relevant can be turned into algorithms, right? So I can give
[982.86 --> 989.38]  you a very concrete example of both, right? In the first case, when we create features,
[989.84 --> 997.22]  we have results showing that we can discriminate Parkinsonian patients that are on the medication,
[997.58 --> 1006.78]  levodopa, or off the medication, using features that include frequency components of the voice that are not
[1006.78 --> 1013.02]  detectable by the human ear. But they are still there because the drug affects, it's psychoactive,
[1013.16 --> 1018.88]  so affects your nervous system. And of course, trivially affects your voice. On the other side,
[1019.04 --> 1027.82]  we study psychosis. And one essential component of what defines a psychotic state of a person is what
[1027.82 --> 1034.08]  psychiatrists call flight of ideas. And that is the notion that these patients may be talking about
[1034.08 --> 1041.90]  something and very dramatically jump the topic to something completely unrelated. So what we did there
[1041.90 --> 1051.10]  was to, using NLP techniques, create an algorithm that will detect those jumps using what's, you know,
[1051.14 --> 1056.06]  a technique called semantic embedding that is, you know, very commonly used in NLP. So, you know,
[1056.06 --> 1064.44]  this is one way in which we interact between the both worlds, right? So learn and formalize as much
[1064.44 --> 1071.38]  as possible, you know, decades or, you know, even centuries of knowledge in psychiatry, psychology,
[1071.52 --> 1078.96]  neurology, and at the same time, trying to leverage all the power of AI and NLP, signal processing,
[1079.30 --> 1082.58]  computer science in general. So I hope that that gives you an idea.
[1082.58 --> 1089.28]  Yeah, definitely. So following up on what you were just saying, Guillermo, it sounds like a ton of
[1089.28 --> 1095.50]  different knowledge from psychiatry that you're trying to kind of infuse in these algorithms and
[1095.50 --> 1100.40]  these techniques. It sounds like there's a bunch of different applicable NLP techniques,
[1100.60 --> 1105.62]  like you were just talking about semantic embedding and other things. I was wondering if you could just
[1105.62 --> 1112.24]  walk us through like what the data is like that you're actually gathering as far as both the features
[1112.24 --> 1117.80]  you're using for inferences and also the training. For example, you know, if you're getting audio,
[1117.94 --> 1124.42]  does that mean you're kind of gathering the audio in this question and answer sort of session and then
[1124.42 --> 1129.48]  converting, you know, doing kind of speech to text? So using a first model to get the text and then
[1129.48 --> 1135.02]  the text is input features to other models that do like the semantic embeddings or other things.
[1135.02 --> 1139.54]  Could you give us a little bit of a sense of that data flow and the structure and type of data?
[1139.54 --> 1150.08]  Absolutely. Yeah. So we work, as Adjie was saying, with either clinical interviews or speech samples that
[1150.08 --> 1159.42]  are gathered having clinical evaluation in mind. So we have a monologue speech samples. We have written
[1159.42 --> 1169.02]  text in some cases, and we also have a dialogue in other cases. And the context is that
[1169.02 --> 1177.36]  we either have semi-structured clinical interviews that seem to be the most effective. And by semi-structured,
[1177.36 --> 1184.94]  I mean, it's not following a very precise flow of a structural flow of questions and follow up,
[1184.94 --> 1193.58]  but not trying to nudge the patient into talking about something and expressing themselves. In other cases,
[1193.58 --> 1202.86]  we have monologues with anchor subjects, right? In some cases can be very short and we typically target
[1202.86 --> 1210.94]  naturalistic samples. So for instance, we ask the patients to talk about typical day in their life or
[1210.94 --> 1220.22]  how their week was or where they would like to go for vacation. Because the idea is that with those type of
[1220.22 --> 1228.22]  prompts, we can reuse them, as Adjie was saying, on a weekly or even daily basis so we can monitor their
[1228.22 --> 1236.06]  state. Then what we do with the data is, yeah, of course we have, in the case of speech, we have the audio files,
[1236.06 --> 1246.14]  and we process them as such. We extract voice features that are very well established in the
[1246.70 --> 1255.34]  field of voice processing. We extract features related to, for instance, the pause distribution,
[1255.34 --> 1262.38]  between words, the phoneme structure, something that's called the vowel space. It's how you pronounce your
[1262.38 --> 1269.34]  vowels that might be different, for instance, across different accents, even in the same language.
[1269.34 --> 1277.90]  And then on the lexical side, we extract the expected low level features so we can parse sentences
[1278.62 --> 1285.90]  into their grammatical components, right? So we can understand how verbs and nouns and adjectives
[1285.90 --> 1294.78]  are used and where in the sentence, and that has shown to be important in central conditions. We also
[1294.78 --> 1303.66]  extract, as I was saying, the idea of semantic embedding. So that allows us to take a word or
[1304.54 --> 1313.26]  sentence and have a notion of how similar that word is to other words. We can use target words that are of
[1313.26 --> 1320.62]  interest for the particular condition and understand how the patient is in their discourse, is getting
[1321.26 --> 1329.74]  closer in meaning or further in meaning for certain concepts that are relevant. And then we also extract
[1329.74 --> 1337.42]  higher level features. And those are more aligned with, as I was saying, concepts from psychiatry.
[1337.42 --> 1347.10]  Just to give an example, we have algorithms that can measure how metaphorical the content of a phrase is,
[1347.10 --> 1357.42]  and that is relevant in psychosis because one of the symptoms of psychosis is in disruption of your
[1358.14 --> 1364.54]  appreciation of metaphors, both in terms of how you understand them and how you produce them.
[1364.54 --> 1374.78]  So that gives you an idea of the full spectrum of features that we analyze, we study from the audio
[1375.74 --> 1380.22]  and from the text side of language.
[1380.22 --> 1386.22]  So Guishermo, that is quite a list of features that you're extracting, kind of going from the
[1386.22 --> 1391.18]  phoneme structure, vowel pronunciation, accents, a lot of the lexical stuff you just covered.
[1391.18 --> 1396.86]  Are there certain patterns that you have found through the data that have been more relevant
[1396.86 --> 1404.30]  than others that you're noticing seem to be weighted heavier in your analysis through NLP?
[1404.30 --> 1409.34]  Are there things that are sticking out as particularly important or has that been established?
[1409.34 --> 1419.50]  Well, what I would say is that language and even more speech production is such a complex
[1419.50 --> 1427.02]  phenomenon. It's so, you know, we know from computer science how difficult it is to deal with it,
[1427.02 --> 1434.70]  how difficult it is to produce a coherent language. It comes natural for us humans to do it,
[1434.70 --> 1444.14]  but any disruption in the health of your brain will have immediately an effect in language.
[1444.14 --> 1451.18]  So, like I said, even for conditions that are considered, traditionally have been considered
[1451.18 --> 1456.78]  motor disorders of Parkinson's, we know and we found, and we are not the only ones, we found
[1456.78 --> 1465.10]  very clear effects in language and even in content, right? So, even if you have something that supposedly
[1465.10 --> 1470.54]  is a motor dysfunction, the content of what you're producing as you speak is affected.
[1470.54 --> 1481.34]  So, yes, we can talk about CAMFUL maybe of features that seem to be popping up often. And one is the one I mentioned
[1481.90 --> 1489.98]  that we originally developed for psychosis, the idea of measuring flight of ideas as a semantic coherence.
[1489.98 --> 1497.34]  That seems to be useful to analyze different conditions and even situations in which,
[1497.34 --> 1506.46]  for instance, a patient may take a psychoactive drug like ecstasy or methamphetamine. But if I had to
[1506.46 --> 1515.34]  answer your question, I would say that every single aspect of language is affected or differently. But
[1515.34 --> 1523.42]  it's affected because, again, language is a very complex phenomenon that involves many, many different
[1523.42 --> 1530.46]  aspects of brain function. So, any tiny disruption will have an effect.
[1530.46 --> 1536.14]  Dr. David P. Another interesting thing that, you know, Gugermo focused on early enough and been very
[1536.14 --> 1543.10]  instructive for us is to really emphasize the spontaneous production of speech. So, basically,
[1543.10 --> 1548.94]  not go in the direction of some rote answer, but rather have the individual, you know, create an answer.
[1548.94 --> 1554.94]  The pre-existing context and answer doesn't exist in that person's mind yet. So, that spontaneous
[1554.94 --> 1559.82]  production is actually eliciting some of these features that he's describing, you know, enhancing the
[1560.62 --> 1566.14]  visibility of those features quite well. So, Gugermo, maybe you want to describe actually the picture
[1566.14 --> 1569.26]  test, which really is a very nice spontaneous production.
[1569.26 --> 1577.26]  Yes. Yeah, that's a very good example. So, we are studying actually a different number of conditions
[1577.26 --> 1588.22]  using this approach that was initially developed decades ago to study cognitive decline. And you can
[1588.22 --> 1595.18]  look it up. It's called the cookie theft task. And there are variations of that. And essentially,
[1595.18 --> 1604.06]  you're shown a picture. It's a drawing. It's a hand drawing of a typical, you know, 1940s, 1950s
[1604.06 --> 1613.42]  in this Americana household situation. There is someone who seems to be a mother doing the dishes,
[1613.42 --> 1621.10]  but she seems to be absent-minded. And there are two kids, a girl and a boy, and the boy is standing on
[1621.10 --> 1629.50]  the stool trying to get a cookie from a jar. So, the task is just to describe that in your own words.
[1629.50 --> 1638.30]  It's something that takes two or three minutes at most. It's very natural. And variations of that can
[1638.30 --> 1646.86]  be used to be repeated, you know, very often. So, you don't get bored. And what happens is that when you
[1646.86 --> 1657.02]  analyze the content, right, of that description of the task, what you say, what type of words you use,
[1657.02 --> 1663.66]  but also the structure, even the syntax of what you are saying, how you're constructing the sentences,
[1663.66 --> 1672.86]  and how flurried or how simplified your speech is, that contains a huge amount of information
[1672.86 --> 1682.06]  about your cognitive state. And that has been used by manual raters, like I said, over decades,
[1682.06 --> 1688.38]  to have an estimate of your cognitive state. But now we can do that in a completely automated
[1689.26 --> 1699.50]  way. And we have shown that we can infer the clinical scales that are produced by the human
[1699.50 --> 1706.54]  evaluators with a very high accuracy, with the advantage that we can do this remotely. And like I
[1706.54 --> 1714.14]  said, we can do this at a very high frequency, and without having to bring the patient to the hospital
[1714.14 --> 1721.34]  or the clinician to the house of the patient. And it has value that goes even beyond the idea of
[1722.30 --> 1728.86]  measuring or estimating cognitive decline, because it can be applied to many other conditions. Because
[1728.86 --> 1735.42]  as I was saying, even something that on the surface looks so natural as it's coming in such a picture
[1735.98 --> 1744.38]  requires a huge amount of brain real estate. And any failure will leave an imprint in the way that
[1744.38 --> 1750.30]  you perform these tasks. I think that leads into a question that's been kind of in the back of my mind
[1750.30 --> 1754.94]  through this whole conversation. I mean, you've mentioned that the way in which you gather data and kind
[1754.94 --> 1760.78]  of the spontaneity of it is really important. And that immediately kind of leads me to think about
[1760.78 --> 1766.54]  bias in data, both in terms of the way that you gather it, but you've also already mentioned like
[1766.54 --> 1772.22]  accents and language variety and that sort of thing. And we've already seen kind of, you know,
[1772.22 --> 1778.30]  disasters in healthcare scenarios where maybe you're trying to like, you know, diagnose skin lesions or
[1778.30 --> 1783.58]  something, and your data only has data from like light skin people or something. And I would guess that
[1783.58 --> 1789.58]  the same sorts of things exist in language in the sense that like both education level, maybe,
[1789.58 --> 1796.06]  but also regional accents, you know, second language, speaking people not speaking in their
[1796.06 --> 1800.06]  first language, all of those things kind of come into play when we start thinking about language.
[1800.06 --> 1806.38]  And I know IBM has also done a lot of work around fairness and bias. I was wondering if that has
[1806.38 --> 1812.78]  entered into this work yet, or is it something that you want to kind of probe further in the future?
[1812.78 --> 1819.34]  So, yes, of course, that we take that into consideration. And we try to account for
[1819.90 --> 1824.94]  those, I don't know to call them biases, but there's the context of the person, right?
[1825.34 --> 1833.42]  It's the personal context and even maybe the group context. Now, we have several cases in which
[1833.42 --> 1843.10]  we can track the patient over time. And for those, we have the best way of accounting for variances,
[1843.10 --> 1851.58]  because we have the history of the patient. So, in some of the studies that we have conducted,
[1852.62 --> 1858.46]  we know that if we didn't have the story, the context of the person, we could not get any results.
[1858.46 --> 1863.82]  Trivially speaking, for instance, if you don't know that the person is a male or female,
[1863.82 --> 1872.06]  the acoustic content would be confounded, right? So, when possible, we try to precisely have studies
[1872.06 --> 1880.70]  that track the individual. And that accounts to a large extent for those biases, as you mentioned.
[1880.70 --> 1888.14]  But also, it's really part of one of the goals that we are pursuing is that the possibility of
[1888.14 --> 1895.82]  personalizing the evaluation and eventually the treatment for a person, right? So, just being able
[1895.82 --> 1904.54]  to track someone on a daily basis that is taking a certain medication or following a certain treatment,
[1904.54 --> 1911.18]  it's one of the ultimate goals that we want to do. And in those cases, we have ways to account for
[1911.18 --> 1915.50]  the biases. This is much easier to account for the individual biases.
[1915.50 --> 1921.90]  So, Ajay, I'm curious, can you kind of describe what the output looks like here? Are we really
[1921.90 --> 1928.62]  talking about, you know, is there one diagnosis or do you have multiple diagnosis as an output? And what
[1928.62 --> 1933.74]  is your, what do your models look like to support that output? Is it different models for each diagnosis
[1933.74 --> 1938.22]  or one model to rule them all, as you might say? What is that output and how are you structuring
[1938.22 --> 1939.50]  your models to get to that output?
[1939.50 --> 1947.66]  Sure, yeah. Actually, just to continue for a second on the issue of language and bias,
[1948.38 --> 1953.42]  you know, the retrospective work that Guillermo has done, he already looked at several different
[1953.42 --> 1959.58]  languages and people speaking in their native languages, English versus Spanish versus Portuguese,
[1959.58 --> 1965.58]  and so on. So, I think that's very important to actually think of this science as well as its
[1965.58 --> 1971.98]  eventual use as being close to what the person already experiences and not actually take the
[1971.98 --> 1978.54]  person into some new territory where, you know, that distortion or bias is actually more pronounced,
[1978.54 --> 1983.42]  right? So, I think that's a research goal that we have to maintain is to actually make the technology
[1983.42 --> 1989.18]  work for the person and not the other way around. So, that is a quest that we are continuing on.
[1989.66 --> 1994.70]  But the retrospective work already shows us that that actually is possible. So, we are encouraged by
[1994.70 --> 1997.98]  the fact that we should be able to bring these technologies into different languages.
[1998.54 --> 2005.26]  Okay. So, to your question of, you know, how does results actually get reported and exactly what are
[2005.26 --> 2011.02]  we describing in that report? First, I would say that this is not really diagnosis. There's nothing
[2011.02 --> 2018.30]  clinically diagnosis-like that is being generated here. Rather, what we are doing is surfacing features
[2018.30 --> 2022.86]  that the clinician is already trained to look for and make sure that those features are actually
[2022.86 --> 2028.06]  visible to the clinician. So, the diagnosis and possible help to the patient, whether it is in
[2028.06 --> 2034.46]  terms of diagnosing or in terms of treating, is being done by the licensed expert practitioner.
[2034.46 --> 2041.02]  So, all that we are doing is using this tool. We are making sure that the patient's own experience
[2041.02 --> 2046.06]  is being captured sufficiently well. Features that are clinically relevant, like the ones that
[2046.06 --> 2052.14]  Kishen was describing, are actually being captured and surfaced. And it is on the basis of those features
[2052.14 --> 2057.90]  that a trained practitioner would actually then be prompted to do what they are trained to and
[2057.90 --> 2062.94]  license to do already. All right. So, this is augmentation, is not, you know, attempting to
[2062.94 --> 2067.90]  do what the practitioner does already, which is diagnose and treat. So, the report actually has,
[2067.90 --> 2076.38]  you know, both graphical as well as numerical and textual form of these features being surfaced,
[2076.38 --> 2082.22]  whether they are in a graph. So, the, you know, disjoint thoughts that Gigermo is talking of can
[2082.22 --> 2088.78]  typically be presented in a graph form. And so, you either have disjoint graphs or extremely complex
[2088.78 --> 2095.50]  graph that is actually demonstrating the complexity of the word choices and the context that the person
[2095.50 --> 2100.94]  is talking about. And a trained psychiatrist is actually then able to look at that and as they're
[2100.94 --> 2107.98]  accustomed to, use those features to actually then be able to make better decisions. So, the most easy
[2107.98 --> 2114.30]  way in which this might get used is for screening purposes. So, you're actually getting a psychiatrist
[2114.30 --> 2120.86]  in the future might actually be getting this kind of report just to keep tabs on what is happening in
[2120.86 --> 2126.94]  life of a person who needs to be watched. And you're using that to actually just watch and screen. And when,
[2127.50 --> 2132.38]  you know, it gets to a threshold of some concern, you're actually indeed intervening, the practitioner
[2132.38 --> 2137.42]  is at that point intervening and doing what they're trained to do. But now you actually have extended
[2137.42 --> 2144.30]  the observation to life of the person and you're able to observe more thoroughly and act upon it
[2144.30 --> 2150.14]  before it becomes catastrophic, right? So, I think that's the more likely usage here. Diagnosing and
[2150.14 --> 2155.42]  treating by itself is actually the hardest problem and that we really need to have practitioners do.
[2155.42 --> 2161.82]  Yeah. Yeah. I think that that brings things together really well and gives us a lot of great context for
[2161.82 --> 2169.18]  the use. And as we kind of wrap up here for the episode, I'd love to first off just thank you guys
[2169.18 --> 2175.58]  for working on some application of AI that really is making a positive difference for people. That's
[2175.58 --> 2183.26]  something that Chris and I always want to promote as much as we can. But I'd love to just get you guys
[2183.26 --> 2189.42]  to share as we kind of wrap up what you're excited about as far as either results that you have now or
[2189.42 --> 2194.62]  maybe next steps that you're going to. And then also for our listeners who are maybe more interested
[2194.62 --> 2201.42]  about this subject, either on the NLP side or the application side, where can they find out more about
[2201.42 --> 2206.14]  your work or the techniques that you're using? So, if you guys could give us a little bit of that
[2206.14 --> 2214.46]  perspective, that'd be great. Well, I have to say that what is keeping me up at night with excitement
[2214.46 --> 2221.58]  is work that we are developing around doing something similar to what we were describing,
[2221.58 --> 2233.74]  but in the context of therapy sessions with, again, the same idea of expanding and providing additional
[2233.74 --> 2243.18]  tools to the therapies to track the evolution of a patient that is undergoing some type of therapy
[2243.74 --> 2249.90]  and being able to integrate information from different sources that are relevant to
[2250.78 --> 2259.90]  the particular individual that is undergoing this therapy. I think this is one of our next frontiers
[2259.90 --> 2266.70]  and it's challenging, but at the same time very exciting. And you know, what excites me the most about this is
[2267.26 --> 2274.30]  a lot of the mental health as well as neurological conditions that individuals experience has really
[2274.30 --> 2283.10]  been either not attended to or being misdiagnosed and not the right kind of help provided or provided only in
[2283.10 --> 2289.74]  bursts and in acute situations, but not really more continuously. What we are witnessing through this
[2289.74 --> 2295.02]  work as well as all other things that are happening with Internet of Things and how technology is intersecting
[2295.02 --> 2301.18]  with our daily lives is a change that we are seeing and experiencing where the technology actually allows us
[2301.18 --> 2307.50]  to do things in a different way. But in this case, you know, going from episodic encounters in the clinic to a
[2307.50 --> 2313.90]  continuous measurement done in the convenience of your home and in your daily routine, what that does is
[2313.90 --> 2321.66]  actually brings attention and allows practitioners to actually address real issues that are beyond what is
[2321.66 --> 2329.26]  happening in the clinic. So it might extend the reach of help that people get. And that is a change. That is
[2329.26 --> 2336.06]  such a huge change for the positive because the unmet needs for mental health are huge. And, you know,
[2336.06 --> 2341.66]  using these kinds of technologies, one is actually able to hopefully increase the aperture through
[2341.66 --> 2347.74]  which these needs are addressed. So that change, I think, is very much for the positive. And, you know,
[2347.74 --> 2352.94]  people who do experience these conditions, whether it is anxiety, depression, cognitive decline,
[2352.94 --> 2359.02]  they need that help. And we are conceivably moving in a direction where that becomes possible for them.
[2359.02 --> 2363.90]  Well, Ajay and Guillermo, thank you very, very much for coming on to this episode.
[2363.90 --> 2370.06]  We will definitely put links to your papers out in the show notes so that our listeners
[2370.06 --> 2375.02]  can access those. If people want to find out more or reach out to you, how would you like them to reach
[2375.02 --> 2375.50]  out to you?
[2375.50 --> 2382.70]  So one place to get to is the IBM Healthcare and Life Science Research website, which features a lot of
[2382.70 --> 2389.82]  our breaking scientific news and including the work that Guillermo is talking of. And that's just at
[2389.82 --> 2396.06]  research.ibm.com slash healthcare and life sciences. And that's a good place to go.
[2396.06 --> 2400.86]  Fantastic. Thank you both for coming on the show. Wish you very well in this work. Goodbye.
[2400.86 --> 2403.26]  Thank you. It's a pleasure talking to you.
[2406.22 --> 2410.30]  All right. Thank you for tuning into this episode of Practical AI. If you enjoyed this show,
[2410.30 --> 2415.10]  do us a favor, go on iTunes, give us a rating, go in your podcast app and favorite it. If you are
[2415.10 --> 2418.94]  on Twitter or social network, share a link with a friend, whatever you got to do, share the show with
[2418.94 --> 2423.50]  a friend if you enjoyed it. And bandwidth for change log is provided by Fastly. Learn more at
[2423.50 --> 2428.06]  fastly.com and we catch our errors before our users do here at change log because of roll bar.
[2428.06 --> 2433.34]  Check them out at roll bar.com slash change log. And we're hosted on Linode cloud servers.
[2433.34 --> 2438.62]  Head to linode.com slash change log. Check them out. Support this show. This episode is hosted by
[2438.62 --> 2444.78]  Daniel Whitenack and Chris Benson. Editing is done by Tim Smith. The music is by Breakmaster Cylinder.
[2444.78 --> 2449.98]  And you can find more shows just like this at changelog.com. When you go there, pop in your email
[2449.98 --> 2454.86]  address, get our weekly email, keeping you up to date with the news and podcasts for developers
[2454.86 --> 2458.78]  in your inbox every single week. Thanks for tuning in. We'll see you next week.
[2464.62 --> 2469.42]  I'm Tim Smith and my show away from keyboard explores the human side of creative work.
[2469.42 --> 2475.34]  You'll hear stories sometimes deeply personal about the triumphs and struggles of doing what you love.
[2475.34 --> 2484.14]  Jumping off into the abyss is kind of my skill. And so I'm not saying that it's not scary. I'm saying
[2484.14 --> 2489.02]  that perhaps my skill is just not being able to estimate how scary it will be.
[2489.02 --> 2496.70]  New episodes premiere every other Wednesday. Find the show at changelog.com slash AFK or wherever you listen to podcasts.
