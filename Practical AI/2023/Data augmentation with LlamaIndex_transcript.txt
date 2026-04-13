[0.00 --> 8.64]  Welcome to Practical AI.
[9.20 --> 15.96]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 --> 18.78]  are changing the world, this is the show for you.
[19.20 --> 24.36]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.36 --> 24.66]  listen.
[24.92 --> 26.76]  Check them out at Fastly.com.
[26.76 --> 32.02]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 --> 33.68]  No ops required.
[34.02 --> 36.08]  Learn more at fly.io.
[42.34 --> 45.34]  Welcome to another episode of Practical AI.
[45.70 --> 47.14]  This is Daniel Whitenack.
[47.24 --> 50.74]  I'm a data scientist and founder of a company called Prediction Guard.
[51.00 --> 56.52]  And I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed
[56.52 --> 56.82]  Martin.
[57.00 --> 57.70]  How are you doing, Chris?
[57.90 --> 58.90]  Doing very well.
[58.98 --> 62.34]  Enjoying this fine springtime weather of LLMs.
[62.84 --> 66.14]  You have the spring LLM bloom, I guess.
[66.14 --> 66.48]  That's right.
[66.70 --> 67.20]  That's right.
[67.66 --> 71.02]  Well, I don't even think we can use the word bloom because that's loaded now.
[71.12 --> 73.28]  Yeah, I was going to say that has a whole different meaning.
[73.50 --> 78.08]  There's no word that's not loaded with some sort of AI meaning at this point.
[78.26 --> 78.66]  Yeah.
[79.06 --> 80.62]  We should just go straight to our guest.
[80.62 --> 88.48]  Yeah, including LLMAs, which we're excited today to have with us Jerry Liu, who is co-founder
[88.48 --> 90.62]  and creator of Llama Index.
[90.92 --> 91.46]  Welcome, Jerry.
[91.94 --> 92.18]  Yeah.
[92.26 --> 94.16]  Thanks, Daniel and Chris, for having me.
[94.20 --> 95.10]  Super excited to be here.
[95.42 --> 95.72]  Yeah.
[96.00 --> 102.22]  I'm really excited because we've had a few conversations in the past and I've used Llama
[102.22 --> 107.36]  Index in some of my own work and also kind of tried some integration stuff with various
[107.36 --> 111.64]  data sources, so I'm really excited to hear a little bit more of the story and kind of
[111.64 --> 112.98]  the vision behind the project.
[113.48 --> 120.44]  If I'm just reading from the docs, Llama Index is about connecting LLMs or large language models
[120.44 --> 121.60]  with external data.
[121.60 --> 127.52]  So maybe a first question, kind of a general question, not specific to Llama Index necessarily
[127.52 --> 133.72]  is like, why would one want to connect large language models with external data?
[134.74 --> 135.62]  Yeah, it's a good question.
[135.62 --> 140.94]  And so for those of you who are already in the space of LLM application development, this
[140.94 --> 144.72]  might sound obvious to you, but for those of you who might be still somewhat unfamiliar,
[145.26 --> 149.64]  large language models have a lot of different sorts of capabilities that are really good
[149.64 --> 153.60]  at answering questions, you know, doing tasks, being able to summarize stuff, basically
[153.60 --> 157.52]  anything you throw at it, like generate a short story, write a poem, it can do.
[157.70 --> 162.74]  And the default mode of interacting with a language model like ChatGPT is that you would write
[162.74 --> 167.00]  stuff to it, you know, in a ChatLG interface, this query would hit the model and you'd get
[167.00 --> 167.62]  back some output.
[168.12 --> 171.64]  I think one of the next questions that people will get into, especially as they're trying
[171.64 --> 177.50]  to explore building applications on top of large language models is how can this language
[177.50 --> 180.46]  model understand my own private data, right?
[180.46 --> 184.06]  Whether you're kind of like a single person or you're an entire organization.
[184.06 --> 189.00]  And these days, there's like a lot of different ways for actually trying to incorporate new
[189.00 --> 190.36]  knowledge into a language model.
[190.72 --> 194.08]  The models themselves are trained on just like a giant corpus of data.
[194.46 --> 198.32]  And so if you're like an ML researcher, your default mode is just how can I train this
[198.32 --> 201.52]  model on more data so that I can try to memorize this knowledge, right?
[201.56 --> 205.02]  And the algorithm there is basically through some sort of like gradient descent through the
[205.02 --> 210.52]  weights or RLHF or any sort of like fancy ML algorithm that actually includes the knowledge
[210.52 --> 211.86]  and the weights of the model itself.
[211.86 --> 216.50]  I think one interesting thing about large language models these days is that instead
[216.50 --> 222.06]  of like training the model, you can actually take the model as is and just like figure out
[222.06 --> 224.28]  how to have it reason over new information.
[224.78 --> 229.62]  And so for instance, like use that input prompt as like the cache space to feed in new information,
[229.90 --> 233.10]  tell to reason over that data and to answer questions over that data.
[233.52 --> 238.00]  And I think that's very interesting because you can take the model itself, which, you know,
[238.00 --> 241.66]  has been trained on a variety of data, but doesn't necessarily have inherent knowledge
[241.66 --> 244.80]  about, you know, you as a person or your organization data.
[245.00 --> 248.60]  But then you can tell it, hey, here's some new data that I have.
[248.66 --> 251.68]  Now, given this data, how can I answer the following questions?
[252.02 --> 256.94]  And this is part of the stack that a lot of people are discovering these days where you
[256.94 --> 261.74]  can actually just use the language model itself as a pre-trained service and then wrap that
[261.74 --> 265.86]  in this overall software system to incorporate your data with the language model.
[265.86 --> 266.66]  Cool.
[266.66 --> 266.78]  Cool.
[266.90 --> 267.14]  Yeah.
[267.32 --> 270.38]  And your project is called Llama Index.
[270.56 --> 275.20]  Now, before the past like few months or six months or whatever, when I was thinking
[275.20 --> 279.82]  about like indices or an index, one of the things that first came to my mind was like,
[279.92 --> 281.86]  oh, I have a database maybe.
[282.04 --> 286.84]  And there's an index that I use to query over that database.
[286.84 --> 293.74]  And some of that is a little bit like fuzzy magic to me in terms of how that actually works
[293.74 --> 295.34]  at the lower level in a database.
[295.34 --> 302.34]  But like, what is this idea of an index or indexing in the context of Llama Index or in
[302.34 --> 306.22]  the context of data augmentation for large language models?
[306.70 --> 307.26]  It's kind of funny.
[307.36 --> 312.16]  I think when we first started the name, it was a bit more of like a casual naming convention.
[312.36 --> 313.72]  You know, it used to be called GPT Index.
[313.72 --> 318.44]  And I kind of made up the name because it sounded roughly relevant to what I was building
[318.44 --> 318.94]  at the time.
[319.30 --> 324.12]  But I think over time, especially as it's morphed into more of a project that people
[324.12 --> 327.34]  are actually using, this concept of an index has become a bit more concrete.
[327.52 --> 329.24]  And so I can articulate that a bit better.
[329.64 --> 334.94]  The idea of Llama Index is, you know, just to step back and talk about the overall purpose
[334.94 --> 339.20]  of the project is to make it really easy and powerful and fast and cheap to connect your
[339.20 --> 340.80]  language models with your own private data.
[341.32 --> 343.52]  And we have a few constructs to do so.
[343.52 --> 345.10]  Within Llama Index.
[345.56 --> 350.18]  And so part of the way you can think about Llama Index is how can we build some sort of
[350.18 --> 355.54]  stateful service around your private data around something that at the moment is somewhat
[355.54 --> 358.80]  stateless, like the language model call is a stateless service, right?
[359.12 --> 361.30]  Because you feed in some input and you get back some output.
[361.68 --> 366.34]  So how can we wrap that in a stateful service around your own data sources so that, you know,
[366.40 --> 370.96]  if you want to ask a question or tell the LLM to do something, it can reference that state
[370.96 --> 371.96]  that you have stored.
[372.44 --> 377.06]  And so if you think about any sort of like data system, there is the raw data that's
[377.06 --> 378.70]  stored somewhere in some storage system.
[378.94 --> 384.56]  There might be like indexes or views like similar to like a database analogy where you can kind
[384.56 --> 386.26]  of look at the data in different ways.
[386.38 --> 388.08]  And I can talk a little bit about how that works.
[388.08 --> 391.86]  And then there's usually some sort of like query interface, right, that you can actually
[391.86 --> 393.18]  query and retrieve the data.
[393.72 --> 398.40]  So if you look at like a SQL database, right, you have, you know, the raw data stored and
[398.40 --> 401.90]  some sort of tables, you can define different indexes over different columns.
[402.02 --> 406.24]  And then the query interface is like a SQL interface, you run SQL, and then it'll be able
[406.24 --> 407.80]  to execute the query against your database.
[408.30 --> 413.72]  And there's a lot of like, kind of roughly similar concepts that apply to thinking about the
[413.72 --> 415.64]  llama index itself as this tool set.
[415.94 --> 420.16]  Because if we're going to build this like stateful service, right, on top, that can
[420.16 --> 421.74]  integrate with large language models.
[422.18 --> 427.22]  By the way, to clarify, we're not like really solving the storage part, right, where we
[427.22 --> 430.30]  integrate with like a ton of different vector storage providers, we integrate with like
[430.30 --> 431.28]  other databases too.
[431.74 --> 435.56]  But if you even think about us as like some sort of data interface or orchestration, you
[435.56 --> 437.68]  know, there's a raw data which needs to be stored somewhere.
[438.00 --> 442.72]  And so if you have like a bunch of text documents, you need to store that in like a vector
[442.72 --> 446.50]  database or MagoDB or S3, all those types of things.
[447.02 --> 450.78]  And then you can define these different indexes on top of this data.
[451.36 --> 454.92]  And the way we think about indexes is how do we structure your data in the right way,
[455.06 --> 458.10]  so that you can retrieve it later for use without lens.
[458.50 --> 460.90]  And so then I can talk a little bit how this works.
[461.02 --> 464.06]  But the set of like indexes that you can define is actually pretty interesting.
[464.46 --> 467.80]  Basically, the set of data structures that offers like a view of your data in different
[467.80 --> 468.06]  ways.
[468.06 --> 473.92]  And then you wrap that in this overall query interface that can, you know, use these indexes
[473.92 --> 479.12]  on top of your data to do retrieval and LLM synthesis and give you back a final answer.
[479.56 --> 483.46]  And so I would look at this in terms of like that components of the overall system.
[483.58 --> 487.12]  There's just like if you're building this like stateful service, there is these three
[487.12 --> 487.62]  components.
[488.08 --> 491.90]  How do you, you know, adjust and store the raw data, index it, and then query it?
[491.90 --> 497.00]  So, uh, I want to actually pull you back for just a moment, uh, as we're kind of learning
[497.00 --> 497.38]  this.
[497.62 --> 502.34]  And if you're an app developer and you're interested in creating a stateful service and you've
[502.34 --> 505.94]  started kind of going down the path about like, well, there's kind of the old school
[505.94 --> 508.54]  way of going and doing a SQL query and all that.
[508.60 --> 512.18]  And now we're using LLM models and adding our data to it.
[512.40 --> 516.46]  I know that we've kind of gone beyond that just a little bit, but if you can back up and
[516.46 --> 518.40]  talk a little bit about what are you getting?
[518.40 --> 522.88]  If you're the app developer and you're listening to this and you're trying to understand like,
[523.02 --> 524.96]  why would I go down that path?
[525.04 --> 528.74]  I'm, you know, I sense that there's value there, but we haven't talked about it versus
[528.74 --> 531.68]  a robust set of SQL queries on your own data.
[531.96 --> 534.74]  Why would you bring in that large language model in the beginning?
[535.14 --> 537.90]  What is it bringing to bear that's worth all of that effort?
[538.04 --> 542.08]  Could you talk a little bit about that baseline value add to it?
[542.62 --> 543.64]  Yeah, that's a really good question.
[543.76 --> 545.50]  And I think I might've jumped the gun a little bit.
[545.52 --> 547.04]  So I appreciate you bringing me back.
[547.04 --> 547.82]  No worries.
[548.28 --> 550.14]  It's because you're excited as are we.
[550.34 --> 554.60]  But I also want to make sure that people listening have a chance to truly understand
[554.60 --> 555.90]  it at the same way that you are.
[556.38 --> 556.56]  Definitely.
[557.20 --> 562.56]  I think one thing about language models that's very powerful is their ability to just comprehend
[562.56 --> 565.12]  unstructured text and also natural language.
[565.68 --> 571.02]  And so this matters in both ways in terms of how you can store the data as well as query
[571.02 --> 571.48]  the data.
[571.48 --> 573.86]  Because now, you know, let's say you're the end user.
[574.36 --> 579.32]  You can just type in a NAFTA language like English question, right, ideally into this interface
[579.32 --> 580.82]  and get back a response.
[581.04 --> 586.32]  And so the setup is way easier than having to learn SQL over some source of data or, you
[586.32 --> 591.56]  know, having to even code up like this very complex like pipeline to try to, you know, like
[591.56 --> 593.16]  parse the data in different ways.
[593.16 --> 597.84]  Because you could treat the language model itself as a black box, feed us something,
[598.04 --> 598.92]  get something out, right.
[599.00 --> 602.58]  And so I think that by itself is a very, very powerful tool.
[602.62 --> 605.48]  And I think these days people are trying to figure out what you can do with that tool.
[605.48 --> 611.30]  So another kind of like illustrative example of like the power of language models using
[611.30 --> 615.62]  this as like intelligent natural language interface is you actually don't have to do
[615.62 --> 618.30]  a ton of data parsing when you actually feed in the data.
[618.78 --> 624.92]  So for instance, let's say you have a PDF document or like any sort of like Microsoft
[624.92 --> 629.74]  Word document or even an HTML web page, just copy and paste that entire thing, right.
[629.84 --> 633.76]  You know, just extract the text from it, dump it into the input prompt, and then just
[633.76 --> 638.06]  like tell the LLM, hey, here's just this like giant blob of text I copied over.
[638.52 --> 641.24]  Now, given this text, can you please answer this following question?
[641.80 --> 645.98]  And the crazy thing is the language model can actually do that, assuming, you know, it
[645.98 --> 647.04]  fits within the prompt space.
[647.36 --> 652.52]  And that's also very powerful because this kind of affects the way you do like ETL and
[652.52 --> 653.56]  data pipelining, right.
[653.62 --> 657.18]  In the traditional sense, if you had a bunch of this like unstructured text, you'd have to
[657.18 --> 661.32]  spend either manual effort or write a complicated program to pull out the relevant bits from
[661.32 --> 666.26]  this text, parse it into some table, store it, and then, you know, run SQL or some other
[666.26 --> 667.44]  like query over this text.
[667.88 --> 672.90]  Whereas here, you know, with the power of language models, you can store this text in a bit more
[672.90 --> 678.20]  of like a messy unstructured format as like raw natural language, and then still figure
[678.20 --> 682.66]  out a way to pull out this unstructured text, just dump it into the input prompt and ask
[682.66 --> 683.20]  a question over.
[683.20 --> 688.12]  Is it conceivable with what you're saying, if I'm thinking as an app developer about
[688.12 --> 692.64]  diving into this, that I'm hearing you say, you're going to do this, which is an additional
[692.64 --> 696.68]  thing to learn and be able to go, you know, it's an additional skill set that you're adding
[696.68 --> 696.94]  on.
[697.22 --> 701.58]  But I also hear you talking about other things that I used to have to do that maybe I don't
[701.58 --> 702.40]  have to do anymore.
[702.62 --> 708.48]  And to some degree, is it realistic to say from an effort standpoint, it becomes a wash once
[708.48 --> 713.20]  you have the skills a little bit, or maybe even you're gaining more power and doing less
[713.20 --> 717.86]  work along the way to do it so that it's kind of like, of course, you would do it going forward.
[718.06 --> 719.52]  Is that a fair way of thinking about it?
[719.94 --> 723.90]  Yeah, so it's an interesting way of thinking about it, because I think the high level question
[723.90 --> 728.16]  is just like, you know, what parts have become easier and what parts have gotten harder once
[728.16 --> 733.72]  you have this language model technology, because on one hand, things have gotten a bit easier
[733.72 --> 737.40]  and powerful to build these expressive like question answering systems with less effort.
[737.40 --> 742.36]  You know, you take in this giant blob of unstructured text, you know, figure out how to store it,
[742.50 --> 743.78]  you feed it into the language model.
[744.12 --> 747.96]  And then all of a sudden, you can ask these questions over these like files that you couldn't
[747.96 --> 752.42]  really do before with more kind of like traditional AI technologies or just like manual programming.
[753.00 --> 757.50]  That said, I think this new paradigm kind of involves its own set of challenges that I'm
[757.50 --> 758.30]  happy to talk about.
[758.60 --> 763.28]  I think there's a lot of like stacks emerging about how to make the best use of language models
[763.28 --> 764.20]  on top of your data.
[764.20 --> 767.32]  And there's some very basic stuff that's happening these days.
[767.42 --> 771.60]  But there's also kind of like more advanced stuff that we're working on.
[771.96 --> 776.36]  And I do think it's very interesting to think about what are the technological challenges
[776.36 --> 780.76]  that are preventing us from unlocking the full capabilities of language models.
[781.24 --> 785.86]  Because again, with a very basic stack, and again, like you can see this, if you just like
[785.86 --> 790.38]  play around chat to be tape, you can already get a ton of value from your data by just like
[790.38 --> 792.78]  doing some very basic processing on top of it.
[792.88 --> 795.16]  And you can start asking questions that you couldn't really ask before.
[795.58 --> 800.64]  But you know, with some more advanced capabilities, and some once you're solving some more interesting
[800.64 --> 804.56]  technical problems, what are kind of like the additional queries that can ask on top of
[804.56 --> 805.94]  your data that you also couldn't do before?
[806.44 --> 811.50]  Before we jump into so I want to kind of dive into the weeds about like the two things that
[811.50 --> 813.34]  you talked about, like how do I index my data?
[813.34 --> 814.54]  How do I query my data?
[814.66 --> 817.14]  All the goodness around that in Lama Index.
[817.30 --> 823.16]  Before we do that, maybe just as also like to set the stage for some people that are coming
[823.16 --> 826.60]  into this and maybe parsing some of the jargon that's thrown around.
[827.10 --> 831.90]  So one of the other things that people are really kind of diving into is thinking about like,
[832.26 --> 833.76]  how do I engineer my prompts?
[833.88 --> 836.78]  How do I chain prompts together and all of that sort of thing?
[836.86 --> 841.92]  And could you highlight because my at least the way I would phrase it, like those two things
[841.92 --> 845.92]  are complementary with the things that you're doing with Lama Index.
[846.34 --> 850.24]  But could you kind of help people understand like, how do those pieces fit together in
[850.24 --> 852.48]  terms of like architecting one of these systems?
[853.16 --> 858.44]  I guess in the end, LLM application development to put it in a very oversimplified view is just
[858.44 --> 861.20]  some fancy form of prompt engineering and prompt training, right?
[861.30 --> 864.96]  It's actually not super different with how we're thinking about building this interface
[864.96 --> 865.52]  with data.
[866.00 --> 869.50]  And so just as a very basic example, you know, if you're kind of coming into the space
[869.50 --> 874.48]  afresh, like a very basic prompt that you could put into a language model is something
[874.48 --> 875.14]  like the following.
[875.56 --> 877.58]  Here is my question, right?
[877.62 --> 881.14]  And then you put the question here and then you put in here's some context.
[881.14 --> 885.22]  And then in this context variable, you just dump all the context that could be relevant
[885.22 --> 886.34]  to the question, right?
[886.38 --> 887.66]  You copy and paste a blog post.
[887.76 --> 891.72]  You copy and paste like API documentation, just copy and paste it into the input prompt space.
[892.08 --> 896.06]  And then now at the bottom, say, given this context, give me the answers to this question.
[896.06 --> 899.00]  And you send it to a language model and then you get back an answer.
[899.50 --> 903.56]  So that's like the most basic like question answer prompt that you could use to kind of
[903.56 --> 907.00]  perform some sort of like question answering and over your data.
[907.18 --> 908.98]  It really is just prompting, right?
[909.02 --> 910.86]  Because you're putting stuff into the prompts.
[911.26 --> 914.56]  You have this overall prompt template and you have variables that you want to fill in.
[914.94 --> 920.74]  I think one interesting kind of like challenge that arises is how can you feed in context
[920.74 --> 922.28]  that exceeds the prompt window?
[922.28 --> 927.20]  Because for GPT-3, it's 4,000 tokens for Anthropic, I guess it's like 100,000 tokens.
[927.58 --> 932.24]  But if you look at like an Uber SEC 10K filing, it's like 160,000 tokens, right?
[932.24 --> 936.42]  So if you want to ask a question, like, what's the summary of this entire document or like
[936.42 --> 939.52]  what are the risk factors in this very specific section of the document?
[939.66 --> 943.44]  How do you feed that entire thing in so that you can basically answer the following question?
[944.00 --> 948.38]  And I think that's where things get a little bit more interesting because you can basically
[948.38 --> 950.06]  do one or more of the following things.
[950.06 --> 955.40]  One is you could have some external model, like something separate from the language model
[955.40 --> 960.34]  prompt that's actually doing retrieval over your data to figure out what exactly is the
[960.34 --> 963.04]  best context to actually fit within this prompt space.
[963.64 --> 970.32]  Two is you can do some sort of synthesis strategies to synthesize an answer over long context, even
[970.32 --> 972.56]  if that context doesn't actually fit into the prompt.
[973.02 --> 977.70]  For instance, you could chain repeated LLN calls over sequential chunks of data and then combine
[977.70 --> 980.40]  the answers together to actually give you back a final answer.
[980.58 --> 981.24]  That's one example.
[981.78 --> 986.44]  In the end, all this architecture is just kind of designed around being able to feed in some
[986.44 --> 988.42]  input to the LLN and get back some output.
[988.68 --> 990.82]  And the core of that really is a prompting, right?
[990.82 --> 994.40]  And so part of this is just like developing an overall system around the prompting.
[1008.58 --> 1015.20]  Well, Jerry, you had mentioned kind of these three levels of integrating external data into
[1015.20 --> 1016.40]  your LLN application.
[1016.40 --> 1020.30]  There's sort of data ingestion and there's like indexing and query.
[1020.56 --> 1026.98]  I'm assuming data ingestion has to do with like, oh, I'm going to connect to the Google
[1026.98 --> 1033.28]  Docs API and like pull the data over and then indexing and query build on top of that.
[1033.40 --> 1038.38]  But before we dive into those second two phases, which is where I think a lot of the cool stuff
[1038.38 --> 1043.66]  that you're doing is found, what should we know about sort of data and the data ingestion
[1043.66 --> 1049.36]  layer in terms of relevance to how LLN index builds on that and other things?
[1050.02 --> 1054.32]  The data ingestion side is just like the entry point to building a language model application
[1054.32 --> 1055.46]  on top of your own data.
[1055.88 --> 1056.98]  I think LLMs are cool.
[1057.26 --> 1059.52]  I want to use it on top of some existing services.
[1059.84 --> 1062.66]  What are those services and how can I load in data from those services?
[1062.66 --> 1068.96]  One component of LLN index is this kind of like community driven hub of data loaders called
[1068.96 --> 1072.74]  LLN hub, where we just offer a variety of different data connectors.
[1072.74 --> 1074.02]  So a lot of different services.
[1074.02 --> 1076.90]  I think we have over like 90 something different data connectors now.
[1077.04 --> 1080.06]  And these include like connections to file formats.
[1080.42 --> 1086.06]  So for instance, like PDF files, HTML files, like PowerPoints, images, even they can include
[1086.06 --> 1091.70]  connectors to APIs like Notion, Slack, Discord, Salesforce, actually, sorry, we actually don't have
[1091.70 --> 1092.22]  Salesforce yet.
[1092.22 --> 1093.16]  That's something that we want.
[1093.92 --> 1094.68]  But it would be cool.
[1095.62 --> 1096.80]  Yeah, it'd be very useful.
[1097.08 --> 1100.70]  If you're interested in contributing a Salesforce loader, please, I would love that.
[1100.70 --> 1106.08]  And then the next part is just like being able to connect to kind of like different sorts
[1106.08 --> 1109.64]  of multi-mobile formats, like audio images, which I think I've already mentioned.
[1110.06 --> 1114.06]  So the idea here is you have all this data, it's stored in some format, it's unstructured,
[1114.16 --> 1116.86]  it could be text or it could even be like images or some other format.
[1117.24 --> 1121.38]  How do you just like load in this data in a pretty simple manner and just wrap it with
[1121.38 --> 1122.72]  some overall document abstraction?
[1123.04 --> 1125.66]  So there's not a ton of tech going on here.
[1125.66 --> 1130.64]  And the reason it's more just like a convenience utility for developers to just like easily
[1130.64 --> 1131.64]  load in a bunch of data.
[1132.12 --> 1136.62]  And again, going back to the earlier point, the reason there's not too much tech is LLMs
[1136.62 --> 1138.76]  are very good at reasoning over unstructured information.
[1138.76 --> 1143.30]  So you actually don't need to do like a ton of parsing on top of this data that you load
[1143.30 --> 1146.14]  to basically get some decent results from the language model.
[1146.14 --> 1150.00]  And so once you actually load in this data in a lightweight container, you can then use
[1150.00 --> 1152.54]  it for some of the downstream tasks like indexing and querying.
[1153.06 --> 1153.54]  Awesome.
[1153.72 --> 1153.88]  Yeah.
[1154.00 --> 1158.70]  And I see like this is, I think, where things get super interesting, like I mentioned.
[1158.94 --> 1164.70]  So in Lama Index, I'm in the docs right now, like you mentioned list and table and tree and
[1164.70 --> 1168.78]  vector store and structured store and knowledge graph and empty indices.
[1168.78 --> 1175.42]  Could you describe like generally how to think about an index within Lama Index?
[1175.62 --> 1178.84]  And then like, why are there multiple of these?
[1179.14 --> 1181.56]  And what categories generally do they fit in?
[1182.06 --> 1185.54]  One way of thinking about this is just taking a step back at a high level.
[1185.68 --> 1189.62]  What exactly does the data pipeline look like if you're building a LLM application?
[1190.16 --> 1194.22]  So we started with data ingestion where you load in a document from some data source like
[1194.22 --> 1196.20]  a PDF document or API.
[1196.20 --> 1198.46]  And now you have this unstructured document.
[1198.84 --> 1202.62]  The next step typically is you want to chunk up the text into text chunks.
[1203.12 --> 1207.40]  So let's say naively, let's say you have just a giant blob of text from a PDF.
[1207.86 --> 1213.64]  You can split it, you know, every 4000 words or so or every 500 words into some set of text
[1213.64 --> 1213.88]  chunks.
[1214.46 --> 1219.56]  This just allows you to store this text in units that are easier to feed into the language
[1219.56 --> 1219.84]  model.
[1220.18 --> 1224.30]  And a lot of this is a function of the fact that the language model itself has limited
[1224.30 --> 1225.14]  prompt space, right?
[1225.14 --> 1228.92]  So you want to be able to chunk up a longer document into a set of smaller chunks.
[1229.34 --> 1230.46]  Now you have these chunks.
[1230.66 --> 1231.50]  They're stored somewhere.
[1231.90 --> 1235.52]  They could be stored, for instance, within a vector database, for instance, like a pine
[1235.52 --> 1236.56]  cone, VVA, Chroma.
[1237.02 --> 1242.12]  They could also be stored, for instance, like a document store like MongoDB, or you could
[1242.12 --> 1244.52]  store it in like files to some on your local disk.
[1244.90 --> 1245.64]  Now they're stored.
[1245.96 --> 1250.68]  The next part is how do you actually want to define some sort of structure over this data?
[1250.68 --> 1255.06]  A basic way of like defining some sort of like structure over this data, and this is where
[1255.06 --> 1258.76]  we got into indices, is just like adding and embedding to each chunk.
[1259.12 --> 1263.64]  And so if you have a set of text, how do you define like an embedding for each set of text?
[1264.04 --> 1267.50]  And that in itself could be treated as like an index, right?
[1267.82 --> 1270.68]  An index is just like a lightweight view over your data.
[1271.08 --> 1273.96]  The vector index is just adding and embedding to each piece of text.
[1273.96 --> 1278.44]  There's other sorts of indexes that you could define to define this like view over your data.
[1278.78 --> 1283.64]  There's a keyword table that we have where you just have a mapping from keywords to the
[1283.64 --> 1284.38]  underlying text.
[1284.78 --> 1290.04]  You could have like a flat list where you just like basically store a subset of node IDs as
[1290.04 --> 1290.96]  like its own index.
[1291.18 --> 1295.60]  Before I get into the technicals of like the indexes and, you know, like what they actually do,
[1295.96 --> 1301.04]  one thing to maybe think about is just like, what are the end questions that you want to ask?
[1301.04 --> 1303.82]  And what are some of the use cases that you'd want to solve?
[1304.10 --> 1308.02]  Before you dive into that, I was going to ask you really quick, could you define what an
[1308.02 --> 1311.80]  embedding is for those people who are learning large language models at this point, just so
[1311.80 --> 1315.04]  they'll understand what it is when you say you're defining that as the index?
[1315.44 --> 1319.66]  Embeddings is a part of kind of a very common stack emerging these days around this
[1319.66 --> 1321.94]  all-align data system that's emerging.
[1322.46 --> 1326.38]  And so an embedding is just a vector of numbers, usually like floating point numbers.
[1326.78 --> 1329.14]  You could have like a hundred of them, a thousand of them.
[1329.14 --> 1331.38]  It depends on the specific embedding model.
[1331.96 --> 1336.10]  And the way an embedding works, it's just think about this list of numbers as a condensed
[1336.10 --> 1338.98]  representation of the piece of content that you have.
[1339.34 --> 1344.06]  You know, if you can somehow in a very abstract manner, take in some piece of context, let's
[1344.06 --> 1348.32]  say this paragraph is about the biography of like a famous singer, right?
[1348.36 --> 1350.36]  And then you get an embedding from that.
[1350.80 --> 1351.76]  It's a string of numbers.
[1351.76 --> 1357.98]  The embedding has certain properties such that this string of numbers is closer to other
[1357.98 --> 1363.04]  numbers that are semantically about like similar content and farther away from other strings
[1363.04 --> 1366.20]  and numbers representing texts that are farther away in terms of semantic content.
[1366.66 --> 1371.26]  So for instance, like if you look at the biography of a singer, it's going to be pretty close to
[1371.26 --> 1376.54]  a biography of another singer versus if it's about, I don't know, like the American revolution
[1376.54 --> 1377.50]  or something like that.
[1377.58 --> 1379.56]  Embedding will probably be a little bit farther away.
[1379.56 --> 1384.50]  And so it's a way of like condensing a piece of text into some vector numbers that has
[1384.50 --> 1387.98]  some mathematical properties where you can measure similarity between, you know, different
[1387.98 --> 1388.92]  pieces of content.
[1389.42 --> 1391.04]  Maybe this is another point of distinction.
[1391.04 --> 1393.82]  And I get all these questions very often.
[1393.82 --> 1396.02]  So I think it's useful to discuss them on the show.
[1396.10 --> 1399.46]  Like last week at ODSC, I got a lot of these sorts of questions.
[1399.46 --> 1406.12]  So like we're talking about bringing in data, creating an index to access that data.
[1406.12 --> 1411.10]  That index might involve like a vector store or embeddings.
[1411.28 --> 1415.38]  But Llama index is sort of not a vector store.
[1415.62 --> 1418.74]  Like it's cool to be a vector database company right now.
[1418.86 --> 1420.84]  But Llama index is something different.
[1420.98 --> 1424.12]  And like, again, these are two things that are complementary, I think.
[1424.32 --> 1428.66]  Could you draw out that distinction a little bit just to help people kind of formulate those
[1428.66 --> 1429.96]  compartments in their mind?
[1429.96 --> 1435.10]  I think these days there's a lot of vector store providers and they handle a lot of the
[1435.10 --> 1436.92]  underlying storage components.
[1437.18 --> 1441.62]  And so if you look at like a Pinecone or Weevy, they're actually dealing with the storage
[1441.62 --> 1442.88]  of these unstructured documents.
[1443.36 --> 1449.60]  One thing that we want to do is leverage these existing kind of like storage systems and expose
[1449.60 --> 1454.94]  query interfaces that I guess a broader range of query interfaces beyond the ones that are
[1454.94 --> 1456.88]  just like directly offered by a vector store.
[1456.88 --> 1461.70]  And so for instance, a vector store will offer a query interface where you can typically query,
[1461.82 --> 1466.62]  you know, the set of documents with an embedding plus like a set of metadata filters plus maybe
[1466.62 --> 1467.64]  some additional parameters.
[1467.80 --> 1472.88]  But we're really trying to build this like broader set of like abstractions and tools through
[1472.88 --> 1477.28]  our indices, our query interfaces, plus like other abstractions that we have under the hood
[1477.28 --> 1482.92]  to basically perform like more interesting and advanced operations and manage the interaction
[1482.92 --> 1487.68]  between your language model and your data and almost like be a data orchestrator on top of your
[1487.68 --> 1488.74]  existing storage solutions.
[1489.20 --> 1493.02]  And so we do see ourselves as separate because we're not trying to build the underlying storage
[1493.02 --> 1493.48]  solutions.
[1493.58 --> 1498.58]  We're more trying to provide a lot of this like advanced query interface capability to the end user
[1498.58 --> 1501.38]  using the power of language models on top of your data.
[1501.38 --> 1505.24]  I think we got a little bit off track a little bit, but I think it was good.
[1505.24 --> 1513.64]  So kind of circling back to the indices that are available in Llama Index and you've talked about
[1513.64 --> 1520.48]  like this pipeline of processing and potentially like one index being like a vector store and maybe
[1520.48 --> 1528.10]  listeners are a little bit more familiar with kind of like vector search or semantic search or that
[1528.10 --> 1530.26]  sort of thing with everything that's going on.
[1530.60 --> 1535.32]  But you have much more than that, like these other patterns and these other indices that enable
[1535.32 --> 1536.20]  other patterns.
[1536.72 --> 1544.60]  Could you describe like some of those alternatives or additions to like vector store index and when
[1544.60 --> 1546.26]  and how they might come into play?
[1546.82 --> 1547.74]  Yeah, that's a good question.
[1547.74 --> 1551.36]  And maybe just kind of like frame this with a bit of context.
[1551.50 --> 1555.46]  I think it's useful to think about certain use cases for each index.
[1555.46 --> 1561.84]  So the thing about a vector index or being able to use a vector store is that they're typically
[1561.84 --> 1566.64]  well suited for applications where you want to ask kind of like fact based questions.
[1567.04 --> 1570.58]  And so if you want to ask a question about like specific facts in your knowledge purpose,
[1570.92 --> 1572.90]  using a vector store tends to be pretty effective.
[1573.36 --> 1577.14]  For instance, let's say your question is, let's say your knowledge purpose is about like American
[1577.14 --> 1578.06]  history or something, right?
[1578.08 --> 1582.58]  And your question is, hey, like what happened, you know, in the year of 1780?
[1582.58 --> 1588.04]  That type of question tends to lend well to using a vector store because the way the overall system
[1588.04 --> 1592.36]  works is you would take this query, you would generate an embedding for the query, you would
[1592.36 --> 1598.44]  first do retrieval from the vector store in order to fetch back the most relevant chunks to the query.
[1598.82 --> 1601.72]  And then you would put this into the input prompt of the language model.
[1602.14 --> 1606.90]  And so the set of retrieve items that you would get would be those that are most semantically
[1606.90 --> 1609.98]  similar to your query through embedding distance, right?
[1609.98 --> 1614.62]  So again, like going back to embeddings, like the closer different embeddings are between your query
[1614.62 --> 1619.48]  and your context, the more relevant that context is, and the farther apart it is, then the less
[1619.48 --> 1619.84]  relevant.
[1619.98 --> 1624.32]  And so you get back the most relevant context or query, feed it to a language model, get back an answer.
[1624.90 --> 1630.26]  There are other settings where standard top K embedding base look up, and I can dive into this
[1630.26 --> 1632.72]  in as much technical depth that you guys would want to.
[1633.12 --> 1637.56]  But there's a settings where like standard kind of like top K embedding base retrieval doesn't work well,
[1637.56 --> 1642.10]  right? And one example where it doesn't typically work well, and this is a very basic example,
[1642.48 --> 1646.82]  is if you just want to get a summary of like an entire document or an entire set of documents.
[1647.20 --> 1652.12]  Let's say, you know, instead of like asking a question about a specific fact, like what happened
[1652.12 --> 1657.24]  in like, you know, 1776, maybe you just want to ask the language model, could you just give me an
[1657.24 --> 1663.52]  entire like summary of American history in like the 1800s? That type of question tends to not lend well
[1663.52 --> 1668.34]  to embedding base look up, because you typically fix like a top K value when you do embedding base
[1668.34 --> 1672.52]  look up, and you would get back very specific context. But sometimes you really want the language
[1672.52 --> 1677.60]  model to go through all the different contexts within your data. So a vector index storing it
[1677.60 --> 1682.22]  with embeddings would create a query interface where you can only fetch like the K most relevant
[1682.22 --> 1687.50]  nodes. If you store it, for instance, with like a list index, you could store the items in a way such
[1687.50 --> 1691.34]  that it's just like a flat list, right? So when you like query this list index,
[1691.34 --> 1696.80]  you actually get back all the relevant items within this list. And then you'd feed it to our
[1696.80 --> 1701.94]  synthesis module to synthesize a final answer. So the way you do retrieval over different indices
[1701.94 --> 1707.74]  actually depends on the nature of these indices. Another just like a very basic example is that
[1707.74 --> 1713.54]  we also have like a keyword table index where you can kind of like, look up specific items by keywords,
[1713.78 --> 1718.76]  right instead of through like embedding base distance. Keywords, for instance, are typically good
[1718.76 --> 1724.10]  for stuff that requires high precision and a little bit like lower recall. So you really want
[1724.10 --> 1729.26]  to fetch like specific items that match exactly to the keywords. This has the advantage of actually
[1729.26 --> 1733.76]  allowing you to retrieve a bit more precise context than something about like vector based
[1733.76 --> 1739.10]  embedding lookup doesn't. The way I think about this is like, a lot of what llama index wants to
[1739.10 --> 1746.16]  provide is this overall query interface of your data. Given any class of queries that you might want to ask,
[1746.16 --> 1751.36]  whether it's like a fact based question, whether it's a summary question, or whether it's, you know,
[1751.36 --> 1756.30]  some more interesting questions, we want to provide the tool set so that you can answer those questions.
[1756.76 --> 1761.60]  And indices, like defining like the right structure of your data is just one step of this overall
[1761.60 --> 1767.32]  process and helping us achieve this vision of like, a very like journalizable query interface over
[1767.32 --> 1772.68]  your data. Some examples of like different types of queries that we support, there's the fact based
[1772.68 --> 1777.44]  question lookup, which is like semantic search using vector embeddings, you can ask like summarization
[1777.44 --> 1783.16]  questions through, you know, using our list index, you could actually run like a structured query. So
[1783.16 --> 1787.02]  you could, if you have a SQL database, you could actually run like structured analytics over your
[1787.02 --> 1792.30]  database and do like text to SQL, you can do like compare contrast type queries where you can actually
[1792.30 --> 1797.24]  look at different documents within your collection, and then like look at the differences between them.
[1797.24 --> 1802.66]  You could even look at like temporal queries where you can reason about like time and then go forwards
[1802.66 --> 1807.64]  and backwards, and basically kind of like, say, hey, this event actually happened after this event,
[1807.90 --> 1812.88]  here's the right answer to this question that you're asking about. And so a lot of what Lama Index
[1812.88 --> 1819.68]  does provide is a set of like tools, the indices, the data ingestors, a query interface to solve like
[1819.68 --> 1821.66]  any of these queries that you might want to answer.
[1840.50 --> 1846.80]  So Jerry, you really got me thinking a lot about this, the possibilities of the query schemes is
[1846.80 --> 1851.50]  pretty darn cool. You know, we kind of started with ingest and moved into kind of indexing. And now
[1851.50 --> 1857.82]  we're talking about queries. Could you kind of give me an example with the tool in a little bit
[1857.82 --> 1862.24]  more of a practical level, because you kind of hit the concepts about like what the possibilities are.
[1862.52 --> 1866.94]  But as someone who hasn't used the tool myself, I'm trying to get a sense of what that workflow is
[1866.94 --> 1872.94]  like, pick what would probably be like a really common query scheme that you're doing and dive into that
[1872.94 --> 1878.24]  just a little bit to give us a sense of a hands on practical, you know, fingers on keyboard sense of
[1878.24 --> 1882.78]  it. Because I'm trying to get a sense of where I'm going to go for playing after we get done with the
[1882.78 --> 1884.86]  episode. So I want to try it.
[1885.08 --> 1890.62]  A hundred percent. I think one thing that has popped up pretty extensively after talking to a variety of
[1890.62 --> 1895.38]  different users is actually financial analysis. I think looking at SEC 10k tends to be a pretty
[1895.38 --> 1899.96]  popular example. If you look at the Anthropic Quad example, they also use SEC 10k.
[1899.96 --> 1905.92]  And my guess the reason it's popular is one, there's just like a ton of text. And so it's just very hard to parse
[1905.92 --> 1911.78]  if you read as a human. Two, it's like a useful thing for people in like financial institutions like
[1911.78 --> 1916.28]  consulting, because you want to like compare and contrast the performance of like different businesses,
[1916.58 --> 1918.52]  you know, and look at the performance across years.
[1918.96 --> 1923.42]  Believe it or not, I actually read 10k's a lot. And that would be a really useful example for me.
[1923.98 --> 1925.54]  Believe it or not, I'm not kidding you.
[1925.96 --> 1929.48]  As a result, we've actually been playing around with a decent amount too.
[1929.48 --> 1935.38]  Yeah. Some of the cool like things that we've been that we're showing that Lama Index can do on top of your 10k's is for
[1935.38 --> 1941.18]  instance, let's say you have like two companies, let's say Uber and Lyft, right for the year 2021, you can actually ask a
[1941.18 --> 1947.16]  question like, can you actually compare and contrast the risk factors for Uber and Lyft or their quarterly earnings across like these
[1947.16 --> 1953.96]  two documents? And one is the Uber 10k, one is a Lyft 10k. This is actually an example where if you do like just top
[1953.96 --> 1959.86]  embedding based lookup, the query fails, because if you ask the question, you know, compare and contrast
[1959.86 --> 1966.56]  Uber and Lyft, and don't do anything to it. And let's say, you know, your Uber and Lyft documents are just in some one
[1966.56 --> 1973.14]  vector index, you don't really have a guarantee you're going to fetch the relevant context to this question that to be able to
[1973.14 --> 1978.36]  answer this thoroughly, right? And then the model might hallucinate, you'll get back the wrong answer. And then you know, it's just not a good
[1978.36 --> 1983.96]  experience. I think what you typically want to do is have some sort of like nicer abstraction layer on top of this
[1983.96 --> 1990.60]  query, that can actually kind of map that query to some plan that that would roughly be like how a human would think
[1990.60 --> 1995.82]  about like executing or answering this question. Let's say you want to compare and contrast the financial performance
[1995.82 --> 2002.64]  of Uber and Lyft in the year 2021. Well, first, okay, what was the financial performance of Uber in 2021? What was the
[2002.64 --> 2008.34]  financial performance of Lyft? You break it down into those two questions. And then for each question, use it
[2008.34 --> 2013.94]  to kind of like look over your respective index, let's say you have an index corresponding to Uber,
[2014.14 --> 2019.70]  and the index corresponding to Lyft, get back the answer, right, get back the actual kind of like
[2019.70 --> 2025.36]  revenue, for instance, for Uber and Lyft, and then like synthesize both of them at the top level again,
[2025.56 --> 2030.70]  be able to like pull in the individual components you extracted from each document, and then synthesize
[2030.70 --> 2036.10]  the final response that's able to compare the two. So that's like an example of something that we can
[2036.10 --> 2040.42]  actually do pretty well with Wama Index. And we have like a variety of tool sets for allowing to do
[2040.42 --> 2045.46]  that. And that's an example of a query that's kind of more advanced, because it requires comparisons
[2045.46 --> 2050.82]  beyond just like kind of asking stuff over a single document. Another example, just to kind of like take
[2050.82 --> 2056.18]  the 10k analogy further is, let's say you have the yearly reports of the same company across different
[2056.18 --> 2061.66]  years, let's say from like 2018 to 2022, you can ask the question like, did revenue like decline,
[2061.66 --> 2067.38]  go up or down in the last like three years. And then you could actually do a very similar process
[2067.38 --> 2072.30]  where given the query interface that we provide, break this question down into some questions over
[2072.30 --> 2077.58]  each year, pull out the revenue, and then basically at the end, do a comparison step to see whether or
[2077.58 --> 2082.64]  not it increased or declined. Just as an aside to any listeners out there wondering why on earth
[2082.64 --> 2087.74]  somebody would read 10ks, especially considering that our audience is focused on on data and such as
[2087.74 --> 2092.84]  if you want to learn about another technology company and really understand what it does and
[2092.84 --> 2098.98]  be able to compare it. This is an example where you can gain tremendous intelligence on another company
[2098.98 --> 2104.78]  with publicly available information. And by comparing multi year 10ks, like you just said, you'll learn
[2104.78 --> 2109.58]  way more about that company than its own employees know about it. So anyway, just thought I'd mention
[2109.58 --> 2115.78]  that as an aside. Yeah, I look forward to hearing your success with speeding up your workflows around
[2115.78 --> 2121.82]  reading the 10k's Chris with Lama Index. I'm excited about this. This is going to save me a lot of time.
[2122.00 --> 2127.22]  Jerry, one of the things that we talked a little bit about in one of our previous conversations,
[2127.22 --> 2133.94]  which I know you've also thought very deeply about and even have like a portion of the docs and
[2133.94 --> 2140.84]  functionality in Lama Index devoted to is evaluation, like query response evaluation,
[2140.84 --> 2149.30]  like, how do I know my large language model like barfed up an answer, right, based on some query,
[2149.30 --> 2155.50]  and I pulled in some external data, and I, you know, inserted some context, and maybe I strung a few
[2155.50 --> 2162.78]  things together, like, how am I to evaluate the output of that? Could you give us maybe a high level
[2162.78 --> 2167.54]  from your perspective, how you think about this evaluation problem, and then maybe go into a little
[2167.54 --> 2172.32]  bit of some of the things that you're exploring in that space? Yeah, totally. Just to preface this,
[2172.44 --> 2178.46]  like, we are super interested in evaluation, or more tailored towards this interface of like your
[2178.46 --> 2182.94]  data with LMS. I didn't dive into that a bit more. And we have some initial evaluation capabilities,
[2182.94 --> 2187.74]  but we're super like, community oriented, like we'd love to just like, you know, kind of like chat with
[2187.74 --> 2191.30]  there's a lot of like different tool sets out there that allow you to do like different types of
[2191.30 --> 2196.78]  evals of your data and building like nice interfaces for doing so. And so I think this is an area of
[2196.78 --> 2201.72]  active exploration and interest for us as well. And so just kind of thinking about this a little
[2201.72 --> 2207.92]  bit more deeply about evaluation is very interesting, because there is the evaluation of each language
[2207.92 --> 2213.44]  model call itself. And then there is the evaluation of the overall system. And so diving into this bit
[2213.44 --> 2218.16]  more, like, at a very basic level, if you have a language model, you have an input, and you get back
[2218.16 --> 2222.52]  some output, you can try to validate whether or not that output is correct, right, given a single
[2222.52 --> 2227.00]  language model call. Did the model actually give you the correct answer given the input?
[2227.32 --> 2231.72]  Did it spit out garbage? Did it like hallucinate that type of thing? The interesting thing about
[2231.72 --> 2236.42]  a lot of systems that are emerging these days, is that they're really like systems around like a
[2236.42 --> 2240.74]  repeated sequence of language model calls. And this applies whether or not you're dealing with like
[2240.74 --> 2245.28]  a more agent based framework, which you know, you ask a question that can like just repeatedly kind
[2245.28 --> 2250.36]  of like do react chain of thought prompting or like be able to pick a tool. But the end result is
[2250.36 --> 2254.36]  is able to give you back a response. Another example, this is like auto GPT, where you just
[2254.36 --> 2257.80]  let it run for like five minutes, and just like keeps on doing stuff like over and over again,
[2257.86 --> 2261.98]  is how it gives you back something. Or, you know, even in the case of retrieval augment to generation
[2261.98 --> 2266.20]  is just like a fancy name for roughly like what we're doing with llama index, which is like a query
[2266.20 --> 2270.94]  interface over your data. Like even with within our system, there could be a sequence of repeated
[2270.94 --> 2275.54]  LLM calls. But the end result is that you send in some input into the system, and you get back some
[2275.54 --> 2279.80]  output. You know, given this high level system, how do you evaluate the input and output properly?
[2279.80 --> 2283.76]  I think in traditional machine learning, typically what you want to have is you want to have like
[2283.76 --> 2288.44]  ground truth labels for every input that you send in. So do you like, for instance, ask a question,
[2288.58 --> 2292.36]  you want to know the ground truth answer, and you want to compare the predicted answer to the
[2292.36 --> 2297.50]  ground truth answer and see how well the predicted answer matches up. This is still like something that
[2297.50 --> 2302.72]  people are exploring these days, even in the space of journalism AI and LLMs, you have ground truth
[2302.72 --> 2307.64]  like text, and then you have predicted text, and you want some way of scoring how close this predicted
[2307.64 --> 2313.06]  text is to ground truth text. I think the core set of eval modules that we have within llama index
[2313.06 --> 2318.40]  actually, are ground truth free or label free. And that part in itself is actually very interesting,
[2318.40 --> 2324.34]  because you have this input, you ask a question, you get back this predicted response, you also get
[2324.34 --> 2329.82]  back the retrieve like sources like the documents themselves. What we found is that you can actually
[2329.82 --> 2336.14]  make another LLM call to just like compare the sources against the response, and then also compare the
[2336.14 --> 2341.62]  query against the sources and the response to see how well all two or three of these components match
[2341.62 --> 2347.10]  up. And this doesn't require you to actually specify what the ground truth answer is, you just look at
[2347.10 --> 2351.92]  the predicted answer, see if it matches up to the query or the context in a separate LLM call. And
[2351.92 --> 2357.86]  it's interesting because one, it makes use of LLM based evaluation, which is kind of like an interesting
[2357.86 --> 2362.06]  way to think about it, basically using the language model to evaluate itself, right? I'm sure there's like
[2362.06 --> 2365.54]  downsides which we can get into, but you know, a lot of people are doing it these days too.
[2365.54 --> 2370.40]  And then the second part is, it doesn't require any ground truth, because you're using the language
[2370.40 --> 2375.46]  model to evaluate the capabilities of its own answer plus context, you don't actually need to as a
[2375.46 --> 2379.24]  human feed in the actual answer. And the benefit of this is that it just saves a bunch of time and
[2379.24 --> 2384.04]  cost, you don't actually need to like label your entire data set to run evals. I still think this
[2384.04 --> 2389.68]  overall like space is probably relatively early. I think there's still some big questions around like
[2389.68 --> 2395.52]  latency and cost if you're trying to really do LLM based evals more fully, like using the LLM
[2395.54 --> 2400.28]  to evaluate a large data set takes a lot of time and costs a lot of money. And so this is generally
[2400.28 --> 2403.60]  kind of like an area that we're still kind of like actively thinking about.
[2403.88 --> 2409.54]  Yeah, that's awesome. As we kind of like get near to the end here, I know things are like
[2409.54 --> 2415.70]  progressing so quickly. I can't keep up with all of your tweet threads about like awesome new stuff
[2415.70 --> 2421.90]  that's happening in LLM index. But I know there's a lot. As you look to kind of the next year,
[2421.90 --> 2426.46]  and like where your mind is at what you really want to dive into and also what what's really
[2426.46 --> 2431.82]  exciting to you about the field. There's a lot of people excited about a lot of different things.
[2431.82 --> 2437.32]  But from your perspective, having been in the trenches building large language model applications,
[2437.64 --> 2443.76]  interacting with users of LLM index, what is it that really excites you moving into this next year
[2443.76 --> 2449.96]  in terms of the possibilities, the real practical possibilities on the horizon and how kind of
[2449.96 --> 2453.64]  our development workflows will be changing in the near future?
[2454.04 --> 2459.60]  Yeah, totally. I think there's a few related components. So this I'm both excited for,
[2459.76 --> 2463.68]  as well as like, you know, the challenges that we're going to solve. Probably the first component
[2463.68 --> 2468.42]  is just being able to build this automated query interface over your data. You know, if you're looking
[2468.42 --> 2472.84]  at all the query use cases that we solve, one of the key questions that we keep going back to is,
[2473.44 --> 2477.06]  here's a new use case on top of this data. And here's a new question that you'd want to ask,
[2477.06 --> 2482.34]  how do we like figure out how to best like fulfill a query request, right? And I think,
[2482.48 --> 2487.36]  especially as your data sources become more complicated, then it's just like, how do you
[2487.36 --> 2492.36]  think about like, how to index and structure the data properly? How do you think about interesting
[2492.36 --> 2496.62]  automated interactions that happen at the query layer between the language model and your data?
[2497.00 --> 2501.02]  How do we like basically just like make sure we solve this request? And then the second component
[2501.02 --> 2505.86]  to this is, we want to make sure that we build this interface set and handle any type of query
[2505.86 --> 2511.32]  throw at it. Now, how do we do this in a way that is like cheap, fast and easy to use? For a lot of
[2511.32 --> 2515.20]  users, once they move on beyond the initial prototyping phase, they think about starting
[2515.20 --> 2519.32]  to minimize like cost and latency. And then think about how do you like pick the best models for
[2519.32 --> 2524.24]  the job, right? There's like the OpenAI API, which works well, generally, you know, they're probably the
[2524.24 --> 2528.86]  best model out there, but it can also be quite slow. And then there's also these like open source
[2528.86 --> 2533.26]  elements popping up, probably like a few new ones every week. And then how do users make the best
[2533.26 --> 2538.38]  decisions whether to use that over their data? And then I think the next part to this is, you know,
[2538.42 --> 2543.56]  a lot of LLM development is moving in this overall trend of like automated reasoning, right? If you
[2543.56 --> 2547.88]  look at like agents and tools, it's an auto GPT and all this stuff. It's just like, how do you make
[2547.88 --> 2553.38]  like automated decisions over your data? And then I think as a consequence, there's always going to be
[2553.38 --> 2558.72]  this trade off between how few constraints can we give it and how many like, like, should we give it
[2558.72 --> 2563.00]  more constraints or fewer constraints, right? Because if you're a constraints, you give to something like this,
[2563.26 --> 2567.76]  it has more flexibility to potentially do way more things. But then also just like error,
[2567.94 --> 2573.16]  right? Like it'll just like make mistakes. And then there's no really no way to correct it easily.
[2573.26 --> 2578.00]  And then you can't really trust the decisions. Whereas if you kind of like constrain the outputs
[2578.00 --> 2584.10]  of these like automated decision makers or agents, then you can potentially get more interpretable
[2584.10 --> 2589.18]  outputs, maybe at the cost of like a little bit of flexibility in terms of functionality. And I think
[2589.18 --> 2593.14]  we've been thinking a lot about that with respect to like the data retrieval and synthesis space.
[2593.26 --> 2600.30]  Right? Like how can we give you back results that are expressive, but also, you know, like perform
[2600.30 --> 2602.62]  well and are going to make mistakes like a ton of time.
[2603.10 --> 2607.80]  Awesome. Yeah, well, I'm really happy that we had a chance to talk through all the great
[2607.80 --> 2614.68]  Lama Index things and make sure if you're not following Jerry on Twitter, find him there. He posts
[2614.68 --> 2620.08]  a lot of great stuff that they're working on. And of course, you can find Lama Index. If you just search
[2620.08 --> 2624.18]  for Lama Index, there's like a great set of docs and all those things. We'll make sure we include
[2624.18 --> 2630.26]  those links in our show notes for people to find out about that and get linked to their docs and their
[2630.26 --> 2636.46]  blog and all the good things. So check out Lama Index. And thank you so much for joining us, Jerry. It's been awesome.
[2636.46 --> 2666.44]  Thank you for listening to Practical AI. Your next step is to subscribe now, if you haven't already. And if you're a longtime listener of the show, help us reach more people by sharing Practical AI with your friends and colleagues. Thanks once again to Fastly and Fly for partnering with us to bring you all Change Talk podcasts. Check out what they're up to at Fastly.com. And we'll see you next time.
[2666.46 --> 2676.12]  And to our Beat Freaking Residents Breakmaster Cylinder for continuously cranking out the best beats in the biz. That's all for now. We'll talk to you again next time.
[2688.46 --> 2689.52]  Game on!
