mkdir -p ~/.streamlit/
echo "
[theme]
primaryColor= '#F63366'
backgroundColor = '#FFFFFF'
secondaryBackgroundColor = '#F0F2F6'
textColor= '#262730'
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml