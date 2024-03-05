*Question-2(Please refer the folder Q2->Harsh_Q2_NGINX)

Commands I used to run
Step-1
You need to download model file(Hugging face model)from drive link 
https://drive.google.com/drive/u/1/folders/15HgHMA6d-jNC9kyGkxi5eTNvUnJX1kuR

And put this model folder inside these two folders
Harsh_Patel_Q2_Q3->Q2->Harsh_Q2_NGINX 
OR
Harsh_Patel_Q2_Q3->Q2->Harsh_Q2_Without_NGINX (If you want to try single thread only flask version)

Step-2
docker build -t flask-nginx .
docker run -p 80:80 flask-nginx

Step-3
and then run the file name with 'op.ipynb' and add whatever text you want to summarize

->I picked the Falconsai/text_summarization model from Hugging Face (https://huggingface.co/Falconsai/text_summarization). Why? Well, I was short on time, super busy, and pretty good at NLP and generative AI stuff (That's what I think... 😉), especially Seq-2-Seq models. Using a model I know well means I spend less time fixing problems. Plus, this one isn't too big, just 60 million parameters, which is good for what I needed. 😀

->To use the code, just type in your text in op.ipynb, and you'll get a summary back. 📝

->At first, I goofed up and used Flask's own server, but then I realized, 'Oops! The task said we needed a proper web server component.' So, I switched to Nginx. It was a bit of a learning curve. I'm sharing both versions – one with Nginx, which can handle lots of requests, and one with just Flask, which can't handle many requests at once. You know, for comparison. 🔄

->I wanted to try something with RAG, but my term's jam-packed with assignments and research projects, so I didn't get to explore that avenue much. 😔
____________________________________________________________________________________

*Question-3(Just run the file which is inside folder Q3->Harsh_Q3.ipynb)

I'm working with a dataset of quotes, and in our previous discussions, we've explored both image and text data. Initially, I had planned to work with audio data, but due to time constraints, I've opted to revisit text data once more. Although the dataset isn't large, it's versatile enough to allow for a comprehensive exploratory data analysis, covering aspects ranging from sentiment analysis to various other analyses. 😊