import os
seed = 1111
csv_file_paths = os.path.join(os.getcwd(), "data")
final_csv_path = 'policy_texts.csv'
cutoff = 0.8
vocab_size = 2000
min_samples = 10
subtopics = [
        'how use collected information', 
        'share or transfer data', 
        'changes and updates', 
        'third parties and online advertising', 
        'user information collection'
        ]


# n_topics = 5
# n_words = 10 
# min_df = 10
# max_iter = 15
# search_params = {
#                 'n_components': [10, 15, 20, 25, 30], 
#                 'learning_decay': [.5, .7, .9]
#                 }


max_length = 40
embedding_dimS = 256
trunc_type = 'post'
oov_tok = "<OOV>"
num_epochs = 20
batch_size = 64
size_lstm  = 256
dense1 = 256
dense2 = 64
keep_prob = 0.5
sentiment_weights = "weights/model.h5"
