[0.00 --> 8.64]  Welcome to Practical AI.
[9.20 --> 15.96]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 --> 18.78]  are changing the world, this is the show for you.
[19.20 --> 24.36]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.36 --> 24.66]  listen.
[24.92 --> 26.76]  Check them out at Fastly.com.
[26.76 --> 32.02]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 --> 33.70]  No ops required.
[34.02 --> 36.08]  Learn more at fly.io.
[42.22 --> 45.90]  Well, welcome to another episode of Practical AI.
[46.22 --> 47.62]  This is Daniel Whitenack.
[47.72 --> 53.40]  I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris
[53.40 --> 56.38]  Benson, who is a tech strategist at Lockheed Martin.
[56.76 --> 57.60]  How are you doing, Chris?
[58.04 --> 58.90]  Doing well, Daniel.
[58.96 --> 59.56]  How are you today?
[59.94 --> 65.36]  I'm actually super excited for this conversation because I don't know about you, but I've just
[65.36 --> 71.00]  been swimming in generative text AI for weeks and weeks.
[71.14 --> 72.44]  As have we all, I think.
[72.60 --> 72.82]  Yeah.
[72.90 --> 79.24]  This conversation feels like I can come up for air and think more to both computer vision
[79.24 --> 85.70]  and generative image AI and other things like that because we've privileged to have with
[85.70 --> 92.46]  us Amanda Waslewski, who is an art historian working in the digital humanities program at
[92.46 --> 93.60]  Uppsala University.
[93.60 --> 100.22]  And she's the author of a new book coming out in May, Computational Formalism, Art History
[100.22 --> 101.38]  and Machine Learning.
[101.88 --> 102.48]  Welcome, Amanda.
[103.14 --> 103.84]  Hi, thanks.
[103.92 --> 104.66]  Thanks for having me.
[105.22 --> 105.56]  Yeah.
[105.86 --> 106.04]  Yeah.
[106.12 --> 108.82]  This is like I say, I'm really excited about this.
[108.82 --> 115.62]  So I have to be honest, I was a little bit intimidated maybe because I don't know a lot
[115.62 --> 116.64]  about art history.
[117.12 --> 122.48]  But in looking at your book and also looking at your amazing research that you've been up
[122.48 --> 130.74]  to, like there's so much practicality in this, both in terms of like what is applicable to
[130.74 --> 134.70]  art historians and those working in that area, but also the things that you're talking about
[134.70 --> 142.88]  in terms of how we think about like machine learning and art and how those relate and especially
[142.88 --> 145.54]  in light of generative things in recent years.
[145.78 --> 148.86]  So yeah, it's super excited about this conversation.
[148.86 --> 155.14]  I'm wondering, you mentioned in the lead up to when we were talking pre-episode that your
[155.14 --> 157.50]  background is more on the art history side.
[157.82 --> 162.94]  Where did the art history and machine learning start to collide for you?
[163.24 --> 171.18]  I actually started out, well, I studied chemistry as an undergraduate briefly before kind of discovering
[171.18 --> 178.84]  art and art history and was a practicing artist for many years before I went back to the
[178.86 --> 180.80]  studying art history again.
[181.52 --> 186.34]  So I had a kind of, I guess I've never been formally trained, but I had a kind of sideline
[186.34 --> 194.02]  doing artwork that was based through using various digital technologies and certain kinds
[194.02 --> 194.52]  of programming.
[194.94 --> 200.00]  And I also kind of worked a little bit in, you know, web design and things like that.
[200.08 --> 205.98]  So I had a kind of background in computational things for both from a kind of art perspective
[205.98 --> 211.82]  and a professional perspective before I actually went into academia and academic art history.
[211.96 --> 217.30]  So I've always had those kind of interests in how art and technology co-aligned.
[217.86 --> 226.80]  And I kind of, I came to this whole field or the kind of emerging image and AI field through
[226.80 --> 232.62]  older things like image databases and how they're sorted by metadata, textual metadata.
[232.62 --> 234.66]  So that was the kind of entry point.
[234.90 --> 239.46]  And then suddenly it seemed that, you know, more and more art collections or digital image
[239.46 --> 242.86]  collections were starting to use different computer vision techniques.
[243.50 --> 249.78]  And so that's kind of how I came at the field through, you know, the way that computer vision
[249.78 --> 254.38]  was increasingly being used to sort large image collections and image collections of art
[254.38 --> 256.24]  in kind of institutional contexts.
[256.24 --> 261.88]  It's interesting that you mentioned both elements of like using machine learning to sort art, but
[261.88 --> 266.84]  also this background of like people using textual metadata to describe art.
[267.08 --> 272.70]  And I know that you use this word formalism, which in my understanding, like has some history
[272.70 --> 273.84]  in the art world.
[273.84 --> 281.48]  But like how standardized is the sort of literature and research around like how you describe the
[281.48 --> 284.22]  features of like an artwork?
[284.22 --> 290.42]  That's probably a very like naive way to ask that question as a person not in the field.
[290.42 --> 297.02]  But like I imagine, you know, metadata to describe artwork is like, you know, artist, Van
[297.02 --> 299.52]  Gogh, you know, medium, like whatever.
[299.86 --> 303.00]  What it seems like what you're talking about goes well beyond that.
[303.08 --> 305.18]  Could you kind of describe that space a little bit?
[305.66 --> 310.20]  As a quick add on, can you also add just a little bit about like what is art history coming
[310.20 --> 310.80]  into that?
[310.80 --> 315.12]  Because a lot of folks on, we probably have a lot of people that are doing machine learning,
[315.12 --> 317.52]  but not a lot of art history background.
[317.52 --> 322.08]  And some people may be wondering, including me a little bit about trying to understand
[322.08 --> 322.64]  what it is.
[322.72 --> 326.84]  So kind of working your way toward where Daniel was, but starting a little bit earlier for
[326.84 --> 327.08]  me.
[327.08 --> 332.82]  Well, one of the ideas of the book was actually to kind of, in my own way, try to like bridge
[332.82 --> 339.64]  this gap because, you know, as I said, I don't have any formal training in any of these like
[339.64 --> 341.58]  sort of the computer science side.
[341.70 --> 346.62]  But, you know, I've, you know, been in this kind of digital humanities milieu where it's
[346.62 --> 352.36]  a kind of combination of some computer science techniques with a kind of humanities focus in
[352.36 --> 352.84]  research.
[353.34 --> 360.08]  So, you know, I wanted with the book to both kind of introduce art history concepts to those
[360.08 --> 365.40]  people working in maybe computer vision, but also, you know, introduce people in art history
[365.40 --> 367.96]  to some of the things that are happening in computer vision.
[368.06 --> 372.84]  So kind of trying to play both sides a little bit, but obviously from my own perspective
[372.84 --> 374.06]  in art history.
[374.30 --> 378.60]  And so art history is not a very old academic discipline at all.
[379.04 --> 386.10]  Its origins in the 19th century revolved around sort of practices of collecting antiquities.
[386.10 --> 393.34]  So ancient Greek and Roman artifacts and that kind of collecting practice started to become
[393.34 --> 400.70]  a more sort of studied and systematic area coalescing into like the first academic art
[400.70 --> 403.66]  history departments came about in the late 19th century.
[404.32 --> 411.90]  And back then, all academic sort of subject matter, the humanities included, kind of aspired to the
[411.90 --> 415.08]  scientific model in the same way that, you know, the natural scientists.
[415.20 --> 418.20]  So empiricism, taxonomy, these kind of things.
[418.26 --> 424.54]  So people at that point in time treated art objects kind of like specimens, like, you know,
[424.56 --> 428.28]  if they were studying plants and the kind of evolution of plants.
[428.42 --> 432.30]  And so early art historians studied art in much that same way.
[432.38 --> 436.36]  They sort of trace the evolution of art through time and through history.
[436.36 --> 442.60]  And so it was really focused on, you know, how the kind of superficial qualities of art
[442.60 --> 449.06]  change over time, rather than a kind of focus on other contextual things like, you know, the
[449.06 --> 454.76]  artist's biography or other kind of circumstantial things about the historical time period.
[454.90 --> 459.46]  But this has been a longstanding debate in the field pretty much since the beginning.
[459.64 --> 462.68]  So it goes both ways and often falls into two camps.
[462.68 --> 467.68]  The so-called formalists, who are the ones who just care about the kind of external appearance
[467.68 --> 469.42]  of images or works of art.
[469.76 --> 474.72]  And then the people who care about the other stuff, the, you know, what the artist was thinking,
[474.82 --> 478.86]  what their intentions were, what their kind of historical context was and all that sort
[478.86 --> 479.12]  of thing.
[479.20 --> 483.24]  So I'm kind of reaching back into that history of art history.
[483.84 --> 488.88]  One thing that kind of interested me in this area was I saw computer vision research, you
[488.88 --> 492.42]  know, so research that had no contact with the art history world, really.
[492.68 --> 498.50]  Using data sets of artworks to answer computer science questions.
[498.76 --> 503.78]  So, you know, not answering art historical questions per se, but in the process, because
[503.78 --> 508.32]  they're using artworks, they're touching on things that are important to art historians
[508.32 --> 510.56]  or that art historians might be interested in.
[510.84 --> 516.26]  But I saw that there was this kind of call back to these formalist methodologies similar to
[516.26 --> 519.98]  what was happening in the late 19th and early 20th century.
[519.98 --> 526.10]  So I was interested in this kind of what I saw as like a revival of these taxonomies kind
[526.10 --> 532.44]  of matching to like really simple way or even sort of, you know, the kind of object recognition
[532.44 --> 534.98]  by finding different motifs or things like that.
[535.12 --> 540.96]  So, yeah, that was my, as having had training in art history and its methodologies, that was
[540.96 --> 545.52]  what kind of piqued my interest in what was happening in computer vision because I saw it
[545.52 --> 551.18]  as kind of like rogue art history that was happening, like without art historians having
[551.18 --> 553.32]  any knowledge that it was happening.
[553.50 --> 558.32]  So I kind of wanted to like call attention to it on one hand for art historians, but
[558.32 --> 564.18]  on the other hand, call attention to some of the art historical issues that, you know,
[564.28 --> 568.84]  computer vision researchers may not have found or had access to.
[568.84 --> 573.72]  So I had that kind of that both directional interest for me.
[574.22 --> 579.28]  I think Daniel and I probably really liked the rogue art historian designation.
[579.64 --> 584.30]  Who knew that machine learning practitioners would be kind of the pirates of the art history
[584.30 --> 585.28]  world in that sense?
[585.48 --> 585.66]  Yeah.
[585.90 --> 586.12]  Yeah.
[586.56 --> 590.16]  I've seen a lot of good parallels or memes recently.
[590.26 --> 594.32]  I think one of my recent ones was like AI is like computer LSD.
[594.32 --> 599.28]  I think probably like rogue art historian is another good one.
[599.90 --> 606.12]  So you mentioned that like machine learning people were integrating artworks like into their
[606.12 --> 609.60]  data sets or to like answer certain types of questions.
[609.60 --> 615.60]  Were those related to like, I can imagine like, oh, if I have these different artworks in my
[615.60 --> 622.38]  data set, maybe I can do image classification and classify like this is an artwork or maybe even
[622.38 --> 629.46]  more detail, like this is an artwork by a person or like in this time period or in this medium or
[629.46 --> 629.90]  something.
[630.26 --> 634.64]  But I could also imagine like artwork has objects in it, right?
[634.72 --> 640.04]  Like, can I recognize objects within an artwork or certain like features, that sort of thing?
[640.10 --> 643.94]  Is that the sort of questions that were being asked or, or what were these questions that you
[643.94 --> 647.62]  kind of started running across that you connected with the art history world?
[647.62 --> 648.22]  Yeah.
[648.38 --> 653.28]  So you hit on sort of two of the main areas that were being addressed.
[653.40 --> 658.14]  And I think from my reading of the literature, as I understand it, the computer vision literature,
[658.72 --> 663.98]  there was a kind of, you know, obviously object recognition in images has been a huge focus
[663.98 --> 673.00]  from the kind of the last 20 years plus, because it has so many, you know, quotidian and nefarious
[673.00 --> 678.90]  applications, you know, you get lots of surveillance applications, but lots of like, you know, we
[678.90 --> 684.44]  open our phones with our face kind of applications and the ability of, you know, a machine learning
[684.44 --> 689.18]  system to like recognize an object has obvious practical applications.
[689.18 --> 695.82]  And so I came across a lot of papers that said something along the lines of, well, recognizing
[695.82 --> 698.58]  objects in a photograph is a solved problem.
[698.58 --> 705.62]  So I think at a certain point in the last like 10 to 15 years, I kind of cover like a
[705.62 --> 708.08]  15 year trajectory of this research in my book.
[708.42 --> 711.90]  Researchers kind of were looking for more difficult data sets to tackle.
[712.02 --> 720.08]  And one of those was art data sets because, sorry, to recognize an object in a kind of stylized
[720.08 --> 723.58]  painting would be something that would be slightly more difficult.
[723.58 --> 724.58]  Yeah.
[724.58 --> 729.48]  So, you know, you had these sort of object recognition activities that were happening,
[729.48 --> 734.20]  but from like my perspective in art history, it's not a very useful exercise.
[734.20 --> 740.32]  You know, I don't care really as an art historian, if there are a bunch of dogs, if you can identify
[740.32 --> 745.70]  a dog in a painting, it's not that interesting as like a tool to use for my research.
[745.84 --> 751.42]  So simultaneously, there was a lot of research happening, which is, you know, the kind of
[751.42 --> 752.70]  categorization by style.
[753.50 --> 759.14]  And this was really interesting to me because this term style in art history is a really
[759.14 --> 760.00]  fraught term.
[760.16 --> 764.60]  It's a really, it has a complicated history and art historians have fought a lot about,
[764.72 --> 767.82]  you know, what does style mean and how do we define it?
[767.82 --> 774.26]  And the, yeah, categorization by style in this terms that you're looking at a kind of superficial
[774.26 --> 778.72]  quality and you're categorizing it by a known kind of textual label.
[778.72 --> 785.50]  I think it's interesting because, you know, this has now really important kind of knock
[785.50 --> 786.84]  on effects in generative AI.
[787.02 --> 793.56]  Like if you open Dali and you see their like kind of suggestion for the initial prompt, they
[793.56 --> 798.72]  suggest you write, they say an impressionist oil painting of sunflowers and a purple vase.
[799.20 --> 805.64]  So right there in the generative AI platforms, you always have these quote unquote style markers.
[805.64 --> 812.50]  So I really wanted to sort of, I guess, unpack what style means for art history and what
[812.50 --> 817.80]  it might mean when we're suddenly applying things like impressionist in the context of
[817.80 --> 819.02]  generative AI.
[819.02 --> 833.72]  Amanda, I love how you brought us along to understand both like this intersection of art history and
[833.72 --> 840.16]  machine learning and how like machine learning was sort of dipping into these formalism elements
[840.16 --> 840.88]  over time.
[841.06 --> 845.40]  You talked about like the prompts in Dali or something like that, like the style.
[845.40 --> 853.66]  When you're talking about now, like art historians kind of realizing how they can employ machine
[853.66 --> 855.26]  learning within art history.
[855.50 --> 858.56]  Is that the sort of thing that they're thinking about?
[858.64 --> 864.72]  Like, like I could imagine if I take a bunch of artwork, you know, clustering image embeddings
[864.72 --> 871.00]  to like look at the style of like what is actually similar between all of these images and that sort of
[871.00 --> 871.28]  thing.
[871.82 --> 875.00]  That was kind of where my mind went when you were talking about style.
[875.16 --> 881.80]  But how have like practically art historians kind of been employing this once they realized
[881.80 --> 887.84]  that machine learning people were kind of like extracting some of these interesting features?
[888.60 --> 888.68]  Yeah.
[888.82 --> 895.12]  So exactly in the way that you just described, there is one of the sort of founding fathers of
[895.12 --> 900.04]  art history, Heinrich Wolfflin, who he pioneered the, you know, so art historians have always
[900.04 --> 906.82]  been kind of, you know, using tech for, you know, various, you know, teaching and or research
[906.82 --> 907.20]  purposes.
[907.20 --> 914.28]  And he pioneered in the early 20th century, the idea of having a double slide projector in
[914.28 --> 917.86]  an art history lecture so that you could compare to artwork.
[918.02 --> 921.82]  It doesn't sound like much to us now, but it was the idea that you could compare side by
[921.82 --> 925.94]  side in a lecture setting to artworks at once.
[926.12 --> 931.52]  And so you would kind of see, but, you know, the human eye is only able to sort of kind of
[931.52 --> 934.08]  take in so many comparisons at once.
[934.20 --> 940.72]  And so the way that these type of technologies have been used in art history context is exactly
[940.72 --> 947.74]  in this kind of mass comparison sense, you know, comparing many, many artworks, many, many
[947.74 --> 952.92]  more than could be possibly compared in a kind of one single view.
[953.30 --> 957.04]  So in kind of literary studies, they have something called distant reading.
[957.24 --> 961.56]  And there's a kind of corollary in art historical studies called distant viewing.
[961.56 --> 968.36]  And the idea is you get a kind of top down, very far away view of general patterns or general
[968.36 --> 968.88]  trends.
[969.04 --> 973.66]  And the hope was that you can kind of notice new things through looking from this distant
[973.66 --> 974.38]  point of view.
[974.38 --> 979.50]  But one of, you know, one of the things that, you know, is important in that is, again, you're
[979.50 --> 982.46]  looking primarily at visual characteristics.
[983.50 --> 985.06]  Can I ask a non-technical question?
[985.22 --> 990.76]  Just when you're doing that remote viewing and you're making those comparisons, like just
[990.76 --> 996.34]  to give me a sense of the field, like what might be an example, like a typical example thing
[996.34 --> 1001.84]  that you're trying to compare aside from whether it's machine learning or entirely, you know,
[1001.84 --> 1006.68]  without technology in the process, just to give me a sense of a touchstone on what that
[1006.68 --> 1007.02]  is.
[1007.16 --> 1010.14]  In terms of what the point of comparison is or?
[1010.68 --> 1010.96]  Yeah.
[1011.10 --> 1011.30]  Yeah.
[1011.32 --> 1015.96]  I'm just kind of curious, just as a newbie to art history and learning from you as we
[1015.96 --> 1020.98]  go, I was just wondering what a momentary, aside from the machine learning side of it,
[1021.06 --> 1023.64]  what would, what are some of the things you're trying to get to with it?
[1023.64 --> 1024.16]  Yeah.
[1024.30 --> 1030.96]  So this is like the classic art history 101, something we call formal analysis or visual
[1030.96 --> 1036.78]  analysis, where the basic step of art history is, you know, first looking without jumping
[1036.78 --> 1043.96]  to context or content of an image or work to look at things like texture, line, shape,
[1044.50 --> 1048.76]  color, those sorts of basic building blocks of visual information.
[1048.76 --> 1053.28]  And once you've kind of understood that, you start to notice details.
[1053.28 --> 1058.32]  And I think it's a way of like looking very closely at an image or an artwork to sort of
[1058.32 --> 1062.22]  understand what that is doing visually, what the composition is doing.
[1062.58 --> 1065.64]  And then the next tool to add on to that is comparison.
[1065.88 --> 1071.70]  So once you understand kind of what's happening on a visual level, purely visual level, you start
[1071.70 --> 1076.64]  comparing it and then you see, okay, so there's different things going on in this other artwork,
[1076.64 --> 1079.52]  maybe from the same time period or maybe from just after it.
[1079.62 --> 1084.78]  And so you kind of start to build an idea or narrative around, you know, how artworks
[1084.78 --> 1085.74]  change over time.
[1086.12 --> 1092.04]  So that's the kind of standard art history, like 101 skill that, you know, we start to
[1092.04 --> 1092.36]  cultivate.
[1092.68 --> 1095.22]  I'm sorry that I took you there, but I appreciate you doing it.
[1095.30 --> 1096.52]  It is helpful for me.
[1096.68 --> 1097.42]  Yeah, no, of course.
[1097.98 --> 1102.44]  No, I think it's, I mean, it's important because it ties back into thinking about what we
[1102.44 --> 1109.06]  want to do if we want to use, you know, machine learning methods to perform those same tasks.
[1109.36 --> 1117.10]  We have to realize or recognize that machine vision doesn't understand images in the same
[1117.10 --> 1123.30]  way that we do as much as we might, you know, remove how we interpret content or context.
[1123.50 --> 1129.24]  The way we kind of dissect an image visually or the way we kind of analyze the visual properties
[1129.24 --> 1132.22]  is going to be very different in machine learning exercise.
[1132.38 --> 1136.50]  And the first way that that's different is that, you know, the vast majority of things
[1136.50 --> 1139.76]  we're dealing with are physical objects that have been digitized.
[1140.32 --> 1142.58]  So there's like a kind of layer of representation.
[1142.92 --> 1144.14]  They're photographs already.
[1144.32 --> 1149.22]  So there's already a difference between, say, looking at an artwork in person in a museum
[1149.22 --> 1151.42]  and looking at the kind of digital reproduction.
[1151.92 --> 1155.94]  I think it is important to sort of understand that foundation as well.
[1155.94 --> 1161.68]  So while you're talking about that and kind of the understanding, it's kind of like, I mean,
[1161.72 --> 1168.04]  my best parallel would be from the NLP world where like chat GPT or something does not understand
[1168.04 --> 1169.30]  user intent, right?
[1169.30 --> 1170.92]  There's no understanding, right?
[1170.98 --> 1178.04]  It can produce text, but we process language different than chat GPT does like as humans.
[1178.04 --> 1184.10]  And like you're saying, someone standing in a museum like processes that experience of standing
[1184.10 --> 1190.68]  in front of an artwork differently than a photograph, an intermediate representation differently than
[1190.68 --> 1196.38]  like a machine might like find features that are good for image classification or something
[1196.38 --> 1196.92]  like that.
[1196.92 --> 1204.88]  I'm wondering, because a lot of these computer vision models are so non-explainable or like
[1204.88 --> 1207.56]  there's an interpretability problem already, right?
[1207.56 --> 1217.32]  In terms of like, I might not know why an image was classified in this class with like a
[1217.32 --> 1219.56]  convolutional neural net or something like that.
[1219.64 --> 1225.04]  Is that a struggle for like taking this field forward in terms of applying machine learning
[1225.04 --> 1225.92]  in these contexts?
[1226.10 --> 1231.12]  Or are there ways to kind of extract some of those main features like you're talking about,
[1231.20 --> 1234.90]  like shape and color and line and other things like that?
[1234.90 --> 1240.90]  Yeah, I think that there's a lot of similar issues actually between the kind of text world
[1240.90 --> 1245.68]  and the image world in terms of this idea of what constitutes meaning or understanding.
[1246.00 --> 1249.06]  Are you guys familiar with the tank classifier problem?
[1249.68 --> 1250.94]  The tank classifier?
[1251.08 --> 1251.68]  I'm not, I'm sorry.
[1251.70 --> 1252.68]  I don't think I am.
[1252.86 --> 1257.34]  Although Chris knows about military vehicles, but I don't know about tanks.
[1257.56 --> 1259.28]  I don't think that's what we're talking about.
[1259.28 --> 1268.72]  It was a kind of apocryphal story that was passed around a lot in sort of machine learning circles.
[1268.96 --> 1275.30]  The story was, and actually the, it dates back to a kind of someone made this up as an example
[1275.30 --> 1277.58]  at some conference, I think in like the 60s.
[1277.96 --> 1281.06]  But it became kind of passed around as like it actually happened.
[1281.06 --> 1289.46]  The story is that the U.S. military during the Cold War wanted to recognize in images the, yeah, the tanks.
[1289.84 --> 1290.18]  I do.
[1290.40 --> 1293.04]  Now that, now that you go into it that way, I do remember this.
[1293.10 --> 1293.32]  Yes.
[1293.54 --> 1293.74]  Yeah.
[1293.82 --> 1298.40]  So like differentiate Soviet versus American tanks in images,
[1298.40 --> 1305.98]  but then ended up accidentally classifying the images by the background weather or environmental conditions.
[1305.98 --> 1313.14]  And that is the kind of thing that I think like really illustrates what we deal with when we're dealing with images,
[1313.14 --> 1321.62]  because we understand things like background and foreground or the kind of subject and surround in a different way.
[1321.90 --> 1328.00]  We interpret those, the kind of illusionistic space of an image in a certain way that, you know,
[1328.06 --> 1335.14]  for a lot of kind of algorithmic classification, that surface is what we might call a kind of democratic surface.
[1335.14 --> 1338.96]  Like all areas initially are kind of treated the same.
[1339.26 --> 1342.68]  It has to be some kind of training to differentiate those.
[1342.78 --> 1345.62]  And of course, it's gotten very sophisticated where it is,
[1345.96 --> 1349.04]  we are able to sort of separate those things out a lot of the time.
[1349.10 --> 1353.14]  But of course, you still get lots of cases like in sort of medical imaging.
[1354.06 --> 1357.14]  Like I read a few things about, you know, during COVID,
[1357.90 --> 1364.68]  they tried to classify, for instance, like COVID infected lungs versus healthy lungs.
[1364.68 --> 1369.30]  But they used a training set of like children's lung imagery.
[1369.50 --> 1375.40]  And so they accidentally classified by children versus adults, which seems like a very silly error to make.
[1375.68 --> 1378.98]  But so we get like issues like that, I think are really important,
[1378.98 --> 1385.30]  because what it points to is that essentially, we're dealing with like a two-dimensional surface to interpret.
[1385.30 --> 1390.98]  But often those are two-dimensional representations of a three-dimensional space that we,
[1391.36 --> 1397.14]  as kind of three-dimensional beings, intuitively understand when viewing an image like that,
[1397.20 --> 1398.48]  or a photograph, for instance.
[1399.10 --> 1405.04]  Whereas, you know, machine learning algorithms only know that we've kind of isolated a certain pattern of pixels
[1405.04 --> 1407.48]  to be a specific object.
[1407.82 --> 1409.90]  And, you know, given lots of examples,
[1410.26 --> 1414.32]  they're quite good at differentiating whatever object we've designated.
[1414.52 --> 1417.84]  But still, there's no kind of understanding of space.
[1417.98 --> 1421.20]  It's not part of the understanding of images in that framework.
[1421.20 --> 1425.76]  So I think that that's kind of one of these interesting examples of like,
[1426.02 --> 1429.00]  just because it successfully identifies something,
[1429.06 --> 1431.66]  doesn't mean it understands what that thing is,
[1431.66 --> 1433.56]  like a dog in a photograph.
[1434.36 --> 1435.22]  Very good explanation.
[1435.72 --> 1438.58]  But I do feel, on behalf of the defense industry,
[1438.58 --> 1443.52]  I should note that we are much better at identifying and classifying tanks today than we used to be.
[1443.78 --> 1447.10]  I don't know if I want to know how good you are.
[1448.90 --> 1452.50]  That might be something that I want to be ignorant of.
[1452.50 --> 1454.84]  I just feel the need to say that, yeah.
[1457.24 --> 1461.58]  I have confidence that things have moved on significantly since the 60s.
[1461.66 --> 1463.50]  Someone should tell Vladimir Putin.
[1463.64 --> 1464.22]  That's all I'm saying.
[1464.34 --> 1465.84]  That's all the politics I'm inserting.
[1466.04 --> 1473.40]  I am really interested in all sorts of things about what we just discussed in terms of the
[1473.40 --> 1475.90]  understanding elements and other things.
[1476.10 --> 1478.18]  But I'm intrigued by this.
[1478.64 --> 1482.26]  In reading through some of the materials about your book and your work,
[1482.40 --> 1491.46]  you talk about how computer scientists often process these sort of like art image data sets
[1491.46 --> 1498.96]  or images that are part of their data sets without any real sort of understanding of art or art history.
[1499.90 --> 1505.16]  And you kind of, one of the things you talk about in the book is how maybe there's an enrichment
[1505.16 --> 1512.36]  of like the data science and computer vision side by understanding more of the sort of humanistic issues
[1512.36 --> 1515.58]  and elements of the artwork and those sorts of things.
[1515.58 --> 1519.48]  Could you describe a little bit what you mean by that and how you think like,
[1519.90 --> 1526.24]  because we mostly talked about machine learning kind of enriching maybe art history or things that could be done there.
[1526.34 --> 1531.20]  What about the other side of that in terms of like things computer scientists could learn
[1531.20 --> 1536.00]  based on this kind of background and research on the digital humanities side?
[1536.00 --> 1542.68]  Yeah, I mean, I think one of the things that is really important to me is this idea that, you know,
[1542.78 --> 1551.22]  the assumption that accepted categories are in some way static or objective and unchanging
[1551.22 --> 1553.94]  can lead to really misleading findings.
[1554.08 --> 1560.06]  So, for example, there was one study that I looked at where they were classifying
[1560.06 --> 1570.26]  paintings by artistic style and they noted, the authors noted that action painting was confused
[1570.26 --> 1575.96]  with abstract expressionism and, you know, said, oh, well, in future, you know,
[1576.02 --> 1580.40]  we will be able to hopefully rectify this categorization error.
[1580.40 --> 1586.94]  But for an art historian, you know, those are two kind of contextually specific style terms
[1586.94 --> 1594.86]  that two competing art critics came up with or groups of critics to, and they have a kind of ideological background.
[1595.10 --> 1601.46]  So there's a reason that some critics wanted to call this mid-century American art movement
[1601.46 --> 1604.88]  abstract expressionism and some wanted to call it action painting.
[1605.18 --> 1608.28]  And neither term is really subservient to one another.
[1608.64 --> 1613.34]  And you don't need to necessarily understand the full kind of art historical picture to like,
[1613.34 --> 1617.50]  you know, say if you're using Dali and you want to make either an abstract expressionist
[1617.50 --> 1622.34]  or an action painting as a style, you probably get good results with both of those terms.
[1622.84 --> 1627.72]  But the kind of issue is that, you know, these are not stable categories.
[1627.94 --> 1632.32]  There's different style categories have very different kind of origins.
[1632.58 --> 1634.36]  They're inconsistent amongst each other.
[1634.60 --> 1638.38]  You know, some of them span a few centuries, some a decade.
[1638.72 --> 1642.18]  Some are small groups of artists who all knew each other and worked together.
[1642.18 --> 1645.54]  Some are kind of catch-all terms or contextual terms.
[1645.68 --> 1650.26]  So I think people, you know, in computer science, they're like, great, I have a new data set to work with.
[1650.30 --> 1651.62]  And here's the categories.
[1651.82 --> 1655.84]  And I'm going to work with this and then see how effective it is, you know, categories.
[1656.02 --> 1661.66]  And that like, that's fine, because they're working on a problem that's different than necessarily what an art historian might work on.
[1661.78 --> 1666.86]  But the reason I kind of insert myself there is I'm like, hey, well, that is actually kind of an art historical problem
[1666.86 --> 1672.74]  that you're working on, but in a kind of way that doesn't understand that these terms are not fact,
[1672.92 --> 1678.14]  that they're not stable in the way that you can kind of like, once you insert something into a database,
[1678.14 --> 1681.22]  it becomes kind of solid in a way that it doesn't.
[1681.28 --> 1685.46]  When you're discussing it like I am, like I could talk for another 20 minutes about, you know,
[1685.46 --> 1691.46]  who came up with these terms and why and, you know, what their political beliefs might be and that sort of thing.
[1692.08 --> 1696.44]  Could you talk, maybe not for 20 minutes, but for some period of time, I'm kind of curious,
[1696.56 --> 1702.96]  because you've kind of posed this problem, you know, that's kind of brought by the data science is the way I'm seeing it.
[1702.98 --> 1706.02]  Whereas you're saying, you know, you may not have those categories, Craig.
[1706.02 --> 1715.64]  What are you proposing as a way of mitigating that in a way that is consistent with art history in terms of approach?
[1716.12 --> 1719.06]  Like how would you, you know, that has that kind of qualitative aspect?
[1719.82 --> 1725.24]  Yeah, I mean, I think like something I was talking about with a colleague who comes from a kind of computer science background
[1725.24 --> 1732.86]  is how do we bring together some of the, you know, concerns and interests of computer science with art history
[1732.86 --> 1735.56]  in a way that is kind of interesting to both sides.
[1736.00 --> 1743.66]  One of those things is, you know, for art historians, the context and the nuance of terms in a kind of qualitative way is important.
[1743.84 --> 1747.30]  But then how do you integrate that into a kind of data context is the question.
[1748.10 --> 1752.24]  And unfortunately, I don't have a really good answer, but I know, you know,
[1752.24 --> 1761.24]  there are researchers who are beginning to sort of combine different, well, text and image or different modalities of information together
[1761.24 --> 1766.94]  to try to create a sort of, you know, or networks, bigger picture about, you know,
[1766.98 --> 1771.50]  how we might understand artworks beyond just a kind of textual category.
[1772.24 --> 1776.02]  So, of course, we can do a kind of like dispense with categories altogether
[1776.02 --> 1781.68]  and do a kind of purely visual kind of like unsupervised, like clustering type thing.
[1782.06 --> 1785.22]  But then what do we call those clusters or what do we call those collections?
[1785.54 --> 1789.02]  And that brings you right back to art history once again.
[1789.02 --> 1798.46]  So it's this kind of how to integrate all this sort of qualitative nuance within a data context is the big problem as I see it.
[1798.52 --> 1802.56]  And I think that's something that I still haven't found or heard a really good solution,
[1802.70 --> 1805.42]  but I've been talking about it with some of my colleagues.
[1805.64 --> 1809.42]  So maybe we'll come up with some bright idea in that area.
[1810.32 --> 1815.38]  Could that change depending on what question you're answering with a given, you know, training session?
[1815.38 --> 1819.20]  Like you could do, you could take different reinforcement learning approaches,
[1819.52 --> 1823.08]  but I would imagine that that might change the output.
[1823.20 --> 1829.96]  And so you'd be looking for an approach that's kind of consistent with what you're trying to achieve from the art history side of things.
[1830.18 --> 1837.56]  Is there any thinking around different approaches based on as you change those that you get different types of outputs?
[1837.56 --> 1844.80]  You know, there's something that you're going for that maybe a data science practitioner without the art history might be going for something different,
[1844.88 --> 1846.28]  kind of as you've already talked about.
[1846.94 --> 1852.68]  What's the thinking around different approaches to it with generative or reinforcement or a combination of them?
[1853.28 --> 1865.00]  I mean, I don't think that, you know, we can expect that me and a computer vision researcher will have the same goals or desires or outputs out of a research question or problem.
[1865.00 --> 1870.84]  But I think from my end, I would like to add some nuance to this kind of the cold data.
[1871.20 --> 1876.04]  Because, of course, even computer vision researchers, they have a kind of quantitative result,
[1876.14 --> 1878.74]  but they end up making an interpretation like the one I just said.
[1878.80 --> 1884.40]  They said, oh, well, we've had this confusion between these two categories and we'd like to fix that.
[1884.40 --> 1895.46]  So there's always a kind of, you know, as much as, you know, data scientists or computer scientists might think they're just concerned with sort of numbers or output or objective facts,
[1895.50 --> 1898.48]  there's always actually a kind of interpretive thing that happens.
[1898.74 --> 1903.26]  So from my point of view, I think, you know, we might not be answering the same research questions,
[1903.26 --> 1911.32]  but we could come together in that kind of in the same space somehow to build a bigger, better picture of what we're like,
[1911.40 --> 1917.12]  whatever phenomenon or artworks or a collection of images that we might be looking at.
[1917.78 --> 1925.20]  I think that's a really good general vision to have, I think, in multiple ways and probably for multiple problems outside of this one.
[1925.20 --> 1945.98]  So one of the things that is mentioned in the book and that you discuss are a couple of these like paradoxes that I find really interesting in the fact that like deep learning as applied to like these features of artwork can be used to both like create and detect forgeries.
[1946.28 --> 1948.22]  So like both of those things are true.
[1948.22 --> 1963.52]  And there's like this side of things where like like high artworks can become digital assets and like digitally generated assets are in certain cases being considered sort of more like the high art side of things.
[1963.52 --> 1973.62]  Like how are you wrestling with these paradoxes coming up that like machine learning and deep learning are operating on both sides of these things?
[1973.62 --> 1986.12]  I mean, I obviously think it's really fascinating, this kind of arms race or, you know, there's a famous quote by Borillio that the invention of the ship is also the invention of the shipwreck.
[1986.50 --> 1988.04]  You can't have one without the other.
[1988.14 --> 1998.18]  So I think it's interesting that there's always the sort of positive forward and the sort of destructive negative element as going on simultaneously.
[1998.18 --> 2011.16]  But I think in terms of like, you know, we really saw generative AI explode, you know, in the last, you know, especially with the image tools in the last year and in some months.
[2011.28 --> 2026.38]  I think, you know, the latest kind of the Pope jacket hoax of the last week really illustrates the extent to which, you know, I mean, we've been kind of distrustful of the authenticity of photographs.
[2026.38 --> 2031.42]  You know, I mean, since photography was invented, people were aware that it could be manipulated.
[2031.66 --> 2036.36]  In the 19th century, you know, we had hand techniques to manipulate photographs.
[2036.50 --> 2037.46]  There's always kind of editing.
[2037.72 --> 2039.90]  There was always different kinds of manipulation.
[2040.34 --> 2043.18]  But of course, it's only just gotten kind of easier.
[2043.52 --> 2056.04]  And, you know, Photoshop, there were a lot of the sort of fears that are currently being talked about in terms of authenticity or believability or fakeness or trust in images were raised in the 90s around Photoshop.
[2056.04 --> 2059.08]  And we kind of, you know, became accustomed to Photoshop.
[2059.34 --> 2072.22]  But I think, you know, this question of authenticity, you know, whether that's in detecting art forgeries or if it's in simply, you know, how we trust the images that we see is kind of rearing up again because we have this access.
[2072.38 --> 2080.08]  Now everyone has access to quite sophisticated tools to create photorealistic images that aren't photographs at all.
[2080.08 --> 2094.82]  And this is something that I've been working around subsequent to after I wrote the book is the, you know, idea of are the images that are created by some of these generative AI platforms that look indistinguishable from photographs?
[2095.02 --> 2097.32]  Can we consider them photographs, actually?
[2097.32 --> 2103.82]  So it's a kind of new tool to make photographs that doesn't have a camera, that doesn't have a lens, doesn't have a photographer.
[2104.02 --> 2108.88]  It's a kind of composite of the learnings of vast data sets.
[2108.88 --> 2114.58]  So that's like all of those questions that I address in the book about like art authentication.
[2114.58 --> 2135.04]  And then on the flip side, you know, the idea you could create a forged or fake artwork from a generative tool are, I think, even more kind of relevant in the last year or few months because of these sort of the new paradigm of creating manipulated images or manipulated photographs.
[2135.04 --> 2165.02]  Yeah, yeah.
[2165.04 --> 2169.26]  It showed the Pope running with police trying to capture him on the street.
[2169.26 --> 2189.78]  But, you know, I've been on these kind of, I guess, doing a kind of auto-ethnographic embedded study of these, lots of these communities on like Reddit and Facebook and other social media that are just like kind of amateurs, you know, doing mid-journey or dolly images or like night cafe or these kind of things.
[2189.78 --> 2196.20]  And I've been on them for, you know, over a year, just like reading posts and reading posts and looking at images.
[2196.20 --> 2213.30]  And even I, you know, after I, you know, spending so much time on these kind of venues and looking at lots of AI generated images, my husband just showed me briefly on his phone on Twitter, like, oh, look, do you see the Pope was wearing this big puffy coat?
[2213.38 --> 2214.56]  I was like, oh, that's weird.
[2214.86 --> 2215.94]  I didn't question it.
[2216.20 --> 2216.28]  Yeah.
[2216.48 --> 2217.68]  And you've been embedded.
[2217.68 --> 2221.06]  Yeah, I mean, I'm someone who's like actively working on this.
[2221.10 --> 2228.42]  So how, you know, how can we expect people to be sort of distrustful when, you know, we want to believe what we see?
[2228.42 --> 2256.68]  And I think also in the kind of last, I mean, not to get too political or anything, but in the last kind of decade, the idea of the photograph as a document of, you know, truth telling medium in terms of things like police brutality or like documenting abuse and other situations as a kind of way to expose those things and trust, you know, incidents where the police may not have told the truth about what happened in a particular situation.
[2256.68 --> 2259.80]  We put a lot of stake in those things.
[2259.98 --> 2263.60]  And so, yeah, then the question becomes, you know, what are we facing now?
[2264.04 --> 2266.96]  Yeah, we have a new way to have manipulated images.
[2267.56 --> 2275.04]  As you were describing that, and I can't, and given the industry I'm in, I can't help but obviously put the filter of my own, my own employment.
[2275.04 --> 2284.56]  But it made me realize that there are common problems that an art historian and that people in the intelligence community, for instance, are struggling to deal with at the same time.
[2284.56 --> 2291.16]  Who knew that there could be career paths crossing between the two with that kind of maybe ominous point?
[2291.16 --> 2312.18]  Where do you think this field is going as you look at doing these different types of qualitative analysis where not everyone is necessarily trying to get the same thing out of combining these fields and recognizing that there are a set of common challenges that, you know, our history has that other fields may have.
[2312.18 --> 2317.88]  Where do you see, from your perspective, from your filter, where do you see this going?
[2318.08 --> 2320.56]  Where do you see your field evolving into?
[2321.12 --> 2324.14]  What kinds of questions do you expect to be asked?
[2324.44 --> 2333.66]  And what new technologies in the AI world do you either expect or maybe hope to see to help you find those answers in the years ahead?
[2333.66 --> 2345.88]  Yeah, I mean, I think like art history in particular is fairly technophobic in terms of like maybe wouldn't be the earliest adopters of, you know, AI techniques per se.
[2346.10 --> 2355.14]  But, you know, I already think maybe I don't have such a like sci-fi dystopian outlook, but rather a kind of very almost boring outlook on.
[2355.14 --> 2368.18]  I think a lot of these tools will just simply be integrated into a research practice the way that chat GPT will be used as a kind of aid or different GPT type things, aid to writing.
[2368.40 --> 2375.50]  Rather, you know, there's a lot of fear right now in academic settings about, you know, quote unquote cheating in terms of those text generators.
[2375.50 --> 2389.12]  But I think similarly in terms of image analysis or image recognition, either stylistic recognition or object recognition will be a really useful tool in terms of sorting through large art data sets.
[2389.32 --> 2400.64]  You know, there's certain kinds of, you know, say for instance, I had a friend who she was studying art in Israel around and before the founding of the Israeli state.
[2400.64 --> 2405.84]  And they had a lot of art exhibitions, but they didn't keep very good records of what the artworks were that they were exhibiting.
[2405.92 --> 2413.46]  So she just had a bunch of photographs of artworks on a wall and had to like set herself to the task of like determining what these artworks were.
[2413.50 --> 2415.78]  And they weren't necessarily, you know, very well-known artworks.
[2416.24 --> 2429.40]  It sounds kind of like a boring application, but, you know, might be a very useful tool in terms of like, OK, if we had the ability to sort of put this image in and try to identify the artists of unknown artworks through these kind of mechanisms.
[2429.40 --> 2432.86]  For my disciplinary perspective, that would be very useful.
[2433.06 --> 2434.92]  I mean, already they're being used.
[2434.92 --> 2451.42]  These kind of computer vision or machine learning techniques are being used to sort large art data sets rather than accessing artworks through textual metadata, accessing them through what can be interpreted visually in particular images.
[2451.42 --> 2460.58]  Or isolating images, extracting images, matching images across different publications or different exhibition venues.
[2460.58 --> 2463.68]  So I have a very kind of boring outlook, I guess.
[2464.22 --> 2473.94]  You know, I don't think it'll lead us to like some kind of scary dystopian feature, but it'll just become a kind of naturalized tool, resource that we can use.
[2473.94 --> 2493.78]  But obviously, you know, with the kind of caveat that we always have to think about ethical issues and also think about what categories mean and how we're kind of organizing and arranging things, not just kind of giving over to the task of organizing to some unknown kind of black box.
[2493.78 --> 2523.76]  I don't think that's boring.
[2523.76 --> 2524.76]  I think that's a lot.
[2524.76 --> 2525.76]  I think that's a lot.
[2525.76 --> 2526.76]  I think that's a lot of work.
[2526.76 --> 2527.76]  I think that's a lot of work.
[2527.76 --> 2528.76]  I think that's a lot of work.
[2528.76 --> 2529.76]  I think that's a lot of work.
[2529.76 --> 2530.76]  I think that's a lot of work.
[2530.76 --> 2536.76]  And I'm happy to have you back on any time to help us parse through some of these things.
[2536.76 --> 2537.76]  Great.
[2537.76 --> 2538.76]  Yeah.
[2538.76 --> 2539.76]  Thank you guys so much.
[2539.76 --> 2540.76]  It's been really interesting and fun.
[2540.76 --> 2541.76]  Thanks.
[2541.76 --> 2551.76]  Thank you for listening to Practical AI.
[2551.76 --> 2556.76]  Your next step is to subscribe now, if you haven't already.
[2556.76 --> 2562.76]  And if you're a longtime listener of the show, help us reach more people by sharing Practical AI with your friends and colleagues.
[2562.76 --> 2567.76]  Thanks once again to Fastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2567.76 --> 2572.76]  Check out what they're up to at Fastly.com and Fly.io.
[2572.76 --> 2578.76]  And to our Beat Freakin' residents, Breakmaster Cylinder, for continuously cranking out the best beats in the biz.
[2578.76 --> 2579.76]  That's all for now.
[2579.76 --> 2580.76]  We'll talk to you again next time.
