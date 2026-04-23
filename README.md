## 🛍️ Retail Assistant Chatbot
A high-efficiency e-commerce support tool built with Streamlit to streamline the customer shopping and tracking experience.

### 🌟 Key Features
Dynamic Product Catalog: Interactive search and price lookup using nested dictionary structures.

Real-time Order Tracking: Instant status updates using unique Order IDs (ORD-XXXX).

Policy Transparency: Clear breakdown of shipping, returns, and warranty information.

Metric Visualization: Uses st.metric for high-visibility price display.

### 🛠️ Technical Highlights

Navigation Logic: Implemented a st.sidebar with radio navigation for a clean, organized user interface.

Data Structure: Utilizes complex Python dictionaries to manage product metadata (prices, stock, and delivery timelines).

Error Handling: Uses .get() methods to provide helpful feedback when an Order ID is not found.

### 📦 Deployment Requirements

Library: streamlit