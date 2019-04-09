# Copyright 2019 Neural Networks and Deep Learning lab, MIPT
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from logging import getLogger
import numpy as np

from deeppavlov.core.common.registry import register
from deeppavlov.core.models.estimator import Component

logger = getLogger(__name__)


@register("preproc_sentiment")
class PreprocSentiment(Component):

    def __init__(self,
                 **kwargs):
        pass

    def __call__(self, expanded_context_batch, top_responses_batch):
        """
        Args:
            expanded_context_batch - batch of dialog contexts, for example: `[['', '', ..., 'Hello'], [...]]`
            top_responses_batch - batch of top selected response candidates, for example: `[['Hello you', ...], [...]]`

        Returns:
            # list of merged sentences (last context utterance + response_i) of size (bs, len(top_responses_batch))
            list of sentiment labels of size: (bs, len(expanded_context_batch) + len(top_responses_batch))
        """
        print("len [expanded_context_batch]: ", len(expanded_context_batch))
        print("len [top_responses_batch]: ", len(top_responses_batch))

        sentiment_sentences_batch = []
        for i in range(len(expanded_context_batch)):
            # merged = []
            # for j in range(len(top_responses_batch[i])):
            #     merged.append(expanded_context_batch[i][-1] + top_responses_batch[i][j])
            # sentiment_sentences_batch.append(merged)
            res_list = []
            # for all context sentences
            for j in range(len(expanded_context_batch[i])):
                sentiment_sentences_batch.append(expanded_context_batch[i][j])
            # for all top responses
            for j in range(len(top_responses_batch[i])):
                sentiment_sentences_batch.append(top_responses_batch[i][j])
            # sentiment_sentences_batch.append(res_list)

        print("len [sentiment_sentences_batch]: ", len(sentiment_sentences_batch))

        return sentiment_sentences_batch
