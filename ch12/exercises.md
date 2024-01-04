# K-nearest neighbors

### 12.1
In collaborative filtering, dealing with different rating strategies among users is an important consideration. One way to address this issue is to normalize the ratings before calculating the similarity or distance between users. Normalization helps to account for variations in rating scales and brings ratings to a common scale.

Here are a couple of normalization techniques that can be used:

1. **Z-Score Normalization:**
   - Calculate the mean and standard deviation of ratings for each user.
   - Normalize each user's ratings by subtracting the mean and dividing by the standard deviation.
   - This centers the ratings around zero and adjusts for the scale of individual users.

   For user Yogi, whose ratings are generally high, this normalization would reduce the impact of his tendency to give high ratings. Similarly, for Pinky, who is choosier with 5s, this normalization would adjust for her tendency.

2. **Min-Max Normalization:**
   - Determine the minimum and maximum ratings given by each user.
   - Normalize each user's ratings to a scale between 0 and 1 using the formula: \[ \text{Normalized Rating} = \frac{\text{Original Rating} - \text{Min Rating}}{\text{Max Rating} - \text{Min Rating}} \]
   - This normalization method scales ratings based on the user's individual range.

After normalization, you can apply the distance formula or similarity measure to find the similarity between users. By doing this, the impact of different rating strategies is minimized, and the focus is shifted towards capturing the relative preferences of users.

Keep in mind that the choice of normalization method may depend on the specific characteristics of your dataset and the goals of your recommendation system. Experimenting with different normalization techniques and observing their impact on the recommendations is often a good practice.

### 12.2
To bias the recommendations system towards the ratings of influencers like Quentin Tarantino and Wes Anderson, you can assign higher weights to their ratings in the collaborative filtering process. This involves adjusting the similarity or distance calculations based on the influencer's ratings. Here's how you can approach this:

1. **Weighted Similarity Calculation:**
   - Assign a weight to each user based on their level of influence. For example, give a higher weight to Quentin Tarantino and Wes Anderson.
   - Modify the similarity calculation to incorporate these weights. One way to achieve this is by multiplying the rating of each movie by the user's weight before calculating the similarity or distance.

   Mathematically, the weighted similarity between users \(A\) and \(B\) can be calculated as:
   \[ \text{Weighted Similarity}(A, B) = \frac{\sum_{i} w_i \cdot r_{A,i} \cdot r_{B,i}}{\sqrt{\sum_{i} w_i \cdot (r_{A,i})^2} \cdot \sqrt{\sum_{i} w_i \cdot (r_{B,i})^2}} \]

   where:
   - \(w_i\) is the weight assigned to the user or influencer for movie \(i\),
   - \(r_{A,i}\) is the rating of user \(A\) for movie \(i\),
   - \(r_{B,i}\) is the rating of user \(B\) for movie \(i\).

2. **Influencer-Specific Recommendations:**
   - When generating recommendations, consider the ratings of influencers more heavily.
   - You can incorporate a bias towards influencer ratings by, for example, boosting the predicted ratings for items that have been highly rated by influencers.

3. **Customized Influence Weighting:**
   - Allow for customization of the influence weights, so that the degree to which influencers' ratings impact the recommendations can be adjusted based on system requirements or user preferences.

It's important to note that while giving more weight to influencers' ratings can enhance the impact of their preferences, it should be done carefully. Over-relying on a small set of influencers may lead to recommendations that are biased towards their tastes and may not generalize well to a broader audience. Balancing the influence of influencers with the preferences of the larger user base is crucial for building a robust and effective recommendation system.

### 12.3
The choice of the number of neighbors in collaborative filtering can significantly impact the performance of the recommendation system. The decision on whether the number of neighbors is too low or too high depends on various factors, including the characteristics of the dataset, the sparsity of user-item interactions, and the computational resources available. Here are some considerations:

**Too Few Neighbors:**
- If you have too few neighbors, the recommendations might not be diverse or representative of a user's preferences.
- The system might be more sensitive to outliers or noise in the data, leading to less reliable recommendations.
- Limited input from neighbors may not capture the diversity of user tastes, resulting in less accurate recommendations.

**Too Many Neighbors:**
- If you have too many neighbors, the recommendations may become too generic and biased towards popular items.
- Computationally, the system might become more resource-intensive as the number of neighbors increases, making real-time recommendations challenging.
- Including too many neighbors might also lead to recommendations influenced by users with very different tastes, reducing the personalization aspect.

**Balancing Act:**
- The optimal number of neighbors often involves a trade-off. It's essential to strike a balance between capturing diverse user preferences and avoiding excessive noise or bias.
- Experimentation with different values for the number of neighbors is often necessary to find the sweet spot for a particular dataset and recommendation algorithm.

**Dynamic Approaches:**
- Some recommendation systems use adaptive or dynamic approaches where the number of neighbors is adjusted based on user preferences or the specific characteristics of the items being recommended.

In practice, the choice of the number of neighbors is often determined through experimentation and evaluation using metrics such as accuracy, diversity, and coverage. Cross-validation techniques and A/B testing can be employed to assess the impact of different neighbor sizes on the performance of the recommendation system. Additionally, leveraging machine learning techniques that automatically learn the optimal number of neighbors based on the data can be explored for more adaptive solutions.