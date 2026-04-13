[0.00 → 8.66] Welcome to Practical AI.
[9.34 → 19.54] If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing the world, this is the show for you.
[20.24 → 24.92] Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 → 35.44] Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on six continents, so you can launch your app near your users.
[35.84 → 37.84] Learn more at Fly.io.
[42.64 → 46.08] Welcome to another episode of Practical AI.
[46.08 → 48.14] This is Daniel Whiten ack.
[48.34 → 54.12] I am the CEO and founder at Prediction Guard, where we're enabling AI accuracy at scale.
[54.12 → 61.56] And I am joined, as always, by my co-host, Chris Benson, who is a principal AI research engineer at Lockheed Martin.
[61.86 → 62.48] How are you doing, Chris?
[62.76 → 64.46] Doing great today, Daniel. How's it going?
[64.60 → 67.54] I know we're recording leading into a holiday weekend here.
[67.82 → 71.00] We are, and so many exciting things.
[71.20 → 82.46] Last week, I got the chance to briefly attend the AI Engineer World's Fair, which is sort of prompted in certain ways by our friends over at the Latent Space podcast.
[82.46 → 84.54] And that was awesome to see.
[85.18 → 98.08] And, of course, a big topic there were all things having to do with vector databases, RAG, all sorts of retrievals, search sorts of topics.
[98.88 → 107.04] And to dig into a little bit of that with us today, we have Bowie Schwaben-Cohen, who is a developer advocate at Pine cone.
[107.28 → 107.52] Welcome.
[108.04 → 109.32] Hi, guys. Thanks for having me today.
[109.52 → 110.84] I'm really excited to be on the show.
[110.84 → 114.32] Yeah, well, I mean, we were talking a little bit before the show.
[114.72 → 125.12] Pine cone is, from my perspective, one of the OGs out there in terms of coming to the vector search, semantic search embeddings type of stuff.
[125.32 → 137.92] Not that that concept wasn't there before Pine cone, but certainly when I started hearing about vector search and retrieval and these sorts of things, Pine cone was already a name that people were saying.
[137.92 → 149.70] So could you give us a little bit of background on Pine cone and kind of how it came about and what it is position-wise in terms of the AI stack?
[150.20 → 152.62] So Pine cone was started about four years ago, give or take.
[152.62 → 163.76] And our founder, Ido Liberty, was one of the people who were instrumental in founding SageMaker over at Amazon and had a lot of experience in his work at Yahoo.
[163.76 → 182.58] And I think that one of the fundamental kind of insights that he had was that the future of pulling insights out of data was going to be found not exclusively, but predominantly in our capability to construct vectors out of that data.
[182.58 → 191.38] And that representation that was produced by neural networks was very, very useful and was going to be useful moving forward.
[191.78 → 197.34] I think he had that insight way before tools like ChatGPT became popular.
[197.34 → 204.86] And so that really gave Pine cone a great edge at being kind of the first mover in this space.
[205.08 → 208.14] And we've seen the repercussions of that ever since.
[208.42 → 217.36] You know, with the rise of LLMs, I think people very quickly came to recognize the limitations that LLMs may have.
[217.36 → 232.56] And it was clear that there needed to be a layer that sort of bridged the gap between the semantic world and the structured world in a way that would allow LLMs to rely on structured data, but also leverage their capabilities as they are.
[232.96 → 238.44] And that is one of the places where vector databases play a very strong role.
[239.10 → 245.66] You know, vector databases are distinct from vector indices in the sense that they are databases and not indices.
[245.66 → 250.94] Right. So like an index may have basically is limited by the memory capacity.
[250.94 → 254.34] Right. That the machine that it's running on allows it to have.
[254.56 → 260.96] Whereas vector databases behave in the way that traditional databases behave and in the way that they scale.
[261.16 → 274.78] Of course, there's a completely different set of challenges, algorithmic challenges that come with the territory of dealing with vectors and high dimensional vectors that don't exist in the world of just simple, you know, text,
[274.78 → 277.04] textual indexing and columnar data.
[277.60 → 281.10] And that's where like the secret sauce of Pine cone lies.
[281.20 → 292.20] Right. It's its ability to handle vector data at scale, but maintain, you know, the speed and maintainability and resiliency of a database.
[292.20 → 297.90] As you were kind of comparing vector databases to indices and then kind of bringing that compared to that.
[298.40 → 306.74] One of the things that I run across still a lot are people, you know, vector databases are really, you know, incredibly helpful now.
[306.80 → 311.46] But there's still a lot of people out there who don't really understand how they fit in.
[311.68 → 317.18] You know, they don't really get it versus the NoSQL versus relational databases or fine-tuning.
[317.18 → 322.62] Yeah. And so and they hear you say it does vectors and stuff like that.
[322.74 → 339.76] Could you take a moment since we have you as an expert in this thing and kind of like lay out the groundwork a little bit before we dive deeper into the conversation about what's different about a vector database that is storing vectors versus storing the same vectors in something else?
[339.76 → 346.00] Like why go that way for somebody who just isn't quite hasn't really ramped up on that yet?
[346.00 → 349.78] So the basic premise is you want to use the right tool for the job.
[349.78 → 358.14] Right. And the basic difference right between a relational database, a graph database and a vector database or a document database for that matter.
[358.14 → 370.12] Right. Is the type of content that they are optimized to index, meaning a relational database is meant to index a specific column and create an index that would be easily traversable.
[370.12 → 375.26] Right. And in scale, it would be able to traverse that across different machines.
[375.26 → 379.22] Right. And do it effectively. Right. Graph database does the same thing.
[379.30 → 382.62] Only its world is nodes and edges. Right.
[382.64 → 391.96] And it's supposed to be able to build an optimized representation of the graph such that it could do traversals on that graph efficiently.
[391.96 → 404.92] In vector databases, vector databases are meant to deal with vectors, which are essentially long, high dimensional set of numbers, meaning like you can think of an array with a lot of real numbers inside that array.
[404.92 → 411.58] And you can think of this collection of vectors as being points in a high dimensional space.
[411.58 → 422.38] And the vector database is building effective representations to find similarities or geometric similarities between those vectors in high dimensional space.
[422.50 → 435.06] And that means that basically it would be very effective at given a vector, finding a vector that is very close, quote unquote, to that vector in a very large space.
[435.06 → 457.68] Right. So to do that, like you need to use a very specific set of algorithms that index the data in the first place and then query that data to retrieve that similar set of vectors to the query vector at a small amount of time and also being able to update or make modification to that high dimensional vector space in a way that is not cost prohibitive.
[457.68 → 464.68] Right. Or time prohibitive. Right. And that's like the crux of the difference between a vector database and other types of databases.
[465.06 → 483.46] Just to draw that out a little bit more. So from your perspective, like what would be if you were to kind of explain to someone, hey, here I've got one piece of text, and I'm wanting to match to some close piece of text in this vector space.
[483.46 → 499.92] What might be advantageous about using this vector based search approach and these embeddings in terms of what they mean and what they represent versus doing like, you know, TF IDF has been around for a long time.
[499.92 → 506.54] I can search based on keywords. I can do a full text search. There are lots of ways to search text.
[507.40 → 515.20] You know, that concept isn't new, but this vector searches seems to be powerful in a certain way.
[515.36 → 517.24] From your perspective, how would you describe that?
[517.94 → 520.84] Yeah, I think that the linchpin here is the word embedding.
[520.84 → 531.84] Right. The vector search capability itself is a pretty straightforward mathematical operation that in and of itself doesn't necessarily have value.
[532.82 → 536.54] Right. It basically it's like other mathematical operations. It's a tool. Right.
[536.88 → 539.08] The question is, like, where does the value come from?
[539.16 → 541.44] And I would argue that the value comes from the embeddings.
[541.44 → 544.44] And we'll talk about what exactly they are.
[544.56 → 552.50] We just point a flag and say embeddings are represented as vectors, which is why the vector database is so critical in this scenario.
[552.90 → 556.48] But why are embeddings helpful in the first place? Right.
[556.48 → 565.02] So embeddings come from a different set, right, like a very wide set of neural networks that have been trained on textual data.
[565.02 → 574.48] And they create within them representations of different terms, different surface forms, sentences, paragraphs, etc.
[574.82 → 578.16] That map onto a certain location in vector space.
[578.38 → 583.12] The cool thing about embeddings is that it just so happens, and we can talk about why,
[583.60 → 590.60] it just so happens that terms that have semantic similarity have a closeness in vector space.
[590.60 → 597.74] And that means that if I search for the word queen and I have the word king embedded as well in my vector database,
[597.90 → 603.70] and I also have the word dog, right, because the word king is more semantically similar to the word queen,
[603.90 → 606.58] I will get that as a result and not the word dog.
[606.94 → 614.78] Right. And that allows me to basically leverage the quote unquote understanding of the world that machine learning models
[614.78 → 620.40] and specifically neural networks have, right, large language models have of the world, right,
[620.48 → 627.74] in a way that I can't quite leverage from other modalities like DF IDF and other, you know, BM25, etc.
[627.98 → 632.56] That like look at a more lexical kind of perspective on the world, right?
[632.78 → 639.16] And so when we talk about, you know, practical use cases, right, like RAG comes up very, very frequently.
[639.16 → 646.46] And the reason for that is because we are in semantic space, a user interacts with the system in semantic space.
[646.52 → 650.02] So that means that they ask the system a question in natural language.
[650.18 → 657.10] We can take that natural language and basically, again, quote unquote, understand the user's intent, right,
[657.12 → 665.36] and map it again into our high dimensional vector space and find content that we've embedded that has some similarity to that intent.
[665.36 → 673.54] Right. And so we're not looking for an exact lexical match, but we're actually able to take a step back, right,
[673.54 → 682.62] and look at the more ambiguous intention and meaning of the query itself and match to it things that are semantically similar.
[682.98 → 683.48] If that makes sense.
[683.82 → 691.76] Would it be fair to say that you're essentially because the output of those structures being embeddings and those are vectors,
[691.76 → 700.66] and therefore you're essentially storing it and operating on it in a closer representation to how they naturally would be.
[700.78 → 706.38] And so you're not doing a bunch of translation just to fit it into a storage medium and to operate on it.
[706.50 → 709.94] Therefore, it's going to be quite a bit faster since you're, is that fair?
[710.14 → 711.44] Is that a fair way of thinking about it?
[711.80 → 718.38] Perhaps we're in a way we're compressing the representation into something very small in a sense, right?
[718.38 → 722.40] So you can think of an image, for example, right?
[722.52 → 725.96] An image would, that could be like a megabyte big, right?
[726.24 → 733.86] We can get a representation that in terms of like its actual size in terms of the vector is order of magnitudes smaller, right?
[733.98 → 738.16] And we can use that representation instead of using the entire image, right?
[738.16 → 739.18] To do our search.
[739.18 → 749.68] Now, it just so happens that, again, when we're doing embeddings for images, right, we get like that same quality where we're not looking at, you know,
[749.78 → 755.50] we're not looking at an exact match or like pixel matching pixel to pixel with images that we have.
[755.74 → 761.66] We can actually look at the semantic layer, meaning what is actually in that picture.
[761.76 → 767.94] So if it's a picture of a cat, we would get, as a result, other pictures of cat we've embedded and saved in the database, right?
[767.94 → 777.38] And that will come out of the representation itself of the embeddings that were a result of like, say, like a clip model that we use to embed our image.
[777.82 → 781.90] So I don't know if it necessarily means that like it simplifies things.
[781.90 → 788.06] In a lot of ways, it actually adds a lot of more oomph to the representation, right?
[788.08 → 792.72] So you can actually match on things that you wouldn't necessarily expect, right?
[792.72 → 808.28] And that's kind of like what the beauty of semantic search in that sense, right, is that users can write something and then get back results that don't even contain, right, anything remotely similar in terms of the surface form to their query.
[808.28 → 811.30] But semantically, right, it would be relevant.
[811.30 → 826.12] Hey, friends, this episode of Practical AI is brought to you by our new friends over at Plum.
[826.40 → 833.40] Plum is a low-code AI pipeline builder that helps you to build complex AI pipelines superfast.
[833.40 → 843.84] You can easily create AI pipelines using their node-based editor, iterate and deploy faster and more reliably than coding by hand without sacrificing control.
[844.22 → 845.58] Deployment is easy.
[845.74 → 848.60] Pipelines are live API endpoints.
[848.92 → 856.38] Eliminate the need for constant code redeployment and debugging by deploying complex AI pipelines as API endpoints.
[856.38 → 858.90] Team collaboration is easy, too.
[859.06 → 866.78] Plum's declarative node-based editor enables you to build quickly while empowering non-technical roles to iterate on what you've done without breaking it.
[867.12 → 877.32] You can build advanced AI features, get structured output every time, transform data and leverage validated JSON schema to create reliable, high-quality structured output.
[877.82 → 879.44] So Plum is built for builders.
[879.88 → 885.26] Early-stage product teams are using Plum to go from idea to validation in record time.
[885.26 → 888.26] To get started, go to useplum.com.
[889.00 → 892.84] That's Plum with a B, as in plumber, to request access today.
[893.22 → 897.34] That's U-S-E-P-L-U-M-B.com.
[897.52 → 899.46] Again, useplum.com.
[915.26 → 923.14] Well, Rowe, I really appreciate also the statement about adding oomph to your representations.
[923.44 → 928.48] I think that would be some type of good t-shirt that could be derived out of that.
[929.04 → 936.22] I see for listeners who are just listening on audio, Rowe's wearing a shirt that says,
[936.46 → 940.74] Love thy nearest neighbour, which is definitely applicable to today's conversation.
[940.74 → 942.26] Well, this is great.
[942.44 → 948.02] So we've kind of got a baseline, in a sense, from your perspective, what a vector database is,
[948.12 → 954.34] why it's useful in terms of what it represents in these embeddings and allows you to search through.
[954.94 → 955.78] You mentioned RAG.
[955.84 → 959.50] We've talked a lot about RAG on the show over time.
[959.50 → 963.52] But maybe for listeners, this is the first episode that they've listened to.
[963.92 → 973.34] What would be the kind of 30 seconds or some type of quick sort of, remember RAG is X from Rory?
[973.76 → 973.96] Right.
[974.14 → 980.76] So I love quoting Andrei Karachi with his observation on LLMs and hallucinations.
[981.32 → 986.86] So people, usually when people talk about RAG, they say, oh, Rags sometimes hallucinate, and that's terrible, right?
[986.86 → 990.82] And Andrei Karachi says, actually, no, they always hallucinate, right?
[990.88 → 992.72] That they do nothing but hallucinate, right?
[992.82 → 993.98] And that's really true, right?
[994.00 → 1000.62] Because LLMs don't have any kind of tethering to real knowledge in a way that we can trust, right?
[1000.74 → 1007.96] We don't have a way to say, hey, I can prove to you that what the LLM said is correct or incorrect based on the LLM itself, right?
[1007.96 → 1010.20] We need to go out and look and search, right?
[1010.20 → 1033.04] And RAG to me is that opportunity where we can take the user's intent, we can tie it using a for example, right, a semantic similarity search to structured data that we can point to and say, this is the data that is actually trusted, and then feed that back to the LLM to produce a more reliable and truthful answer.
[1033.04 → 1046.50] Now, that's not to say that RAG is going to solve all of your problems, but it's definitely going to give you at least a handle on what's real and what's not, what's trusted and what's not, and where the data is coming from, where those responses are coming from.
[1046.80 → 1062.06] And it shifts the role of the LLM from being your source of truth to basically being a thin natural language wrapper that takes the response and makes it palatable and easy to consume to a human being.
[1062.06 → 1079.86] Great. Yeah. I think a lot of people have done a sort of, maybe they've done even their own demo with sort of naive RAG, maybe pulling in a chunk from a document that they've loaded into some vector database, they inject it into a prompt, and they get some useful output.
[1079.86 → 1096.32] One of the things that I think we haven't really talked about a lot on this show, we've talked about advanced RAG methods to one degree or another, but I know Pine cone, along with other vector database providers, offer more than a simple just search.
[1096.32 → 1113.94] That's the only function you can do. There's a lot more to it that can make things useful in particular, like having, you know, you mentioned, Pine cone mentions kind of namespaces that can be used, metadata filters, sort of hybridized ways of doing these searches.
[1113.94 → 1117.94] Could you kind of help our listeners understand a little bit?
[1117.94 → 1125.94] So they may understand, here's my user statement, I can search that against the database and get maybe a matched document.
[1125.94 → 1147.62] But for an actual application, like an application in my company that I'm building on top of this, what are some of these other key pieces of functionality that may be needed for an enterprise application or for a production application that go beyond just the sort of naive search functionality in a vector database?
[1147.62 → 1177.60] Yeah, for sure.
[1177.62 → 1187.88] So you can use those tools and selection boxes, etc. That come from the application that are more set in stone, so to speak. They're not just like natural language. They're categorical data, for example.
[1188.40 → 1198.86] And you can use those to limit the result set, right, so that you hit only what you want. That is something that is very common to see in a lot of different production scenarios.
[1198.86 → 1210.60] And could you give maybe an example of that, like in a particular use case that you've run across, like what might be those categories or what, just to give people something concrete in their mind?
[1210.60 → 1227.40] Yeah, for example, like you can imagine a case where, I'm not going to name the customer, but like you can imagine the case where you want to perform a RAG operation, but you want to do it on a corpus of documents, but not on the entire corpus, but rather on a particular project within that corpus.
[1227.40 → 1238.18] So imagine that you have multiple projects that your product is handling, like finance and, you know, HR and whatever, engineering, right?
[1238.26 → 1242.88] And you want to perform that search and then limit it only to a particular project.
[1242.88 → 1253.52] And in that case, right, you would use the categorical data that is associated with the vectors that you've embedded and saved in Pine cone to only get the data for that particular project, right?
[1253.54 → 1255.30] That is like a kind of super simple example.
[1255.74 → 1260.06] But it can go beyond that, right, and move into like the logic of your application.
[1260.06 → 1266.60] So like you can imagine a case where, you know, you're looking at a movie, a movie data set, right?
[1266.60 → 1275.64] Like, and you want to search through different plot lines of movies, but you want to limit the results only to a particular genre, right?
[1275.76 → 1276.82] That's another case, right?
[1276.82 → 1278.90] Like we can just leverage metadata.
[1279.06 → 1283.64] You can think of wanting to limit the results to a time span, right?
[1283.74 → 1285.48] A start and end date, right?
[1285.48 → 1296.66] Things of that sort that kind of like have to do more with the nature of when and how and what category the vector belongs into and not specifically the contents of the vector, right?
[1296.80 → 1297.80] So that's one thing.
[1298.54 → 1304.82] Namespaces are another feature that we've seen as being like incredibly important for multi-tenant kind of situation.
[1304.94 → 1309.46] And multi-tenant rag has become kind of like a very strong use case for us.
[1309.46 → 1316.44] And that's where, you know, you see a customer and that customer has customers of their own and not one or two, but many, many, many.
[1316.82 → 1325.56] And in that case, you definitely don't want to have all the documents that all the subcustomers have to be co-located in one index.
[1325.78 → 1328.62] And in that case, you basically break them apart, right?
[1328.64 → 1329.88] So they're still in one index.
[1330.04 → 1333.80] So management of the index overall is maintained under one roof.
[1333.80 → 1341.86] But the actual content and the vectors themselves are separated out physically from one another in namespaces.
[1342.28 → 1345.30] They're sort of sub-indexes to that super index.
[1346.00 → 1351.00] And that's another feature that we've seen as being super important to our enterprise customers.
[1351.00 → 1362.94] As you're looking at these enterprise customers and with maybe most enterprises, you know, getting into rag at this point at some level and trying to find use cases for their business to do that.
[1363.04 → 1366.30] I know, you know, my company and lots of other companies are doing this.
[1366.94 → 1376.88] What are some of the ways that they should be thinking about these different use cases when we're talking about rag and semantic search and multimodal things that Pine cone does?
[1376.88 → 1382.58] What are good entry pathways for them to be thinking about how to do this?
[1382.68 → 1386.70] Because, you know, they may have come up with their own, their kind of own internal platform.
[1386.84 → 1387.94] It might have some open source.
[1388.04 → 1390.12] It might have some products already in play.
[1390.36 → 1393.46] But maybe they don't have a vector database in play yet.
[1393.90 → 1403.96] And so, you know, how do they think about where they're at when you guys are talking to them, and you're saying, let me, you know, we've, because we've been talking in the show so far about kind of the value of the vector database.
[1403.96 → 1408.90] And the kind of these use cases, but not necessarily kind of easy pathway.
[1409.04 → 1414.64] So how do you onboard enterprise people to take advantage of the goodness on this?
[1415.16 → 1416.18] Yeah, that's an excellent question.
[1416.26 → 1426.88] And in fact, it's like a quite a big of a challenge because it ends up being, you know, a straightforward pipelining challenge that has existed from the beginning of, you know, the big data era.
[1426.88 → 1433.12] Right. Like, how do I how do I leverage all the insight that is locked in my data beneficially?
[1433.22 → 1440.02] Right. And the sad part about this story is that it always depends on the specific use case.
[1440.02 → 1448.46] And it's hard to give a silver bullet a sort of light at the end of the tunnel is that we've recently published a tool called the rag planner.
[1448.46 → 1460.94] And its purpose is to basically help you figure out what do you need to do to get from where you are to an actual rag application and follow through all the different steps that are required in between.
[1461.24 → 1468.94] Right. And sort of like understand, like from an understanding of like where your data is stored, how frequently it updates, like what the scale of your data is, et cetera, et cetera.
[1468.94 → 1473.88] To the point where it could give you some recommendation as to like, what are like the steps that you have to do?
[1473.98 → 1477.86] Like in terms of do you build a batch pipeline? Do you build a streaming pipeline?
[1478.52 → 1480.76] What tools should you be using to do those things?
[1480.82 → 1482.96] What kind of data cleaning are you going to need to do?
[1483.30 → 1486.54] What embedding models are you going to want to use to do this? Right.
[1486.56 → 1489.44] Like, how are you going to evaluate the results of your rag pipeline?
[1489.54 → 1491.44] So all of these questions are pretty complex.
[1491.82 → 1494.48] So what I would say is a general rule of thumb.
[1494.48 → 1498.96] First, like you have to evaluate whether rag is for you.
[1499.28 → 1505.52] Right. So, for example, there are a lot of situations where, you know, rag may be the wrong choice.
[1505.86 → 1508.20] Right. Because the data that you have.
[1508.46 → 1515.60] Right. And the actual capability of answering the end users questions based on that data does not match up.
[1515.70 → 1524.46] Right. And that's how you get to see, you know, cases where, you know, chatbots sort of spit out results that may seem ridiculous.
[1524.48 → 1529.10] But nobody catches it. And companies get into a lot of hot water because of it.
[1529.18 → 1537.70] Right. There are a lot of scenarios where it's much easier to start that journey and to sort of develop the muscle memory that's required in order to set these things up.
[1537.70 → 1543.32] In a lot of these use cases, you see, like, a lot more internal processes, definitely in bigger companies.
[1543.48 → 1551.00] Right. Where, like, there's a very big team that just needs access to its internal knowledge base efficiently.
[1551.22 → 1554.46] But it's not a system that is going to be mission-critical.
[1554.70 → 1555.78] Right. In any way.
[1555.78 → 1560.14] So, like, if a person gets a wrong answer, it's not going to be the end of the world.
[1560.24 → 1561.54] Nobody's going to get sued. Right.
[1561.66 → 1567.40] And so what I would say is there's definitely a learning curve here for big organizations for sure.
[1567.92 → 1577.34] It's usually recommended to develop, again, that internal knowledge of what the expectation versus the realities on the ground is going to be.
[1577.34 → 1581.34] To have, like, a perfect idea of how you assess risk in those situations.
[1581.60 → 1586.82] And most importantly, how to evaluate the results that are produced by those systems.
[1586.82 → 1589.78] Right. Because a lot of people are like, OK, you build the RAC system.
[1589.96 → 1591.96] Great. And now produces answers. I'm done. Right.
[1591.98 → 1593.40] Like, we're everybody's happy.
[1593.78 → 1596.84] That's farthest from the truth that you could possibly be. Right.
[1596.84 → 1603.58] Like, these systems need to be continuously monitored and feedback needs to be continuously collected to the point where you can understand.
[1603.58 → 1613.16] Right. Like, how changes in your data and the way that you're interacting with it, changes in large language models that you're implying are actually affecting the end result.
[1613.28 → 1618.32] Right. Are going to be. And how your users are actually interacting with the system overall.
[1618.50 → 1621.96] Right. How all of these things kind of coexist and happen together.
[1622.22 → 1624.56] And are they working in the way that you want them to?
[1624.72 → 1628.40] And of course, you want to do that, you know, in a quantitative and not qualitative way. Right.
[1628.40 → 1630.78] So, like, there's a lot of instrumentation that has to go into it.
[1630.78 → 1635.50] I'm curious as a little follow-up to that and obviously leaving specific customers out of it.
[1635.94 → 1644.36] Are you tending to see more internal use cases of RAC deployment to internal, you know, groups of employees and stuff, maybe from a risk reduction?
[1644.52 → 1650.28] Are you seeing more of an external I'm going to get this right out to my customers and try to beat my competition to it?
[1650.32 → 1652.94] Like, where do you think the balance is as of today?
[1653.52 → 1656.14] I think that there's a widespread and I think that it's a journey. Right.
[1656.14 → 1676.60] Like, I think that, like, the more tech native companies that we see that are more, I would say, forward-looking or, you know, technologically adapt to kind of do these things quickly are more ready to not only take risks, but take educated risks in this space with the evaluation that comes with it.
[1676.60 → 1679.98] Right. So, like, these are not just like let's set and forget, but they actually know what they're doing.
[1679.98 → 1685.30] In those cases, you see them going out to production with very big deployments.
[1685.96 → 1688.12] That is our bread and butter, I would say, at the moment.
[1688.30 → 1694.04] Right. With companies that are more traditional that have been like they're not necessarily getting tech native.
[1694.28 → 1699.72] You see a more cautious sort of progression, which is only to be expected.
[1699.72 → 1701.80] Right. Like, I think that's kind of like natural to see.
[1701.80 → 1711.48] Well, Run, I have something that I saw on your website, which was new to my knowledge, which I think is also fascinating.
[1711.66 → 1725.54] One of the things that I've really liked in experimenting with vector database rag type of systems as an AI developer is having the ability to run something without a lot of compute infrastructure,
[1725.54 → 1743.94] maybe in an embedded way or an on this index, something that I can spin up quickly, something that I don't have to deploy a Kubernetes cluster or something to or set up a bunch of kinds of client server architecture to set up and test out maybe a prototype that I'm doing.
[1743.94 → 1753.60] And I see Pine cone is talking about Pine cone serverless now, which is really, really intriguing to me, just based on my experience in working with people.
[1754.48 → 1760.36] This sort of serverless sort of implementations of this vector search, I think, can be really powerful.
[1760.60 → 1771.04] So could you tell us a little bit about that and how that kind of evolved and what it is, what's the current state and how Pine cone thinks about the serverless side of this?
[1771.04 → 1785.62] So serverless came about after we realized that tying compute and storage together is going to limit the growth factor that our bigger customers are expecting to see.
[1785.98 → 1789.96] And it basically makes growth kind of prohibitive in a space, right?
[1789.96 → 1805.24] And so we had to find a way to break apart these two considerations while maintaining the performance characteristics that our customers are expecting and are used to having from our previous architecture.
[1805.24 → 1814.22] So essentially, like serverless has been a pretty big undertaking on our side to ensure that, you know, the quality of the database is maintained.
[1814.44 → 1820.96] But at the same time, we can reduce cost dramatically for customers to just give you like an idea.
[1821.16 → 1831.40] Like for the same cost of storing about, I don't know, around 500,000 vectors before you can now store 10 million.
[1831.40 → 1834.26] Right. And that's a humongous difference. Right.
[1834.32 → 1836.02] Like it's an order of magnitude difference.
[1836.18 → 1849.94] I think that like to accomplish that, right, like there was like a lot of very clever engineering that had to happen because, again, now having compute and storage separated apart means that storage can become very cheap.
[1849.94 → 1856.94] But on the other hand, it requires you to handle the storage strategy and retrieval and a lot cleverer way.
[1857.44 → 1863.22] We have a lot of content on the website that kind of delves deeper into how exactly technically that was achieved.
[1863.30 → 1865.68] And we won't be able to cover that given the time that we have.
[1865.68 → 1886.28] But like the basic premise is that you can now grow your vectors index to theoretically infinity, but practically to tens of billions and hundreds of billions of vectors without the cost of the expense becoming prohibitive, which is the main drive for us with our bigger customers and also with smaller customers.
[1886.28 → 1888.28] Like you can start experimenting.
[1888.28 → 1909.28] We have like an incredibly generous free tier that allows you to start, you know, like you said, right, like if I'm just a developer on my own testing things and trying to understand how vector database works in my world, it's very unlikely that I'll be able to tap the entire free tier plan even several months in with many, many vectors stored.
[1909.28 → 1915.76] Right. And it will work the same way that our pro serverless tiers work in terms of its performance.
[1916.20 → 1918.96] So it's not like a reduced capacity or performance in any way.
[1919.36 → 1922.28] So you get to feel exactly what it would feel like.
[1922.80 → 1926.64] And the effort that's required to stand it up is minimal to negligible.
[1926.96 → 1930.50] Right. You just set up an account and the SDK is super, super easy to use.
[1930.88 → 1934.30] Yeah. And I understand it or sort of representing things right.
[1934.30 → 1937.46] Like in terms of the, you know, massive.
[1937.86 → 1944.34] So there is a massive engineering effort, I'm sure, as you mentioned, to achieve this because it's not a trivial thing.
[1944.34 → 1952.30] But in terms of the user perspective, like if people use Pine cone before, and they're using Pine cone now, you already mentioned the performance.
[1952.30 → 1955.44] Is the interaction similar?
[1955.44 → 1961.16] It's just this sort of scaling and sort of from the user perspective, scaling and pricing.
[1961.82 → 1963.58] And maybe also you could touch on.
[1963.84 → 1975.08] So Pine cone is people might be searching for different options out there and some of them would require you to have your own infrastructure or some of them are hosted solutions.
[1975.48 → 1982.34] Pine cone, at least in its kind of most typical form, would be hosted by you.
[1982.34 → 1989.94] And yeah, could you just talk a little bit about the user experience pre and post serverless and then also kind of the infrastructure side?
[1990.04 → 1993.02] Like what do people need to know, and what are the options around that?
[1993.50 → 1995.22] In terms of what happened pre and post.
[1995.44 → 2001.92] So before serverless, there was like a lot of possible configuration choice that you could do.
[2002.06 → 2005.88] Right. Like so like there was, in fact, a lot of confusion with our users.
[2005.88 → 2009.48] You know, like what exactly is the best configuration for me?
[2009.60 → 2011.88] Should I use like this performance kind of configuration?
[2012.76 → 2016.00] Should I use like the throughput optimized configuration?
[2016.24 → 2017.48] What exactly am I supposed to use?
[2017.62 → 2020.56] And like the pricing mechanism was a little bit convoluted.
[2020.70 → 2028.18] And I think that like serverless, the attempt there was to simplify as much as possible and to make it really, really dead simple.
[2028.18 → 2032.58] Right. For people to start and use, but also grow with us.
[2032.70 → 2042.48] Right. So again, like I said, like the bottom line is, you know, the external view into what Pine cone offers may have looked pretty similar.
[2042.74 → 2048.62] Right. So like if you're just a user, you may say like, hey, like I got like a cheaper Pine cone bill this month.
[2048.62 → 2051.28] And, you know, like I can store a lot more.
[2051.96 → 2052.52] Always a good thing.
[2052.82 → 2055.50] Right. Always a good thing. Right. But not super amazing. Right.
[2055.54 → 2061.84] Like, but the end result is the question is like, what happens when, you know, you can actually store a lot more vectors?
[2062.02 → 2064.12] Right. What does that unlock for you?
[2064.22 → 2076.48] And again, I think that like the end of the day, right, like the way that we see Pine cone and this may help us kind of talk about like what's next for Pine cone is a place where your knowledge lives.
[2076.48 → 2080.28] Right. And it allows you to build knowledgeable AI applications.
[2080.84 → 2085.16] Right. And having more knowledge is always net positive.
[2085.16 → 2099.72] Right. In that context. Right. So the assumption is that like, you know, as AI applications grow, they accumulate more and more and more knowledge, and they become that more powerful with any additional knowledge that you can stuff into them.
[2099.72 → 2104.06] And so there's like actual value beyond the fact that you can store more.
[2104.38 → 2106.26] Right. Like and it's cool. Right.
[2106.26 → 2112.16] Your application actually becomes more powerful because it can handle more types of use cases.
[2112.60 → 2119.62] It has a better ability to be more accurate and respond truthfully to a user when they are interacting with it.
[2119.62 → 2137.26] And so I think that like in general, like there's like this blatant kind of value that is only going to be apparent once people really experience what it means to have, you know, a million documents that are stored in Pine cone versus 10 million documents that are stored in Pine cone.
[2137.46 → 2140.16] And that effect is going to be very powerful.
[2140.16 → 2143.76] I think that's the majority of the benefit that I see.
[2143.92 → 2151.02] Maybe that gets to the next thing which I was going to ask about which I also see the announcement around Pine cone assistance.
[2151.82 → 2154.08] And I'd love to hear more about that.
[2154.34 → 2161.94] Like what is from, of course, sometimes maybe that can be loaded language also for people in the AI space.
[2161.94 → 2168.74] But in terms of this assistance functionality for Pine cone, what are you trying to enable, and where do you see it headed?
[2168.74 → 2174.26] So that has to do with the question that Chris had before, which is like, what is the journey, right, for customers, right?
[2174.62 → 2193.18] And I think that like as a general purpose that we had around assistance was to reduce the friction between me having a bunch of documents that I want to interact with, with an LLM or an AI in some form and capacity to the point where that actually works, right?
[2193.44 → 2195.86] There are a bunch of ways of going about it, right?
[2195.86 → 2213.88] I think Pine cone wants to bring, you know, on top of our very robust vector database, a very smooth experience that lets users really do very little and get all the value out of Pine cone without having to think too much about it.
[2213.88 → 2225.60] So for that purpose, we don't only have the ability to take your documents and then embed them and, you know, do the end-to-end process of creating that completion endpoint for you, right?
[2225.92 → 2230.64] We're also the ones providing the actual inference layers as well, right?
[2230.72 → 2238.00] And so it's not going to be, again, if you asked like me, like this question is like, how do you build a RAG pipeline, right?
[2238.00 → 2239.64] Like a year ago, even, right?
[2239.80 → 2243.92] I'd have to tell you, hey, you have to go to like some embedding provider.
[2244.18 → 2252.84] You have to find someone who would do like your, you know, PDF extraction or, you know, take the data and chunk it and do all this stuff, right?
[2252.84 → 2254.04] No more, right?
[2254.10 → 2262.30] Like the reality here is you can take a set of documents, throw them at this knowledge assistant and the rest is kind of quote unquote magic, right?
[2262.32 → 2267.40] It just happens for you behind the scenes while maintaining the quality that you want to get.
[2267.40 → 2270.72] And at the scale that Pine cone can deliver, right?
[2270.78 → 2272.54] Which is again, another differentiator.
[2272.94 → 2278.44] So like I said before, Pine cone is built to withstand hundreds of billions of documents, right?
[2278.60 → 2285.34] That of vectors that you would store with us and still be able to produce responses in a reasonable amount of time.
[2285.76 → 2290.42] And that's true for knowledge assistant because assistant sits on top of the vector database.
[2290.42 → 2296.14] So it sounds like that may be a perfect way, especially for small organizations.
[2296.40 → 2301.10] You know, we talked about enterprise, and they have a certain infrastructure and teams to go with that.
[2301.36 → 2310.08] But there's so many more small organizations out there that have very little in terms of trained people necessarily to do that.
[2310.14 → 2315.56] And they don't have all the infrastructure in place, and they're looking, you know, with assistants and serverless,
[2315.56 → 2320.40] they're looking for simple ways to onboard and get utility out of it.
[2320.80 → 2334.46] Would you say that the combination of serverless and assistants and then maybe whatever they might have in AWS or whatever platform that they're using is kind of just made to gel easily for them so they can get to something working pretty quick?
[2334.82 → 2334.92] Yeah.
[2335.00 → 2340.80] I mean, at the end of the day, like if you think about it, right, like the process shouldn't be as complicated as it is, right?
[2340.80 → 2346.76] It's just that there are many parts to it and nobody picked up the gauntlet of saying like, hey, we'll just do it all.
[2346.92 → 2347.28] You know what I mean?
[2347.70 → 2351.26] Because all of it is quite complicated to do right.
[2351.68 → 2351.82] Right.
[2351.98 → 2359.38] And so, yeah, like I think that like initially we'll see smaller organizations kind of, you know, picking that up because they don't have the resources.
[2360.00 → 2366.28] But as time moves along, you know, you're going to have to ask yourself, even as a bigger organization, do I want to own this pipeline?
[2366.78 → 2367.02] Right.
[2367.38 → 2368.94] Is it something that I need to own?
[2369.08 → 2369.36] Right.
[2369.36 → 2372.24] And what value am I getting from actually owning all of this?
[2372.36 → 2372.50] Right.
[2372.82 → 2375.88] And so, yeah, like it would be interesting to see.
[2376.00 → 2378.38] So like this is a very, very new product still on public beta.
[2378.76 → 2384.86] And it will be interesting to see how the market kind of reacts to it and sort of experiments with it.
[2384.86 → 2398.72] But my bet is that as time progresses and knowledge assistants themselves become more capable doing things maybe beyond RAG or beyond simple RAG, quote unquote, that, you know, like more and more.
[2398.72 → 2402.62] More sophisticated organizations might want to actually give it a try.
[2402.62 → 2415.16] And that really brings us maybe to a good way that we like to end episodes, which is asking our guests to sort of look into the future a little bit and not necessarily predict it because that's always hard.
[2415.16 → 2419.54] But to look into the future and kind of what are you excited about?
[2419.54 → 2432.38] It could be related to vector databases specifically or pine cones specifically, but maybe it's more generally in terms of how the AI industry is developing, the sorts of things that you're seeing customers do that are encouraging.
[2432.38 → 2439.56] Whatever that is, what sort of keeps you excited about where things are headed going into the rest of this year?
[2440.00 → 2451.60] I'm excited about the fact that we're seeing sort of like a resurgence of what you would call traditional AI kind of come back into the fold in the form of, for example, Graph RAG.
[2451.60 → 2467.54] I think that like the notion here is that, you know, for the longest time, and I think it's been since like, you know, GPT-3.5, you basically saw like this, like, I think over indexing on LLMs, right?
[2467.92 → 2468.88] For good reasons, right?
[2468.90 → 2469.94] Like they're super exciting.
[2470.12 → 2471.62] They're very powerful, right?
[2471.62 → 2473.30] And they can do really, really cool things, right?
[2473.30 → 2489.50] But with that said, it's as if every other technology that has ever existed before just like dropped off the face of the earth and nobody has ever like talked about like, okay, wait, so what can we do with those things and LLMs, right?
[2489.58 → 2491.94] Like, and where do LLMs fit in the bigger picture?
[2492.36 → 2497.86] I think that vector databases kind of like put LLMs in their place a little bit in the sense that, you know what I mean?
[2497.86 → 2502.14] Like you're not thinking of the LLM as being the end all, be all, like this is the only tool that we need.
[2502.14 → 2512.14] I'm very excited to think of LLMs as these operators or agents that can tap into the capabilities that exist in other systems.
[2512.64 → 2520.80] And I think that what we're going to see more and more and more is that people are going to figure out like in what subset of the ecosystem does each tool belong?
[2520.88 → 2523.14] So what set of problems that each tool solve?
[2523.40 → 2530.78] For example, like a vector database solves like the problem of bridging the gap between the semantic world and the structured world.
[2530.78 → 2537.14] A graph database can solve problems like reason, like formal reasoning over well-structured data.
[2537.74 → 2543.12] Relational databases can solve a whole set of different problems that they used to be solving, like aggregation, et cetera, et cetera.
[2543.72 → 2553.28] And then you can imagine that LLMs and agents can sit as sort of like an orchestrating mechanism and a natural language interface mechanism on top of all those things together.
[2553.28 → 2555.46] And that's what I'm excited to see.
[2555.60 → 2571.72] Like it's kind of when like the community as a whole is going to like wake up from its like LLM fever dream and sort of realize that like there's other things out there and realize that it has so many more powers that it could yield to make really exciting applications.
[2571.72 → 2572.72] That's awesome.
[2572.72 → 2573.00] That's awesome.
[2573.18 → 2586.74] Well, thanks for painting that picture for us, Run, and for taking time to dig into so many amazing insights about vector databases and embeddings and knowledge management in general.
[2587.30 → 2594.70] So, yeah, appreciate what you all are doing at Pine cone and hope to have you on the show again to update us on all those things.
[2595.00 → 2595.58] Thank you so much.
[2595.66 → 2596.32] Thanks for having me.
[2596.32 → 2596.36] Thank you.
[2596.36 → 2596.44] Thank you.
[2601.72 → 2604.82] All right.
[2604.98 → 2607.48] That is Practical AI for this week.
[2608.28 → 2609.30] Subscribe now.
[2609.48 → 2614.46] If you haven't already, head to practicalai.fm for all the ways.
[2614.92 → 2620.86] And join our free Slack team where you can hang out with Daniel, Chris, and the entire Changelog community.
[2621.46 → 2626.08] Sign up today at practicalai.fm slash community.
[2626.60 → 2629.36] Thanks again to our partners at fly.io.
[2629.36 → 2632.52] To our beat freaking residents, Break master Cylinder.
[2632.82 → 2633.62] And to you for listening.
[2633.98 → 2635.74] We appreciate you spending time with us.
[2636.08 → 2637.28] That's all for now.
[2637.52 → 2639.20] We'll talk to you again next time.
