from .utilities.pinecone_connector import (
    get_bert_embeddings,
    get_model,
    get_pinecone_connection,
)
from .utilities.langchain_connector import get_langchain_connection
from pinecone import ServerlessSpec
import pandas as pd


data = pd.read_csv("app/dataset/pair_data.csv")

index_name = "one-space-index"


def get_data(data):
    data["vectors"] = data["prompt"].apply(get_bert_embeddings)
    return data


def upload_vectors(pc):
    data_new = get_data(data)

    if index_name not in pc.list_indexes():
        pc.create_index(
            name=index_name,
            dimension=get_model().config.hidden_size,
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )

    index = pc.Index(index_name)

    upload_data = [
        (
            str(i),
            vec.tolist(),
            {
                "text": txt,
                "hq1": hq1,
                "hq2": hq2,
                "mq1": mq1,
                "lq1": lq1,
                "lq2": lq2,
                "lq3": lq3,
                "lq4": lq4,
                "lq5": lq5,
            },
        )
        for i, vec, txt, hq1, hq2, mq1, lq1, lq2, lq3, lq4, lq5 in zip(
            data_new.index,
            data_new["vectors"],
            data_new["prompt"],
            data_new["hq1"],
            data_new["hq2"],
            data_new["mq1"],
            data_new["lq1"],
            data_new["lq2"],
            data_new["lq3"],
            data_new["lq4"],
            data_new["lq5"],
        )
    ]

    batch_size = 100
    for i in range(0, len(upload_data), batch_size):
        batch = upload_data[i : i + batch_size]
        index.upsert(vectors=batch)

    print("Data uploaded successfully!")


def query_vectors(pc, query_str):
    index = pc.Index(index_name)
    query_vector = get_bert_embeddings(query_str)

    results = index.query(
        vector=[query_vector.tolist()],
        top_k=10,
        # include_values=False,
        include_metadata=True,
    )
    similar_texts = [
        {
            "prompt": match["metadata"]["text"],
            "hq1": match["metadata"]["hq1"],
            "hq2": match["metadata"]["hq2"],
            "mq1": match["metadata"]["mq1"],
            "lq1": match["metadata"]["lq1"],
            "lq2": match["metadata"]["lq2"],
            "lq3": match["metadata"]["lq3"],
            "lq4": match["metadata"]["lq4"],
            "lq5": match["metadata"]["lq5"],
        }
        for match in results["matches"]
    ]
    print(similar_texts)
    return similar_texts


def query_langchain(vector):
    print(vector)
    response = get_langchain_connection(data=vector)
    print(response)
    return response


def delete_index(pc):
    pc.delete_index(index_name)
