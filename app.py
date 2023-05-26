import argparse
from flask import Flask, request, jsonify, abort
from Bio import SeqIO
from Bio import pairwise2
app = Flask(__name__, static_url_path='', static_folder='templates')

# Command line arguments
parser = argparse.ArgumentParser(description='Federated Hits')
parser.add_argument('fasta_file', type=str, help='Path to reference fasta file')
args = parser.parse_args()

# Load reference sequences
reference_sequences = list(SeqIO.parse(args.fasta_file, 'fasta'))

# Smith-Waterman algorithm implementation
def smith_waterman(query_sequence, reference_sequence):
    return pairwise2.align.localxx(query_sequence,reference_sequence,score_only=True)

# API key validation function
def validate_api_key(api_key):
    authorized_keys = ['key1', 'key2', 'key3']
    print(f'Checking: {api_key}')
    if api_key not in authorized_keys:
        abort(403)

# GET request handler
@app.route('/federated_hits', methods=['GET'])
def federated_hits():
    # Validate API key
    api_key = request.args.get('api-key')
    validate_api_key(api_key)

    # Get query sequence
    query_sequence = request.args.get('query-sequence')

    # Find top 5 hits
    hits = []
    for reference_sequence in reference_sequences:
        score = smith_waterman(query_sequence, str(reference_sequence.seq))
        hits.append({'id': reference_sequence.id, 'similarity_score': score, 'expression_score': 1.0, 'thermostability': 1.0})
    hits = sorted(hits, key=lambda x: x['similarity_score'], reverse=True)[:5]

    # Return hits as JSON response
    return jsonify(hits)

if __name__ == '__main__':
    app.run()
