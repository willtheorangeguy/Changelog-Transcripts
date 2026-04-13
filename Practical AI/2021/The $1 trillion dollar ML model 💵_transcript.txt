[0.00 --> 6.22]  ask yourself whether this business problem really requires an AIML model or not. I think that's
[6.22 --> 13.02]  very, very critical. We're living in this space where sometimes AIML models are not very well
[13.02 --> 19.38]  explained. And hence, we need to be crystal clear about the data that goes into the models. The
[19.38 --> 25.12]  attributes that we're building bases this data so that what comes out of the algorithm, we're very
[25.12 --> 30.36]  clear about what decision is it really making. And hence, once you solve the problem that yes,
[30.52 --> 35.60]  this problem requires an AIML model, then the questions about okay, what kind of techniques
[35.60 --> 42.22]  are out there? Is it data which is very structured? And that's where I have labels the one zero Daniel
[42.22 --> 46.98]  that you were talking about? Or is it unstructured? And therefore, the techniques I would like to apply
[46.98 --> 52.34]  is things like NLP. So once you started the technique problem, it gets into really understanding
[52.34 --> 56.40]  the data that was feed into it, and therefore the features that you want to generate.
[56.40 --> 66.06]  BAML for ChangeLog is provided by Fastly. Learn more at Fastly.com. Our feature flags are powered
[66.06 --> 71.82]  by LaunchDarkly. Check them out at LaunchDarkly.com. And we're hosted on Leno cloud servers. Get $100
[71.82 --> 78.82]  in hosting credit at Leno.com slash ChangeLog. Hey friends, this episode of Practical AI is brought
[78.82 --> 84.38]  to you by Codeish, a podcast from the team at Heroku that explores code, technology, tools, tips,
[84.38 --> 89.02]  and developer life. There's tons of great conversations on the Codeish podcast, so I would
[89.02 --> 93.36]  encourage you to check it out and subscribe. But in particular, I wanted to bring to your attention
[93.36 --> 100.62]  two episodes, episode 98 and 99, where Julien Duque explores the ethical and technical sides of deep
[100.62 --> 106.78]  fakes. The rise of manipulated pictures and videos and other forms of computer-generated media are able
[106.78 --> 112.42]  to cause uncertainty and doubt in what we see and hear online. So how are we able to use these tools
[112.42 --> 118.96]  for good, if at all? Here's a sneak peek. Let's say we want to do a deep fake of my voice,
[119.36 --> 125.58]  and we train the model, and we have enough data and everything. This will be also able to
[125.58 --> 134.16]  imitate my accent, for example, like how I pronounce English and the strong pieces of my accent,
[134.40 --> 141.06]  or is not there yet. It really depends. If there would be a person with similar accent on the input,
[141.06 --> 146.86]  then it would be fine, but it's kind of cheating. You can think it's cheating,
[147.36 --> 151.34]  because we're reusing accent of a different person that's similar to your accent. But if it would be
[151.34 --> 159.32]  like an American native speaker or a British person with a British accent, or like whatever other
[159.32 --> 168.18]  accent, then it will kind of be a mixture on the output. So we're not there yet in terms of converting
[168.18 --> 173.66]  accents. It's a little bit more difficult than we initially anticipated, because like when we started
[173.66 --> 178.62]  the company, we thought it would be, you know, we'll kind of solve it in a year or something. But then it
[178.62 --> 186.40]  turned out, oh no, we're here for much longer. Check these episodes out. Links are in the show
[186.40 --> 192.72]  notes to both episodes, or head to heroku.com slash podcasts to listen and subscribe. Again,
[192.72 --> 196.76]  check the show notes for links, or go to heroku.com slash podcasts.
[208.62 --> 215.58]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[215.88 --> 220.88]  productive, and accessible to everyone. This is where conversations around AI, machine learning,
[220.88 --> 225.58]  and data science happen. Join the community and Slack with us around various topics of the show
[225.58 --> 230.18]  at changedog.com slash community, and follow us on Twitter. We're at Practical AI FM.
[230.18 --> 244.48]  Welcome to another episode of Practical AI. This is Daniel Whitenack. I am a data scientist with
[244.48 --> 250.46]  SIL International, and I'm joined as always by my co-host, Chris Benson, who is a principal
[250.46 --> 256.58]  emerging technology strategist at Lockheed Martin. How are you doing, Chris? I am doing very well. We're
[256.58 --> 264.20]  just in the normal late December holiday rush as we record this. All's well. Yes, trying to get all
[264.20 --> 270.04]  those year-end projects that you promised were going to be done by the end of 2020 done.
[270.60 --> 275.64]  I've already failed on that because I'm already on my holiday break now as of today is my first day.
[275.80 --> 282.30]  Oh, congrats. That's a done deal. Anything I didn't do is into 2021 so I can walk back in with excuses
[282.30 --> 289.02]  next year. Yeah, not that there would be any reason this year, you know, nothing happened this year
[289.02 --> 296.26]  that would throw projects off. I don't know what, you know, this whole pandemic thing, you know, you
[296.26 --> 302.66]  name it. It's been quite a crazy year. I'm optimistic with vaccines out that 2021 will be a much better
[302.66 --> 310.04]  year for all. Yeah, well, I'm looking forward to our Christmas at home with a small group. Yes.
[310.04 --> 317.04]  Some good food, but also just sort of a break and a nice relaxing time. Reset. Yep. Reset and then
[317.04 --> 323.72]  jump back into the year. I hope all of our listeners have a wonderful break as well. And if you happen to
[323.72 --> 330.32]  be working on fun side projects during your break, let us know in our Slack channel or on LinkedIn or
[330.32 --> 336.54]  Twitter or somewhere and we'd love to hear about those. I'm really excited, Chris. One of the things
[336.54 --> 343.36]  that I know that we've been requested a couple of times in our Slack channel is a little bit deeper
[343.36 --> 350.72]  dive into financial applications of AI from someone that has that expertise. And we definitely have
[350.72 --> 358.62]  that someone with us this week. This week, we have Madherma Kandewal, who is vice president and head
[358.62 --> 362.90]  of American Express AI Labs. Welcome, Madhs. How are you doing?
[363.30 --> 365.56]  Hello. I'm doing well. How are you all?
[366.04 --> 370.28]  Doing great. It's wonderful to have you here. We appreciate you taking the time.
[370.80 --> 376.88]  Before we jump into all things AI and finance, could you just give us a little bit of a picture
[376.88 --> 381.62]  of your background and how you got interested in AI and ended up doing what you're doing now?
[381.62 --> 388.96]  Sure. Personally, I am born and brought up in New Delhi, India, and I have spent over 15 years
[388.96 --> 396.22]  in American Express. And in this tenure, I have held a variety of roles with increasing responsibilities.
[397.10 --> 404.86]  I'm currently the vice president and the head of Amex AI Labs. And in this role, I lead the charter of
[404.86 --> 410.86]  building state-of-the-art AI products and capabilities, which solve high-impact,
[410.86 --> 417.00]  complex business problems across the company needs. And my teams are based out of Bangalore
[417.00 --> 423.46]  and New York. And if I reflect back, I think, you know, in this tenure, I have always taken roles
[423.46 --> 429.58]  where I feel I've been in uncharted territories. But at the same time, I've always felt supported
[429.58 --> 434.84]  in every step of my career to pursue these opportunities as well. So that's a little bit
[434.84 --> 435.44]  about myself.
[435.90 --> 440.84]  Awesome. Yeah, that's so cool. I'm wondering, so you mentioned this American Express,
[440.84 --> 449.34]  AI Labs. I know that it's fairly common in especially larger organizations to have a sort
[449.34 --> 454.96]  of innovations lab or even set up a specific lab for AI applications because it's sort of a,
[455.08 --> 460.70]  it's a newer thing that maybe the rest of the organization doesn't have a lot of experience
[460.70 --> 467.22]  with or it needs special sort of prototyping. Is that the kind of model at American Express?
[467.22 --> 472.66]  Or what does it mean sort of labs? Is it more of a research thing or how does that work?
[473.30 --> 481.52]  Yeah. So I think on the contrary, American Express has been investing in the space of AI ML for a number
[481.52 --> 490.10]  of years now. And the way the labs has shaped up as of today, it has a role to play when it comes to
[490.10 --> 498.60]  research. But it also has a role to play where we provide tools and platforms to our modeling community
[498.60 --> 507.22]  so that they are able to utilize AI ML in a manner that can drive business impact. And we also have
[507.22 --> 513.70]  multiple AI ML teams sitting within our business units, which are really excelling in their own domain.
[513.70 --> 522.38]  But labs really comes in to solve for those horizontal company-wide needs that may exist and may need to
[522.38 --> 529.60]  get into a specialization zone, which these specific teams may not have the expertise in. But I wouldn't
[529.60 --> 536.32]  say that AI ML really sits only within this lab. It's pretty much integrated across the company domains,
[536.86 --> 539.88]  be it risk, be it marketing, as well as servicing.
[539.88 --> 546.68]  I am always curious. I like to ask people, as you moved into taking charge of this capability
[546.68 --> 551.98]  within American Express, and if you look at just like not the whole career, but maybe just the last
[551.98 --> 556.54]  couple of positions, were you like the natural person? Or was this something where you said,
[556.62 --> 561.68]  this is a really cool thing, I want to lead and I'm volunteering? How did you get into it? Because
[561.68 --> 566.40]  I love hearing the stories about how people got into this space because they're always different. So
[566.40 --> 572.24]  what was yours in terms of the short term? So I think, I know you are asking me for the short term, but I'll
[572.24 --> 576.28]  take you back to 2005 when I joined. Okay, that's fine. Whatever you want to do is good.
[577.24 --> 582.12]  Because at that time, you know, my role was pretty much around marketing and customer acquisition.
[583.00 --> 589.42]  And we were building traditional models to be able to solve that problem. But as my role matured,
[589.42 --> 597.14]  we got into the space of digital marketing, which really led to a plethora of volume of offers coming
[597.14 --> 602.48]  into the ecosystem. And the only way we could solve that problem and yet be relevant to our customers
[602.48 --> 608.90]  is really venture into the zone of machine learning. And that's where, you know, this entire interest
[608.90 --> 616.32]  came into being, where we started using AI and ML, so that we could personalize our digital assets for
[616.32 --> 622.38]  our customers. When you asked me whether I was the natural choice, I think, you know, it was a two-way
[622.38 --> 628.02]  street. Like this was an area that was of huge interest for me. And thankfully, my leaders also
[628.02 --> 634.48]  saw my ability to be able to create these solutions, but also create it in a manner that could drive
[634.48 --> 640.70]  scale. And hence, I am where I am. Gotcha. No, that sounds great. You were the natural person who
[640.70 --> 644.68]  could do it because you were the person who can make it actually happen. Well, I'll take that.
[644.68 --> 652.38]  Okay. Fair enough. Yeah. It's always interesting to me too, that this sort of space, there is a very
[652.38 --> 658.60]  close connection to research that's going on, whether that's academic research and that's coming into
[658.60 --> 666.76]  a company or whether that's actually research, you know, within the company itself. How has it been for
[666.76 --> 674.48]  your AI labs in terms of actually productizing research and the balance between researching
[674.48 --> 681.98]  something that, you know, may never be able to be productized versus specifically scoping out things
[681.98 --> 689.34]  that have a product in mind? Yeah. I think often, you know, research doesn't really start with the
[689.34 --> 695.88]  mindset that we will be able to productize it. I think there's a huge learning in even failing at a
[695.88 --> 702.24]  research because you learn something even then. And, you know, while often there would be a business
[702.24 --> 709.96]  problem at hand that you're trying to solve, but AI labs is a team of PhDs and MS who are always
[709.96 --> 716.96]  challenging the status quo. And when you challenge the status quo, you pretty much go about researching
[716.96 --> 723.80]  what may be industry best, what may be something that we could utilize, not immediately, but maybe three
[723.80 --> 731.28]  years down the line. And in that process, there is learning for us where we may not be able to
[731.28 --> 737.76]  productize the entire solution, but we may be able to carve out pieces from it, which could be relevant
[737.76 --> 743.82]  to what we are solving today or even in the future. So I think there are stories of enough successes,
[743.82 --> 749.44]  but there are also stories of failures. And I, as a leader, I'm quite proud of those failures as well.
[749.44 --> 755.08]  That's what has made us learn what we need to do differently as we venture into these
[755.08 --> 755.94]  researches again.
[756.82 --> 761.70]  So one of the things you talked about was kind of making that evaluation for what three years out
[761.70 --> 768.44]  might be. How do you evaluate that given that this field is moving fast and you have the business
[768.44 --> 772.84]  drivers that are pushing you in the directions that you need things to go for your business?
[773.26 --> 778.48]  That's a kind of a combination of the technical forecasting and the business forecasting.
[778.48 --> 783.78]  How do you and your team make those kind of judgments given what is clearly, you know,
[783.78 --> 786.04]  not enough information at any given point in time?
[786.62 --> 792.86]  Yeah, I think it's a combination of one knowing the business well, but also one being strong
[792.86 --> 799.04]  technically. And I'm glad we are a team which actually have a great combination of the two.
[799.80 --> 806.28]  Often we're able to solve problems, not because we're asking a team, what is your AIML problem?
[806.28 --> 813.22]  The often question that we ask is, tell us what is the day-to-day process that you do today,
[813.68 --> 819.20]  right? And when somebody explains to us what their process is or what their product is,
[819.62 --> 826.54]  often ideas are generated together as to how we could make that better using AIML.
[827.04 --> 829.06]  So let me take a few examples for you.
[829.48 --> 834.46]  When I was talking about early on in the career when we were building traditional models, right,
[834.46 --> 839.94]  and personalization in the space of digital assets, be it the website, mobile app, email,
[840.82 --> 848.42]  the problem at hand was we have this shelf full of offers. What we don't know is which one to pick
[848.42 --> 855.32]  out when our customers on the channel. And the only way we could solve that was to build best-in-class
[855.32 --> 861.68]  machine learning algorithms. Another example, so this example that I talked about was for our
[861.68 --> 867.66]  external customers. But another example here is for our internal customers or colleagues,
[868.20 --> 874.00]  where we have started to integrate AI in operational functions as well. And that's really speeding up
[874.00 --> 879.38]  our manual processes. You know, if you were to ask these teams, they would spend hours, you know,
[879.44 --> 885.44]  in doing these processes themselves. But our products are now able to free up that time for them so that
[885.44 --> 891.88]  they can spend time into doing deeper analytics and more complex tasks. I think one example of that is
[891.88 --> 898.70]  how we have created a tool for our vendor management team that pretty much identifies potential duplicate
[898.70 --> 904.56]  invoices, which otherwise they were spending so many hours figuring it out themselves. So I think these
[904.56 --> 911.02]  are areas where we are driving solutions, not because we ask the question of what is the AIML
[911.02 --> 914.72]  need that you have, but because we understood the problem at hand.
[915.34 --> 921.58]  Yeah, it's something interesting to me as you're speaking about all of these solutions that some
[921.58 --> 929.56]  of them are maybe not what first comes to mind when people think about AI and finance. So maybe some
[929.56 --> 934.66]  people think of like, oh, like quants on Wall Street that are like optimizing trades or something like
[934.66 --> 940.70]  that. Maybe other people think of fraud detection or risk analysis, which is something that
[940.70 --> 946.66]  comes up a lot and I'm sure is very relevant still within American Express. We'll hopefully talk about
[946.66 --> 952.48]  soon. But it seems like there's these other applications too that are really coming out of
[952.48 --> 957.06]  the fact that American Express is a large organization. You're dealing with a lot of,
[957.20 --> 965.32]  let's say, documents, or you also have customer support type issues or marketing type things that you
[965.32 --> 970.82]  have to deal with. As I'm looking through the website of the AI labs a little bit, it talks about
[970.82 --> 977.22]  natural language processing, document recognition and processing. And like those two things, like NLP and
[977.22 --> 982.26]  these sort of computer vision things might not be the first thing that come to my mind when I'm thinking
[982.26 --> 989.92]  about AI in the sort of financial vertical. What is the balance on your team? Is there a lot of that
[989.92 --> 998.38]  sort of operational support that you're doing internally or is a lot of the focus on direct sort of models
[998.38 --> 1004.98]  that impact your actual financial products? What's kind of the balance there? And how do you think about that?
[1005.48 --> 1013.12]  So I wouldn't say the focus is primarily on the automation part or the document processing part. I think the focus
[1013.12 --> 1023.28]  of the use of AI ML in the company is really within risk, credit risk, marketing and servicing. That's really
[1023.28 --> 1033.04]  what is impacting our external customers. That's where the focus has been. And we have obviously created
[1033.04 --> 1042.08]  or improved our overall usage of machine learning in just advancing in this space. Yes, you know, while we have
[1042.08 --> 1050.78]  been mastering that art, we have also started to invest into areas of NLP, of areas of automation
[1050.78 --> 1058.88]  and driving value in that as well. But, you know, as you said, Daniel, I think the story is left untold
[1058.88 --> 1065.80]  if we don't talk about fraud prevention, which is where it all started within American Express.
[1065.80 --> 1074.00]  And for the listeners, like fraud prevention is really one of the first areas where we deployed machine learning models.
[1074.50 --> 1082.68]  And this was, you know, back in 2010. And we saw a dramatic increase in our ability to detect fraud
[1082.68 --> 1087.94]  with the usage of these machine learning models. And it goes back to, you know, what we believe in,
[1087.94 --> 1095.80]  that we would like to have our customers' backs and really servicing our customers is our top priority.
[1095.80 --> 1099.76]  And keeping fraud rates low is key to achieving this goal.
[1099.76 --> 1111.22]  Changelog++ is the best way for you to directly support practical AI.
[1111.74 --> 1116.16]  Join today and unlock access to a private feed that makes the ads disappear,
[1116.16 --> 1122.14]  gets you closer to the metal and help sustain our production of practical AI into the future.
[1122.94 --> 1128.88]  Simply follow the Changelog++ link in your show notes or point your favorite web browser
[1128.88 --> 1135.40]  to changelog.com slash plus plus. Once again, that's changelog.com slash plus plus.
[1136.74 --> 1139.12]  Changelog++. It's better.
[1158.88 --> 1166.50]  So Mads, I love it that you started getting into this fraud prevention topic, because I know one of the things
[1166.50 --> 1174.20]  when I'm teaching AI workshops or something, a lot of the examples that I might give when I'm first introducing
[1174.20 --> 1180.66]  machine learning or AI, or maybe like in courses online or something like that, people talk about,
[1180.66 --> 1188.28]  you know, fraud detection, and they have like some data set where it's maybe a set of, you know, numbers indicative of
[1188.28 --> 1196.44]  transactions or a person's history or something, and then like a one or a zero for fraud or not fraud, right?
[1196.74 --> 1204.58]  And I assume, and this is just, I'm very curious about this, personally, I assume that the situation is
[1204.58 --> 1210.18]  definitely much more complicated than that. Like there's different types of fraud, there's different
[1210.18 --> 1216.06]  data that's relevant to those different types of fraud. Would you be able to just give us a little
[1216.06 --> 1223.72]  kind of overview or a sense of, like, what types of fraud are your sort of primary concerns and what
[1223.72 --> 1226.00]  data is related to that fraud?
[1226.52 --> 1233.78]  Yeah, absolutely. So I think when it comes to fraud, the number one problem that we are faced with,
[1233.78 --> 1241.60]  even in the space of online fraud is really our ability to detect fraud in real time basis.
[1242.00 --> 1247.80]  So what that means is that when a transaction is actually taking place, can we make a decision
[1247.80 --> 1254.06]  whether or not that transaction is fraudulent? And if you think about American Express transactions,
[1254.06 --> 1263.42]  like we have more than $1.2 trillion transactions annually. And we would like to, yeah, and we would like
[1263.42 --> 1271.96]  to create this decision in almost milliseconds when the transaction is taking place, right? And that is
[1271.96 --> 1281.52]  where the need for really building machine learning models that can be deployed in real time becomes the
[1281.52 --> 1288.50]  number one ask so that we're able to service our customers. So while, you know, the fraud definition
[1288.50 --> 1297.00]  or the data has remained one zero, it has magnified basis, the number of transactions that exists globally.
[1297.74 --> 1303.42]  But at the same time, with digital coming into play, you have online transactions happening,
[1303.42 --> 1311.78]  it becomes difficult for you to detect fraud, because it's often not happening at the physical address
[1311.78 --> 1320.32]  or the residents. So there are a variety of, I would say, identifiers, which feed into our models to be able to detect that.
[1320.32 --> 1326.72]  But what is more critical is our ability to really run this algorithm in real time,
[1327.28 --> 1334.16]  which is where a lot of the engineering, a lot of the architecture is coming into play to deploy these models.
[1334.16 --> 1342.06]  That number you said definitely caught me. It was something over a trillion transactions per year or something like that,
[1342.14 --> 1349.74]  which I think if my rough math, quick math comes out, that's like more than a couple million a minute,
[1349.88 --> 1351.52]  which is crazy to me.
[1352.28 --> 1352.90]  That's called scale.
[1353.50 --> 1353.72]  Yeah.
[1354.60 --> 1355.42]  That's called scale.
[1355.66 --> 1356.54]  Yeah, yeah, yeah, yeah.
[1356.54 --> 1364.26]  So I can definitely confirm that I have never done two million inferences in a minute with any of my models.
[1365.40 --> 1371.28]  So I'd like to, let me ask a follow-up, and it might not be a fair question, because I'm not sure if this is specific,
[1371.58 --> 1375.12]  but I'm curious, are there certain types of fraud?
[1375.12 --> 1381.32]  Because in the sense of like, is it just fraud, and there's kind of one generic type where something comes in?
[1381.76 --> 1385.06]  Or are there different classifications of fraud that you're looking for?
[1385.06 --> 1388.00]  And then I was mainly asking that as a follow-up.
[1388.06 --> 1390.96]  And then as you address that, I'm kind of curious, like, what do you do with it?
[1391.00 --> 1395.62]  Because you're talking about real time there, and you may have a customer on the phone, or transactions are coming in.
[1395.88 --> 1401.88]  How do you integrate the output of the model, whatever that fraud is, into your actual operation,
[1402.18 --> 1407.52]  so that it's usable in that real time or maybe near real time context that you're having to deal with?
[1408.20 --> 1414.44]  So I think I may not be able to provide a lot of details about the fraud modeling.
[1414.44 --> 1415.06]  No worries.
[1415.22 --> 1418.08]  And I wasn't sure if that was a fair question to ask anyway.
[1418.28 --> 1423.94]  So if you want, you can move right on from that, because in some cases, when we talk with folks,
[1424.00 --> 1426.94]  we don't know what their area specifically is and what it isn't.
[1427.02 --> 1429.74]  So just go straight to the model question.
[1430.74 --> 1435.30]  When you put it through, you mentioned kind of that real time capability.
[1435.68 --> 1437.00]  What happens at that point?
[1437.10 --> 1439.94]  Not just with the model itself, but the output of the model.
[1440.10 --> 1442.38]  How does that get used in the real world?
[1442.38 --> 1447.06]  What does that look like for companies who don't have that capability at this point?
[1447.18 --> 1453.30]  What does that integration of model output and humans dealing with stuff in real time look like?
[1454.06 --> 1454.24]  Sure.
[1454.48 --> 1460.56]  So I think I'll go back to the example of personalization on our digital assets,
[1461.12 --> 1466.40]  where the data scientists are really building the best-in-class models, right?
[1466.40 --> 1474.32]  So they are pretty much figuring out for a given problem where you want to surface up relevant content for your customers.
[1474.70 --> 1481.10]  How would you really go about figuring out what is relevant at that point in time when the customer is on the channel?
[1481.10 --> 1492.40]  But while we build this model, you want to be able to pretty much run this model in real time so that you're able to surface up the content on the digital asset.
[1492.40 --> 1497.66]  And that's where the entire architectural design or the engineering comes into play.
[1497.82 --> 1509.06]  And we work very closely with our technology partners, where we are, in technical terms, really scoring this model in real time, where the data is coming in in real time.
[1509.06 --> 1517.44]  And we're able to figure out from all of the content that is available on a website or a mobile app,
[1517.62 --> 1521.60]  what is that one content that we want to show up for this customer?
[1521.94 --> 1529.06]  So you would imagine that there is a full-blown capability that is sitting behind in the ecosystem,
[1529.06 --> 1536.66]  which is really running all of these logics in play and surfacing up that content for that customer.
[1536.66 --> 1541.28]  So I think that's really what brings it all together.
[1542.02 --> 1545.66]  And as you would imagine, there are teams which would be data scientists.
[1545.86 --> 1549.38]  There would be teams which are marketing teams, which are really figuring out the content.
[1549.76 --> 1560.06]  There are our technology partners who are really designing this ecosystem so that all in all works in tandem to bring up the content on our digital asset.
[1560.06 --> 1567.60]  Well, as Chris knows, I usually am the one that gets hung up on sort of practicalities.
[1567.88 --> 1573.02]  And that number that you mentioned is still sticking in my brain and this sort of real time thing.
[1573.22 --> 1577.40]  And I know that there's a lot of people out there that are like, you know,
[1577.44 --> 1582.54]  they're not doing that scale of inferencing and real time sort of stuff,
[1582.54 --> 1589.62]  but they're still wanting to maybe they're integrating a model in their web application and they still want their web application to be responsive.
[1590.00 --> 1594.10]  Or they're trying to scale that up, you know, as their company is growing.
[1594.24 --> 1603.78]  I want to, you know, not miss the opportunity to ask you if, you know, as you've sort of scaled up these models over time,
[1603.78 --> 1613.44]  are there any kind of practical tips that you can give practitioners or even just like team leads or something that you could,
[1613.72 --> 1618.28]  you know, any practical tips that you could give them such that they're not building,
[1618.28 --> 1622.90]  you know, models and integrations of models that never sort of,
[1623.36 --> 1628.90]  they never see the benefit out of because they take, you know, 15 seconds to do an inference or something.
[1629.08 --> 1631.70]  And, you know, you can just never integrate it.
[1631.70 --> 1636.46]  You've done something that not many of us have done, you know, at that level of scale and performance.
[1636.68 --> 1642.06]  Yeah. So any tips there or anything that comes to mind in terms of guidance for teams on that subject?
[1642.54 --> 1649.94]  Absolutely. I think the prerequisite of an AI ML model is not just if you're running a real time application.
[1650.50 --> 1656.64]  I think a lot of AI ML models also exist, even if they're running in a batch process,
[1656.64 --> 1658.70]  which means that they're running once in a month.
[1658.70 --> 1668.74]  But I think the first and foremost tip I would want to give is ask yourself whether this business problem really requires an AI ML model or not.
[1669.16 --> 1671.38]  I think that's very, very critical.
[1671.38 --> 1679.32]  I think we're living in this space where sometimes AI ML models are not very well explained.
[1679.60 --> 1684.62]  And hence, we need to be crystal clear about the data that goes into the models.
[1684.84 --> 1690.64]  The attributes that we're building bases this data so that what comes out of the algorithm,
[1690.86 --> 1694.32]  we're very clear about what decision is it really making.
[1694.32 --> 1699.88]  And hence, once you solve the problem that, yes, this problem requires an AI ML model,
[1700.44 --> 1704.68]  then, you know, the questions about, OK, what kind of techniques are out there?
[1704.92 --> 1707.70]  Is it data which is very structured?
[1708.10 --> 1712.36]  And that's where, you know, I have labels, the one zero, Daniel, that you were talking about.
[1712.70 --> 1714.22]  Or is it unstructured?
[1714.34 --> 1718.34]  And therefore, the techniques I would like to apply is things like NLP, right?
[1718.34 --> 1724.94]  So once you've started the technique problem, it gets into really understanding the data that will feed into it
[1724.94 --> 1727.04]  and therefore the features that you want to generate.
[1727.52 --> 1732.70]  I think, you know, a lot of the practices that we used to apply for the traditional models
[1732.70 --> 1736.00]  still hold for the AI ML models as well.
[1736.52 --> 1741.46]  But the AI ML models give us the higher accuracy that we need.
[1741.84 --> 1746.28]  They give us an ability to work with large amounts of data, right?
[1746.28 --> 1754.82]  And they give us an ability to be able to churn the output in almost millisecond in case you have a real-time application.
[1755.28 --> 1761.42]  But it will still give you the accuracy bump even if your application required a batch model.
[1762.02 --> 1763.48]  So those would be some of the tips.
[1763.94 --> 1764.80]  And that's great.
[1764.86 --> 1765.72]  That's great information.
[1765.92 --> 1769.88]  I love the fact that you're talking about the fact that not everything needs to be an AI model
[1769.88 --> 1774.66]  because I think that's a really core wisdom in this field that is important not to lose sight of
[1774.66 --> 1780.12]  because there is a cost to deploying deep learning models that is higher than other things.
[1780.38 --> 1786.92]  And so, you know, the fact that you're recognizing that data science is larger than just this niche here.
[1787.40 --> 1791.44]  So how do you do that when you have so many use cases to address?
[1791.64 --> 1794.74]  And you talked about kind of starting with the fraud detection,
[1795.00 --> 1799.20]  but, you know, that there are many areas that you're using various types of modeling.
[1799.20 --> 1801.58]  How do you approach an evaluation?
[1801.84 --> 1804.18]  Not only – and I don't necessarily mean just a technical evaluation,
[1804.38 --> 1809.02]  but the business evaluation in terms of there's a problem that we need to solve
[1809.02 --> 1815.50]  and we have an array of tools which we might apply in terms of models that we might apply to solve those.
[1815.74 --> 1821.42]  How do you make that evaluation of, you know, what should be a particular AI architecture
[1821.42 --> 1823.44]  or say, you know what, we don't need that.
[1823.50 --> 1826.26]  We could use a standard regression on this.
[1826.26 --> 1830.34]  How do you go through the process regardless of what the problem is that you're addressing?
[1830.92 --> 1832.88]  How does your team address that process?
[1833.52 --> 1839.58]  I think that problem at hand, Chris, is really when you're facing that problem first time.
[1840.02 --> 1845.02]  Because once you've figured it out, you know, you would repeatedly just enhance your current logic.
[1845.22 --> 1851.74]  But first time, I would say that, you know, any team would build the best segmentation possible,
[1852.34 --> 1854.32]  the best AI ML model possible.
[1854.32 --> 1860.74]  And if you were to just compare the two, if your AI ML model is really able to surpass your segmentation,
[1860.98 --> 1867.80]  you would justify the added complexity, the added cost of really implementing the AI ML model, right?
[1868.12 --> 1873.14]  But if your AI ML model is pretty much performing at the same level as a segmentation,
[1873.72 --> 1878.20]  one would question, do you really need an AI ML model to solve this problem or not?
[1878.20 --> 1881.88]  And I think that's a very fair way of looking at it as well.
[1882.44 --> 1888.84]  But once you have, you know, for this given problem with the current set of data that exists,
[1889.22 --> 1893.64]  with the solution at hand that you have in mind, a segmentation may be as good.
[1894.66 --> 1896.42]  And that's how you would approach it.
[1896.92 --> 1900.82]  But time changing, data quantum changing,
[1900.82 --> 1904.50]  the same problem may require an AI ML solution.
[1905.00 --> 1911.34]  So I think we almost need to keep re-evaluating the need given the context.
[1911.50 --> 1913.06]  The context is very important.
[1913.96 --> 1919.34]  And of course, you know, as I said, that while we have people who are professions,
[1919.82 --> 1922.94]  you know, in this field in itself for a number of years,
[1923.28 --> 1928.02]  we also have, you know, dedicated teams who play the oversight role as well.
[1928.02 --> 1932.16]  So I, as a data scientist, while I would have built a model,
[1932.70 --> 1937.36]  another team would act as an oversight and make sure that what I have built
[1937.36 --> 1942.98]  and how it is being used is actually adhering to the way we want to function as a company.
[1943.18 --> 1950.88]  So that brings in that added layer of ensuring that we are solving the business problem as it needs to be.
[1958.02 --> 1974.88]  So I guess to ask the next question, you have, you're operating in a, in this business environment where you have to deal with regulation.
[1975.42 --> 1981.84]  There's, you know, I, I'm like Daniel now, Daniel, you've got the, the trillions number stuck in my head as well.
[1981.84 --> 1987.96]  Uh, I've been thinking about that and, and I'm thinking like the, the world that you're operating in from a,
[1988.06 --> 1993.66]  in terms of like regulation, you know, another new big topic is now AI ethics of data.
[1993.82 --> 1996.48]  You know, there's so many areas that to dive into.
[1996.60 --> 2004.50]  You're dealing with things at such a scale, especially with ongoing regulation and with this relatively new over the last couple of years,
[2004.50 --> 2015.24]  topic of AI ethics, how has American Express dealt and dived into and, you know, mitigated the issues and address the new thinking associated with this,
[2015.56 --> 2019.14]  you know, and you can go anywhere you want to go with this question, but I'm, I'm really curious how,
[2019.14 --> 2022.92]  how your team has approached the, the regulation and ethical concerns.
[2023.44 --> 2031.14]  Yeah, I think since the start American Express, we have always ensured that whatever models that we build,
[2031.14 --> 2034.30]  they are free from unlawful bias.
[2034.98 --> 2043.40]  And to meet this commitment, we are very, very intentional in what data we do not collect and how we build our models as well.
[2043.84 --> 2050.12]  All of the colleagues who are involved in the development as well as maintenance of our strategies and models,
[2050.30 --> 2052.70]  they go through very vigorous training.
[2053.36 --> 2057.78]  And these trainings would include some of the fair lending laws that exist.
[2057.78 --> 2064.20]  And this, these become prerequisite before you even initiate any form of modeling in the company.
[2064.58 --> 2068.10]  We also conduct extensive fair lending reviews.
[2068.48 --> 2071.30]  I was talking to you about an oversight team that exists,
[2071.30 --> 2076.78]  and that really ensures that we remain vigilant against any kind of bias.
[2077.54 --> 2084.70]  So I think those are some of the steps that we've always taken as we entered into the space from traditional modeling.
[2084.70 --> 2091.74]  So I want to follow up on that, actually, because it's something I've been thinking about probably for the last couple of years,
[2091.74 --> 2101.64]  because there was a, there was an article by DJ Patil, who is the chief data scientist in the US, Hillary Mason and O'Reilly.
[2101.64 --> 2116.48]  And they talked about this idea that doing sort of quote, good data science or ethical data science also helped you do good data science in the sense of like being more proficient at the things that you're doing.
[2116.60 --> 2129.08]  So for example, Mads, you talked about sort of knowing, you know, what model produced what result and making sure things were tracked and knowing what data was used in what model.
[2129.08 --> 2139.48]  I was wondering if this is something you've seen played out on your teams, where if you do kind of put in the effort to make sure that you're tracking your experiments,
[2139.48 --> 2146.64]  you have sort of a really good understanding of what data is, is coming into and out of models,
[2146.64 --> 2151.14]  and you actually monitor those models over time and put that infrastructure in place.
[2151.14 --> 2161.96]  If that helps you kind of when you're doing upgrades to the models, or it helps you in understanding, you know, where the models are failing such that you can actually in the end,
[2162.28 --> 2174.20]  if those may be things that some people might see as burdensome, if those could actually help you in the end to do better AI or do better data science, is that something you've experienced?
[2174.20 --> 2204.18]  Yeah, all the time.
[2204.20 --> 2207.70]  But we can't even understand when we need to go to do better practices, so that it's not in good shape.
[2207.70 --> 2208.44]  Interesting.
[2208.76 --> 2220.70]  So looking back to what I was saying, like, if we are very clear about the attributes feeding to my model, very clear about for that instance that I'm talking about of approval versus decline,
[2220.84 --> 2231.08]  what really contributed to that decision, that number one for an existing model is making me better aware of what is really fading into that decision.
[2231.08 --> 2259.30]  But tomorrow, as data starts to drift, as anomalies start to enter, I would then be able to understand now it's time for me to basically, you know, think about alternative feeds, alternative techniques, you know, whatever that indication is, that's also better governed when I understand what's really entering into the ecosystem or what is really changing or causing that delta.
[2259.30 --> 2278.26]  Yeah. So, yeah, as I said, Daniel, that would be pretty much all the time. And that would be how all of our data scientists function within American Express, really knowing what exists in the models, but also monitoring it all the time so that we are making those decisions at the right time.
[2278.26 --> 2289.30]  Gotcha. And I have a follow up for that, that I'm that I'm wondering, there's a problem that all of us in the in this industry that use these tools have got to find our way through.
[2289.30 --> 2305.70]  And that is, that since you're doing inference on deep learning models, and you have, you know, the features going in, you have a lot of data going in. But you know, you have, though work is being done, obviously, on explainable AI, and there's a whole kind of mini industry that's starting to develop to address that.
[2305.70 --> 2324.32]  How does American Express address the fact that if you're using a deep learning model that is inferencing, and you don't have that deterministic capability of explaining what happened, what kind of you know, that that requires you to have policies in place and stuff to, to accommodate that? How have you guys approached that?
[2324.32 --> 2343.00]  It's always interesting, it's always interesting, because every company that deploys these at scale has to have something in mind on how they're going to address it. And you know, if you have customers, and they're saying, well, why did I fail a particular check or something like that? How do you approach that if you don't have a deterministic, explainable path to do that with? What's your approach?
[2343.00 --> 2369.70]  Yeah, so I think, as I said, as a part of AI labs, we also build platforms and products, which basically help our modelers, build their machine learning models. And one of the things which is integrated into these platforms is their ability to look at their model scores, and also interpret their model scores at scale.
[2369.70 --> 2395.90]  But at the same time, I would also say that American Express is in the process of enhancing our own internal ethical AI principles, so that we ensure colleagues across the company uphold and adhere to these values when we use AI. And this is being done through a cross-functional partnership between executive leadership across our data-related organizations, as well as risk and compliance.
[2395.90 --> 2404.98]  So I'm curious, but while we still have some time to do this, I want to definitely give you a chance to brag a bit on your team.
[2404.98 --> 2413.92]  Because I see, I'm looking through your website, again, on the AI labs, and there's a section about published research and all of that.
[2414.02 --> 2424.90]  And there's just some really amazing things that seem like are going on, like you see detecting sarcasm and numerical portions of text, a tool for end-to-end distributed deep learning.
[2424.90 --> 2434.38]  There's a tool to assess availability of container-based systems, joint distributed representation of text and structure of semi-structured documents.
[2434.38 --> 2439.26]  There's just a lot of cool stuff, and that's just to list out a few of these things.
[2439.98 --> 2452.42]  Are there any projects or kind of breakthroughs that you'd like to brag a little bit about in terms of your team and what they've accomplished or what they're working on?
[2452.42 --> 2457.12]  So you actually talked a lot about those, Daniel.
[2457.24 --> 2476.98]  But I think, you know, while we have been lately investing in a lot of AI-based automation, where we are, you know, creating a suite which would cater to a lot of our internal colleagues when they deal with really long, complex documents.
[2476.98 --> 2492.26]  I think one space in NLP that we have been working is our ability to really talk to complex data or complex reports in very simple natural language.
[2492.26 --> 2511.18]  And, you know, this is able to surface up the needs for our senior leaders in their ability to extract information that may be the need of the hour in a fraction of a second where we traverse through a very complex data source.
[2511.18 --> 2530.66]  And in one of the recent conferences, we also presented this as a paper where, you know, what we really have been able to implement is, again, at scale, be whatever complex data that you produce.
[2530.66 --> 2542.68]  If you want your users to understand that data and be able to extract information from it, how could you use our product or platform to be able to do that?
[2542.68 --> 2559.86]  I can't reveal a lot of the details sitting behind or the brain part of it, but just imagine your ability to really amplify the usage of a complex data just because you made it available to non-technical users.
[2559.86 --> 2578.42]  But even within technical users, when new members are getting onboarded and they are getting trained on really how to, you know, work with a very complex data, this product actually enables and helps them as well and visualizes for them what they would have written in their patch code.
[2578.42 --> 2583.86]  Did that result in a similar output as this report would do?
[2584.70 --> 2586.14]  Yeah, that's very interesting.
[2586.14 --> 2597.84]  I know that there's people working on sort of a variety of things related to that, like, you know, generating natural language reports out of data.
[2597.94 --> 2600.96]  So like data to text sort of tasks.
[2601.70 --> 2612.10]  It sounds like part of what you're after is it's almost like you could ask questions or do some comprehensibility of complex data.
[2612.10 --> 2622.94]  But I'm sure that that data that you're searching over, I imagine it involves, you know, PDF documents and Word documents and videos and whatever.
[2623.10 --> 2631.40]  I'm assuming there's a whole variety of that that, you know, is internal to, you know, whatever it's called, American Express's archive.
[2631.40 --> 2637.22]  I know we're a big enough organization where I work, where we have literally what's called the archive.
[2638.12 --> 2645.22]  And there's so much in there, but it is sometimes a chore to sort of find that.
[2645.30 --> 2650.62]  Now, we have really amazing archive managers who pretty much can find anything for me.
[2650.68 --> 2654.14]  And they're doing that intelligence for me a lot of times.
[2654.14 --> 2660.86]  But it sounds like you're wanting to sort of enable people, give them that sort of archive specialist superpower almost.
[2661.06 --> 2661.60]  Is that right?
[2662.02 --> 2662.24]  Yeah.
[2662.40 --> 2670.22]  And to add to that, if we were to work across different documents, not only in terms of types, but even in terms of languages,
[2670.22 --> 2675.32]  because we support all of the global markets, that just increases the complexity.
[2676.04 --> 2680.98]  What may work for English will definitely most likely not work for Spanish.
[2680.98 --> 2685.02]  So, yeah, it definitely requires that investment of time.
[2685.12 --> 2691.36]  It also requires that expertise to really get into and extract that value for the business outcome.
[2692.06 --> 2696.88]  So, you're already starting to address my next question, at least in the shorter term.
[2697.46 --> 2701.82]  And that is kind of winding us up with kind of where you see things going.
[2701.82 --> 2711.52]  And you can kind of take that question any way you want to go from terms of AI, how AI affects American Express, the future of business in that.
[2711.90 --> 2719.58]  I'm just really curious to see if you look out beyond things that are being productized today and kind of the future,
[2719.82 --> 2724.66]  what kind of some of those aspirations are that you haven't yet addressed, things that would be like,
[2724.94 --> 2727.98]  if we could do that, that would be really cool, that kind of thing.
[2727.98 --> 2736.68]  What are you thinking? What would you like to see in that kind of medium to long-term horizon in terms of how AI impacts American Express?
[2737.24 --> 2745.96]  I think, Chris, the fact is that AI ML is already quite deeply integrated in most of the functions within finance vertical.
[2745.96 --> 2756.92]  And I think I expect it to only expand even further in the future from the core functions, such as credit decisioning we talked about, fraud detection.
[2757.22 --> 2764.74]  I know, Daniel, you have that number in your mind, marketing, servicing, even governance and compliance.
[2764.74 --> 2766.80]  We talked about those elements, right?
[2766.80 --> 2773.84]  But I think it's also expanding to some of the ancillary functions, such as process automation, cloud strategy.
[2774.38 --> 2780.14]  And I think AI ML is truly modernizing and streamlining finance as we think about it.
[2780.66 --> 2786.62]  For American Express, I would say it's really these three themes that matter to us.
[2787.08 --> 2794.76]  We want to use our data assets with the freshest data possible to make it real-time decisions.
[2794.76 --> 2803.68]  Second, we want to produce data products at scale so that we are always improving the quality.
[2804.42 --> 2808.96]  And third, we want to double down on improving customer service and experiences.
[2809.40 --> 2811.98]  I think these are really at the heart of it.
[2812.26 --> 2817.96]  And I can just imagine a future where we will keep investing in the space of AI ML.
[2818.62 --> 2821.54]  Awesome. That's really great to hear.
[2821.54 --> 2828.12]  And I know I do, and I'm sure Chris does appreciate your perspective on these topics.
[2828.46 --> 2836.16]  Being in a position where you have scaled some of these things up, it's just really tremendous to get that perspective and understand some of those things.
[2836.62 --> 2842.22]  Thank you for taking time near holidays and winter break to chat with us about these things.
[2842.22 --> 2843.82]  It's been really great.
[2844.06 --> 2847.50]  And we hope you get some time off before the new year starts.
[2847.76 --> 2850.26]  And thank you so much for the insights.
[2850.78 --> 2852.06]  Thank you so much for having me.
[2852.28 --> 2852.98]  This was amazing.
[2872.22 --> 2876.44]  And if you get value from the show, please do share it with a friend or a colleague.
[2876.62 --> 2878.00]  We appreciate you spreading the word.
[2878.84 --> 2881.74]  Practical AI is hosted by Daniel Whitenack and Chris Benson.
[2882.08 --> 2883.48]  It's produced by Jared Santo.
[2883.74 --> 2885.84]  And our music is provided by Breakmaster Cylinder.
[2886.38 --> 2888.52]  We are brought to you by some awesome sponsors.
[2889.10 --> 2891.54]  Shout out to Fastly, Linode, and LaunchDarkly.
[2891.88 --> 2892.72]  That's all for now.
[2892.92 --> 2897.80]  Stay tuned for the next episode where the guys talk ML Commons and advancing the ML community.
[2897.80 --> 2900.66]  That one's hitting your podcast feed next week.
