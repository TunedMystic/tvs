const utils = require('../utils');


describe('Test main', () => {
    it('should serialize params correctly', () => {
        const testData = [
            [{}, ''],
            [{q: 'test'}, 'q=test'],
            [{q: 'test string'}, 'q=test%20string'],
            [{q: 'some search text', page: 3, sort: 1}, 'q=some%20search%20text&page=3&sort=1'],
        ];

        for (const testItem of testData) {
            expect(
                utils.serializeParams(testItem[0])
            ).toBe(testItem[1]);
        }
    });
});
