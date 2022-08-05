# Open several files

# This program will read first file line by line and save into new file
# with open('text_files//lorem.txt', 'r', encoding='UTF8') as rfile:
#     with open('text_files//text_copy.txt', 'w', encoding='UTF8') as wfile:
#         for line in rfile:
#             wfile.write(line)


# # Picture file sample
# with open('text_files//python.jpg', 'rb') as rfile:
#     with open('text_files//python_copy.jpg', 'wb') as wfile:
#         chunk_size = 4096
#         rfile_chunk = rfile.read(chunk_size)
#         while len(rfile_chunk) > 0:
#             wfile.write(rfile_chunk)
#             rfile_chunk = rfile.read(chunk_size)