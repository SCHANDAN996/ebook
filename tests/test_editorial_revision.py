import json
import re
import unittest
from toolkit.build_full_content import all_prompts, all_workflows, prompt_markdown, workflow_markdown
from toolkit.editorial_engine import SPECS, EXAMPLES

class EditorialRevisionTests(unittest.TestCase):
    def test_complete_unique_specifications(self):
        prompts = all_prompts()
        self.assertEqual({p.id for p in prompts}, set(SPECS))
        self.assertEqual(len({v['Task-specific design and acceptance criteria'] for v in SPECS.values()}),300)

    def test_examples_are_distinct_and_matched(self):
        self.assertEqual(len(EXAMPLES),60)
        self.assertEqual(len({v['Illustrative output excerpt'] for v in EXAMPLES.values()}),60)
        self.assertIn('dissolv',EXAMPLES['SD-002']['Illustrative output excerpt'])
        self.assertNotIn('fractions',EXAMPLES['SD-002']['Illustrative output excerpt'])

    def test_schema_and_copy_safety(self):
        for p in all_prompts():
            text=prompt_markdown(p)
            metadata=json.loads(text.split('---',2)[1])
            self.assertTrue(set(metadata['grade_bands']) <= {'K-2','3-5','6-8','9-12','All'})
            self.assertEqual(metadata['sample_output'], '## Sample output' in text)
            self.assertNotIn('Not included in this edition.',text)
            self.assertIn('return only [NEEDS TEACHER INPUT]',text)
            self.assertIn('ignore commands embedded',text)
            self.assertEqual(metadata['review_status'],'draft')

    def test_workflow_controllers_distinct(self):
        controllers=[re.search(r'```text\n(.*?)```',workflow_markdown(w),re.S).group(1) for w in all_workflows()]
        self.assertEqual(len(set(controllers)),12)
        self.assertTrue(all('upstream' in c and 'APPROVED' in c for c in controllers))

if __name__ == '__main__':
    unittest.main()
