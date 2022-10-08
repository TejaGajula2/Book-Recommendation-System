ratings.merge(books,on='ISBN')
num_rating = ratings_with_name.groupby('Book-Title').count()['Book-Rating'].reset_index()
num_rating.rename(columns={'Book-Rating':'num_ratings'},inplace=True) num_rating

avg_rating = ratings.groupby('Book-Title').mean()['Book-Rating'].reset_index() 
avg_rating.rename(columns={'Book-Rating':'avg_rating'},inplace=True) 
avg_rating

Popular_books = num_rating.merge(avg_rating, on='Book-Title')
Popular_books

Popular_books = Popular_books[Popular_books['num_ratings'] >= 250].sort_values( 'avg_rating', ascending=False).head(50)
Popular_books = Popular_books.merge(books, on='Book-Title').drop_duplicates(
'Book-Title')[['Book-Title', 'Book-Author', 'Image-URL-M', 'num_ratings', 'avg_rating']] popular_df['Image-URL-M'][0]
