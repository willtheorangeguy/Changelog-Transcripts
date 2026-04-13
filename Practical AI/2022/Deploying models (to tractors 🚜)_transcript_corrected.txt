[0.00 → 2.10] It's all about intuition, I guess, these days.
[2.28 → 3.90] Everything is changing so fast.
[4.32 → 7.22] It's very hard to actually try to predict something.
[7.52 → 9.58] And what we do is an iterative process.
[10.18 → 12.22] We try every time and then we refine.
[12.62 → 14.82] And that's exactly how we look at the field itself.
[14.96 → 21.02] So if we see a company or a specific field where we feel that what they need to do in
[21.02 → 25.68] order to solve the problem they're trying to approach is actually an iterative process
[25.68 → 29.52] where you have a model, and you're constantly refining, rebuilding a better model.
[30.00 → 32.30] Then this is a great fit for ML Ops.
[32.62 → 36.50] If you have enough automation, you can really accelerate the process.
[40.40 → 41.64] Hey, Jared here.
[42.22 → 46.44] One of the things we can count on in the software industry is change.
[47.12 → 51.76] The state-of-the-art changes so fast, in fact, that keeping up can feel like a whole other
[51.76 → 53.68] job on top of your actual job.
[54.50 → 56.56] That's why we created Change Log Weekly.
[56.56 → 61.44] It's our totally free newsletter that we drop in your inbox each and every Sunday.
[62.08 → 67.02] We link to the latest news, the best articles, and the most interesting projects that you
[67.02 → 67.72] should be aware of.
[68.22 → 72.94] We also add a little commentary from us saying why something's important, pointing you to
[72.94 → 76.46] other instances of a trend, or just making a dorky joke to keep it lively.
[76.46 → 81.98] So if you haven't yet, I recommend subscribing to Change Log Weekly and help us help you keep
[81.98 → 82.64] up with the latest.
[83.52 → 86.80] Head to changelog.com slash weekly and sign up today.
[86.98 → 89.56] Again, it's totally free and we never spam you.
[89.70 → 90.04] Yuck.
[90.90 → 94.42] One last time, that's changelog.com slash weekly.
[94.42 → 113.04] Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive,
[113.04 → 114.68] and accessible to everyone.
[115.04 → 119.34] This is where conversations around AI, machine learning, and data science happen.
[119.34 → 125.10] Join us at practicalai.fm slash community and follow the show on Twitter.
[125.30 → 127.46] We're at practicalai.fm.
[127.70 → 132.34] Thank you to our partners at Vastly for shipping our pods superfast all around the world.
[132.54 → 134.40] Check them out at fastly.com.
[140.64 → 144.24] Welcome to another episode of Practical AI.
[144.60 → 146.28] This is Daniel Whiten ack.
[146.28 → 149.86] I'm a data scientist with SIL International.
[150.44 → 154.90] I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed
[154.90 → 155.16] Martin.
[155.42 → 156.02] How are you doing, Chris?
[156.32 → 157.34] I am doing well, Daniel.
[157.40 → 158.06] How are you today?
[158.46 → 159.42] Doing well.
[159.60 → 165.52] Yeah, it's been an interesting couple months and lots of new projects kicking off, so keeping
[165.52 → 165.90] busy.
[166.10 → 169.28] But we just came back from a little bit of vacation last week, which was nice.
[169.48 → 172.30] You got to tell everyone where you went now, now that you've actually brought that up.
[172.36 → 172.78] Okay, yeah.
[172.88 → 175.34] So we drove down to warmer weather.
[175.34 → 181.28] So we live in the Midwest of the United States and drove down to Alabama, did some hiking,
[181.84 → 188.16] kind of back up through Mammoth Cave, which I learned is the world's largest cave network
[188.16 → 189.36] system thing.
[189.54 → 191.80] I don't know the proper terms, but yeah, that was fun.
[192.00 → 193.48] So it went underground for a bit.
[194.06 → 195.72] And yeah, it was a good time.
[196.08 → 196.30] Yeah.
[196.30 → 201.78] And I'm pretty psyched for a couple of reasons for this show, Chris, because of course, I
[201.78 → 203.86] always enjoy talking with you.
[204.06 → 208.64] But we've also got some familiar technology because we had, I don't know if you remember
[208.64 → 213.80] a while back, we had an episode, I think at the time it was called Allegro AI, which is
[213.80 → 214.62] ML Ops.
[214.62 → 216.68] They've since rebranded to Clear ML.
[217.40 → 221.42] And we've got Moses Gutman, who is Clear ML CEO and co-founder.
[221.62 → 225.74] But we've also got one of their partners, Green Eye.
[225.86 → 232.94] We've got Alain Klein-Or bach, who is the CTO and co-founder at Green Eye, which is an agricultural
[232.94 → 234.62] AI company.
[235.26 → 236.24] So this is going to be fun.
[236.32 → 242.16] We're going to talk about agriculture, AI, ML Ops, and get to chat with some old friends
[242.16 → 242.54] as well.
[242.66 → 244.04] So welcome, Alain and Moses.
[244.36 → 244.72] Thank you.
[244.80 → 245.74] Thank you for having us.
[245.86 → 246.64] Pleasure to be here.
[246.98 → 251.40] Yeah, it's great to revisit ML Ops with Clear ML.
[251.82 → 253.46] We had that show previously.
[253.46 → 260.04] And of course, ML Ops is sort of like, even since we had that show, just kind of exploding
[260.04 → 262.76] as a topic that's on people's mind.
[262.76 → 267.78] What has that been like, Moses, in terms of just like this sort of meteoric rise of
[267.78 → 272.60] people caring about ML Ops and how they actually practically do machine learning?
[273.06 → 276.18] So I think that the market really matured in the last two years.
[276.52 → 281.62] I guess it's probably COVID accelerating the process where everyone is working remotely.
[281.78 → 287.12] So you have to have automated processes, and you got to log everything because you cannot
[287.12 → 290.10] call your colleagues every minute or so.
[290.10 → 296.18] And I think that the problems that we kind of discussed in theory two years ago became
[296.18 → 303.90] very day-to-day practical problems that companies and individuals run into on a daily basis.
[304.28 → 309.84] And now it's become a problem that if before it was nice to have, now it became like a must
[309.84 → 310.88] for most companies.
[310.88 → 318.54] Back then, only a few understood the benefits and kind of the need for this very comprehensive
[318.54 → 320.56] approach where everything is streamlined.
[321.22 → 325.92] And I think now it's kind of common knowledge, probably not that common to actually implement,
[326.18 → 328.16] but at least the understanding is there.
[328.70 → 328.86] Yeah.
[328.86 → 336.36] And Along, in terms of your company, which is sort of like has customers who are in the
[336.36 → 342.02] agriculture vertical, but is very much like at its core an AI company from my understanding,
[342.84 → 346.04] like how, I don't know the full history of Green Eye.
[346.16 → 347.88] So maybe you could give a little bit of that.
[348.04 → 354.90] But did you sort of like do a bunch of ais as Green Eye and then kind of like come to the
[354.90 → 361.26] Flops problems or from the beginning, was that something that you kind of needed and
[361.26 → 362.68] was problematic for you?
[362.72 → 364.88] So you kind of started with that early on?
[365.26 → 366.34] Hey, it's a good question.
[366.56 → 372.36] We actually started from different goals or different objectives of Green Eye and until
[372.36 → 374.10] we established what Green Eye is about.
[374.22 → 380.80] So we started hacking about the laptop and training on the GPU on the laptop and stuff like that.
[380.80 → 385.96] And really understand there is no scale in it in many, many, many ways.
[386.66 → 395.70] And even at a server there, and we needed to install CUBA and CUBA and using no app to
[395.70 → 402.12] keep the script running and really all the best, worst practice that you can ever, that you can do.
[402.26 → 403.08] There's no shame.
[403.22 → 404.28] We've all been there.
[405.98 → 406.54] Yeah.
[406.54 → 410.32] So we started with no Flops at all, really no Flops.
[410.96 → 415.52] And I think a few years ago, my brother, one of them told me, hey, try Docker.
[416.04 → 417.28] And I said, no, no, no.
[417.68 → 418.92] And the rest is history.
[419.22 → 425.10] Three years later today, we are completely Voucherized from end to end, Kubernetes all the way,
[425.20 → 426.00] cloud and edge.
[426.32 → 432.86] And this has changed everything because then we realized we can do a lot of Flops all around
[432.86 → 433.68] and move stuff.
[433.68 → 434.12] Yeah.
[434.86 → 440.56] And maybe just stepping back in terms of green eye, I think, Chris, I don't know if you remember
[440.56 → 442.88] this, but I forget in what episode it was.
[442.92 → 444.66] I think it was one of our fully connected episodes.
[444.66 → 451.74] We were using the example of like spraying in crop fields as an example of like this sort
[451.74 → 459.16] of scale between like compute, completely human manual process up to like automation and
[459.16 → 460.28] how that's changed.
[460.28 → 465.98] It struck me, Chris, that neither of us are farmers and really know much about that process.
[466.54 → 469.88] So Along, this is very much like the world you live in.
[469.96 → 474.76] So maybe you could just step back and let us know a little bit about like AI and agriculture
[474.76 → 480.34] before we kind of talk about some of the other Flops things that your company is doing along
[480.34 → 481.04] with Clear ML.
[481.04 → 487.04] Like what is AI and agriculture look like generally, and how has that developed over time?
[487.62 → 487.82] Sure.
[487.92 → 489.06] So I must be honest.
[489.22 → 490.52] I'm not a farmer as well.
[490.78 → 493.64] I'm from the technical side, but I like what we are doing.
[493.64 → 502.34] So in the beginning image, I think you can divide the interests into two, the ones that give
[502.34 → 507.88] tools to other farmers to get more information and more details about the field, the crop,
[508.10 → 510.08] the yield or anything like that.
[510.10 → 516.70] And you can divide the other group is the tools that make the decision by themselves.
[516.70 → 528.16] So you get a lot of true cool companies like in Israel, Tehran is, Prosper, other cool that doing a lot of intelligence in the field.
[528.40 → 532.22] They collect data, they analyze it and show the farmers' insight.
[532.58 → 538.62] You get drones there, you get satellites there, you get the pivots and cameras and et cetera.
[538.62 → 545.88] And from the other end, you get decision-making tools that driving the tractors, autonomous sprayers,
[546.04 → 554.02] like the same domains that we are, Blue River and John Deere, a position that was, I think, four years from now.
[554.14 → 561.84] As a follow-up to that, I'm curious, you know, we're so used to on the show kind of talking about these very technical topics.
[561.84 → 568.72] And yet, you know, the clientele that your company is serving is one that is getting into technology as we've talked about.
[568.80 → 573.92] But if you look at the broad history, hasn't really been something that we associate with high-tech and all.
[574.42 → 583.46] What is the merger of something as cutting edge as deep learning ML ops, you know, on one side with farming on the other,
[583.68 → 586.02] you know where that's making this massive transition?
[586.02 → 593.20] What's it like being in that space where you're presumably kind of tying together two very, very different worlds?
[593.36 → 594.16] We really like it.
[594.24 → 596.78] We are really a very developable company.
[597.00 → 603.26] We have like chemistry, we have agronomics, we have data science, we have real time.
[603.78 → 610.08] And we have everything for everything, cloud and ML ops and business sizes, spray operators.
[610.08 → 616.66] And being in this spot that everything is connected, the technology is related to the field is, we really like it.
[616.78 → 622.78] You need to have the business to run and to make sense from a monetized perspective.
[622.78 → 626.06] But it's also nice to do something nice.
[626.32 → 631.40] Yeah, it's nice to apply AI, I'm sure, to a problem that we all have, which are we all need food.
[631.40 → 641.12] So I saw in one of the videos on your site, this sort of like, and this is where my knowledge of all the machinery and stuff,
[641.22 → 643.74] but I'm assuming this is like a spraying machine.
[643.90 → 646.26] I don't know if it's specifically for spraying, but it sprays.
[646.74 → 649.18] And then you've kind of got cameras.
[649.52 → 654.46] So I don't know if you could maybe just describe this sort of machine and like the arms of the machine.
[654.78 → 659.88] And like, just so people have a visual of kind of like where your technology fits in.
[659.88 → 663.84] So maybe I restarted to understand the problem that we are solving.
[664.02 → 667.00] So imagine you have a garden, and you grow vegetables there.
[667.28 → 669.74] And what you do in your free time, you are weeding.
[669.94 → 675.34] You are taking the weed out because they compete with your vegetable about resource, sun, water, etc.
[676.04 → 678.98] And when you are getting bigger, you are starting to use mechanical tools.
[679.26 → 686.50] And when you get huge, like farmers in the Midwest, Nebraska and Iowa and all of this area,
[686.50 → 690.64] you started to put chemicals because you cannot control the size of farming.
[690.64 → 692.84] You put chemicals, and you want to do it fast.
[693.18 → 695.10] So you don't put with a small tractor.
[695.36 → 700.66] You have dedicated sprayer, self-proper ate sprayer, 66-meter-long boom.
[700.88 → 702.40] And it's a monster.
[702.94 → 709.74] You can walk underneath without the need to bend under the sprayer.
[709.74 → 717.44] So it's a huge monster that you just drive to do as much as accurate as possible in short time.
[717.90 → 722.34] And what we are doing in Green Eye, instead of assuming the worst case scenario,
[722.50 → 725.54] that every spot in the field is weeds there.
[725.54 → 732.94] So instead of doing that, we are putting sensors, cameras, and our computers, and nozzles,
[733.14 → 738.80] and everything else we are using to spray only when you need to spray.
[739.24 → 746.94] So instead of putting 100% of chemicals over 5,000 acres filled, you are putting 10% for it.
[747.30 → 751.46] And so you're saving money and the world's saving chemicals.
[751.82 → 753.52] And it's a win-win situation.
[753.52 → 756.54] So about your question, sorry, I forgot.
[757.30 → 758.94] So we have a big sprayer.
[759.12 → 762.64] We have cameras, each like three meters long.
[762.74 → 766.04] And we are just filming the entire boom.
[766.56 → 769.04] We are putting the cameras looking a bit ahead.
[769.34 → 770.58] So we have time to process.
[771.00 → 774.86] Everything is done in real time, no connectivity at all to the cloud.
[775.32 → 780.32] So Moses, you know, as I'm listening to Alain talk about his story,
[780.32 → 786.08] and as we're doing this, I'm thinking back to kind of starting with these cutting edge ML Ops.
[786.24 → 789.58] When you're looking at the landscape on your side,
[789.98 → 792.96] as someone who's bringing this technology to bear in the marketplace,
[793.80 → 797.38] how are you evaluating different opportunities in industry?
[797.52 → 799.32] I mean, is it just that everything is open?
[799.70 → 801.84] Do you have a way of looking and saying,
[801.84 → 808.98] I see an opportunity where this technology in a particular industry is going to be very useful?
[809.54 → 812.60] How do you make this kind of judgment calls on how to engage?
[812.96 → 813.58] Good question.
[813.86 → 817.10] So first, it's all about intuition, I guess, these days.
[817.26 → 818.90] Everything is changing so fast.
[819.32 → 822.58] It's very hard to actually try to predict something.
[822.76 → 824.88] If I'm referring back to machine learning.
[824.88 → 827.08] And what we do is an iterative process.
[827.86 → 830.48] And we try every time and then we refine.
[830.92 → 833.08] And that's exactly how we look at the field itself.
[833.22 → 839.48] So if we see a company or a specific field where we feel that what they need to do
[839.48 → 844.50] in order to solve the problem they're trying to approach is actually an iterative process
[844.50 → 848.34] where you have a model, and you're constantly refining, rebuilding a better model,
[848.58 → 851.12] then this is a great fit for ML Ops.
[851.12 → 854.48] Because that basically means that if you have enough automation,
[854.92 → 856.60] you can really accelerate the process.
[856.94 → 859.76] If not, obviously, you have to do the same process only manually,
[859.96 → 866.54] which time to market wise really increases the time for you from the research phase
[866.54 → 871.06] to actually something that is working where you have some alpha in the middle.
[871.56 → 874.84] And when you see a process where you can say,
[874.98 → 878.24] you know what, with a bit of automation, this model will really work.
[878.24 → 882.16] Like not 90% of the time, which means one out of 10 you fail,
[882.26 → 885.44] which is not like in theory, 90% looks sounds fine.
[885.54 → 889.02] But in practicality, this is not something you can actually sell.
[889.44 → 892.76] You think to yourself, okay, the only thing that I need is a bit for
[892.76 → 895.04] more information from the field itself.
[895.04 → 899.62] And then I can just refine the model, rerun it, get a better performance,
[899.62 → 901.04] and then just repeat the process.
[901.16 → 902.92] Then basically I'm golden.
[902.92 → 907.40] I can take it to different scenarios and get my model up and running.
[907.90 → 910.88] And every time we see one of those scenarios,
[911.10 → 915.10] then that's just kind of the moment where we hear the bling,
[915.28 → 919.02] okay, this is a perfect fit for automation for ML Ops
[919.02 → 920.96] as kind of holistic approach.
[920.96 → 941.54] We are going to 7, 3, 2, 1.
[942.00 → 943.92] I'm Karl AAU, host of Ship It,
[944.04 → 948.04] a show with weekly episodes about getting your best ideas into the world
[948.04 → 949.22] and seeing what happens.
[949.22 → 951.96] We talk about code, ops, infrastructure,
[952.24 → 955.78] and the people that make it happen like charity majors from Honeycomb.
[956.18 → 959.02] We act like great engineers make great teams,
[959.18 → 961.16] and it's exactly the opposite, in fact.
[961.42 → 964.30] It is great teams that make great engineers.
[964.84 → 968.20] And they finally win the founders of continuous delivery.
[968.56 → 971.36] Start off assuming that we're wrong rather than assuming that we're right.
[971.62 → 974.24] Test our ideas, try and falsify our ideas.
[974.38 → 976.38] Those are better ways of doing work,
[976.38 → 978.68] and it doesn't really matter what work it is that you're doing.
[978.80 → 980.50] That stuff just works better.
[980.72 → 985.00] We even experiment on our own open-source podcasting platform
[985.00 → 988.48] so that you can see how we implement specific tools and services
[988.48 → 992.06] within changelog.com, what works and what fails.
[992.28 → 994.96] It's like there's a brand-new hammer, and we grab hold of it,
[995.02 → 996.32] and everyone gathers around.
[996.40 → 1000.20] We put our hand out, and we strike it right on our thumb.
[1000.46 → 1003.28] And then everybody knows that hammer really hurts.
[1003.44 → 1005.92] When you strike it on your thumb, I'm glad those guys did it.
[1005.92 → 1007.62] I've learned something instead, yeah.
[1007.78 → 1010.02] I think that's a very interesting perspective,
[1010.32 → 1012.38] but I don't see it that way.
[1012.54 → 1012.76] Okay.
[1012.88 → 1015.98] It's an amazing analogy, but I'm not sure if that applies here.
[1016.30 → 1018.62] Listen to an episode that seems interesting or helpful,
[1018.76 → 1020.42] and if you like it, subscribe today.
[1020.54 → 1021.66] We'd love to have you with us.
[1021.66 → 1051.64] We'll see you next time.
[1051.64 → 1055.92] Alex was just talking about with sort of where the value of Flops
[1055.92 → 1058.26] really comes in with automation.
[1058.56 → 1064.02] You gave the example, sort of the concrete example of the spraying,
[1064.46 → 1070.86] detecting places to spray within a field with this massive machine
[1070.86 → 1074.16] that has the sensors or the cameras on it.
[1074.16 → 1083.02] So how does the automation or the retraining of models that you're using, where does that come in?
[1083.26 → 1088.74] How often, and what sorts of things are you automating in practicality?
[1089.00 → 1092.12] I think I can spend hours to answer fully of this question.
[1092.24 → 1103.10] But I must say, the things about Flops and MLE in general, if you compare to understanding a field in the industry like coding, deploying in servers, etc.,
[1103.10 → 1105.12] there is no best practice yet.
[1105.36 → 1110.00] The entire industry, everyone invent something on its own and doing something else.
[1110.78 → 1119.54] We are starting getting to some main path, but there is no best practice that everyone is agreeing on.
[1119.70 → 1123.58] So I think from our side, we had a lot of challenges.
[1124.06 → 1126.18] We have challenges of data and controlling the data.
[1126.32 → 1131.34] We have a massive amount of data, more than millions of images over the field.
[1131.34 → 1138.98] And one of the challenges is getting a model that was trained to the tractor.
[1139.80 → 1143.60] And before we had any automation, we did, okay, we trained the model.
[1144.06 → 1146.38] And then we froze it.
[1146.52 → 1152.08] And we are using Tensor RT and Onyx to Tensor RT and stuff like that.
[1152.30 → 1155.62] And we did it manually, like each step at a time.
[1155.62 → 1160.00] I think like we got 10 models a year to the tractor.
[1160.32 → 1165.68] When we got automation, we have thousands of models to the tractors and rerun.
[1165.84 → 1171.98] And when a researcher finished training, there is a click and everything is done automatically.
[1172.22 → 1172.78] It's convert.
[1173.16 → 1175.92] He's got metrics there, tooth, killer, mail.
[1176.44 → 1177.66] And what is done?
[1177.86 → 1183.54] He's checking the converting if we didn't miss anything by the converter, like performance.
[1183.54 → 1189.50] And we got the end of the file there to the tractor by a single click.
[1189.94 → 1195.24] So I think this is one example of automation that Flops really changed it.
[1195.54 → 1199.44] Do I remember correctly that you're also running Kubernetes on the embedded devices?
[1200.22 → 1200.98] Yes, yes.
[1201.08 → 1202.80] We're running Kubernetes on the embedded devices.
[1203.06 → 1206.98] This is completely a game change in our end.
[1206.98 → 1212.64] Because this is also a conversation different that I can speak hours about.
[1213.44 → 1218.00] And that's when you say on the embedded devices, we're talking about like on the tractor.
[1218.14 → 1218.74] On the tractor.
[1218.90 → 1219.26] Yeah, yeah.
[1219.34 → 1223.98] We have a few devices there, and they are running K3S.
[1224.10 → 1225.50] It's the light version of Kubernetes.
[1225.50 → 1231.52] It's really nice because we can best practice from the cloud, and we get best practice to the edge.
[1232.08 → 1240.54] And for example, if we want to use clear mail from the edge or from the clouds, it doesn't really make us any different to us.
[1240.54 → 1245.82] So we know how to press and move the secrets and how to use it.
[1245.90 → 1248.76] And we just do this in this sense.
[1249.26 → 1255.72] So you have full visibility to the tractors inside the same dashboard that you're developing in.
[1256.18 → 1259.48] And you have the entire cycle streamlined?
[1259.88 → 1261.84] So something like that.
[1262.22 → 1263.00] Good setup.
[1263.16 → 1263.68] I like it.
[1263.68 → 1275.88] I can connect any running tractor around the world that is online now and just doing even SSH to the machine.
[1276.40 → 1278.40] I can view it all.
[1278.76 → 1281.68] But this is bigger one than the ML Ops.
[1283.54 → 1285.76] This is like we call it Special Ops.
[1285.98 → 1286.54] Special Ops.
[1286.66 → 1287.14] I like that.
[1287.28 → 1291.54] We actually have dedicated team that's doing research around Special Ops.
[1291.54 → 1296.16] So we have ML Ops and DevOps and IoT Ops.
[1296.68 → 1297.76] Now there is Finos.
[1298.50 → 1303.32] This is the team that moves one step ahead and doing a lot of checks.
[1303.70 → 1308.44] I tried to find when we started to use the clear mail.
[1308.60 → 1311.06] I searched clear mail, and then I understand I need to search Allegro.
[1311.32 → 1317.20] And I didn't find the right point how we got to know Moses and his guys.
[1317.20 → 1319.24] So I'm not really sure.
[1319.36 → 1326.98] But before we got to know him, we used Below Pipeline to do the runs and to do the metrics.
[1327.22 → 1331.00] And we got there to a big wall of complexity.
[1331.34 → 1337.62] And we shift the training from Below Pipeline to clear mail.
[1337.62 → 1341.56] I'd like to ask a follow-up question about something you were saying a moment ago.
[1341.94 → 1345.98] And it's something kind of close to what I'm doing when I'm not podcasting.
[1346.54 → 1354.12] And that is when you talked about having Kubernetes in all the places, in this case on the tractor, and you talked about K3S.
[1354.62 → 1362.46] Can you tell us a little bit about I'm a big advocate in Kubernetes in all the places at various scales as a setup.
[1362.46 → 1372.14] And so since in your use case, you have done that, I'd love to hear how you arrived at that and what benefit you think it's given you.
[1372.32 → 1373.66] Why do that?
[1373.68 → 1376.72] Because most people don't think about putting Kubernetes in all the places.
[1376.98 → 1378.56] They're running kind of in the cloud.
[1378.72 → 1383.06] They don't have, they're not out on the edge yet the way you are where you're way out on the edge.
[1383.22 → 1391.72] And as someone who also in my day job works out on the edge, I'm curious what your thoughts are about how Kubernetes in all the places is a good model going forward.
[1391.72 → 1399.82] So Chris, you don't think people when they think of the ideal deployment target for Kubernetes, they don't think immediately tractor?
[1400.34 → 1401.60] I'm glad that he does.
[1401.68 → 1402.34] I'll say that.
[1403.80 → 1405.46] Should be right next to it.
[1406.04 → 1407.52] We are in sprayer world.
[1408.02 → 1408.96] It's a good question.
[1409.14 → 1415.08] We started, when we started containers, we started with no Kubernetes, and we did like our own deployment system.
[1415.08 → 1421.14] And we fast, like in months, we had the role of keep them alive, visioning and everything.
[1421.26 → 1423.32] And then we understand, okay, someone solved this problem.
[1423.54 → 1426.94] It's no way that, and then we got to Kubernetes on the cloud.
[1427.26 → 1432.24] And the edge, we still use containers, but with different orchestrator.
[1432.46 → 1435.90] We had the Azure IoT, if you know it.
[1435.90 → 1440.90] And we used it for a while, and then we got another role.
[1441.42 → 1447.12] Because Kubernetes has this concept of separation, virtual separation of pods.
[1447.24 → 1450.04] And this is an amazing idea.
[1450.98 → 1455.94] And the other orchestrators didn't edit, and we understand, okay, we need to change.
[1455.94 → 1461.56] And it was not easy, because nothing is really ready to ARM 64-bit.
[1461.84 → 1467.38] You'd be surprised that most of the libraries, maybe today there are some that are more,
[1467.52 → 1473.54] but most of the libraries, like one year, two years from now, no vision for ARM 24-bits.
[1473.66 → 1479.54] And it was like, there is no way that we are on the edge of the edge as a young company.
[1479.54 → 1484.00] Do you think that NVIDIA, having bought ARM recently, will have any impact on that?
[1484.00 → 1487.16] Not buying ARM, failing to buy ARM.
[1487.58 → 1489.00] Failing to buy ARM, yeah.
[1489.90 → 1490.16] Yeah.
[1490.28 → 1494.18] I think the regulation issues might affect it.
[1494.30 → 1495.70] I forgot about that.
[1495.82 → 1496.78] That's a good point.
[1497.66 → 1497.92] Yeah.
[1498.60 → 1502.94] But definitely, I think we'll be here for the edge.
[1503.80 → 1509.00] And Kubernetes, back to your question, help us a lot.
[1509.00 → 1517.72] For example, when we have a new researcher or a new programmer or whatever, he does not do anything on his laptop.
[1518.16 → 1525.52] The laptop is only the gate to the pod that runs on the tractor or on the cloud.
[1525.86 → 1526.72] And this is the workspace.
[1526.72 → 1536.16] So if we get to the tractor or in our subject, the research, a research come to the company, a new research.
[1536.36 → 1538.24] We just hired a new one.
[1538.76 → 1540.32] And she's perfect one.
[1540.84 → 1547.38] And she's got just get, okay, you get access to, we still use Below for a notebook server.
[1547.38 → 1552.68] And so if she needs a workspace, she just clicks and gets a new notebook.
[1553.26 → 1555.14] And she can use our tool.
[1555.44 → 1557.74] We use PyCharm for remote interpreter.
[1558.10 → 1560.04] And you just connect to the pods there.
[1560.22 → 1561.38] And you get all the data.
[1561.94 → 1563.68] And you can play from your PyCharm.
[1563.78 → 1564.94] You can play from your notebooks.
[1565.48 → 1567.04] And this is possible.
[1567.54 → 1569.44] You can get it in different ways.
[1569.44 → 1571.40] But this is mainly possible.
[1571.54 → 1576.82] All the games of sharing and forwarding with Kubernetes is much easier.
[1577.52 → 1581.78] And this is true for the edge and for the clouds.
[1582.26 → 1584.36] So no one installing any dependency.
[1584.54 → 1588.66] I don't know if you play with Java Home or something like that or NPM install.
[1588.98 → 1595.40] Or no one installing anything on his computer besides the ID, our philosophy in general.
[1595.84 → 1596.98] Everything containerized.
[1596.98 → 1600.32] There's no workspace to be installed in any way.
[1600.46 → 1603.74] And this is really up specifically in ML environment.
[1604.86 → 1610.06] So Alain, in terms of like the automation that you're talking about before, you mentioned
[1610.06 → 1613.62] this sort of information about like thousands.
[1613.88 → 1619.60] You're able to sort of do more than like thousands of models a year now versus like a sort of order
[1619.60 → 1622.16] of magnitude lower now that you didn't have automation.
[1622.16 → 1626.84] I'm wondering if you could talk a little bit more about like for your case, it's, and I'm
[1626.84 → 1631.10] trying to think of like maybe weeds sort of look similar.
[1631.50 → 1638.32] So like what kind of needs to be updated so much throughout the sort of year for these
[1638.32 → 1641.62] like vision models or whatever models you're running.
[1641.80 → 1645.66] And then like, could you describe maybe a little bit more?
[1645.82 → 1650.38] You mentioned kind of bringing in new data, training the model, and then having the pipeline
[1650.38 → 1655.20] to push it out to the tractor and deciding when and when not to do that.
[1655.20 → 1660.20] It'd be interesting to hear about the sort of when and when not question in terms of like
[1660.20 → 1666.14] what you test within like your ML ops to determine when you push something out and how you do that.
[1666.14 → 1666.40] Yeah.
[1666.40 → 1666.44] Yeah.
[1666.44 → 1666.48] Yeah.
[1666.48 → 1667.62] It's a good question.
[1667.62 → 1672.98] I will start with the first one about the models and the numbers models.
[1672.98 → 1680.48] I think in the end, well, from my experience, I might be wrong, but having one model to rule
[1680.48 → 1682.96] them all or something like that, it's not enough.
[1682.96 → 1690.58] You got the vision of YOLO, Retina Net or any other model, and you need to put more effort
[1690.58 → 1697.32] to solve a real world problem because you have very, a lot of variables, a lot of irons
[1697.32 → 1704.66] in the real world, and you need to combine classical vision and deep learning one.
[1705.38 → 1711.40] So I think in the end, we have metrics on the cloud for the models, for the big models
[1711.40 → 1712.60] and so on.
[1713.04 → 1719.56] But at the end, we want to have metrics on the devices, on the tracks of the runs themselves.
[1719.86 → 1726.00] So we keep constantly testing ourselves on the real environment, how we are doing.
[1726.24 → 1732.00] Also in the terms of performance, not only metrics, performance speed wise, a cycle clock,
[1732.30 → 1734.22] how fast we can go.
[1734.54 → 1737.80] Today, we can go about six meters per second.
[1738.36 → 1740.10] You guys speaking, my per hour.
[1740.10 → 1744.60] So it's about 12 around this area, mile per hour.
[1744.98 → 1747.56] So this is a huge factor for us.
[1747.74 → 1752.74] Besides that, we have different crops, different geography and everything changed.
[1753.12 → 1756.86] The landscape changed, the weather changed, the sunlight changed.
[1757.74 → 1763.24] It's a completely different game to play in Israel, for example, and the Midwest.
[1763.24 → 1764.74] The farmers changed.
[1764.74 → 1768.84] Some used tilt and some in Midwest.
[1768.84 → 1771.66] They mostly stopped using tilt.
[1771.70 → 1778.26] They just keep the crops, the old crops there and letting the ground do their magics and just
[1778.26 → 1780.04] sitting above the old crops.
[1780.04 → 1784.76] So everything is changed, and we need to react to those changes.
[1784.76 → 1787.64] So this is for the first one.
[1788.44 → 1793.84] And the second one, I think that every tractor run that we are doing or any other way that
[1793.84 → 1800.08] we are getting data, we try to get as much as variance as possible.
[1800.64 → 1807.64] So retraining our model by one or two or even, I don't know, 500 images are not the game.
[1807.64 → 1810.52] It won't change a lot for the model.
[1810.78 → 1812.06] We have a lot of them.
[1812.54 → 1818.16] So we try to understand when few models don't agree with each other or something like that
[1818.16 → 1823.76] or tricks like that to understand when there is information that is interesting to rerun
[1823.76 → 1825.00] a train on it.
[1825.28 → 1832.90] So are you logging your sort of data pre-processing and data set like creation and you're training
[1832.90 → 1841.20] runs in the sort of ML Ops and kind of building training off of certain triggers or something
[1841.20 → 1844.56] that you have set up, or how does that work?
[1845.00 → 1849.18] So one of the challenges of ML Ops is reproducibility.
[1849.62 → 1852.54] I think this is a really hard one to get right.
[1853.06 → 1856.32] You get code versioning, and then you get dependency.
[1856.98 → 1862.32] And well, okay, let's say you solve that with Git and Docker, but then you get data versioning
[1862.32 → 1869.38] and then in all of that, you need some system that will take everything from every place
[1869.38 → 1873.74] you need, and then you need to push it and just click play and rerun it.
[1874.10 → 1877.30] So reproducibility is really hard.
[1877.50 → 1881.60] And if you did like, I don't know, half a year ago, you did something good, and you want
[1881.60 → 1883.66] to go back to it, it's really hard.
[1883.88 → 1889.62] So we try to log as much as possible from the system perspective and from the training and
[1889.62 → 1890.58] the research perspective.
[1890.58 → 1897.34] What's nice about Clear ML that we are using it not only from ML Ops, we are using the
[1897.34 → 1898.90] dashboard in general.
[1899.10 → 1903.70] So we're just pushing everything that we want to use as metrics and show stuff there.
[1903.96 → 1908.36] So from this perspective, we just log everything possible.
[1909.02 → 1913.04] And if it's visible, we can use Clear ML for it.
[1913.04 → 1918.02] But also we want to push our limits and to run faster and faster.
[1918.26 → 1921.00] And if we run faster, we can do even more stuff.
[1921.44 → 1925.62] Today we did a quid, but our mission is to spray less, grow more.
[1926.04 → 1932.92] So we want to do fungal size and pesticides and fertilizer and et cetera.
[1932.92 → 1941.78] So we need more compute power or to be better and what we are doing and saving computer power
[1941.78 → 1942.76] for different tasks.
[1943.18 → 1948.90] So we try to log everything and be better and what we are doing.
[1949.08 → 1949.76] Quick question.
[1950.08 → 1951.72] You mentioned retraining models.
[1951.92 → 1954.86] Do you have like a model per tractor or scene?
[1954.86 → 1956.28] No, no, no, no.
[1956.40 → 1964.66] It's not tractor or scene, but we retrain a model like, okay, there are different reasons
[1964.66 → 1965.70] why to do it.
[1966.14 → 1974.80] Fixed, maybe we want to improve it in different variants of the appearance of the backgrounds
[1974.80 → 1976.68] or anything like that.
[1976.68 → 1983.54] Or we want to make sure that we got a new weed that we don't know, or we are not familiar
[1983.54 → 1983.90] with.
[1984.06 → 1989.92] So instead of doing a zero shot that we are kind of doing or one shot that we are doing
[1989.92 → 1996.32] so we can stop the system for doing this for a specific weed that became more common.
[1996.72 → 2000.26] But in general, we are playing with a lot of tools.
[2000.48 → 2004.94] We are trying to get in line with the best practice in the industry.
[2004.94 → 2007.14] And we are also experimenting.
[2007.84 → 2011.68] It's not just for the experiment, but it's for the research to be better.
[2012.30 → 2020.10] So in this sense, we might be running the same train or if we want to verify that we
[2020.10 → 2023.20] got the same result, like a real research.
[2023.78 → 2024.54] Not real.
[2024.64 → 2027.50] It's not academic, but in this sense.
[2028.02 → 2028.32] Okay.
[2028.54 → 2034.44] Well, given the fact that you're training so many models, you're updating a lot of models,
[2034.44 → 2039.60] it sounds like there's a lot of training scenarios that you're encountering.
[2039.70 → 2041.60] You're kind of doing this at scale.
[2042.42 → 2047.10] And you've been sort of partnering with Moses and his team to do this.
[2047.44 → 2053.78] I'm curious, actually, from Moses, from your perspective, sort of looking back on the things
[2053.78 → 2061.10] you've been trying to enable with Clear ML and seeing someone use it at a larger scale like
[2061.10 → 2066.60] this, what are some of the things that you kind of like, you thought were going to be
[2066.60 → 2071.54] important and ended up being important in terms of like the things you're tracking or
[2071.54 → 2073.18] the features that you've enabled?
[2073.38 → 2077.78] And maybe what are some things that like, or maybe you didn't expect, and now you're thinking
[2077.78 → 2080.76] about differently than you when you started things out?
[2081.08 → 2083.86] As a follow-on to that, what insights are growing in your head?
[2083.86 → 2086.18] I'll try to cover everything.
[2086.36 → 2087.22] I'll probably forget.
[2087.36 → 2088.26] So just remind me.
[2088.58 → 2088.78] Okay.
[2088.96 → 2093.96] I'll start where, so I think that Along's team were the first to say, guys, we want better
[2093.96 → 2094.96] connectivity with Kubernetes.
[2095.92 → 2099.80] And the reason I remember is we'll start this discussion.
[2099.90 → 2102.74] A lot of our features are actually driven by the community.
[2103.34 → 2107.72] And Along and his team started from the open source and kind of graduated.
[2107.72 → 2112.52] In a way, basically they just said, we're sick and tired of maintaining our own servers.
[2112.76 → 2113.80] Plural, they had many.
[2114.06 → 2115.48] And they just said, it's not worth it.
[2115.56 → 2116.72] Just go do that for us.
[2117.18 → 2120.44] And we had multiple conversations even before.
[2121.06 → 2124.82] So we try to keep a very active stack channel and GitHub.
[2125.06 → 2127.26] So we actually, this is how we develop features, right?
[2127.32 → 2129.80] Basically people would say, hey, I want to build something.
[2129.92 → 2131.64] And then it's just a crazy idea.
[2131.84 → 2135.12] And then we try to think about, okay, maybe this is doable.
[2135.40 → 2136.30] It kind of makes sense.
[2136.30 → 2139.10] And if it does, then we try to figure out first how to hack it.
[2139.10 → 2144.44] So someone can continue with their day job and kind of build on top of it.
[2144.68 → 2149.40] And then try to realize, is there a way to actually structure it into the platform itself?
[2149.58 → 2154.28] And if there is, we try to figure out a way to actually put it in there and see if there's
[2154.28 → 2154.60] traction.
[2155.08 → 2160.38] And one of the things that I remember that Along and Sam were the first to do was to better
[2160.38 → 2164.22] connect the orchestrator with the Kubernetes cluster.
[2164.22 → 2169.48] Basically, when we started developing it, it was like, I don't know, a long time ago.
[2169.76 → 2170.88] Kubernetes was not a thing.
[2171.46 → 2173.48] So containers were, but Kubernetes was not.
[2173.56 → 2180.12] It was just before Google just released Kubernetes as an open source solution, before it kind
[2180.12 → 2181.08] of killed Docker.
[2181.46 → 2183.86] So we started with Docker as kind of bare metal.
[2184.02 → 2187.84] So we said, okay, fine, we'll have the orchestrator that will just pull jobs, set up the container,
[2187.90 → 2189.22] and then run everything inside the container.
[2189.22 → 2190.74] And they do that, and it's great.
[2191.12 → 2194.48] But the resource management or allocation of Kubernetes is terrific.
[2195.14 → 2200.84] So these guys came, and they said, look, guys, we have a Kubernetes cluster, and we like the
[2200.84 → 2202.56] idea of your orchestrator.
[2202.78 → 2207.78] So basically, Clear Mail orchestrator will do, think of it as a dynamic Docker file, in a
[2207.78 → 2207.94] way.
[2208.16 → 2209.16] I'm over simplifying.
[2209.58 → 2214.10] Base Docker image with the ability to kind of control that kind of Docker file you need
[2214.10 → 2217.06] to do in runtime, but then also introduce some caching.
[2217.06 → 2222.74] Bottom line, you do not have to have a container per job just to accelerate.
[2222.94 → 2227.50] Because when you streamline a process, you cannot have every step containerized.
[2227.58 → 2232.48] You end up with thousands of containers that no one will know who is using, and no one will
[2232.48 → 2234.34] delete because someone might be using.
[2234.60 → 2235.98] And basically, yeah, you get the idea.
[2236.38 → 2242.28] Anyhow, so they said, okay, we love Kubernetes because it allows us to schedule resources very
[2242.28 → 2242.78] easily.
[2242.78 → 2247.68] But then when the research is scheduled, we want this dynamic approach and obviously visibility,
[2247.96 → 2249.94] which is obviously hard with Kubernetes.
[2250.60 → 2255.82] We also don't want our users, like the data scientist developers, to have actual access
[2255.82 → 2258.08] to the Kubernetes cluster because, well, no.
[2258.42 → 2263.98] So I think that was the first time we developed what we now call the Kubernetes glue, which
[2263.98 → 2268.14] basically kind of converts a job from Clear ML into a Kubernetes job.
[2268.14 → 2272.56] Basically trying to figure out whether this job can actually be executed on Kubernetes to
[2272.56 → 2275.60] give you kind of better visibility into the cluster itself.
[2276.26 → 2282.14] So users can basically push jobs into what we call a queue, which is, think of it as in
[2282.14 → 2286.50] Kubernetes terminology, it's basically like the template YAML that you'll be using for that
[2286.50 → 2287.38] specific job.
[2287.38 → 2290.06] Only you have a priority queue on top of it.
[2290.06 → 2295.76] So it kind of implicitly holds the setup itself, which is kind of resources, et cetera, but
[2295.76 → 2297.18] also priority on top.
[2297.38 → 2301.40] And then use that in order to schedule, use Kubernetes as basically your resource scheduling,
[2301.54 → 2307.68] which it is terrific for, but it's lacking the scheduler itself, like order and priority,
[2307.82 → 2308.06] et cetera.
[2308.18 → 2310.52] This is exactly what the glue itself adds.
[2310.52 → 2317.04] And obviously it solves for the problem of making sure that the end users, meaning the
[2317.04 → 2320.24] data scientists will have access to the Kubernetes cluster, right?
[2320.56 → 2323.42] So that was a first feature that we added just because of them.
[2323.46 → 2327.60] And this is how we heard on, so you guys are running Kubernetes on the edge device?
[2327.68 → 2330.90] And we were amazed, but someone is trying to do that.
[2331.36 → 2336.70] So I feel completely obligated to throw yet another buzzword in just to ask you about if
[2336.70 → 2337.32] you have an opinion.
[2337.52 → 2338.84] And that is, that is...
[2338.84 → 2339.92] Don't go blockchain, Chris.
[2339.92 → 2344.44] Well, that's a yet another one right there you threw out, Daniel.
[2345.16 → 2349.44] No, I'm just going to stick with kind of microservice architecture when you were talking
[2349.44 → 2353.44] about, you know, all the containers out there and managing that.
[2353.54 → 2357.94] And as people kind of are moving more and more into microservice architecture over time
[2357.94 → 2362.52] and segregating off all their functions and yet trying to keep them together, does Clear ML
[2362.52 → 2366.12] as a platform have an opinion on that in any way?
[2366.12 → 2367.20] Or do you not care?
[2367.30 → 2369.84] Are you agnostic about, you know, where do people end up?
[2369.92 → 2372.70] So if I throw the word microservices at you, what do you say?
[2373.00 → 2373.98] Okay, that's terrific.
[2374.28 → 2374.82] I love it.
[2374.88 → 2380.26] Because microservices is in Kubernetes was invented, basically to manage them.
[2380.34 → 2382.92] But the idea behind a microservice, it's alive.
[2383.46 → 2385.44] It's production ready.
[2385.92 → 2387.28] And it has to be stable.
[2387.48 → 2390.92] Like the default of Kubernetes is if it fails, restart it.
[2390.98 → 2393.10] Because you had a good reason to put it there.
[2393.10 → 2395.78] This is not what is going on with Flops.
[2395.84 → 2398.76] If it failed, then it'll continue failing.
[2399.24 → 2400.56] Like just drop it.
[2400.76 → 2401.48] That's the default.
[2401.62 → 2403.90] That's the total opposite of microservices.
[2404.40 → 2405.64] And that's basically our approach.
[2405.70 → 2408.62] Our approach is use Kubernetes for what it's good for.
[2408.74 → 2412.52] So you probably have another cluster doing whatever microservices that you're running,
[2412.64 → 2413.40] which is terrific.
[2413.62 → 2418.90] But for the Flops perspective, use Kubernetes as a resource scheduler more than anything else.
[2419.10 → 2421.92] It's basically the opposite of the default of Kubernetes.
[2421.92 → 2427.66] And then I guess the bridge is serving models, which is actually a microservice.
[2428.10 → 2433.20] But you want that elasticity because you still want to be able to change it without
[2433.20 → 2435.62] building new dockers all the time.
[2435.70 → 2440.58] You actually want that to be in-flight model upgrades, canary, etc.
[2440.70 → 2444.56] That you probably want to control from outside, not from like an LB perspective.
[2444.90 → 2448.00] So this is kind of the bridge between the two, at least from our perspective.
[2448.00 → 2452.98] So if I'm getting sort of just like stepping back and thinking, I'm kind of trying to connect
[2452.98 → 2456.96] some of the things Along, you've said in terms of how things are working on your end.
[2457.06 → 2463.70] You sort of have data coming in off of the tractors, coming into various like maybe data
[2463.70 → 2469.34] processing jobs, which might be queued up on a queue, which runs through Clear ML.
[2469.34 → 2475.12] That might sort of lead then into like model training jobs, which I agree.
[2475.36 → 2480.62] So I love your illustration, Moses, about like you expect a lot of model training jobs to
[2480.62 → 2480.92] fail.
[2481.26 → 2486.66] So like Kubernetes, like spinning up a service in Kubernetes to run a training is sort of
[2486.66 → 2489.98] like the opposite of like a lot of what they had in mind.
[2490.24 → 2493.48] But anyway, so you sort of spin up these jobs in a queue.
[2493.48 → 2498.12] So from the data scientist perspective, you're basically just saying, hey, I want to use this
[2498.12 → 2501.02] data to train a model, put it in a queue.
[2501.24 → 2503.26] It runs a training and finishes or not.
[2503.70 → 2510.22] But then like that model then, which has like a version, it's tied to the data, then sort of
[2510.22 → 2510.98] gets shipped out.
[2511.12 → 2515.32] Does it get, in your case, does it get shipped out kind of like Moses is saying to a service
[2515.32 → 2522.66] that's running in your like edge K3S cluster, like as a rest service for what's going on
[2522.66 → 2523.30] on the tractor?
[2523.48 → 2524.46] Or how does that piece work?
[2524.58 → 2525.14] It's a good question.
[2525.24 → 2528.06] I think we can see two paths to start the training.
[2528.34 → 2533.12] One path is from the data, as you spoke, and then the other path is for the researchers
[2533.12 → 2539.60] want to test the code or new experiment, new model, or et cetera, and want to fire a training.
[2539.60 → 2547.60] So when we started, let's take the example for the researcher, he just goes in his ID and
[2547.60 → 2555.10] he just connects to the remote workspace that is on Kubernetes that runs Below, Jupiter's,
[2555.26 → 2555.98] and so on.
[2556.02 → 2557.24] And he's just playing there.
[2557.60 → 2559.36] And he just click remote executed.
[2559.90 → 2567.02] This runs to Moses servers and tells the Clear ML system to speak, to log everything.
[2567.02 → 2571.20] Like, okay, I want to use this container and this is the changes I did.
[2571.50 → 2576.82] Like Moses says, it does not create new containers for every step.
[2576.88 → 2578.94] So he just keeps the changes.
[2579.54 → 2583.38] Moses, if I'm saying something wrong here, feel free to fix me.
[2583.64 → 2585.68] And then it goes to Moses servers.
[2585.86 → 2591.72] And then from there, it's going back to our servers as our agent there that Moses spoke
[2591.72 → 2592.06] about.
[2592.18 → 2596.02] This is the glue and this start the training.
[2596.02 → 2601.54] So this is the training and the training continuously reports to Clear ML, to the main server.
[2602.04 → 2605.04] What's the status and what's the metrics.
[2605.72 → 2611.98] And once we have metrics, we can decide one of the two, if we are free a new version for
[2611.98 → 2617.68] testing on the edge, or we are stopped there and just keep this track and moving on.
[2618.06 → 2624.50] And the inference you're running on the Kubernetes cluster as a service or as like on the K3S
[2624.50 → 2625.70] as a REST service.
[2625.70 → 2627.38] So this is a tricky one.
[2627.62 → 2631.68] We have something in the box that is not in production.
[2631.84 → 2634.08] When I'm saying production, like internal production.
[2634.46 → 2642.94] Research that we are planning to have K3S inside a pod to have a special environment
[2642.94 → 2644.98] for the developers that is separate.
[2645.18 → 2646.42] Like a cluster in this cluster.
[2646.90 → 2647.50] Something like that.
[2647.50 → 2649.48] But let's keep this aside.
[2649.78 → 2654.02] We are using at the moment KF serving to serve the model internal.
[2654.72 → 2659.20] So our metric system, just when we get a new model, we just serve it.
[2659.50 → 2663.06] And the metrics just doing API REST service locally.
[2663.66 → 2667.30] And this is something like a microservice that you say.
[2667.52 → 2669.38] One is responsible entirely.
[2669.64 → 2671.88] It does not know anything about the metric itself.
[2671.88 → 2676.08] You can just probe it in to get results for each one of what you want to do.
[2676.60 → 2679.28] And there was another tool that is doing the metrics.
[2679.44 → 2686.24] And it just probes the service, and it can emulate and then report metrics to the Clear ML service.
[2686.44 → 2688.52] So we have three different services.
[2688.98 → 2692.16] Clear ML is not micro, but the other two are.
[2692.38 → 2693.96] And I think this is the cycle.
[2694.24 → 2696.74] We have a human decision in between.
[2696.74 → 2702.36] So we don't do the entire cycle for every model and not for every data.
[2702.94 → 2708.08] So I have a final question that's addressed to both of you in turn.
[2708.24 → 2709.54] I want to start with Along.
[2709.66 → 2713.14] I'm actually letting Moses cheat and hear what Along's answer is.
[2713.66 → 2713.78] Yay.
[2714.22 → 2716.34] So Moses, I'm throwing you a bone on that one.
[2716.68 → 2718.24] So here's the question.
[2718.48 → 2724.22] As you are thinking about kind of these amazing uses of technology,
[2724.22 → 2729.32] both from the technology creator and from the technology implementer's perspectives.
[2729.82 → 2731.90] And you were thinking about what's next.
[2732.02 → 2733.54] What are you wanting to do next?
[2733.60 → 2734.86] You've made it this far.
[2735.34 → 2736.64] You've had tremendous success.
[2737.08 → 2740.32] And you've got to have something that when you go to bed at night, you're going,
[2740.90 → 2742.28] maybe I could do that.
[2742.96 → 2747.80] Along, I'd first like to hear for you as the implementer in a very specific use case,
[2748.14 → 2748.96] what you're thinking.
[2748.96 → 2754.40] And then Moses, hint, hint, now that you've heard his question, you know, you can answer
[2754.40 → 2755.08] yours as well.
[2755.20 → 2756.70] So Along, I'll throw it to you first.
[2757.10 → 2760.48] So I have many things in my mind.
[2760.64 → 2763.62] A lot of imagination before I go to sleep.
[2763.96 → 2768.70] Sometimes I see bounding boxes and just seeing them and seeing them and seeing them.
[2768.78 → 2770.46] Sometimes I see different stuff.
[2770.46 → 2777.28] But yeah, in a larger scale, I think still in green eye perspective, we can do,
[2777.90 → 2784.22] and we are about to do the both that I said in the industry about decision-making and helping
[2784.22 → 2787.84] the farmer because we are already scanned the field.
[2787.92 → 2793.84] And we have byproduct of a lot of data and high quantity of data, high resolution data
[2793.84 → 2794.92] from the field.
[2794.92 → 2798.06] So our goal is to do both.
[2798.72 → 2806.26] And we have lots of idea that in the pipeline to also, one, to get, to make the decision
[2806.26 → 2806.84] ourselves.
[2806.94 → 2811.60] And the other one is to help the farmer get better decision for different stuff that's
[2811.60 → 2813.16] not related to sprayer at all.
[2813.54 → 2814.20] That was a good answer.
[2814.76 → 2815.76] Moses, how about you?
[2816.30 → 2818.98] So two things I can expose here.
[2818.98 → 2825.52] So one, we are working now, this is public in one of the repositories, on the new version
[2825.52 → 2828.10] of the serving solution.
[2828.56 → 2835.04] Basically, we're not fans of KF Serving as an infrastructure because it's very hard.
[2835.36 → 2838.00] If you have a single model, if you're not changing it, that's fine.
[2838.14 → 2841.14] But if you're constantly changing them, it's not easy.
[2841.66 → 2843.44] Adding preprocessing is not easy.
[2843.62 → 2845.30] Metrics, everything is hard.
[2845.30 → 2851.78] So together with a lot of people from the community, we redesigned the Clear Mail serving.
[2852.28 → 2854.92] So now it's internal testing, and it's very, very nice.
[2855.08 → 2861.24] Basically, you can add the preprocessing without even code, deploy it, have it autoscale on your
[2861.24 → 2861.86] Kubernetes classes.
[2862.00 → 2868.54] It's basically building a serving service that is flexible and that you can change online,
[2868.68 → 2869.42] which is terrific.
[2869.66 → 2871.68] This is what we want from these type of services.
[2871.68 → 2877.64] So this is something that we're working on, and I'm hoping that we will be able to release
[2877.64 → 2879.66] before the end of next month.
[2879.88 → 2882.48] So I think we have a talk in GTC.
[2882.64 → 2884.50] So before the talk, that's a deadline, basically.
[2885.20 → 2888.24] We will have to release it, which is, it's always good to have a deadline.
[2888.84 → 2893.46] And the other thing that we're working on, and this is really research, we're sort of trying
[2893.46 → 2895.62] to wrap our heads around how to actually solve it.
[2895.68 → 2897.98] And that's coming directly from Along, actually.
[2898.14 → 2900.70] So he was one of the guys that said, oh, I really want that.
[2900.70 → 2902.10] And he's not the only one.
[2902.50 → 2907.26] So we always want to make sure that we're not building for a very specific problem, that
[2907.26 → 2909.30] it's actually a wide thread problem.
[2909.62 → 2914.60] And that problem is, I have a lot of data stuck there, there in the backend of Clear Metal,
[2914.68 → 2916.46] which basically means like multiple databases.
[2916.82 → 2921.66] I just want to be able to query more deeply, like create a dashboard.
[2922.22 → 2923.18] Like the data is there.
[2923.24 → 2923.58] I know.
[2923.68 → 2924.30] I put it there.
[2924.60 → 2929.60] Now I want to have better interface for the database without actually accessing the database.
[2929.60 → 2932.74] Like this is doable, but probably kind of too risky.
[2932.96 → 2938.16] So we're trying to think how to hack together like a dashboard solution on top of it to allow
[2938.16 → 2941.84] you to better create better visibility for an entire process.
[2941.84 → 2947.20] Because the entire idea is to make this entire ML Ops holistic approach.
[2947.20 → 2951.86] Basically means that if you have data, you should be able to use it in whatever step you're
[2951.86 → 2954.04] along the way of developing your product.
[2954.04 → 2958.86] And this is something that is a making, but will be found its way out there very soon.
[2958.96 → 2959.34] I'm hoping.
[2959.66 → 2960.12] That's awesome.
[2960.38 → 2962.86] I'm super excited to explore those things.
[2963.10 → 2963.62] I'm a fan.
[2963.74 → 2968.42] So pretty excited to hear about the serving and the other things coming along.
[2968.42 → 2974.40] And I appreciate both of you being willing to kind of talk through, first, give
[2974.40 → 2979.44] us an update on what is now Clear ML, which previously we talked about as Allegro and all
[2979.44 → 2984.36] the great things you're doing, but also in the context of this use case with Green Eye.
[2984.52 → 2987.46] So I'm really impressed with what each of you are doing.
[2987.64 → 2989.74] And yeah, thank you both for joining.
[2989.98 → 2990.36] Thank you.
[2990.48 → 2991.00] Thank you.
[2991.00 → 2995.12] All right.
[2995.26 → 2997.24] That is Practical AI for this week.
[2997.54 → 3004.06] If this is your first time listening, subscribe now at practicalai.fm or just search for Practical
[3004.06 → 3005.82] AI in your favourite podcast app.
[3006.02 → 3006.54] We're in there.
[3006.94 → 3010.10] And if you're a longtime listener, please do share the show with your friends.
[3010.28 → 3012.98] It is the best way you can help Practical AI succeed.
[3013.46 → 3018.40] Thanks again to Vastly for shipping our shows superfast all around the world to Break master
[3018.40 → 3019.36] Cylinder for the Beats.
[3019.36 → 3021.52] And to you for listening, we appreciate you.
[3021.84 → 3022.96] That's all for this week.
[3023.10 → 3024.20] We'll talk to you again next time.
[3049.36 → 3054.10] Breakless Luxor.
[3054.22 → 3054.98] Okay.
[3054.98 → 3055.20] Puts ES, been.
[3055.20 → 3067.72] Sita-
[3067.72 → 3068.92] Bit.
[3068.92 → 3069.22] Okay.
[3069.22 → 3071.08] Get up.
