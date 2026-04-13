[0.00 --> 6.60]  In Impira, we really wanted to create an experience where users could easily see whether the predictions were right or wrong.
[6.98 --> 13.28]  And then if the predictions are wrong, or if they feel compelled to give us feedback that they're right, they could correct or confirm things.
[13.60 --> 17.78]  And every time they do that, we drive the feedback into the model and incrementally train it.
[17.94 --> 29.24]  And so because of that design, we basically structured the machine learning approach to be one that is very, very lightweight and something that can train and evaluate really, really quickly.
[30.00 --> 59.98]  Thank you.
[60.00 --> 62.00]  Thank you.
[62.00 --> 78.30]  Welcome to another episode of Practical AI.
[78.30 --> 85.98]  This is the podcast that likes to bring practical issues in artificial intelligence and learn as we go.
[86.18 --> 88.68]  I am your co-host, Chris Benson.
[89.28 --> 95.20]  Daniel Whitenack is unfortunately traveling right now, so he's going to miss what I'm sure is going to be a pretty cool conversation.
[96.02 --> 104.46]  And without further ado, I would like to introduce our guest today, Ankur Goyal, who is the founder and CEO of Impira.
[104.64 --> 105.34]  Welcome to the show.
[105.34 --> 106.56]  Thank you so much for having me.
[106.60 --> 107.20]  I'm really excited.
[107.58 --> 108.24]  Yeah, absolutely.
[108.48 --> 111.76]  So we've got a bunch of cool things to dive into today.
[112.30 --> 120.10]  I guess if you could just, as a start, kind of before we actually dive into the topic, kind of tell us how you got here.
[120.34 --> 120.94]  Who are you?
[121.08 --> 121.96]  What's your story?
[122.34 --> 129.90]  And how did you arrive so that you could tell the world about what you're going to be talking about today, which is your company and Doc Query in particular?
[129.90 --> 135.78]  Awesome. Yeah. So I actually don't have a mathematical background in machine learning or AI.
[136.16 --> 139.16]  I've been working on relational databases for a really long time.
[139.46 --> 144.22]  I actually started doing research on them in school and worked at a company called Single Store.
[144.22 --> 148.28]  I joined as the second employee and was the VP of engineering there for some time.
[148.82 --> 156.02]  And what got me into the space is actually talking to our customers who were able to make use of data that is structured,
[156.02 --> 161.72]  but really struggled when the data that they wanted to work with didn't fit inside of the relational database that we built.
[161.72 --> 164.68]  And so I thought, you know, there has to be a better way.
[165.44 --> 172.66]  And looking around me, it was clear that the progress, and this was back in 2017, and a lot has changed since then,
[172.76 --> 179.94]  but even back then it was really clear that the progress on the machine learning side would make it possible for people to work with any kind of data,
[179.98 --> 183.46]  no matter how structured or messy or complicated it is.
[183.46 --> 185.46]  And that's what we're all about at Impira.
[185.66 --> 193.42]  We're one part database and one part machine learning technology that basically makes it really easy to work with unstructured data.
[194.06 --> 194.46]  Very cool.
[194.66 --> 201.56]  You know, as you came into the industry and, you know, getting ready to set up your company and looking at that with unstructured data,
[202.30 --> 211.56]  like, could you tell us a little bit about what you were walking into and why you chose the particular path in the industry that you did?
[211.56 --> 215.86]  You know, what was it that attracted you down the path that you did as an entrepreneur?
[216.32 --> 219.04]  Yeah, it was first thing I'll say is definitely a windy road.
[219.40 --> 223.52]  And we didn't know exactly what we were getting ourselves into when we started.
[223.88 --> 235.18]  So actually, when we started, we thought that the really big problems in helping companies work with unstructured data would be in helping them work with image and video content.
[235.18 --> 241.62]  And I think as it's becoming really clear now with images and videos, the bottleneck is actually creation.
[241.84 --> 242.86]  It's not understanding.
[243.52 --> 248.40]  And so we learned that, you know, just purely on the market side of things a few years ago.
[248.40 --> 258.34]  And as kind of a funny coincidence, because one of the models that we ran on data that people uploaded was OCR, which is optical character recognition.
[259.08 --> 269.50]  Some of our customers started asking, you know, you can do this stuff with images and videos, but can you also analyze the data that is in my invoices and, you know, my forms and other documents?
[269.50 --> 277.34]  And we realized that there was actually a really exciting opportunity for us to help companies work with this kind of unstructured data.
[277.48 --> 281.32]  And so kind of a happy accident we discovered together with our customers.
[281.78 --> 290.06]  You know, it's interesting that you mentioned that particular example, because I know when I think of things like invoices and I run a separate from this, I run a nonprofit.
[290.32 --> 294.48]  So I kind of have that business hat I have to wear separately.
[294.48 --> 303.60]  You know, I'm thinking of things like PDFs and things, you know, that are not typically what we're thinking of when we're training models.
[303.88 --> 312.30]  You know, it's not the form that we're usually we're not going and pulling a bunch of data out of a database to train on or sources off the Internet or whatever.
[312.80 --> 319.66]  So that's a little bit of a different take from your typical avenue into machine learning off the bat.
[319.66 --> 324.20]  How you like like what is you started recognizing that was a challenge?
[324.58 --> 330.56]  Did that worry you at all in terms of recognizing that you had you were going to kind of take a different approach?
[330.90 --> 331.74]  It probably should have.
[332.08 --> 338.78]  But as usual with with myself and co-founders and kind of how we think it didn't.
[338.78 --> 349.60]  And actually, Richard, who's our CTO, came up with a really powerful approach to solving this problem that uses primarily computer vision, actually, to reason about PDF files.
[349.82 --> 356.04]  And so for a long time and we're foreshadowing a little bit with Doc Query, which kind of brings these worlds together.
[356.04 --> 360.94]  But for a long time, actually, a lot of the work that we did used computer vision.
[361.08 --> 369.50]  And so we thought if a PDF is like a hybrid of text and visual stuff, we leaned on the side of the visual stuff.
[369.76 --> 374.44]  And that has a number of advantages and disadvantages, which we've learned over time as well.
[375.08 --> 376.82]  So you've mentioned PDFs.
[376.96 --> 381.60]  Do you focus strictly on PDFs or are there other file formats that you end up working with as well?
[381.60 --> 389.24]  What we do is we take almost any file you could throw at the system that you could, you know, like self-identifies as a document.
[389.52 --> 398.04]  Anything from PDF files to emails, HTML files, scanned images, pictures from your phone, just about anything.
[398.54 --> 407.18]  And we do a bunch of pre-processing up front that basically normalizes anything you upload into a fairly consistent data structure.
[407.18 --> 421.72]  So from, you know, whatever you put into the system, we normalize it into a bunch of pixels, a bunch of text, and a bunch of bounding boxes that tell you, you know, where the pieces of text are, as well as a few kind of other things.
[421.72 --> 437.24]  Gotcha. So before we dive fully into kind of how you're approaching it at this point, what was in place, you know, both from the early machine learning days as we're going back a few years talking about that, but also, you know, you mentioned OCR.
[437.94 --> 449.30]  And like, what were the approaches people were taking and what was the mental model around that that you were looking at and saying, that's not good enough, you know, based on what you were starting to think?
[449.42 --> 451.14]  What was the world looking like at that point?
[451.14 --> 460.20]  You know, what's really interesting about this is OCR is not a new thing. Neither is reading data from invoices or other kinds of documents.
[460.76 --> 468.30]  But for some reason, most businesses don't take advantage of it. And I think that's because the solutions out there are just not easy enough to use.
[468.70 --> 477.50]  And so we've always thought about this from the standpoint of what does it take to make something that's actually so easy to use that it provides value for someone.
[477.50 --> 482.82]  So, you know, the solutions that existed prior, they fell into a few different buckets.
[483.16 --> 494.96]  One is something called an OCR template, where basically you take OCR text and then you draw a box of XY coordinates, you know, around exactly where the text needs to be.
[494.96 --> 504.72]  And if you're working maybe at the DMV or something and taking identical documents and scanning them with an identical scanner every time, that approach can actually work really well.
[505.22 --> 510.22]  You know, in reality, I'm sure with the invoices that you're working with in your business, it's never that simple, right?
[510.22 --> 517.58]  And so that's an example where, you know, the user experience and cost barrier in practice can be just prohibitively high.
[518.10 --> 527.04]  Another technique that was really emerging when or emerging as more popular when we started is this really big pre-trained model approach.
[527.04 --> 532.18]  So AWS has a product called Textract, for example, which is actually it's a great product.
[532.72 --> 540.92]  And what it allows you to do is upload any document into it and it will give you back some kind of data structure about what's in the document.
[541.64 --> 547.30]  And the nice thing about this approach is you don't need to do any of that template definition or, you know, anything like that.
[547.64 --> 555.38]  But the challenging thing about it is that if the results aren't what you expected, then you don't really have any recourse, you know, to solve for it.
[555.38 --> 566.18]  So we actually, a number of our early customers were using Textract and building machine learning models on top of Textract to normalize the data to be consistent.
[566.32 --> 570.16]  And they realized, you know, this is just not, what are we doing here, right?
[570.68 --> 576.98]  So it was essentially a Band-Aid that they were kind of creating on top of the product they were using or the service they were using.
[577.26 --> 578.80]  A very fancy Band-Aid, yeah.
[578.80 --> 587.52]  So, you know, with, and I know that we have seen kind of evolutions over quite a long time in OCR, you know, in terms of that.
[587.70 --> 591.18]  And you mentioned something, though, that made me curious.
[591.18 --> 598.86]  You were talking about, like, if you are using one of those early models that were pre-trained and then you didn't get what you wanted out of it.
[598.86 --> 610.30]  Can you talk a little bit about, like, what kinds of problems might arise in terms of, like, why weren't they getting it out of those models to kind of define a little bit about the space that you're fixing, you know, going forward?
[610.54 --> 610.88]  Absolutely.
[611.32 --> 611.58]  Yeah.
[611.58 --> 615.80]  So there are two or three classes of problems.
[616.02 --> 617.18]  I think there are three.
[617.62 --> 627.54]  So the first kind of problem is, let's say you take a relatively low quality image, like a scan that maybe is actually hard for a human to even decipher.
[627.66 --> 630.54]  Or maybe it has really bad handwriting or something like that.
[630.54 --> 633.50]  And you upload it into one of these products.
[633.66 --> 639.96]  If it can't read the handwriting or it can't read past the quality, there's really nothing you can do about it.
[639.96 --> 642.08]  And so that's one class of problem.
[642.44 --> 654.24]  Another class of problem is if you just consider a single document and you upload it into a service like this, it may not actually pick up all of the fields that are in the document.
[654.76 --> 660.22]  So one of the problems that we see, it's almost like, you know, bald spots or something in the document.
[660.82 --> 661.90]  It'll just miss things.
[662.04 --> 668.62]  And if it misses something, there's no way of telling it, like, hey, please don't miss this field next time.
[668.62 --> 671.00]  I mean, you know, there's no input like that that you can provide.
[671.10 --> 674.84]  Because it's all pre-trained and you've got what you got to work with at that point, right?
[675.00 --> 675.36]  Exactly.
[675.70 --> 676.08]  Exactly.
[676.60 --> 684.06]  And the third thing is that if you imagine, you know, working with many, many documents, they all might have different bald spots.
[684.06 --> 695.48]  And so you might have two documents, which for a user have the same schema, meaning they have the same fields that you want to extract, but you upload them into a schema-less service and you get back two different schemas.
[695.48 --> 707.34]  And that's actually where some of our early users were implementing their own machine learning models to try to translate from the schema that the pre-trained model produces to the schema that they actually want to work with.
[707.74 --> 710.24]  That is not a problem I had really considered.
[710.50 --> 713.86]  That's an interesting side effect that you get on that.
[713.86 --> 717.42]  So you end up training in those early models.
[717.60 --> 719.84]  You end up, you know, having the trained model.
[720.02 --> 722.86]  You are running the document through the model.
[723.08 --> 731.26]  It comes up with both the whitespace issues and it also leaves you with the problem of an inferred schema that was not intended.
[731.66 --> 738.64]  And then I assume that at the end of that, you're trying to kind of get it all corrected back to what it needs to be.
[739.22 --> 742.42]  So that's a lot of manual effort there.
[742.42 --> 749.42]  You may have some tooling to help you along, but there's kind of a manual cleanup process that you're having to go through.
[749.96 --> 752.02]  So definitely interesting.
[752.28 --> 761.58]  One of the things I wanted to ask about as far as that goes is you talked about OCR, but we're also talking about language models here.
[761.80 --> 764.22]  And you said that you were starting with the visual models.
[764.36 --> 770.16]  So we're not yet talking about any kind of NLP, natural language processing or anything like that, I'm assuming.
[770.16 --> 773.80]  We're talking about some sort of early visual model that's pre-trained.
[774.16 --> 774.46]  That's right.
[774.54 --> 779.44]  Although in Impira, the model that we had early on was actually not pre-trained.
[779.58 --> 785.40]  Because of how it works, it would actually learn just on the user's documents that they uploaded.
[785.80 --> 786.36]  Interesting.
[786.36 --> 787.24]  Yeah.
[787.24 --> 817.22]  Thank you.
[817.24 --> 847.22]  Thank you.
[847.24 --> 855.20]  So that we kind of get a sense of how we would ultimately get to what I'm going to get to in a moment, which is kind of where, you know, where DocQuery has landed.
[855.34 --> 864.92]  But kind of tell us a little bit about how what that that pathway from I've identified the landscape to here's a much better way of doing it.
[864.92 --> 869.40]  Yeah, so we kind of set ourselves up with a few constraints early on.
[869.66 --> 873.36]  One of them was that we wanted to make the product completely self-service.
[873.90 --> 884.36]  And our definition of that was that a user can sign up on our website without talking to anyone, onboard onto the product, and then evaluate whether it works on their documents or not.
[884.36 --> 888.22]  The second thing is that we wanted to support documents of any schema.
[888.78 --> 892.90]  So if we hadn't seen that particular document type before, that's totally fine.
[893.00 --> 894.86]  We'd be able to learn about it on the fly.
[894.86 --> 902.98]  And third thing was that we wanted the product to be incredibly easy for a non-technical user to use and work with.
[902.98 --> 923.22]  And so what we did after performing a lot of user research is realized that most of our users are either beginner or advanced Excel users, meaning we could safely assume that our users were able to work with Excel at a basic level, like entering data and some basic formulas and stuff.
[923.32 --> 929.88]  And then we could also assume that some of our more advanced users are really, really powerful Excel users.
[929.88 --> 938.64]  And so in Impira, even from the very start, you've been able to kind of create these really complex expressions and formulas and stuff.
[938.64 --> 955.48]  And we realized the reason for all of this is that, and if you sort of tie it back to what I was saying about pre-trained models not evolving when you notice something is wrong, we really wanted to create an experience where users could easily see whether the predictions were right or wrong.
[955.48 --> 962.42]  And then if the predictions are wrong, or if they feel compelled to give us feedback that they're right, they could correct or confirm things.
[962.76 --> 966.96]  And every time they do that, we drive the feedback into the model and incrementally train it.
[967.46 --> 979.94]  And so because of that design, we basically structured the machine learning approach to be one that is very, very lightweight and something that can train and evaluate really, really quickly.
[980.40 --> 984.64]  And so that's kind of the overall approach for how we tackled it.
[984.64 --> 992.58]  So I have what seems to me like it may be an odd question, but as you were kind of talking your way through that, it's what came to mind.
[993.02 --> 996.74]  What are the things that you need to really be able to do with the document?
[996.90 --> 1002.56]  You know, with .query being called .query, for instance, like what does it mean to query a document?
[1002.78 --> 1005.74]  I mean, because that could be interpreted in so many ways.
[1005.88 --> 1010.78]  It started something as simple as people doing control F to do a find on a document.
[1011.02 --> 1012.26]  Oh my God, I love this question.
[1012.26 --> 1014.42]  Yeah, what are the things that matter?
[1014.58 --> 1016.40]  Because it occurred to me, I don't know what those are.
[1016.64 --> 1023.44]  Yeah, so I'd say like from a user's standpoint, there are a few different things that they're really interested in.
[1023.88 --> 1032.10]  And then we can talk a little bit about the sort of Imperius technology and what part of that we hit and what part of it we missed until we introduced .query.
[1032.10 --> 1035.78]  But, you know, users care about one is integration.
[1036.12 --> 1040.16]  So there are really common workflow for a lot of different types of documents.
[1040.52 --> 1044.46]  And I'm sure you'll relate to this from your nonprofit business as well.
[1044.54 --> 1046.70]  But you receive documents through email.
[1046.70 --> 1049.58]  You have to interpret them to some extent.
[1050.16 --> 1055.08]  And that could mean, you know, reading the whole document or just eyeballing something and figuring out where it should go next.
[1055.52 --> 1058.44]  And then you need to take that information and shove it somewhere.
[1058.98 --> 1071.78]  And what that looks like in a workflow like accounts payable, for example, is receiving an invoice through email, opening the invoice on your screen, and then manually keying in the information into your ERP system.
[1071.78 --> 1075.82]  And there's usually some judgment or interpretation that goes in as well.
[1075.94 --> 1079.16]  So it's not these things are never totally literal.
[1079.70 --> 1085.34]  You might be making sure that, you know, the purchase order number that's on the invoice is actually one that's in your database.
[1085.34 --> 1095.22]  You might check that, you know, shipping plus subtotal plus tax equals the total and sending an email back to the vendor if it doesn't or doing some other stuff as well.
[1095.38 --> 1097.48]  And so that's kind of like the basic workflow.
[1097.60 --> 1101.70]  The other thing that people really want to do is ask questions.
[1101.78 --> 1109.74]  So, you know, not just sort of run the formula of like, does this plus this plus this equal that, but say like, are these two numbers equal?
[1109.74 --> 1114.06]  Or of these 100 invoices, which ones are due next week?
[1114.06 --> 1117.98]  Or what was the most expensive line item on this invoice?
[1118.60 --> 1121.16]  And that, it kind of overlaps with search.
[1121.46 --> 1129.64]  Although what we see is that people, they're looking for answers to questions that are fairly analytical in nature.
[1129.64 --> 1133.02]  And a lot of this is done, you know, very, very manually today.
[1133.60 --> 1133.80]  It is.
[1133.86 --> 1134.64]  So it's kind of funny.
[1134.66 --> 1141.18]  And it's funny that you referenced me doing the nonprofit thing because these are agonies.
[1141.28 --> 1151.90]  They're little things that I know for a fact because just to bring in my own experience into the conversation, my wife and I are doing these administrative tack, you know, things that we have to do.
[1151.90 --> 1155.68]  We have a group of volunteers and all, but most of the admin falls to us.
[1156.02 --> 1163.10]  And they're tasks that neither one of us is particularly trained in, nor particularly are they things we love to do.
[1163.56 --> 1167.68]  And so as you were describing that, I was like, oh, yeah, that was a pain.
[1167.72 --> 1168.70]  Oh, yeah, that's painful.
[1168.92 --> 1170.16]  Yeah, that's painful as well.
[1170.16 --> 1174.00]  So it's interesting that you've identified all of these pain points.
[1174.00 --> 1181.92]  And I realize you're not specifically talking about nonprofits or small organizations, but indeed, they are things that definitely impact us as users.
[1182.50 --> 1186.88]  We do actually have quite a few nonprofit users and customers of Empira.
[1187.10 --> 1191.12]  So we've heard this feedback very directly from them as well.
[1191.28 --> 1191.40]  Yeah.
[1191.40 --> 1199.74]  So as you've kind of recognized all this, can you talk a little bit about what Empira has done and how DocQuery fits into that?
[1199.92 --> 1205.54]  And like within the scope of you've kind of laid out the problem and you've laid out kind of approach to solution.
[1205.82 --> 1212.22]  Could you talk a little bit about how that is kind of realized in Empira and broad and specifically in DocQuery?
[1212.76 --> 1213.18]  Absolutely.
[1213.36 --> 1213.52]  Yeah.
[1213.60 --> 1219.52]  So if you think about what I mentioned with Empira, there are a few things that really stand out.
[1219.52 --> 1223.10]  One is that users can work with any field that they want.
[1223.36 --> 1224.96]  They can create any schema that they want.
[1225.36 --> 1228.42]  And the second is that we really care about ease of use and simplicity.
[1229.14 --> 1241.26]  And so if you rewind back a few months, we were in kind of a state where you could create whatever field that you wanted, but you had to provide at least one label on the document.
[1241.42 --> 1244.64]  Like you had to highlight and click something to teach the model.
[1244.64 --> 1253.14]  And even though you didn't have to do it for every single format that you uploaded, you had to do it for most of the formats that you uploaded at least one label.
[1253.24 --> 1263.98]  So if you imagine with invoices, if you had like 100 different vendors, you might need to provide like 50 or 60 labels to teach the model about the breadth of vendors that you had.
[1263.98 --> 1273.76]  And so what we started thinking is, okay, how do we solve the problem of making it so you don't need to provide any labels in this case?
[1273.90 --> 1284.10]  And not only would that provide a much better user experience, but it also would mean that we'd be able to address the long tail of variety a lot better.
[1284.10 --> 1294.90]  And that means that if you upload something that we haven't seen before or doesn't look like something that you've trained your model on, it still has a fighting chance at extracting the data correctly.
[1295.56 --> 1306.96]  And so we started open-endedly exploring, like pull our head kind of out of the sand of all of our impura context and open-endedly started exploring what else was out there.
[1306.96 --> 1318.90]  And actually the first thing I did, I remember doing it on the car ride to the airport from New York back to San Francisco, was copy-paste manually the text out of a bunch of invoices.
[1319.18 --> 1326.16]  To your point earlier, like PDFs have all the structure, but I was just copying it out and basically ignoring all of the structure.
[1326.16 --> 1339.94]  And on Hugging Faces website, trying out a few different models that are pure text question answering models and pasting the text into the website and asking questions like, what is the invoice number and what is the total?
[1340.46 --> 1344.14]  And I was just blown away by how accurate it was.
[1344.14 --> 1346.78]  It wasn't not even like 60% accurate, right?
[1346.88 --> 1356.84]  But still like with no context about this problem, nothing to do with invoices, no training data about invoices, no PDF structure or anything like that.
[1357.24 --> 1358.70]  It was like that accurate.
[1359.08 --> 1361.14]  And so that kind of blew my mind.
[1361.30 --> 1367.76]  I mean, if it was that accurate with something that was so distant from what we were doing, it meant a few things.
[1367.90 --> 1371.52]  One is we could probably do better if we put in a little bit of effort.
[1371.52 --> 1383.80]  Two, you know, we had this epiphany that the framework of question answering allows a sort of infinite canvas of any fields or any questions that you want, which is very in line with our product's philosophy.
[1384.46 --> 1399.24]  And then three, because something that has never looked at any documents like the ones I was pasting into the text box, because it was working so well with that, that probably meant that it would solve that generalization problem that I mentioned earlier.
[1399.24 --> 1409.04]  And so that sort of experience, I still remember the car ride and I still remember, you know, working on my hotspot and stuff and furiously kind of playing with it.
[1409.08 --> 1410.96]  That sort of kicked off this whole idea.
[1411.36 --> 1412.26]  That's very interesting.
[1412.50 --> 1414.24]  And I know this is fairly recent.
[1414.50 --> 1419.66]  You've actually hit a whole bunch of things that I want to, I'm going to touch on with a couple of follow-up questions.
[1420.02 --> 1422.02]  First of all, this was a recent announcement.
[1422.10 --> 1424.24]  It was only on September 1st that you announced .query.
[1424.24 --> 1429.54]  And another thing that you mentioned just now was hugging face and stuff.
[1429.70 --> 1435.64]  So I'm curious about several things that, you know, I'll kind of throw several out to you.
[1435.94 --> 1440.30]  How has that model evolved that you've had as you've done this?
[1440.34 --> 1441.34]  You had started in the visual.
[1441.70 --> 1444.84]  You talk about large language models in your Twitter.
[1445.26 --> 1449.94]  There's obviously an evolution of, you know, deep learning technologies that you're applying here.
[1449.94 --> 1454.14]  And as you did that, how did hugging face fit into that?
[1454.40 --> 1458.20]  We have a habit of talking about hugging face quite a lot on this show.
[1458.32 --> 1459.48]  We're big fans.
[1459.84 --> 1462.22]  So how did all that come together?
[1462.40 --> 1462.42]  Yeah.
[1462.52 --> 1466.18]  The evolution, hugging face, everything fit in with that.
[1466.64 --> 1468.68]  So we're also big fans of them.
[1468.78 --> 1474.12]  And we've actually had the distinct pleasure of collaborating with them on this problem.
[1474.12 --> 1493.68]  So essentially what happened is they have this cool thing called a pipeline and a pipeline for people like me who are not machine learning experts and barely understand what logits are, like any of this kind of stuff, abstracts away all of that complex machinery and makes it really easy to work with models.
[1493.68 --> 1500.96]  And so the pipeline that I was experimenting with is called the question answering pipeline, and it's all over their website.
[1501.20 --> 1505.86]  And any model that kind of fits the question answering framework works with it.
[1506.08 --> 1521.52]  So after we saw this, Richard and I chatted and we were aware of some work out of Microsoft for a project called Layout LM, which is a language model that in addition to taking text as input, it also takes bounding boxes for each word of text.
[1521.52 --> 1529.90]  And so that kind of introduces the geometric information into the model that is actually super relevant to our problem.
[1530.38 --> 1537.90]  And just to give you an example, you might have the text invoice number, and then the actual invoice number might be to the right of it.
[1538.22 --> 1543.68]  And if you turn that into plain text, then even a plain text model could pick up on that relationship.
[1544.24 --> 1548.54]  On the other hand, you might have the word invoice number and then the text beneath it.
[1548.54 --> 1551.76]  And you might have some other text to the right of the word invoice number.
[1551.98 --> 1558.82]  And without the bounding box information, it's actually really hard for a model to be able to pick up on that kind of relationship.
[1559.50 --> 1564.14]  And so Layout LM seemed like a really promising approach to solving that.
[1564.14 --> 1577.88]  But for some reason, when we dug around Hugging Face and scoured GitHub and Google at large to see if there was a question answering pipeline that worked with Layout LM, we just couldn't find anything.
[1577.88 --> 1602.00]  And it seemed to us like, wow, if we had this awesome experience working with text-based question answering, and we know we're not the only people trying to work with documents, but there's nothing quite that easy out there, maybe we should kind of take the lead on this and make it just that easy to do document-based question answering as well.
[1602.00 --> 1611.46]  And so we reached out to the team at Hugging Face, actually just by filing a GitHub issue, and they were incredibly receptive to the idea.
[1612.20 --> 1630.16]  And over a month of collaboration and working with them, we actually contributed the document question answering pipeline that's now in Hugging Face and a model that's pre-trained and MIT licensed and everything that you can play with and work with and even put into production that works with it and actually makes it that easy.
[1630.16 --> 1660.14]  Thank you.
[1660.16 --> 1664.76]  Really, really, really leading-edge technologies from Hugging Face in terms of their pipeline.
[1665.38 --> 1669.94]  What made you decide as an entrepreneur to release DotQuery as open source?
[1670.20 --> 1672.22]  What was the business motivation there?
[1672.74 --> 1676.74]  Yeah, so I think there are maybe three reasons for it.
[1677.10 --> 1680.58]  The first is not the business motivation, but just the personal motivation.
[1681.04 --> 1685.62]  When things are open source and they're easy to work with, it removes all barriers to innovation.
[1685.62 --> 1701.42]  And I think selfishly as someone who cares a lot about innovation, but also as a member of the tech community at large, I think being able to contribute to people innovating and making it easier for them to innovate and play with ideas, it's just very important to me.
[1701.42 --> 1706.72]  From a business standpoint, the second thing is you could think about it in terms of distribution.
[1706.72 --> 1729.68]  So in exchange for providing something that's generally useful to a large community of people, we have the opportunity to get some mindshare and for them to familiarize themselves with us as a company, to experience technology that we create and form an opinion about how credible we are as product builders and so on,
[1729.68 --> 1737.30]  in a way that doesn't require them to give us email or talk to a salesperson or anything like that.
[1737.48 --> 1747.62]  And so just purely from the standpoint of distribution, it's actually really valuable to us as a company to have the mindshare and attention associated with it.
[1747.62 --> 1758.64]  And then the last thing is being confident about what our proprietary strategy can be in the context of having open source stock query.
[1759.32 --> 1767.48]  And there are a couple of things that make me really confident that we can still be a really successful proprietary product.
[1767.48 --> 1784.06]  The most important one is that when you, as a customer, use our product, you have this really real-time data flywheel, which allows you to correct things, review things, integrate things, and the models will keep improving just for you to be able to do that.
[1784.24 --> 1791.26]  And time and time again, we've seen how important that is for people to put models into production in commercial settings.
[1791.26 --> 1802.18]  And we know that the ease of use UI security integrations workflow involved is something that is actually really hard to build and engineer yourself.
[1802.38 --> 1806.86]  And so we know that that's extremely valuable and we feel confident in that.
[1807.02 --> 1819.38]  And so if something, you know, for things outside of that, that kind of opens up the possibility of open sourcing them and still being able to derive a lot of value from this kind of core proprietary product.
[1819.38 --> 1829.44]  You said something that struck me right there about kind of having that level of confidence and the fact that you already knew it was hard to kind of build those things out.
[1829.88 --> 1838.92]  That is something that stops a lot of would-be entrepreneurs right in their tracks, you know, is that you've kind of dived into the deep end of the pool.
[1838.92 --> 1848.16]  You've said a couple of times in our conversation that, you know, you were not coming into this as a world-class deep learning expert yourself, you know.
[1848.30 --> 1853.52]  You've built a team obviously around it, but you were coming in as someone with an idea.
[1853.52 --> 1871.34]  What gave you the confidence or the bravery to kind of to dive into the deep end of the pool and do something that we normally associate with people who might have a different background, you know, have all that heavy math and years of deep learning, modeling and stuff like that.
[1871.82 --> 1873.88]  How did you get past that?
[1873.90 --> 1880.42]  Because there are probably a thousand people listening right now that, you know, they want to be entrepreneurs.
[1880.60 --> 1881.26]  They've tried it.
[1881.32 --> 1882.78]  Maybe they've tried and failed.
[1882.78 --> 1884.54]  How did you get past those hurdles?
[1885.08 --> 1885.24]  Yeah.
[1885.36 --> 1888.92]  So I'll give you the real answer and the inspiring answer.
[1889.16 --> 1889.52]  Okay.
[1889.64 --> 1890.04]  Fair enough.
[1890.30 --> 1892.32]  The real answer is just stupid naivete.
[1893.50 --> 1895.12]  Like I didn't even think about that.
[1895.18 --> 1901.62]  And I've learned and been humbled so many times by so many smart people over the past 10 years.
[1902.12 --> 1905.12]  And I'm still pretty stupid and still pretty naive.
[1905.22 --> 1907.50]  And I hope I am that way for some time.
[1907.82 --> 1909.40]  But that's the real answer.
[1909.40 --> 1935.10]  Now, the, I think, more hopefully inspiring version of that is that as someone who is not deeply familiar with the math and deeply entrenched in the existing workflow for how things operate, it gives you a really unique perspective on what it would take to make something easy to use and simple enough that non-experts can take advantage of it.
[1935.10 --> 1941.02]  And I think a lot of what you're doing as an entrepreneur is bringing together two perspectives.
[1941.02 --> 1945.90]  The one perspective are the people who you can feel need something.
[1946.44 --> 1952.08]  And the other perspective is the perspective of the people who feel they can build that thing.
[1952.08 --> 1973.44]  And as someone who's not a machine learning person, it's very easy for me to go onto Hugging Faces website and play with the question answering model and then try to read the documentation about the layout LM model, which had no examples and nothing that easy to use and see the difference.
[1973.44 --> 1982.30]  Simply because I was, I just didn't understand enough about the model complexity and so on to actually understand.
[1982.74 --> 1984.52]  And so I was able to see that difference.
[1985.02 --> 1990.52]  And I think actually knowing more than I had at the time would have prevented me from doing so.
[1990.64 --> 2001.72]  Now that I've actually learned a decent amount about this stuff, I don't have that same experience when I'm like reading through papers about models or documentation and I almost miss it.
[2001.72 --> 2003.74]  I'm curious as you've done that.
[2003.80 --> 2013.04]  And by the way, you're like, I really think that what you said was quite wise in terms of kind of having that always willing to learn, you know, knowing that you're never there.
[2013.24 --> 2014.34]  I think so.
[2014.82 --> 2018.80]  You've had several really great insights, I think, in your process.
[2019.04 --> 2027.18]  And, you know, one of which was the benefit of doing it as open source, which scares a lot of people off, obviously, in terms of as a business model.
[2027.18 --> 2037.10]  But, you know, one of the things that we know is that when you have a great product, you're solving a problem well, and you put it out there like that, it makes it very accessible, as you mentioned earlier.
[2037.46 --> 2049.56]  So adoption tends to be much higher when you do that, because it's, you know, people can can dive in at whatever level that, you know, they're comfortable with and give it a shot and figure out, you know, how to engage you going forward.
[2049.56 --> 2056.52]  As you do that, like, what, what do you think is are the next steps for dot query and appear at large there?
[2056.76 --> 2060.22]  And then, and then I'll ask you kind of a broader question after that.
[2060.24 --> 2067.76]  But I'm kind of curious, very specific to dot query, where do you think it's going to go over the next year or so from an adoption standpoint?
[2067.76 --> 2071.26]  And in terms of like, what's your short term vision for that?
[2071.26 --> 2091.48]  Yeah, so in the very near term, thanks to like, just a fantastic flood of feedback of users, both through, you know, GitHub and discord, among other channels, we have a pretty good sense of the types of questions that people want to ask about a document that they can't currently ask with dot query.
[2091.48 --> 2105.88]  And the really beautiful thing about the question answering framework is that it actually encourages that creativity, people can really easily type, you know, whatever question they want, and either get an answer or not get an answer.
[2106.04 --> 2116.92]  And so the two kinds of questions that people keep trying to ask that we're not able to answer about a single document with dot query are what kind of document something is.
[2116.92 --> 2123.88]  So like, for example, is this an invoice, or is this a purchase order, or is this an invoice from this vendor?
[2124.36 --> 2127.52]  And the other kind of thing they're trying to ask are questions about tables.
[2127.94 --> 2137.74]  And we actually support an example of a question about tables would be like, give me all the line items on this invoice, or what are all of the descriptions?
[2138.46 --> 2141.32]  Or what is the first or second or third description?
[2141.90 --> 2144.88]  Or what is the highest total value or something like that?
[2144.88 --> 2156.94]  And these are things that we actually are fortunate to have a good amount of data for, and in the very near term, are basically expanding the question answering model to be able to support.
[2157.22 --> 2167.78]  We have looked at other model frameworks, for example, things like document classification as a framework, or, you know, like visual table detection and stuff.
[2167.78 --> 2171.48]  And we have a lot of experience trying these things out within the Empira product.
[2171.80 --> 2177.74]  But we feel pretty confident that we can basically expand the question answering framework to support them.
[2177.84 --> 2180.52]  And we just love the fact that it's an infinite canvas.
[2180.52 --> 2192.74]  The next step from there, which I'm extremely excited about, is allowing people to ask natural language questions over multiple documents, or a pile of documents, if you will.
[2193.00 --> 2196.40]  And that could be things as simple as like, what are all the invoices?
[2196.66 --> 2200.04]  Or, you know, find me all the invoices in my Google Drive folder.
[2200.30 --> 2204.88]  Or things that are more complicated, like, what are the invoices that are due next month?
[2204.88 --> 2207.46]  Or, which invoices am I past due on?
[2207.84 --> 2213.44]  Or, which invoice from this vendor is the one that's most relevant to this contract?
[2213.68 --> 2214.86]  Or something like that.
[2215.44 --> 2216.60]  Is that farther out, though?
[2216.72 --> 2222.10]  Or is that something that would be, is that something you think is, like, are you close to that?
[2222.18 --> 2224.74]  Or do you think it's going to take a little while to get to that point?
[2225.30 --> 2226.90]  Well, the model is training right now.
[2227.88 --> 2230.90]  There's a few moving parts that we're trying to figure out.
[2231.02 --> 2232.78]  That kind of, that was a great answer right there.
[2232.78 --> 2233.08]  Yeah.
[2233.70 --> 2235.66]  I mean, like, literally training right now.
[2235.80 --> 2239.54]  I kicked off the most recent run right before the podcast.
[2240.44 --> 2247.26]  I'll give you the teaser for how that works, which is that, actually, we've studied this problem a lot through Impero's product.
[2247.42 --> 2250.58]  Because, long story short, people actually do this kind of stuff with Impero.
[2250.76 --> 2256.88]  You can extract fields, and then you can write queries over the fields as well.
[2257.28 --> 2260.98]  And we actually have a pretty powerful query language that makes all of this possible.
[2260.98 --> 2274.66]  And what we've realized is that you can take natural language and basically compile it into a query, which consists of both relational algebra and other models or questions to ask of documents.
[2275.20 --> 2279.38]  And so we're cooking this framework and making it work.
[2279.38 --> 2282.22]  And we've seen some really exciting initial results.
[2282.48 --> 2284.78]  But I don't think it's going to be too long before that's possible.
[2285.24 --> 2299.40]  And then as we think about it further, one of the things that we did, and I'd encourage anyone who's interested in the space to throw any idea you have at it, is we opened up a discussion on GitHub about, like, what are things that you'd like to be able to type that have to do with documents?
[2299.40 --> 2305.78]  And what's interesting is a lot of the questions or things that people want to type are also actions.
[2305.78 --> 2315.70]  So things like organize all of these documents into folders by their document type or forward along all of these things to this email address.
[2315.70 --> 2329.42]  And so I'm not exactly sure how we're going to tackle this in the open source part of the equation versus our product versus integrations with other products, because even our product doesn't do all of these things.
[2329.64 --> 2342.84]  But I think purely from the machine learning standpoint, we're starting to think about what the right framework looks like, both on the machine learning side and on the application side to make it possible to type things like that.
[2342.84 --> 2372.00]  And then the last thing I'll say is that as we push further into DocQuery, it's become increasingly clear to us that even though this question answering approach is incredibly relevant to working with documents, and it happens to work really well, this framework of having one or more things of data and asking questions about it is an incredibly powerful paradigm for people to work with data.
[2372.00 --> 2380.20]  And so our vision is increasingly becoming making it really easy for anyone to ask anything of any data.
[2380.62 --> 2384.78]  And how we sequence those parts together, we're still learning.
[2384.78 --> 2397.70]  I suspect one of the really great benefits of open sourcing DocQuery is going to be engaging people in the community who have different flavors of this use case to apply it in different domains.
[2397.70 --> 2413.58]  Like we probably won't build models that analyze video, but you could use 75% of DocQuery to manage getting the question, semantically representing it, turning it into relational algebra, yada, yada, yada.
[2413.82 --> 2418.78]  And someone really smart in the community could plug in the video aspect of it.
[2418.78 --> 2421.34]  And so that's kind of where I see the future of this.
[2421.54 --> 2434.44]  And I think open source in particular is going to be a really powerful vector for us to engage a much larger audience than our limited engineering bandwidth has the capacity to support over the long term.
[2435.44 --> 2437.76]  Well, Ankur, that is very inspiring.
[2437.76 --> 2445.14]  It's kind of funny because, you know, on a day-to-day basis, many of us would think of just kind of document management as a fairly mundane thing.
[2445.34 --> 2454.44]  But it's such a huge impact on people's lives in a billion small ways in terms of making that better.
[2454.98 --> 2460.90]  It's definitely something that brings a lot of value to a lot of people around the globe.
[2461.12 --> 2463.46]  So thank you so much for coming on the show.
[2463.56 --> 2465.18]  It was a fascinating conversation.
[2465.56 --> 2466.70]  Thank you for what you're doing.
[2466.70 --> 2469.04]  Thank you for taking the approach that you've taken.
[2469.68 --> 2474.76]  And I'm looking forward to finishing up as this little nonprofit manager.
[2475.04 --> 2479.92]  I'm excited to use that to make my life just a little bit better going forward.
[2480.04 --> 2480.50]  Thanks a lot.
[2480.66 --> 2480.90]  Awesome.
[2481.14 --> 2482.56]  And send us any feedback you have.
[2482.64 --> 2483.06]  We'd love it.
[2483.22 --> 2483.66]  Absolutely.
[2492.42 --> 2493.32]  All right.
[2493.44 --> 2495.04]  That is our show for this week.
[2495.04 --> 2497.66]  If you dig it, don't forget to subscribe.
[2498.22 --> 2500.84]  Head to practicalai.fm for all the ways.
[2501.36 --> 2506.78]  And if Practical AI has benefited your life, pay it forward by sharing the show with a friend or a colleague.
[2507.12 --> 2510.08]  Word of mouth is the number one way people find shows like ours.
[2510.50 --> 2513.36]  Thanks again to Fastly for fronting our static assets.
[2513.66 --> 2516.08]  To Fly.io for backing our dynamic requests.
[2516.64 --> 2518.18]  To Breakmaster Cylinder for the beats.
[2518.44 --> 2519.34]  And to you for listening.
[2519.60 --> 2520.24]  We appreciate you.
[2520.56 --> 2521.44]  That's all for now.
[2521.44 --> 2523.20]  We'll talk to you again on the next one.
