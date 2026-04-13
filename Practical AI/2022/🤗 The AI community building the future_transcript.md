[0.00 --> 4.64]  I feel like the most important thing on Hugging Face is actually Hugging Face Hub.
[5.04 --> 10.48]  So basically at Hugging Face, we are trying to solve open source machine learning in general.
[10.48 --> 12.90]  And this involves a couple of problems.
[13.28 --> 16.22]  Like one of them is reproducibility of your experiments.
[16.82 --> 27.34]  And also how easy to infer your models are such that people can just go and stress test your models and see if it works for your use case.
[27.34 --> 33.12]  The essence of the open source ML in general, that can your model actually be used by someone else?
[43.38 --> 51.26]  Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive, and accessible to everyone.
[51.62 --> 55.92]  This is where conversations around AI, machine learning, and data science happen.
[55.92 --> 61.68]  Join us at practicalai.fm slash community and follow the show on Twitter.
[61.88 --> 63.86]  We're at Practical AI FM.
[64.28 --> 68.90]  Thank you to our partners at Fastly for shipping our pods super fast all around the world.
[69.14 --> 71.00]  Check them out at fastly.com.
[77.18 --> 80.16]  Welcome to another episode of Practical AI.
[80.50 --> 82.02]  This is Daniel Whitenack.
[82.02 --> 85.16]  I'm a data scientist with SIL International.
[85.48 --> 90.78]  And I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed Martin.
[90.98 --> 91.70]  How are you doing, Chris?
[92.22 --> 93.44]  I'm doing okay, Daniel.
[93.56 --> 94.90]  It's so good to be talking to you today.
[95.16 --> 95.70]  It is.
[95.76 --> 96.66]  It's wonderful.
[96.92 --> 98.62]  It's a little bit of an odd day.
[98.72 --> 103.32]  I'm joining from a hotel in Dublin because I'm attending ACL,
[103.66 --> 108.96]  which for those that don't know is one of the big NLP conferences in the research world.
[108.96 --> 110.28]  And that's been fun.
[110.40 --> 115.82]  It's been tiring because I just forgot how tiring an in-person conference was.
[117.10 --> 119.78]  Is everyone else dragging around too?
[120.04 --> 121.60]  Are they all just kind of slumped over?
[121.80 --> 122.12]  I think so.
[122.22 --> 127.14]  There's not consistent coffee in all the places, which is unfortunate.
[127.64 --> 129.14]  So that's tough.
[129.14 --> 137.88]  But one thing that I have heard mentioned quite a bit at ACL consistently is Hugging Face.
[138.54 --> 145.04]  And we're really privileged today to have Merva from Hugging Face with us.
[145.08 --> 148.24]  She's a developer advocate engineer at Hugging Face,
[148.64 --> 152.98]  really creating a lot of great content on the web and great tutorials
[152.98 --> 157.20]  and also making really significant contributions on the open source side.
[157.60 --> 159.46]  I'm really excited to have you with us, Merva.
[159.94 --> 162.00]  I'm so happy that you have invited me.
[162.08 --> 162.94]  Thank you so much.
[163.36 --> 164.96]  Yeah, great to have you here.
[165.24 --> 169.98]  I'm wondering if you could kind of give us a little bit of the backstory
[169.98 --> 176.00]  of how you got connected with Hugging Face and NLP, maybe more generally.
[176.62 --> 180.62]  Like what was the state of sort of Hugging Face when you joined?
[180.62 --> 184.80]  Because we'll be talking a lot about like kind of how it's progressing in this episode.
[184.80 --> 187.60]  But I'm wondering kind of what its state was when you joined
[187.60 --> 190.16]  and what got you excited about it at that time?
[190.70 --> 191.38]  Great question.
[191.60 --> 197.70]  So I have met NLP at my senior year at the university, actually.
[198.24 --> 204.34]  And literally my first project was text mining and doing a classification
[204.34 --> 209.28]  using naive bias in R about climate change sentiments.
[209.28 --> 213.56]  You know, if people believe it or not, I have scraped some tweets and, you know,
[213.62 --> 217.10]  classified them in a data science class that I have taken.
[217.76 --> 220.06]  And I was like, I'm going to make this my job.
[220.26 --> 225.56]  And then I later joined to boot camps, did masters and, you know,
[225.86 --> 228.78]  started working somewhere as a machine learning engineer.
[229.46 --> 230.98]  You know, did everything I could.
[230.98 --> 236.70]  I worked two years as a machine learning engineer doing mostly natural language processing
[236.70 --> 239.44]  and also a bit of analytics on the side.
[239.88 --> 241.28]  I was building chatbots.
[241.54 --> 245.16]  I was doing information retrieval tools and so forth.
[245.34 --> 247.44]  And I was using Hugging Face back then.
[247.88 --> 252.52]  But prior to that, prior to building information retrieval tools
[252.52 --> 257.72]  and also like putting Hugging Face into my chatbot with the birth embeddings and such,
[257.72 --> 265.46]  how I met Hugging Face was that I have watched Thomas Wolfe's video on the future of NLP.
[265.74 --> 268.46]  And I was like, he's explaining it so well.
[268.46 --> 270.14]  And I have become a fan.
[270.46 --> 274.62]  And then once I have seen him posting about this sprint,
[274.84 --> 276.88]  community sprint on data sets.
[277.16 --> 279.42]  And I was like, can I join as well?
[279.46 --> 281.64]  And then I started contributing to Hugging Face.
[281.64 --> 286.20]  And then I later tried my chances with the audio sprint as well.
[286.44 --> 289.62]  And I was like, I met people over there.
[290.20 --> 294.04]  And I have learned a lot of things, like things like, you know,
[294.06 --> 297.54]  like they have taught me about CICD, styling, formatting,
[297.54 --> 299.88]  and contributing to open source actually,
[300.34 --> 303.84]  which is, it was my first time contributing to open source.
[303.84 --> 308.14]  And I was so excited when my first PR got merged.
[308.46 --> 312.06]  And I was like, you know, I kept helping other people out over there.
[312.14 --> 316.46]  And I was like, I'm going to be that person that is going to help people out in this.
[317.74 --> 319.80]  So that's, that's so amazing.
[319.80 --> 327.70]  I love that story because it is very intimidating for a lot of people to figure out that process
[327.70 --> 329.92]  of committing in open source.
[330.46 --> 333.22]  And of course, some communities are more welcoming than others.
[333.22 --> 335.58]  I know Hugging Face is, is very welcoming.
[335.58 --> 338.44]  And there's a lot of great discussion that happens and all of that.
[338.44 --> 341.86]  But this is a little bit off topic, but I think it's on, on topic,
[342.34 --> 345.32]  at least as far as the open source side of Hugging Face.
[345.32 --> 350.94]  But what, what sort of advice would you give people that are looking maybe to
[350.94 --> 357.06]  start contributing to the open source side of data science or machine learning or
[357.06 --> 361.12]  that side of, of the world, the, the open source community,
[361.12 --> 366.08]  that maybe not even just with Hugging Face, but there's so many great tools out there,
[366.16 --> 373.28]  whether it's, you know, Spacey or TensorFlow, it's, you know, itself or all sorts of things.
[373.28 --> 380.52]  So basically libraries like scikit-learn or, you know, Hugging Face transformers
[380.52 --> 386.86]  occasionally have sprints in which the contributors are, you know, talking to you,
[387.00 --> 391.26]  you know, they are giving you issues or like if there is a, for instance,
[391.26 --> 396.34]  like if we are going to train models, there is a list of languages that the models need to be trained on.
[396.34 --> 400.92]  And then there's a data set. So all you have to do is to actually train the model and,
[400.92 --> 406.38]  you know, improve it. So there are a couple of sprints also same with scikit-learn.
[406.38 --> 411.56]  As far as I know, you know, get, you can get help from contributors actively rather than being in
[411.56 --> 419.22]  async in GitHub. And I would suggest to be, you know, aware of those sprints and community events.
[419.22 --> 425.52]  Like in Hugging Face, we have a lot of them. For instance, recently we had like a sprint about
[425.52 --> 431.02]  renewing the docs and adding type hints and other stuff for the TensorFlow side of transformers,
[431.10 --> 439.22]  which was a good, good first contribution in my opinion. So I think sprints are a good way to begin
[439.22 --> 445.02]  with. And other than that, it's just good first issues on the repository.
[445.02 --> 451.74]  You mentioned that you were kind of building chatbots before joining Hugging Face. Could you
[451.74 --> 459.12]  tell us a little bit more about that and like maybe how that shaped what you perceived as what was kind
[459.12 --> 465.56]  of needed in NLP tooling? It sounds like you found a lot of what you thought was needed in terms of
[465.56 --> 471.12]  Hugging Face and transformers, but how did that process of like trying to build a chatbot, what did
[471.12 --> 477.80]  that teach you or help you learn or maybe introduce to you in terms of challenges for people wanting to
[477.80 --> 478.72]  do that sort of thing?
[479.40 --> 484.40]  So it heavily depends on what you're building, actually. So in my first job, I was building an
[484.40 --> 490.30]  automation bot that was, you know, like talking to you and automatically creating an appointment for
[490.30 --> 496.62]  you or cancel your appointment in the background for us for service companies. And over there, I was
[496.62 --> 505.36]  mostly doing machine learning part. It is usually about how you solve the text classification problem
[505.36 --> 512.66]  and improve your data. I was using Grouse open source. And if you are having a narrow domain chatbot,
[512.66 --> 518.10]  like I don't know, pizza ordering chatbot or whatever, it's a very easy to solve problem because
[518.10 --> 524.06]  mostly you are solving a text classification problem at the end, trying to understand the end user.
[524.06 --> 532.32]  And like to iterate over your model and everything, it's easy. For my second job, it was really hard
[532.32 --> 537.90]  because like I come from an, you know, like applied math operations research type of background,
[537.90 --> 544.96]  and I do not have any developer background. And I had to do the API side and, you know,
[545.08 --> 551.16]  learning Flask and everything. I was doing both the backend and the chatbot itself. And I was also
[551.16 --> 558.24]  building this tool that was, that helped the, we had some researchers, the chatbot was about,
[558.42 --> 565.00]  you know, like it was like a friendly chatbot sort of like replica, but you could ask questions to it
[565.00 --> 571.10]  about your life standards, or like, you can ask questions like, Hey, I cannot sleep. What can I do
[571.10 --> 578.48]  about it? And we had like a researcher team that was looking into these answers in the papers and
[578.48 --> 583.78]  looking for statistical evidence that certain thing is good for your health. But the chatbot was
[583.78 --> 589.20]  rather so hard to make because basically conversational agents are divided into two.
[589.36 --> 596.32]  You have stuff like BlenderBots, DialogPT, generative models that basically you can talk about anything
[596.32 --> 604.16]  like T0, whatever. The second part is chatbots that are based on intent and action, which is like,
[604.16 --> 610.24]  you have to write your own training data. It's not anything like zero shot or whatever.
[610.78 --> 618.08]  You have to define all of your actions to every single intent. It's hard to make a generalization
[618.08 --> 622.62]  over this and still be in control of what your bot is going to say, because we know that these
[622.62 --> 631.56]  language models are a bit biased. You know, they tend to be sexist, racist, rude sometimes. So like,
[631.56 --> 638.10]  it's a hard problem to solve. So that's why I kind of quit on doing that because like, I kind of gave,
[638.10 --> 646.02]  I would rather, you know, work in a, you know, chatbot that had narrower domain because like,
[646.12 --> 652.14]  it's not solvable basically without language models. And like with language models, I would rather not
[652.14 --> 658.94]  put a language model in front of an end user freely with no filtering or whatever. So,
[658.94 --> 667.14]  and I also like help them out. Like there was this research team and I have built a tool that would,
[667.18 --> 671.90]  you know, answer their questions from the research papers. And for that, I have used sentence
[671.90 --> 678.04]  transformers, which I was using through hugging face. Like first time I can, I cannot forget how I
[678.04 --> 684.80]  use pipeline for the first time. And I was incredibly amazed on, I was like, it's just one line of code and I
[684.80 --> 691.02]  can just get answer to my question. I just passed my model. I, this, I have fine-tuned a model based on
[691.02 --> 697.62]  some, um, basically there was this biomedical birth and I have fine-tuned it on some tasks for
[697.62 --> 703.36]  information retrieval and I called pipeline and I was like, is this for real? Like, does this actually
[703.36 --> 710.20]  work? And I was pretty amazed. And then later I looked into it and I was like, they made an
[710.20 --> 716.50]  abstraction over, you know, all of the, you know, pre-processing inference and post-processing
[716.50 --> 723.06]  and put it in a box. And like, how smart is this? You know, it's like an engineering, uh, marvel,
[723.22 --> 728.24]  you know, like it's just amazing. So I had a totally different follow-up question a minute ago,
[728.30 --> 733.12]  but I'm actually wanting to ask you about this. I think a lot of the folks that we talked to on the
[733.12 --> 737.78]  show have come from developer backgrounds and they're kind of, you know, they kind of already have that
[737.78 --> 741.54]  and they're moving into other skills and you've come in the reverse way from that.
[741.74 --> 747.18]  And you kind of had this, this moment there. What was the hardest thing as you were transitioning
[747.18 --> 752.38]  into this skillset, you know, as you're talking about this history and that was kind of an awe
[752.38 --> 758.44]  moment that you had was the hardest thing that what it took to kind of move into being able to be
[758.44 --> 764.04]  productive. So basically in my previous job, I was just shipping stuff and, you know, like my,
[764.04 --> 770.36]  you know, quality of my code wasn't nitpick and everything to like, you know, my PRs weren't
[770.36 --> 778.82]  passing very, you know, in a long time. So in here, because we are working in, I am working with,
[779.06 --> 787.62]  you know, like a very big teams and very big code bases. I can see how I can refactor things or,
[787.82 --> 792.92]  you know, like how can, how I can improve things. So I'm mostly learning development in a way.
[792.92 --> 799.46]  And also like how UX matters. That's a very, like, I feel like it's a billion dollar question,
[799.60 --> 805.58]  how you handle your UX and how you develop tools. Because like most of my time at Hugging Face is
[805.58 --> 813.38]  actually passing with either developing a tool for people on the Keras side. I recently started
[813.38 --> 819.26]  working on scikit-learn as well. On the other side, I'm just, you know, building fancy demos to
[819.26 --> 825.22]  showcase people what transformers can do or like other, you know, like libraries can do
[825.22 --> 831.52]  for, you know, machine learning in general. So I have realized later on that UX actually
[831.52 --> 839.10]  is hard when you do not come from that background. And also how you can improve your code. It's just
[839.10 --> 844.56]  endless. Like there will, there will always be someone nitpicking your code and it's just the
[844.56 --> 851.64]  most beautiful thing because you keep learning from that. So I am just grateful to work here. And
[851.64 --> 858.80]  I, I feel like I did improve myself from the start, but it was like, at first it was hard because
[858.80 --> 865.70]  previously I was only optimizing my models and, you know, nobody questioned my code, you know, that much.
[865.70 --> 890.36]  Merva, you, you've already mentioned like a number of things that I'd love to dig into a little bit
[890.36 --> 897.44]  deeper because there's all sorts of pieces of the puzzle that fit into sort of what hugging face
[897.44 --> 903.80]  is and the ecosystem. I was wondering if you could kind of help us just like set the stage for this
[903.80 --> 911.80]  discussion with, you have hugging face, you have sort of model and data set stuff, you have transformers,
[912.00 --> 917.60]  somehow Keras, and like you even mentioned scikit-learn. Could you just kind of give us an overview of
[917.60 --> 923.74]  like, you know, how you would see the hugging face ecosystem and how the various pieces fit together?
[924.50 --> 933.12]  Yeah, sure. So like what hugging face is working on, like if you were to ask to a random person in
[933.12 --> 938.96]  the company, I feel like the answers would differ, but I feel like the most important thing on hugging
[938.96 --> 944.96]  face is actually hugging face hub. The reason why is because it's, so basically at hugging face,
[944.96 --> 950.42]  we are trying to solve, you know, open source machine learning in general. And this involves a
[950.42 --> 959.48]  couple of problems, like one of them is reproducibility of your experiments. And also how easy to infer your
[959.48 --> 966.26]  models are such that people can just go and stress test your models and see if it works for your use
[966.26 --> 972.24]  case. And another thing is, you know, like the essence of the open source ML in general, that can your
[972.24 --> 980.96]  model actually be used by someone else for their own use case, which is not likely for the most of the,
[980.96 --> 986.68]  you know, like tasks like tabular data related stuff. But, you know, it applies for computer vision
[986.68 --> 994.86]  tasks, audio classification tasks, at least within language, or it applies for NLP because your features
[994.86 --> 1001.52]  are usually universal. If not, it's language specific, but, you know, for at least for computer
[1001.52 --> 1008.30]  vision, you can do, you can just go ahead and just pick a object detection or like image segmentation
[1008.30 --> 1014.04]  model and use it in your use case. So with the hub, we are actually trying to do this and we want to
[1014.04 --> 1021.58]  have, we want to get people to declare the limitations of their model, declare the biases in their model,
[1021.58 --> 1029.14]  so that we can have good open source models on the hub. And we don't only have transformers on the
[1029.14 --> 1034.62]  hub, we have like various libraries. So for instance, we host the Stanza models from Stanford NLP.
[1035.20 --> 1043.40]  We have Keras models, like we are integrating various libraries, LNLP, Keras, PyTorch image models,
[1043.40 --> 1051.26]  you name it. For instance, with spaces, what we want to do is we want to get people to see
[1051.26 --> 1057.62]  if a thing is possible. Like for instance, I can just demonstrate a very small thing,
[1057.78 --> 1065.02]  like a product and do a POC to my colleagues. There are like a couple of use cases and things
[1065.02 --> 1072.46]  you can use hugging face up for your end-to-end workflows. But like my favorite thing inside is,
[1072.64 --> 1078.40]  I think, spaces right now because I'm a master's student. Most painful thing for me,
[1078.40 --> 1085.64]  and I know for the TAs and professors is to actually reproduce my project and, you know,
[1085.70 --> 1090.98]  like setting up the environments, you know, running it and, you know, like you have to specify how to
[1090.98 --> 1095.88]  do that instead. Like, you know, I'm just sending them the spaces link of my project. For instance,
[1095.88 --> 1102.72]  this year I have, you know, like Fourier transform space with Streamlit and I have just sent it to
[1102.72 --> 1108.94]  them. It's also good for, you know, like in my previous job, I was like a machine learning engineer
[1108.94 --> 1115.90]  and I have built like in my first job, I was looking for ways to just put my model out there.
[1116.40 --> 1122.86]  And I had zero idea how to use Flask or, you know, like right front end or whatever. Like it was so hard
[1122.86 --> 1129.40]  for me. Like, why would I be spending my time? Like, especially if you're in a startup, like you do
[1129.40 --> 1136.30]  everything. Why would I spend my time just to, you know, it's, it's, I'm not even putting this into
[1136.30 --> 1142.90]  production. I just want to showcase this to a client or like, you know, the end user. Like, why would I
[1142.90 --> 1150.30]  spend most of my time just trying to put this over there through, I don't know, like just build a demo,
[1150.30 --> 1157.54]  like that doesn't even look good with, I don't know, Flask and just channel it with NG Rock or
[1157.54 --> 1164.36]  whatever. I think when I was on board, being on board, that spaces wasn't better and like not so
[1164.36 --> 1171.00]  many people had access to it. When I discovered, you know, spaces and Streamlit and Gradu, and I was
[1171.00 --> 1178.12]  like, this really touches many pain points on that side, especially if you're a data scientist,
[1178.12 --> 1184.80]  most of the data scientists are actually statisticians or, you know, math folks who do
[1184.80 --> 1192.20]  not have development background, but are working in startups. So it's actually very smart to just
[1192.20 --> 1199.30]  write like five lines of codes and just drag and drop your app.py file into spaces and voila,
[1199.36 --> 1206.14]  you can just show it to your clients or your end user or your teacher or your family or your favorite
[1206.14 --> 1211.86]  pets. I have a question that is, you've been taking us through this and it kind of almost
[1211.86 --> 1216.32]  starts with the fact that as a, you know, kind of having gotten to the expertise that you've gotten
[1216.32 --> 1221.18]  to, but you've kind of taken us through this development as you've taken this journey of
[1221.18 --> 1228.00]  learning and the ecosystem around Hugging Face has grown tremendously over that time and the tools are
[1228.00 --> 1233.70]  getting amazing. And as you are communicating this to people who are getting into it, you've got a big
[1233.70 --> 1239.00]  challenge just to communicate the ecosystem and all the things that are available, but how do you also,
[1239.66 --> 1244.36]  you clearly from, from what you were just talking about, kind of remember that beginner's mind.
[1244.58 --> 1251.46]  And so as you're bringing new people into the community and teaching them how to be effective
[1251.46 --> 1256.74]  and productive in what they're doing with within the ecosystem, how have you managed to stay grounded
[1256.74 --> 1261.76]  in that way so that you can accomplish both? You can, you can sync with them at that beginner level
[1261.76 --> 1265.64]  and yet you can get them up to that point where they can run themselves.
[1266.18 --> 1271.00]  It's really hard actually, because there is so many good stuff in the ecosystem. It's just
[1271.00 --> 1276.48]  understanding, you know, the user journey and like what they are going through and trying to touch where
[1276.48 --> 1282.76]  you can fix their problems in their journey. So Hugging Face recently started to invest in
[1282.76 --> 1289.68]  tabular data as well. And like, because I was previously a data scientist, I know what an average data
[1289.68 --> 1296.44]  scientist does. And I think like a couple of things you can do is, for instance, use datasets library to
[1296.44 --> 1303.92]  host your datasets, which in most of the platforms, you cannot host datasets that's more than a hundred
[1303.92 --> 1309.42]  gigabytes, by the way. And Hugging Face datasets allow you to do that. And you can even stream your
[1309.42 --> 1315.32]  dataset. You know, like take your dataset, just do like an exploratory data analysis. You can,
[1315.32 --> 1323.12]  if you want to do a presentation and if you don't want to show people notebook, you can do that through
[1323.12 --> 1331.10]  streamlets or Gradio, like, you know, graphs about your data or like a profile. And then after that,
[1331.12 --> 1336.82]  you can just train your model and push it to the hub and build a space for it so that you can show
[1336.82 --> 1342.34]  what your model is capable of. You know, you can just put your baseline and see, like,
[1342.34 --> 1350.98]  let people test it so that it works. So I feel like the answer changes a lot according to what you
[1350.98 --> 1357.64]  are working on and like what side you are on, on the equation. Like, are you a machine learning
[1357.64 --> 1363.74]  engineer? Are you a data scientist? Also like it changes according to the person you are asking to,
[1363.86 --> 1371.00]  but I am, I really like to ask people about their journey and see what type of problem we can solve
[1371.00 --> 1376.50]  with that. So for instance, for end-to-end things, it's more like that. On the other hand, if you're,
[1376.56 --> 1383.52]  you know, an LP person, you can again, like take a dataset, train a model with transformers.
[1384.02 --> 1390.96]  Like for the previous use case, you cannot do much with transformers because it's not used much in the
[1390.96 --> 1396.66]  table or data, but like we have a couple of integrations for the, you know, various libraries.
[1396.66 --> 1402.02]  And I can say like, for instance, type of problems we are solving are like, for instance,
[1402.64 --> 1408.38]  we want you to reproduce your experiments. And like, we want other people to know that models
[1408.38 --> 1414.30]  have limitations and everything. So for instance, currently what I'm working on, on the hub is
[1414.30 --> 1420.08]  for the scikit-learn at least, we, I want to, you know, enable collaboration for scikit-learn.
[1420.08 --> 1426.84]  Like I am currently designing automated model cards for scikit-learn in which it automatically
[1426.84 --> 1435.00]  produces model cards that has your models attributes today, also the datasets attributes.
[1435.16 --> 1441.16]  I have done the same for the Keras. And for instance, I have put inside metrics, you know,
[1441.22 --> 1447.96]  from model history, I have put models architecture using graphes. Like you can also have like
[1447.96 --> 1456.74]  tensor board logs and you write like one line of code to just push your model to the hub and let
[1456.74 --> 1464.00]  it host your tensor board logs and your model card over there. And if sometimes like if your model is
[1464.00 --> 1471.66]  working out of the box, then there is an inference widget as well. Same way you can just with one line
[1471.66 --> 1478.30]  of code, you can just load your model. Yeah. Like we want to tackle reproducibility this way so that
[1478.30 --> 1485.88]  people know that this model has this metric, it has this hyper parameters that this, you know,
[1485.94 --> 1494.68]  training, we want to version them this way. So for NLP, again, you can just train a model,
[1495.44 --> 1500.96]  push it to the hugging face hub and just, you know, like the inference widget opens or like you can build
[1500.96 --> 1508.24]  a demo with again, very few lines of code because like a Gradio, for instance, Gradio has the same
[1508.24 --> 1513.64]  philosophy as transformers. I would say it has something called pipe. It's leverages hugging
[1513.64 --> 1520.76]  faces pipelines to load an interface. So when you call interface that load on a model, it automatically
[1520.76 --> 1526.50]  knows what type of inputs that model takes, what type of output that model takes. It will just
[1526.50 --> 1535.48]  create the interface for you in one line of code. I'm always amazed by the abstractions done to save
[1535.48 --> 1542.94]  your time as a developer. You know, I think every user has a different story with like, I would first
[1542.94 --> 1548.96]  get to know the person and tell them, you know, Hey, you can do it like this. And just like, you can
[1548.96 --> 1553.86]  utilize hugging face hub like this because otherwise it's incredibly distributed. Like there are so many
[1553.86 --> 1561.52]  things in the ecosystem. I have also done a project called hugging face tasks. I am still maintaining
[1561.52 --> 1566.92]  it. So I have come up with this when I was on board that. So basically I have worked with a lot of
[1566.92 --> 1573.42]  software developers who wanted to build machine learning products. And I know that these people,
[1573.64 --> 1580.76]  they just need to know basic Python. Like if they want to do a POC to a data scientist to actually
[1580.76 --> 1587.16]  express what they want, because they do not need to like for the, for the POC, they do not need to
[1587.16 --> 1593.86]  know much about machine learning. So all they have to do is just to go to hub and, you know, filter the
[1593.86 --> 1600.12]  models, find the model according to their use case and just call pipeline or inference API on it.
[1600.12 --> 1610.26]  So most of the people do not know that. And, uh, they also do not know what the tasks are capable of,
[1610.26 --> 1615.36]  like what you can do with an object detection model or what you can achieve with a name density
[1615.36 --> 1622.06]  recognition model. So I wanted to show them, Hey, if you want to build X products, then you can just
[1622.06 --> 1629.24]  filter for these models and just call pipeline on that model and use it and like check the models
[1629.24 --> 1634.92]  metrics, you know, like if this metric is on this level, then this means that model is good.
[1635.36 --> 1641.90]  This model takes X as an input and outputs Y as an output. So that's why you can use it for,
[1642.10 --> 1647.10]  I don't know, information retrieval. It's also a bit complicated from the machine learning side,
[1647.24 --> 1654.30]  so many fancy things going on, but you actually do not know to need all of that. You just need to know
[1654.30 --> 1662.40]  which task is suited for you and you just need to call it. I have developed this with this beautiful
[1662.40 --> 1671.04]  team of developers and, uh, we have released that around, I think it was around January or February.
[1671.70 --> 1676.88]  I just want to, you know, just go and tell every single software developer, Hey, you just need to
[1676.88 --> 1681.34]  know this and you do not need to learn machine learning from scratch.
[1706.88 --> 1714.22]  So Merva, I, I can definitely hear like just the great respect that you have for, for your team and
[1714.22 --> 1720.04]  also like this collaborative environment that you're obviously a part of. And I know that, um,
[1720.04 --> 1725.32]  even just today, the day that we're recording this anyway, Hugging Face, you know, announced
[1725.32 --> 1731.98]  more collaborative features and community features on the hub. I was wondering kind of from your
[1731.98 --> 1737.38]  perspective and how you've like grown to work internally with the Hugging Face team on different
[1737.38 --> 1742.14]  models and different tools and that sort of thing. What are you excited about in terms of the
[1742.14 --> 1748.32]  collaborative features of Hugging Face and what this might enable for the future of the hub?
[1748.94 --> 1758.24]  Good question. So we have announced the pull requests and the community feature today in which you can
[1758.24 --> 1763.62]  open a pull request to someone else's repository and this repository can be a model repository,
[1763.62 --> 1769.88]  which it contains model and the model files like, you know, configuration or tokenizer.
[1770.16 --> 1778.68]  If it's an NLP model, it has model card that improves reproducibility and open source machine learning.
[1778.68 --> 1785.46]  You have data set repositories in which you have data sets, cards and data sets themselves,
[1785.46 --> 1792.70]  or it can be a space repository in which it has the application file. Or if you do not host your
[1792.70 --> 1800.00]  model on Hugging Face, it might have your model. So this way people can improve each other's works
[1800.00 --> 1805.64]  like we do in GitHub. So in here, we do not want to actually duplicate work of GitHub,
[1806.18 --> 1811.82]  but given Hugging Face is mostly focused on models and, you know, the infrastructure as well,
[1811.82 --> 1818.32]  like we use Git's large file system to host models and data sets that are very big. Previously,
[1818.32 --> 1825.70]  we were versioning data sets and versioning, you know, models, data set spaces. Like why not
[1825.70 --> 1834.12]  do pull requests on them? So this might mean like, for instance, I have a big TensorFlow model and
[1834.12 --> 1840.36]  people want to use in PyTorch or for instance, you know, someone has a PyTorch model, they want to,
[1840.82 --> 1846.88]  but I want to use it in the TensorFlow ecosystem because TensorFlow has like nice production level
[1846.88 --> 1855.16]  tools in the TensorFlow extended. So if I want to, like, I can just port it, but like, if I also want
[1855.16 --> 1862.30]  to contribute those weights to the repository, then I can just do that. Like I can just open a pull request
[1862.30 --> 1869.10]  in order to contribute those TensorFlow weights to that repository. Or if someone has, has a space
[1869.10 --> 1877.10]  that is broken or needs to be improved, I don't know, like by means of anything, like needs a
[1877.10 --> 1882.26]  description or something like that, or like limitations that I have found in that space.
[1882.52 --> 1889.36]  If it has a bias that I have stress tested and needs to be declared, then I can just open a pull
[1889.36 --> 1895.20]  request or just, you know, discuss that, Hey, I have found this bias in your model. And like,
[1895.28 --> 1901.74]  either like, let's declare this or, you know, try to improve the model. Or if I have a data set,
[1901.80 --> 1908.04]  then I can just change, I can just tweak stuff in the data set itself and just contribute that.
[1908.26 --> 1913.40]  And also have like discussions regarding the models, because like, for instance, like if someone
[1913.40 --> 1920.02]  has a specific model that has, that is using a different, different mask token or whatever,
[1920.18 --> 1924.86]  they are, if they are inference, which is problematic, I just want to go and tell them,
[1925.28 --> 1929.80]  Hey, you can improve your model like this, or you can improve your space like this. If you were to
[1929.80 --> 1934.82]  cache this function, then your space would be faster. You know, I just want to go and tell them
[1934.82 --> 1940.30]  that, but I cannot, I wasn't able to do it because like, there was no way except for, you know,
[1940.30 --> 1946.02]  like there's a Twitter handle on the people's profiles, which I think like, if I were to just
[1946.02 --> 1954.04]  go and tell them, it would be a bit creepy. So it's nice that we have like, now, now we have a
[1954.04 --> 1959.14]  discussion section, which I can, you know, just tell people, Hey, if you were to do this, you know,
[1959.22 --> 1964.48]  your, that would be faster. Or if I, I can just open a pull request and let them see
[1964.48 --> 1970.80]  how their space is improved because then they can just clone and just pull and just,
[1970.80 --> 1976.98]  you know, serve it on their local or just make another space and just see before merging that
[1976.98 --> 1982.76]  how their work would look like, how my work looks like on their space or model.
[1983.16 --> 1988.18]  Yeah. I'm curious, you know, I think that'll be a really big change because, you know, you've
[1988.18 --> 1995.18]  referenced GitHub and if you think about what GitHub did for the open source world by coming
[1995.18 --> 2000.86]  into being, Git was already there, the social aspect and that collaborative aspect, it fundamentally
[2000.86 --> 2004.88]  changed the community worldwide. Like, I mean, it was not the same thereafter.
[2005.26 --> 2011.16]  Yeah. How do you envision the social changes or what are you aspire to or hope for,
[2011.26 --> 2016.16]  for the changes based on this? Do you think it will propel the community in the same,
[2016.16 --> 2021.78]  that same kind of massive shift that we saw in the, in the broader open source world?
[2022.20 --> 2025.02]  For GitHub, it's literally my favorite social media.
[2027.84 --> 2028.88]  Probably all of us.
[2028.96 --> 2030.56]  Good analogy, Chris. Yeah.
[2031.34 --> 2036.62]  I just love, you know, like how to follow people and, you know, see what they are starring,
[2037.04 --> 2043.46]  you know, to see interesting projects over there. And I feel like at some point we might evolve
[2043.46 --> 2047.94]  to that as well, you know, someone else stars a space and, you know, like that's a really
[2047.94 --> 2054.44]  interesting one. So let me just go and look. And like, even more like maybe like, I don't know,
[2054.44 --> 2062.00]  messaging or whatever. I am not in control of this. I just know that, you know, like we are also trying
[2062.00 --> 2069.50]  to somehow like increase the collaboration. And that's what GitHub actually achieved. Like
[2069.50 --> 2077.46]  there are awesome libraries out there where people contribute to, but for machine learning side,
[2077.60 --> 2083.70]  it's not the optimal thing to use. Like for instance, recruiters or like technical interviewers,
[2083.82 --> 2089.24]  they wouldn't go to all of my GitHub machine learning projects. And even if they did, they
[2089.24 --> 2095.30]  won't understand anything. But like, for instance, I have spaces in which someone could just go ahead
[2095.30 --> 2100.84]  and see that, Hey, this person is actually doing in this space, what I'm looking for,
[2100.90 --> 2107.66]  how did they achieve that? And maybe I should hire them or just, you know, hosting model weights,
[2107.98 --> 2113.24]  like very heavyweight model weights and just, you know, like cloning them is a pain. Like,
[2113.30 --> 2118.68]  why would I just want to clone everything in a repository? That is a, that is a model. Like,
[2118.68 --> 2126.38]  I would love to see if that model works first through a widget or space and just do that.
[2127.00 --> 2135.42]  So for that side, it's more optimal and we are looking for ways to increase the collaboration and
[2135.42 --> 2142.14]  like give people more, uh, like a better UX in collaboration with features like this. And also
[2142.14 --> 2148.46]  excited to see, uh, what's next. I feel like the, what's next is, you know, notebook weaver,
[2148.46 --> 2156.34]  and such. I'm quite excited for that. So let's see what happens. I am like, I am not full in full
[2156.34 --> 2162.76]  control of the hub roadmap, but like, it's mostly about the collaboration. Yesterday there was another
[2162.76 --> 2169.94]  feature launched and it was, so in model cards, you have a metadata section in which you define,
[2169.94 --> 2177.32]  you know, languages and everything. You can also define the models that are in a specific paper.
[2177.32 --> 2184.74]  It redirects you to the paper itself where you can see which model is actually there. So,
[2185.42 --> 2192.40]  you know, again, uh, we are also investing in evaluation. So sort of like papers with code
[2192.40 --> 2199.12]  leaderboards in which you can see, you know, which model is state of the arts in the task,
[2199.20 --> 2204.48]  in the hugging face hub. So you can directly use that model. It's, it's more about, you know,
[2204.48 --> 2212.36]  evaluating the model and doing a leaderboard style thing. It's mostly about, uh, I, again,
[2212.44 --> 2217.98]  like open source machine learning, what we are trying to do rather than social media network,
[2217.98 --> 2221.16]  but it's might evolve that way.
[2221.16 --> 2229.50]  Yeah. I, uh, have a digression that includes an ACL story. Um, I forgot who I saw on Twitter
[2229.50 --> 2234.10]  yesterday. I forget who from hugging face said we're going to announce something tomorrow. And I
[2234.10 --> 2239.74]  said, Oh, great. I'll, you know, I'll check. Yeah. Julian. Yeah. So I was like, okay, I'll check,
[2239.82 --> 2245.24]  but I was in talks most of the day. Right. And the one talk, the last talk I went to today was
[2245.24 --> 2250.40]  called quality at a glance. It was from the Masakane group, um, which works in African languages,
[2250.98 --> 2257.56]  Yulia and, um, others. And, uh, they were analyzed a whole bunch of open data sets,
[2257.82 --> 2263.88]  crawled data sets that are on, you know, hugging face as well, but they're sort of used widely.
[2263.88 --> 2269.86]  And they looked at the quality of those data sets and found very, very interesting and disturbing
[2269.86 --> 2276.90]  things. Like I think in common crawl aligned, there's certain languages, all of the data in
[2276.90 --> 2283.06]  that language is not in that language. Like 0% of the data labeled in that language is in that
[2283.06 --> 2290.86]  language. So one of those I think was like the Romanized Arabic, um, includes 0% Romanized Arabic.
[2291.06 --> 2295.40]  I was like thinking about this as I was leaving ACL. And then I was like, Oh yeah, I got to check,
[2295.40 --> 2300.12]  you know, Twitter to see what hugging faces thing is. And then I looked and it was like,
[2300.12 --> 2305.72]  make PRs on data sets. And I was like, Oh, I need to like circle back around and go right back in
[2305.72 --> 2311.40]  there and like, talk to them about how we can get some PRs on like, uh, CC aligned and other data
[2311.40 --> 2316.88]  sets. So it was just like perfect. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Someone else can just open a,
[2316.88 --> 2319.88]  open a discussion about how that language doesn't contain.
[2319.88 --> 2327.32]  We, we do, we do like, we have like a really great ethics team. Like you probably know them. We
[2327.32 --> 2336.04]  have Meg, we have Sasha, we have Yasin, like, uh, they are just doing amazing work. We recently have
[2336.04 --> 2344.76]  Jada and like every time something happens, like we see an inappropriate use case around humans, for
[2344.76 --> 2352.44]  instance, like the, the use cases around the like personal identifiable information is actually
[2353.08 --> 2361.64]  sometimes problematic. We do stress tests, uh, the spaces and models to, you know, reach out to the
[2361.64 --> 2369.32]  people, Hey, you know, your model might have bias. Would you declare it? So we do actually care about
[2369.32 --> 2376.68]  the limitations around models and also ethical restrictions regarding, you know, you know,
[2376.68 --> 2385.40]  biases, personal information and everything as much as we can. So yeah, it's a hard problem to solve
[2385.40 --> 2391.72]  because it's all philosophical. Like in the end, like ethics is a bit philosophical, but like how you
[2391.72 --> 2399.48]  can actually put that in practice is a big question. And in case of hugging face hub, we do care about,
[2399.48 --> 2405.32]  you know, in the models that we train in big science or the models that we have on the hub,
[2405.32 --> 2411.88]  we do care that, you know, like if it has a bias, we declare it, we care about the data and everything.
[2411.88 --> 2418.52]  Yeah. So important. And yeah, I really appreciate hugging face really taking a stance there and
[2418.52 --> 2425.08]  putting a lot of effort into that. So as we kind of close out here pretty soon, you've mentioned a
[2425.08 --> 2430.04]  bunch of things that you either are working on or, or have worked on as part of like the open source
[2430.04 --> 2436.52]  ecosystem around hugging face. I'm wondering like, what's that thing that like keeps you up at night
[2436.52 --> 2443.08]  or the thing that's like on your mind that you'd love to do or dig into, but you haven't yet,
[2443.08 --> 2448.52]  what excites you or maybe like is, is something you want to dig into at some point in the future?
[2448.52 --> 2455.72]  So in hugging face, uh, like there is a certain group of people like me that do not really have
[2455.72 --> 2461.72]  specific things. Like in hugging face, uh, we just, nobody, nobody actually tells you, you know,
[2461.72 --> 2468.28]  you should do X, Y, you just, you know, go and pick a responsibility and that's your thing from
[2468.28 --> 2476.76]  that moment. So what I did was so far, like I did the tasks and I did, uh, like a Keras integration
[2476.76 --> 2483.24]  in which I have done model cards and tensor board and stuff. And like, I really become so happy whenever
[2483.24 --> 2490.92]  I see a Keras repository with a model card inside, because I know that people actually find it useful and
[2490.92 --> 2497.16]  just keep using it. I am currently working on how we can, how we can use hugging face hub for the
[2497.16 --> 2503.64]  tabular data. So I'm working with an amazing scikit-learn core contributor that is currently
[2503.64 --> 2512.60]  in hugging face. He's Adrian. Like we are currently working on a package that is focused on how we can
[2513.16 --> 2519.32]  improve the production capabilities of scikit-learn because like you use for instance pickle, which is,
[2519.32 --> 2525.16]  which can run arbitrary code on your machine. If you, you know, just pulled any pickle and just
[2525.72 --> 2534.36]  this realize it, it's a bit hard problem to tackle. And we want to post whatever information we can have
[2534.36 --> 2539.96]  about the model. So like currently I'm working on that side. For instance, if it's a tree based model,
[2539.96 --> 2546.76]  you can visualize it three. If it's a clustering model, depending on what type of clustering model that is,
[2546.76 --> 2554.52]  it can be like a dendrogram or like a visual, like with the PCA, or if you have like a, you know,
[2554.52 --> 2561.80]  linear model, you can put the hyperplane. So I am trying to, you know, put those stuff and also
[2562.60 --> 2569.40]  what model has learned through feature importance, shabty values and everything. So what I want is I want
[2569.40 --> 2575.96]  people to call one line of code and just push their models on the hub, which will create these model
[2575.96 --> 2583.80]  cards with, you know, several information. And I also am working like we are all supporting Gradio.
[2583.80 --> 2590.60]  And I'm also working on how we can leverage Gradio for table or data stuff as well. Because like
[2590.60 --> 2598.36]  previously Gradio was mainly focused on the modalities, like, you know, text or audio or
[2598.36 --> 2605.00]  computer vision and the components are, if you take a look at the documentation are focused on that,
[2605.00 --> 2610.52]  but like we can do, you know, like you can just drag and drop a data set and just automatically
[2610.52 --> 2615.72]  visualize everything regarding that data set. And that's quite magical. Like I remember first time
[2615.72 --> 2620.52]  I used Pandas profiling and also data analysis baseline library, you know, like there are a
[2620.52 --> 2627.72]  couple of libraries that enable you to profile your data sets, train baseline models, do like an
[2627.72 --> 2634.84]  auto ML, like teapots. I remember using then I was like, this is witchcraft. Like this is so good.
[2635.80 --> 2643.00]  You know, it's just, it saves so much time. And I was like, you know, recently I realized we can
[2643.00 --> 2650.04]  actually do that on the hub. Currently I am building like two tools. One is like profiling a data set
[2650.84 --> 2658.12]  and like a Gradio, it's like a Gradio interface that does it. We have recently released in Gradio
[2658.12 --> 2663.96]  something called blocks, which is more flexible than an interface. So you can, you have tabs and
[2663.96 --> 2672.04]  you have rows and you can put multiple stuff inside. So I'm currently building two spaces. Like,
[2672.04 --> 2678.28]  as I told you, I either build, like I maintain or add something to the Hugging Face Hub library or
[2678.28 --> 2685.48]  something else or do demos. So currently I'm working on something that is like an auto EDA,
[2685.48 --> 2694.52]  like a Pandas profiling. And another thing is an auto ML tool sort of. So yeah, these type of things
[2694.52 --> 2700.76]  also like save a lot of time and also lower the barrier of entry, I think, because like you have a
[2700.76 --> 2707.00]  baseline model and you can just, it will push your best baseline model to hub. And maybe you can create
[2707.00 --> 2713.40]  like a space really easily on that, which you can later go and tell your local data scientist,
[2713.40 --> 2721.64]  Hey, I want this, but improved version. I really love this. You know, I was a big fan of Hugging Face for
[2721.64 --> 2728.28]  like, I don't know, since I saw Thomas's video, I think it's been two years or something. I don't remember.
[2728.28 --> 2734.12]  And I'm still a big fan of Hugging Face. Like I go and talk in, you know, Python conferences and
[2734.12 --> 2738.92]  people approach me and say, I'm a big fan of your conference. And I'm like, me too.
[2741.80 --> 2747.96]  That's great. Well, we're, we're certainly big fans here and appreciate the way that you're building,
[2748.52 --> 2755.40]  the way that you're building really community and collaboration around AI and data sets and all of
[2755.40 --> 2760.44]  these things. So yeah, really appreciate your work, Merva. And yeah, I appreciate you taking
[2760.44 --> 2765.88]  time to talk to us. It was fun. Thank you so much for inviting me. I enjoy like talk. I could talk
[2765.88 --> 2771.16]  about Hugging Face all day and I would, you know, worry that people would get bored of me. So it's nice
[2771.16 --> 2777.80]  to meet people like you who are fans of Hugging Face as well. Of course. We'll talk to you soon. Bye-bye.
[2777.80 --> 2785.80]  Bye-bye.
[2786.84 --> 2793.08]  All right, that is Practical AI for this week. If this is your first time listening, subscribe now
[2793.08 --> 2799.16]  at practicalai.fm or just search for Practical AI in your favorite podcast app. We're in there.
[2799.40 --> 2804.04]  And if you're a longtime listener, please do share the show with your friends. It is the best way you
[2804.04 --> 2809.72]  can help Practical AI succeed. Thanks again to Fastly for shipping our shows super fast all around the
[2809.72 --> 2814.52]  world to Breakmaster Cylinder for the Beats and to you for listening. We appreciate you.
[2814.52 --> 2825.56]  That's all for this week. We'll talk to you again next time.
