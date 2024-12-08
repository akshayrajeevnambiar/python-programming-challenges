from collections import Counter

# write a funciton to count the number of unique words in a file
def count_unique_words(file_path):
    counter = Counter()

    with open(file_path, 'r') as file:
       data =  file.read()
       
       for word in data.replace('.', '').split():
           counter[word] += 1

       sorted_counter = dict(counter.most_common(20))

       print(f"Total Number of Words: {len(counter)}")
    
       for key, value in sorted_counter.items():
           print(f"Word: {key}, Count: {round((value / len(counter)) * 100, 2)}%")


# print the data that we retrived 
count_unique_words("sample.txt")